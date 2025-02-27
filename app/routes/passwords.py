from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.password import PasswordEntry
from app.schemas.password import PasswordCreate, PasswordResponse
from app.services.auth import encrypt_data, decrypt_data
from app.services.auth import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/passwords/", response_model=PasswordResponse)
def store_password(entry: PasswordCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    encrypted_password = encrypt_data(entry.password)
    new_entry = PasswordEntry(user_id=user["id"], service_name=entry.service_name,
                              encrypted_password=encrypted_password)

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry


@router.get("/passwords/", response_model=list[PasswordResponse])
def list_passwords(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    passwords = db.query(PasswordEntry).filter(PasswordEntry.user_id == user["id"]).all()
    return passwords


@router.delete("/passwords/{password_id}")
def delete_password(password_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    entry = db.query(PasswordEntry).filter(PasswordEntry.id == password_id, PasswordEntry.user_id == user["id"]).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Password not found")

    db.delete(entry)
    db.commit()
    return {"message": "Password deleted successfully"}
