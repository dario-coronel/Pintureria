from sqlalchemy import Column, Integer, String, Float, ForeignKey
from config.cnx import Base

class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True)
    nombre = Column(String, index=True)
    precio_venta = Column(Float)
    precio_costo = Column(Float)
    proveedor_id = Column(Integer, ForeignKey('proveedores.id'))  # Relación con proveedores
    categoria = Column(String)  # Pinturas, Pinceles, Otros
