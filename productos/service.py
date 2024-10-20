from productos.entity import Producto
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class ProductoService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def obtener_todos(self):
        """Obtiene todos los productos de la base de datos."""
        try:
            return self.db_session.query(Producto).filter_by(deleted=False).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener productos: {str(e)}")
            return []

    def obtener_por_id(self, producto_id: int):
        """Obtiene un producto por su ID."""
        try:
            return self.db_session.query(Producto).filter_by(id=producto_id, deleted=False).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener producto por ID: {str(e)}")
            return None

    def agregar_producto(self, producto_data):
        """Agrega un nuevo producto."""
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
            return nuevo_producto
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error al agregar producto: {str(e)}")
            return None

    def actualizar_producto(self, producto_id: int, producto_data):
        """Actualiza un producto existente."""
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
                return producto
            return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error al actualizar producto: {str(e)}")
            return None

    def eliminar_producto(self, producto_id: int):
        """Elimina (lógica) un producto."""
        try:
            producto = self.obtener_por_id(producto_id)
            if producto:
                producto.deleted = True  # Eliminación lógica
                self.db_session.commit()
                return producto
            return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error al eliminar producto: {str(e)}")
            return None
