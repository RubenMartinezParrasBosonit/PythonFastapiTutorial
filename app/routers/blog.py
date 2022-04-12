from typing import List
from fastapi import  APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import  schemas, connection, oauth2
from ..repository import blog

router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(connection.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(connection.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(connection.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(connection.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(connection.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get(id, db)