from typing import List
from fastapi import  APIRouter, Depends
from sqlalchemy.orm import Session
from .. import  schemas, connection
from ..repository import user

router = APIRouter(
    tags=['Users'],
    prefix='/user'
)

@router.get('/', response_model=List[schemas.User])
def show_users(db: Session = Depends(connection.get_db)):
    return user.get_all(db)

@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id:int, db: Session = Depends(connection.get_db)):
    return user.get_user(id, db)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(connection.get_db)):
    return user.create(request, db)

@router.put('/{id}', response_model=schemas.User)
def update_user(usuario_id:int, entrada: schemas.UserUpdate, db: Session = Depends(connection.get_db)):
    return user.modify(usuario_id, entrada, db)

@router.delete('/{id}', response_model=schemas.Respuesta)
def delete_user(usuario_id:int, db: Session = Depends(connection.get_db)):
    return user.delete(usuario_id, db)