from pintureria import create_app  # Importamos la función de crear la app

# Crear la aplicación Flask
app = create_app()

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)

