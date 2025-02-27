from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    passwords = relationship("PasswordEntry", back_populates="user")
