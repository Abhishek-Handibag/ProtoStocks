# main.py


import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from schemas.schemas import LoginRequest, TokenResponse, Item
from jose import JWTError, jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()

app = FastAPI()

# JWT config
JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

# Auth dependency
security = HTTPBearer()

def verify_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)):
	token = credentials.credentials
	try:
		payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
		return payload
	except JWTError:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Invalid or expired token",
			headers={"WWW-Authenticate": "Bearer"},
		)




@app.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
	# Hardcoded credentials
	valid_email = "admin@gmail.com"
	valid_password = "admin"
	if request.email == valid_email and request.password == valid_password:
		# Create JWT token with iat, exp, sub
		now = datetime.now(timezone.utc)
		expire = now + timedelta(minutes=60)
		payload = {
			"sub": request.email,
			"iat": int(now.timestamp()),
			"exp": int(expire.timestamp()),
		}
		token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
		return {"access_token": token, "token_type": "bearer"}
	else:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Invalid email or password",
			headers={"WWW-Authenticate": "Bearer"},
		)

@app.get("/")
def read_root():
	return {"message": "Welcome to ProtoStocks FastAPI backend!"}

# Protected endpoint
@app.post("/items/", response_model=Item, dependencies=[Depends(verify_jwt)])
def create_item(item: Item):
	return item
