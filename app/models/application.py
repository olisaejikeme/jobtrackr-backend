from datetime import date

from sqlalchemy import Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    company_name: Mapped[str] = mapped_column(String, nullable=False)
    job_title: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=True)

    status: Mapped[str] = mapped_column(String, nullable=False)
    application_date: Mapped[date] = mapped_column(Date, nullable=True)

    job_link: Mapped[str] = mapped_column(String, nullable=True)
    job_description: Mapped[str] = mapped_column(Text, nullable=True)

    resume_id: Mapped[int] = mapped_column(Integer, ForeignKey("resumes.id"), nullable=True)

    notes: Mapped[str] = mapped_column(Text, nullable=True)

    # Relationships
    user = relationship("User", back_populates="applications")
    resume = relationship("Resume", back_populates="applications")