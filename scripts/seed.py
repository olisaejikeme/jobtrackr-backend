from app.db.session import SessionLocal
from app.enums.role_status import RoleStatus
from app.models.role import Role
from app.models.user import User
from app.core.security import hash_password

def seed():
    db = SessionLocal()
    try:
        # Create roles
        admin_role = db.query(Role).filter_by(name="ADMIN").first()
        user_role = db.query(Role).filter_by(name="USER").first()

        if not admin_role:
            admin_role = Role(name="ADMIN", status=RoleStatus.ACTIVE)
            db.add(admin_role)

        if not user_role:
            user_role = Role(name="USER", status=RoleStatus.ACTIVE)
            db.add(user_role)

        db.commit()

        db.refresh(admin_role)
        db.refresh(user_role)

        # Create admin user
        existing_admin = db.query(User).filter_by(email="admin@jobtrackr.com").first()

        if not existing_admin:
            admin = User(
                name="Admin",
                email="admin@jobtrackr.com",
                password_hash=hash_password("admin123"),
                status="ACTIVE",
                role_id=admin_role.id
            )
            db.add(admin)
            db.commit()

    finally:
        db.close()


if __name__ == "__main__":
    seed()