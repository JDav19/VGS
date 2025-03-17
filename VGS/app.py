from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Base de datos simulada
juegos = [
    {'id': 1, 'nombre': 'The Legend of Zelda', 'precio': 59.99},
    {'id': 2, 'nombre': 'Hollow Knight', 'precio': 7.49},
    {'id': 3, 'nombre': 'Stardew Valley', 'precio': 8.99},
    {'id': 4, 'nombre': 'The Elder Scrolls V: Skyrim', 'precio': 34.99}
]

# Inicializar el carrito en la sesión
@app.before_request
def inicializar_carrito():
    if 'carrito' not in session:
        session['carrito'] = []

@app.route('/')
def index():
    return render_template('index.html', juegos=juegos, carrito=session['carrito'])

@app.route('/agregar/<int:juego_id>')
def agregar_al_carrito(juego_id):
    juego = next((j for j in juegos if j['id'] == juego_id), None)
    if juego and juego not in session['carrito']:
        session['carrito'].append(juego)
        session.modified = True
    return redirect(url_for('index'))

@app.route('/quitar/<int:juego_id>')
def quitar_del_carrito(juego_id):
    session['carrito'] = [j for j in session['carrito'] if j['id'] != juego_id]
    session.modified = True
    return redirect(url_for('index'))

@app.route('/vaciar')
def vaciar_carrito():
    session['carrito'] = []
    session.modified = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
