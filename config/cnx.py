from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexión a SQLite 
DATABASE_URL = "sqlite:///./pintureria.db"

# Crear el engine de SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Crear la sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para la creación de modelos
Base = declarative_base()

# Función para inicializar la base de datos (crear tablas)
def init_db():
    Base.metadata.create_all(bind=engine)
