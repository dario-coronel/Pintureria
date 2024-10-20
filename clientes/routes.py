from flask import Blueprint, request, render_template, redirect, url_for
from sqlalchemy.orm import Session
from config.cnx import SessionLocal
from clientes.entity import Cliente

clientes_bp = Blueprint('clientes', __name__)

# Listar clientes
@clientes_bp.route('/clientes')
def listar_clientes():
    session = SessionLocal()
    clientes = session.query(Cliente).all()
    session.close()
    return render_template('clientes.html', clientes=clientes)

# Crear nuevo cliente
@clientes_bp.route('/clientes/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        session = SessionLocal()
        nuevo_cliente = Cliente(
            nombre=request.form['nombre'],
            direccion=request.form['direccion'],
            telefono=request.form['telefono'],
            email=request.form['email'],
            localidad=request.form['localidad']
        )
        session.add(nuevo_cliente)
        session.commit()
        session.close()
        return redirect(url_for('clientes.listar_clientes'))
    return render_template('nuevo_cliente.html')
