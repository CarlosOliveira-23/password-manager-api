from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class PasswordEntry(Base):
    __tablename__ = "password"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    service_name = Column(String, nullable=False)
    encrypted_password = Column(String, nullable=False)

    user = relationship("User", backref="passwords")
