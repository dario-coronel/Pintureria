import logging
from productos.entity import Producto
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Configurar logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductoService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def obtener_todos(self):
        """Obtiene todos los productos"""
        try:
            productos = self.db_session.query(Producto).filter_by(deleted=False).all()
            logger.info(f"Se han obtenido {len(productos)} productos.")
            return productos
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al obtener productos: {str(e)}")
            return []

    def obtener_por_id(self, producto_id: int):
        """Obtiene un producto porID."""
        try:
            producto = self.db_session.query(Producto).filter_by(id=producto_id, deleted=False).first()
            if producto:
                logger.info(f"Producto obtenido: {producto.nombre}")
            else:
                logger.warning(f"No se encontró el producto con ID: {producto_id}")
            return producto
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al obtener producto por ID: {str(e)}")
            return None

    def agregar_producto(self, producto_data):
        """Agrega un producto."""
        try:
            nuevo_producto = Producto(
                codigo=producto_data['codigo'],
                nombre=producto_data['nombre'],
                precio_venta=producto_data['precio_venta'],
                precio_costo=producto_data['precio_costo'],
                categoria=producto_data['categoria'],
                proveedor_id=producto_data['proveedor_id']
            )
            self.db_session.add(nuevo_producto)
            self.db_session.commit()
            logger.info(f"Producto añadido: {nuevo_producto.nombre}")
            return nuevo_producto
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al agregar producto: {str(e)}")
            return None

    def actualizar_producto(self, producto_id: int, producto_data):
        """Actualiza producto existente."""
        try:
            producto = self.obtener_por_id(producto_id)
            if producto:
                producto.codigo = producto_data['codigo']
                producto.nombre = producto_data['nombre']
                producto.precio_venta = producto_data['precio_venta']
                producto.precio_costo = producto_data['precio_costo']
                producto.categoria = producto_data['categoria']
                producto.proveedor_id = producto_data['proveedor_id']
                self.db_session.commit()
                logger.info(f"Producto actualizado: {producto.nombre}")
                return producto
            else:
                logger.warning(f"No se encontró el producto con ID: {producto_id} para actualizar")
                return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al actualizar producto: {str(e)}")
            return None

    def eliminar_producto(self, producto_id: int):
        """Elimina un producto."""
        try:
            producto = self.obtener_por_id(producto_id)
            if producto:
                producto.deleted = True 
                self.db_session.commit()
                logger.info(f"Producto eliminado: {producto.nombre}")
                return producto
            else:
                logger.warning(f"No se encontró el producto con ID: {producto_id} para eliminar")
                return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al eliminar producto: {str(e)}")
            return None
