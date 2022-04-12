from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://<user>:<password>@<ip>/<databaseName>"



engine = create_engine(DATABASE_URL)

localSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

def get_db():
    try:
        db = localSession()
        yield db
    finally:
        db.close()

