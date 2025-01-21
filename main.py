from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para el formulario 1: Notas
@app.route('/formulario1', methods=['GET', 'POST'])
def formulario1():
    promedio = None
    estado = None
    if request.method == 'POST':
        # Obtener datos del formulario
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        # Calcular promedio y estado
        promedio = (nota1 + nota2 + nota3) / 3
        estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

    # Renderizar el formulario con resultados (si existen)
    return render_template('form1.html', promedio=promedio, estado=estado)

# Ruta para el formulario 2: Nombres
@app.route('/formulario2', methods=['GET', 'POST'])
def formulario2():
    nombre = None
    longitud = None
    if request.method == 'POST':
        # Obtener datos del formulario
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]
        # Calcular el nombre más largo y su longitud
        nombre = max(nombres, key=len)
        longitud = len(nombre)

    # Renderizar el formulario con resultados (si existen)
    return render_template('form2.html', nombre=nombre, longitud=longitud)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
