# JobTrackr Backend

A robust REST API for managing job applications, resumes, and user authentication, built with FastAPI.

## Live API
* **Base URL:** [https://jobtrackr-api-fatu.onrender.com](https://jobtrackr-api-fatu.onrender.com)
* **Swagger Docs:** [https://jobtrackr-api-fatu.onrender.com/docs](https://jobtrackr-api-fatu.onrender.com/docs)

> **Note on Free Tier Hosting:** > This API is hosted on Render's Free Tier. The instance spins down after periods of inactivity. Please allow **60-90 seconds** for the initial request to process if the service is currently "sleeping."

---

## Tech Stack
* **Framework:** FastAPI
* **Database:** PostgreSQL (Render/Neon)
* **ORM:** SQLAlchemy
* **Migrations:** Alembic
* **Authentication:** JWT (JSON Web Tokens)
* **Architecture:** Modular Service-Repository Pattern

---

## Features
* **Secure Auth:** JWT-based authentication and password hashing with Bcrypt.
* **RBAC:** Role-Based Access Control (Admin/User permissions).
* **Job Tracking:** Full CRUD logic for applications with **Soft Delete** support.
* **Resume Management:** Logic for handling and linking user resumes.
* **Data Integrity:** Standardized API responses and robust error handling.

---

## Local Setup
1. **Clone the repo.**
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Set Environment Variables:** Configure `DATABASE_URL` and `JWT_SECRET`.
4. **Run Migrations:** `alembic upgrade head`
5. **Start Server:** `uvicorn app.main:app --reload`

---

## License
This project is proprietary and not licensed for commercial use.
