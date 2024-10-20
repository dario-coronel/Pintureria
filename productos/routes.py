from flask import Blueprint, request, render_template, redirect, url_for
from sqlalchemy.orm import Session
from config.cnx import SessionLocal
from productos.entity import Producto
from proveedores.entity import Proveedor

productos_bp = Blueprint('productos', __name__)

# Listar productos
@productos_bp.route('/productos')
def listar_productos():
    session = SessionLocal()
    productos = session.query(Producto).all()
    session.close()
    return render_template('productos.html', productos=productos)

# Crear nuevo producto
@productos_bp.route('/productos/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        session = SessionLocal()
        nuevo_producto = Producto(
            codigo=request.form['codigo'],
            nombre=request.form['nombre'],
            precio_venta=request.form['precio_venta'],
            precio_costo=request.form['precio_costo'],
            proveedor_id=request.form['proveedor_id'],
            categoria=request.form['categoria']
        )
        session.add(nuevo_producto)
        session.commit()
        session.close()
        return redirect(url_for('productos.listar_productos'))
    return render_template('nuevo_producto.html')
