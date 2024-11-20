from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session
from config.db import get_db
from models import userModel
from schemas import userSchema
from schemas import document_schema
from config.cloudinary_config import upload_pdf,delete_pdf
from datetime import datetime


user = APIRouter()


@user.post("/users", response_model=userSchema.UserResponse)
def create_user(user: userSchema.UserCreate, db: Session = Depends(get_db)):
    new_user = userModel.User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@user.get("/users", response_model=list[userSchema.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(userModel.User).all()
    return users


@user.post("/documents", response_model=document_schema.DocumentResponse)
def upload_document(date: str = Form(...),
                    type: str = Form(...),
                    grade: int = Form(...),
                    section: str = Form(...),
                    file: UploadFile = None,
                    db: Session = Depends(get_db)):
    try:
        url = upload_pdf(file)

        new_document = userModel.Document(
            date=datetime.strptime(date, "%Y-%m").date(),
            url=url,
            type=type,
            grade=grade,
            section=section
        )
        db.add(new_document)
        db.commit()
        db.refresh(new_document)
        return new_document
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user.get("/documents", response_model=list[document_schema.DocumentResponse])
def get_all_documents(db: Session = Depends(get_db)):
    documents = db.query(userModel.Document).all()
    return documents


@user.get("/documents/{id}", response_model=document_schema.DocumentResponse)
def get_document_by_id(id: int, db: Session = Depends(get_db)):
    # try
    document = db.query(userModel.Document).filter(
        userModel.Document.id == id).first()

    if not document:
        
        raise HTTPException(status_code=404, detail="Document not found")

    return document
  
@user.get("/documents/type/{type}", response_model=list[document_schema.DocumentResponse])
def get_documents_by_type(type: str, db: Session = Depends(get_db)):
    # try
    documents = db.query(userModel.Document).filter(
        userModel.Document.type == type).all()

    if not documents:
        
        raise HTTPException(status_code=404, detail="Document not found")

    return documents
  
@user.delete("/document/{id}", status_code=204)
async def delete_document(id: int, db: Session = Depends(get_db)):
  document = db.query(userModel.Document).filter(userModel.Document.id == id).first()
  if not document:
      raise HTTPException(status_code=404, detail="Documento no encontrado")
  delete_pdf(document)
  
  db.delete(document)
  db.commit()
  return {"detail": "Documento eliminado correctamente"}
  
  
    
  
    


# @user.get("/users")
# def get_users():
#     return conn.execute(users.select()).fetchall()

# @user.post("/users")
# def create_users(user:User):
#     new_user = {"name":user.name}
#     result = conn.execute(users.insert().values(new_user))
#     print(result)
#     return "ejecutado"
