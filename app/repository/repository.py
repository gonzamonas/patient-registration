from sqlmodel import Session

from app.models.patient import Patient


async def save_patient(
    session: Session, name: str, email: str, phone: str, document_path: str
) -> None:
    new_patient = Patient(
        name=name, email=email, phone=phone, document_path=document_path
    )
    session.add(new_patient)
    session.commit()
    session.refresh(new_patient)
