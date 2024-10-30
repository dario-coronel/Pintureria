from flask import Flask, render_template
from config.cnx import init_db
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pintureria.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        init_db()  
    
    from productos.routes import productos_bp
    from clientes.routes import clientes_bp
    from proveedores.routes import proveedores_bp
    
    app.register_blueprint(productos_bp, url_prefix='/productos')
    app.register_blueprint(clientes_bp, url_prefix='/clientes')
    app.register_blueprint(proveedores_bp, url_prefix='/proveedores')
    
    @app.route('/')
    def index():
        template_path = os.path.join(app.template_folder, 'index.html')
        if os.path.exists(template_path):
             return render_template('index.html') 
        else:
            return f"Template not found at path: {template_path}"

    return app
