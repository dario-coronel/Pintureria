from flask import Flask
from config.cnx import init_db
from flask_sqlalchemy import SQLAlchemy

# Crear la instancia global de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la base de datos para Flask-SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pintureria.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # Asegurarnos de que las tablas se creen solo una vez
    with app.app_context():
        init_db()  # Esto inicializará la base de datos
    
    # Registrar los blueprints
    from productos.routes import productos_bp
    from clientes.routes import clientes_bp
    from proveedores.routes import proveedores_bp
    
    app.register_blueprint(productos_bp, url_prefix='/productos')
    app.register_blueprint(clientes_bp, url_prefix='/clientes')
    app.register_blueprint(proveedores_bp, url_prefix='/proveedores')
    
    return app
