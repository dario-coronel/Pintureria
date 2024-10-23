from sqlalchemy import Column, Integer, String, Float, ForeignKey
from config.cnx import Base 

class Producto(Base):
    __tablename__ = 'productos'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Float)
    categoria = Column(String)
    stock = Column(Integer)
    proveedor_id = Column(Integer)
    proveedor_id = Column(Integer, ForeignKey('proveedores.id'))  
    categoria = Column(String)  
