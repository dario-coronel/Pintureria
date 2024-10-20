from config import create_app  # Importamos la función para crear la app

# Crear la aplicación Flask
app = create_app()

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
