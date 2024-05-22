from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base





SQLALCHEMY_DATABASE_URL = "postgresql://prasanna:123@localhost:5432/fast_api"
Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Import the models to create the tables



# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

