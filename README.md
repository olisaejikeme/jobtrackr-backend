# JobTrackr Backend

Backend service for managing job applications, resumes, and user authentication.

## Live API & Docs
* **Base URL:** [https://jobtrackr-api-fatu.onrender.com](https://jobtrackr-api-fatu.onrender.com)
* **Swagger UI:** [https://jobtrackr-api-fatu.onrender.com/docs](https://jobtrackr-api-fatu.onrender.com/docs)

> **Performance Note:** > As this is hosted on a Render Free Instance, the service spins down after periods of inactivity. The first request may experience a **Cold Start delay of up to 90 seconds**.

---

## Tech Stack
* **Framework:** FastAPI
* **ORM:** SQLAlchemy
* **Migrations:** Alembic
* **Database:** PostgreSQL
* **Auth:** JWT (JSON Web Tokens)

---

## Features
* **Secure Auth:** JWT-based login and registration.
* **RBAC:** Role-Based Access Control for Users and Admins.
* **Applications Management:** Robust API for tracking job search status.
* **Resume Logic:** Tools for associating resumes with specific applications.
* **Soft Delete:** Data recovery safety using soft-delete logic.
* **Architecture:** Clean, modular **Service-Repository** pattern.

---

## Local Setup
1. Clone the repo and navigate to the root.
2. Create a `.env` file with `DATABASE_URL` and `SECRET_KEY`.
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `alembic upgrade head`
5. Start server: `uvicorn app.main:app --reload`

---

## License
This project is proprietary and not licensed for commercial use.
