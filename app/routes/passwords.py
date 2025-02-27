from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.password import PasswordEntry
from app.schemas.password import PasswordCreate, PasswordResponse
from app.services.dependencies import get_current_user
from app.services.security import encrypt_data, decrypt_data
from app.core.logging_config import logger

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/passwords/", response_model=PasswordResponse)
def store_password(
        entry: PasswordCreate,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    encrypted_password = encrypt_data(entry.password)
    new_entry = PasswordEntry(
        user_id=user["id"],
        service_name=entry.service_name,
        encrypted_password=encrypted_password
    )

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    logger.info(f"User '{user['username']}' stored a password for '{entry.service_name}'")

    return new_entry


@router.get("/passwords/", response_model=list[PasswordResponse])
def list_passwords(
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    passwords = db.query(PasswordEntry).filter(PasswordEntry.user_id == user["id"]).all()
    logger.info(f"User '{user['username']}' retrieved stored passwords")
    return passwords


@router.get("/passwords/{password_id}", response_model=PasswordResponse)
def get_password(
        password_id: int,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    entry = db.query(PasswordEntry).filter(
        PasswordEntry.id == password_id, PasswordEntry.user_id == user["id"]
    ).first()

    if not entry:
        logger.warning(f"User '{user['username']}' attempted to access a non-existing password (ID: {password_id})")
        raise HTTPException(status_code=404, detail="Password not found")

    decrypted_password = decrypt_data(entry.encrypted_password)
    logger.info(f"User '{user['username']}' retrieved password for '{entry.service_name}'")

    return PasswordResponse(
        id=entry.id,
        service_name=entry.service_name,
        encrypted_password=decrypted_password
    )


@router.delete("/passwords/{password_id}")
def delete_password(
        password_id: int,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    entry = db.query(PasswordEntry).filter(
        PasswordEntry.id == password_id, PasswordEntry.user_id == user["id"]
    ).first()

    if not entry:
        logger.warning(f"User '{user['username']}' attempted to delete a non-existing password (ID: {password_id})")
        raise HTTPException(status_code=404, detail="Password not found")

    db.delete(entry)
    db.commit()

    logger.info(f"User '{user['username']}' deleted password ID {password_id}")

    return {"message": "Password deleted successfully"}
