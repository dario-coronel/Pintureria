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

    #def __repr__(self):
    #    return f"<Cliente(id={self.id}, nombre={self.nombre}, apellido={self.apellido})>"

    #def to_dict(self):
    #    """Método para convertir la instancia del cliente a un diccionario."""
    #    return {
    #        "id": self.id,
    #        "nombre": self.nombre,
    #        "apellido": self.apellido,
    #        "direccion": self.direccion,
    #        "email": self.email,
    #        "telefono": self.telefono,
    #        "cuit": self.cuit,
    #        "deleted": self.deleted
    #     }

