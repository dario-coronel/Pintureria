import logging
from clientes.entity import Cliente
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ClienteService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def obtener_todos(self):
        """Obtiene todos los clientes de la base de datos."""
        try:
            clientes = self.db_session.query(Cliente).filter_by(deleted=False).all()
            logger.info(f"Se han obtenido {len(clientes)} clientes.")
            return clientes
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al obtener clientes: {str(e)}")
            return []

    def obtener_por_id(self, cliente_id: int):
        """Obtiene un cliente por su ID."""
        try:
            cliente = self.db_session.query(Cliente).filter_by(id=cliente_id, deleted=False).first()
            if cliente:
                logger.info(f"Cliente obtenido: {cliente.nombre}")
            else:
                logger.warning(f"No se encontró el cliente con ID: {cliente_id}")
            return cliente
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al obtener cliente por ID: {str(e)}")
            return None

    def agregar_cliente(self, cliente_data):
        """Agrega un nuevo cliente."""
        try:
            nuevo_cliente = Cliente(
                nombre=cliente_data['nombre'],
                direccion=cliente_data['direccion'],
                telefono=cliente_data['telefono'],
                email=cliente_data['email'],
                localidad=cliente_data['localidad']
            )
            self.db_session.add(nuevo_cliente)
            self.db_session.commit()
            logger.info(f"Cliente añadido: {nuevo_cliente.nombre}")
            return nuevo_cliente
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al agregar cliente: {str(e)}")
            return None

    def actualizar_cliente(self, cliente_id: int, cliente_data):
        """Actualiza un cliente existente."""
        try:
            cliente = self.obtener_por_id(cliente_id)
            if cliente:
                cliente.nombre = cliente_data['nombre']
                cliente.direccion = cliente_data['direccion']
                cliente.telefono = cliente_data['telefono']
                cliente.email = cliente_data['email']
                cliente.localidad = cliente_data['localidad']
                self.db_session.commit()
                logger.info(f"Cliente actualizado: {cliente.nombre}")
                return cliente
            else:
                logger.warning(f"No se encontró el cliente con ID: {cliente_id} para actualizar")
                return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al actualizar cliente: {str(e)}")
            return None

    def eliminar_cliente(self, cliente_id: int):
        """Elimina (lógica) un cliente."""
        try:
            cliente = self.obtener_por_id(cliente_id)
            if cliente:
                cliente.deleted = True  # Eliminación lógica
                self.db_session.commit()
                logger.info(f"Cliente eliminado: {cliente.nombre}")
                return cliente
            else:
                logger.warning(f"No se encontró el cliente con ID: {cliente_id} para eliminar")
                return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            logger.error(f"Error al eliminar cliente: {str(e)}")
            return None
