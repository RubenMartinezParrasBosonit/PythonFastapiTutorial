from sqlalchemy.orm import Session
from .. import  model, schemas, hashing
from fastapi import HTTPException, status

def get_all(db: Session):
    users = db.query(model.User).all()
    return users

def get_user(id: int, db: Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    return user

def create(request: schemas.User, db: Session):
    user = model.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def modify(usuario_id: int, entrada: schemas.UserUpdate, db: Session):
    usuario = db.query(model.User).first_by(id=usuario_id).first()
    usuario.nombre = entrada.nombre
    db.commit()
    db.refresh(usuario)
    return usuario

def delete(usuario_id: int, db: Session):
    usuario = db.query(model.User).first_by(id=usuario_id).first()
    db.delete(usuario)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta