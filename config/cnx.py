from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexión a SQLite (puedes cambiar a otro motor si lo necesitas)
DATABASE_URL = "sqlite:///./pintureria.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Inicialización de la base de datos
def init_db():
    Base.metadata.create_all(bind=engine)
