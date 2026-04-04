# JobTrackr Backend

Backend service for managing job applications, resumes, and user authentication.

## Live API

- Base URL: https://jobtrackr-api-fatu.onrender.com  
- Swagger Docs: https://jobtrackr-api-fatu.onrender.com/docs  

## Tech Stack

- FastAPI  
- SQLAlchemy  
- Alembic (migrations)  
- PostgreSQL (Render)  
- JWT Authentication  

## Features

- User authentication (JWT)  
- Role-based access (User/Admin)  
- Applications CRUD  
- Resume management  
- Soft delete support  
- Modular service and repository architecture  

## Setup

### Clone the repository

Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Create a .env file:

DATABASE_URL=your_database_url
SECRET_KEY=your_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

Run migrations
alembic upgrade head
Start the server
uvicorn app.main:app --reload
Deployment
Backend: Render
Database: Render PostgreSQL

Authentication
JWT-based authentication
Include token in request headers:
Authorization: Bearer <token>
Architecture
API → Services → Repositories → Database

```bash
git clone https://github.com/your-username/jobtrackr-backend.git
cd jobtrackr-backend
