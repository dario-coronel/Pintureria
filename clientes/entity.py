from sqlalchemy import Column, Integer, String
from config.cnx import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    direccion = Column(String, nullable=True)
    email = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    cuit = Column(String, nullable=True)
    deleted = Column(Integer, default=0)  # 0: Activo, 1: Eliminado
