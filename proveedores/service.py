from proveedores.entity import Proveedor
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class ProveedorService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def obtener_todos(self):
        """Obtiene todos los proveedores de la base de datos."""
        try:
            return self.db_session.query(Proveedor).filter_by(deleted=False).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener proveedores: {str(e)}")
            return []

    def obtener_por_id(self, proveedor_id: int):
        """Obtiene un proveedor por su ID."""
        try:
            return self.db_session.query(Proveedor).filter_by(id=proveedor_id, deleted=False).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener proveedor por ID: {str(e)}")
            return None

    def agregar_proveedor(self, proveedor_data):
        """Agrega un nuevo proveedor."""
        try:
            nuevo_proveedor = Proveedor(
                razon_social=proveedor_data['razon_social'],
                direccion=proveedor_data['direccion'],
                telefono=proveedor_data['telefono'],
                email=proveedor_data['email']
            )
            self.db_session.add(nuevo_proveedor)
            self.db_session.commit()
            return nuevo_proveedor
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error al agregar proveedor: {str(e)}")
            return None

    def actualizar_proveedor(self, proveedor_id: int, proveedor_data):
        """Actualiza un proveedor existente."""
        try:
            proveedor = self.obtener_por_id(proveedor_id)
            if proveedor:
                proveedor.razon_social = proveedor_data['razon_social']
                proveedor.direccion = proveedor_data['direccion']
                proveedor.telefono = proveedor_data['telefono']
                proveedor.email = proveedor_data['email']
                
                self.db_session.commit()
                return proveedor
            return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error al actualizar proveedor: {str(e)}")
            return None

    def eliminar_proveedor(self, proveedor_id: int):
        """Elimina (lógica) un proveedor."""
        try:
            proveedor = self.obtener_por_id(proveedor_id)
            if proveedor:
                proveedor.deleted = True  # Eliminación lógica
                self.db_session.commit()
                return proveedor
            return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error al eliminar proveedor: {str(e)}")
            return None
