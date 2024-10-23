from clientes.entity import Cliente
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class ClienteService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def obtener_todos(self):
        try:
            return self.db_session.query(Cliente).filter_by(deleted=False).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener clientes: {str(e)}")
            return []

    def obtener_por_id(self, cliente_id: int):
        try:
            return self.db_session.query(Cliente).filter_by(id=cliente_id, deleted=False).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener cliente por ID: {str(e)}")
            return None

    def agregar_cliente(self, cliente_data):
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
            return nuevo_cliente
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error al agregar cliente: {str(e)}")
            return None

    def actualizar_cliente(self, cliente_id: int, cliente_data):
        try:
            cliente = self.obtener_por_id(cliente_id)
            if cliente:
                cliente.nombre = cliente_data['nombre']
                cliente.direccion = cliente_data['direccion']
                cliente.telefono = cliente_data['telefono']
                cliente.email = cliente_data['email']
                cliente.localidad = cliente_data['localidad']
                
                self.db_session.commit()
                return cliente
            return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error al actualizar cliente: {str(e)}")
            return None

    def eliminar_cliente(self, cliente_id: int):
        try:
            cliente = self.obtener_por_id(cliente_id)
            if cliente:
                cliente.deleted = True  # Eliminación lógica
                self.db_session.commit()
                return cliente
            return None
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error al eliminar cliente: {str(e)}")
            return None
