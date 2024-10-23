from sqlalchemy import Column, Integer, String, Boolean
from config.cnx import Base

class Proveedor(Base):
    __tablename__ = 'proveedores'

    id = Column(Integer, primary_key=True, index=True)
    razon_social = Column(String, unique=True, index=True)
    direccion = Column(String)
    telefono = Column(String)
    email = Column(String, unique=True)
    deleted = Column(Boolean, default=False)
