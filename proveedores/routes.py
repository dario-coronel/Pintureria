from flask import Blueprint, request, render_template, redirect, url_for
from sqlalchemy.orm import Session
from config.cnx import SessionLocal
from proveedores.entity import Proveedor

proveedores_bp = Blueprint('proveedores', __name__)

# Listar proveedores
@proveedores_bp.route('/proveedores')
def listar_proveedores():
    session = SessionLocal()
    proveedores = session.query(Proveedor).all()
    session.close()
    return render_template('proveedores.html', proveedores=proveedores)

# Crear nuevo proveedor
@proveedores_bp.route('/proveedores/nuevo', methods=['GET', 'POST'])
def nuevo_proveedor():
    if request.method == 'POST':
        session = SessionLocal()
        nuevo_proveedor = Proveedor(
            razon_social=request.form['razon_social'],
            direccion=request.form['direccion'],
            telefono=request.form['telefono'],
            email=request.form['email']
        )
        session.add(nuevo_proveedor)
        session.commit()
        session.close()
        return redirect(url_for('proveedores.listar_proveedores'))
    return render_template('nuevo_proveedor.html')
