# ProtoStocks

ProtoStocks is a beginner-friendly stock market simulator built with FastAPI. It allows users to practice trading decisions, manage portfolios, and learn about stock markets in a risk-free environment.

## Features
- **FastAPI Backend**: High-performance API using FastAPI.
- **JWT Authentication**: Secure login with JWT tokens (see `/login` endpoint).
- **User Endpoints**: Example endpoints for login and item management (expandable for more features).
- **Project Structure**:
  - `main.py`: FastAPI app with authentication and endpoints.
  - `run.py`: Uvicorn server runner for development.
  - `schemas/`: Pydantic models for request/response validation.
  - `controllers/`, `helpers/`, `models/`, `services/`: (Placeholders for future logic.)
- **Environment Variables**: Uses `.env` for secrets (e.g., `JWT_SECRET`).

## Getting Started
1. **Install dependencies**:
	```sh
	pip install -r requirements.txt
	```
2. **Set up environment variables**:
	- Create a `.env` file with `JWT_SECRET=your_secret_key`.
3. **Run the server**:
	```sh
	python run.py
	```
4. **API Docs**:
	- Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive Swagger UI.

## Example Endpoints
- `POST /login`: Get JWT token (use email: `admin@gmail.com`, password: `admin` for demo).
- `GET /`: (To be implemented) Home endpoint.

## Requirements
See `requirements.txt` for all dependencies.

## Folder Structure
```
ProtoStocks/
├── main.py
├── run.py
├── requirements.txt
├── pyproject.toml
├── schemas/
│   └── schemas.py
├── controllers/
├── helpers/
├── models/
├── services/
```

---
*This project is under active development. More features and endpoints coming soon!*
