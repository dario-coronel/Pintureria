from flask import Flask
from config.cnx import db  # Importamos la configuración de la base de datos
from clientes.routes import cliente_bp
from productos.routes import producto_bp
from proveedores.routes import proveedor_bp

def create_app():
    """
    Crea la aplicación Flask y la configura con la base de datos y los blueprints.
    """
    app = Flask(__name__)
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pintureria.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Registramos los blueprints
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    app.register_blueprint(producto_bp, url_prefix='/productos')
    app.register_blueprint(proveedor_bp, url_prefix='/proveedores')

    return app
