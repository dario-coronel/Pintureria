import logging
from proveedores.entity import Proveedor
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProveedorService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def obtener_todos(self):
        """Obtiene todos los proveedores"""
        try:
            proveedores = self.db_session.query(Proveedor).filter_by(deleted=False).all()
            logger.info(f"Se han obtenido {len(proveedores)} proveedores.")
            return proveedores
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al obtener proveedores: {str(e)}")
            return []

    def obtener_por_id(self, proveedor_id: int):
        """Obtiene proveedor por su ID."""
        try:
            proveedor = self.db_session.query(Proveedor).filter_by(id=proveedor_id, deleted=False).first()
            if proveedor:
                logger.info(f"Proveedor obtenido: {proveedor.razon_social}")
            else:
                logger.warning(f"No se encontró el proveedor con ID: {proveedor_id}")
            return proveedor
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al obtener proveedor por ID: {str(e)}")
            return None

    def agregar_proveedor(self, proveedor_data):
        """Agrega un proveedor."""
        try:
            nuevo_proveedor = Proveedor(
                razon_social=proveedor_data['razon_social'],
                direccion=proveedor_data['direccion'],
                telefono=proveedor_data['telefono'],
                email=proveedor_data['email']
            )
            self.db_session.add(nuevo_proveedor)
            self.db_session.commit()
            logger.info(f"Proveedor añadido: {nuevo_proveedor.razon_social}")
            return nuevo_proveedor
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al agregar proveedor: {str(e)}")
            return None

    def actualizar_proveedor(self, proveedor_id: int, proveedor_data):
        """Actualiza proveedor existente."""
        try:
            proveedor = self.obtener_por_id(proveedor_id)
            if proveedor:
                proveedor.razon_social = proveedor_data['razon_social']
                proveedor.direccion = proveedor_data['direccion']
                proveedor.telefono = proveedor_data['telefono']
                proveedor.email = proveedor_data['email']
                self.db_session.commit()
                logger.info(f"Proveedor actualizado: {proveedor.razon_social}")
                return proveedor
            else:
                logger.warning(f"No se encontró el proveedor con ID: {proveedor_id} para actualizar")
                return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al actualizar proveedor: {str(e)}")
            return None

    def eliminar_proveedor(self, proveedor_id: int):
        """Elimina proveedor."""
        try:
            proveedor = self.obtener_por_id(proveedor_id)
            if proveedor:
                proveedor.deleted = True
                self.db_session.commit()
                logger.info(f"Proveedor eliminado: {proveedor.razon_social}")
                return proveedor
            else:
                logger.warning(f"No se encontró el proveedor con ID: {proveedor_id} para eliminar")
                return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al eliminar proveedor: {str(e)}")
            return None
