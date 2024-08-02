from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comparar_numeros', methods=['GET', 'POST'])
def comparar_numeros():
    mayor = menor = None
    error = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])
            nums = [a, b, c]
            mayor = max(nums)
            menor = min(nums)
        except ValueError:
            error = "Por favor, ingrese números válidos."
    return render_template('comparar_numeros.html', mayor=mayor, menor=menor, error=error)

@app.route('/convertir_calificacion', methods=['GET', 'POST'])
def convertir_calificacion():
    letra = None
    error = None
    if request.method == 'POST':
        try:
            nota = float(request.form['nota'])
            if 1 <= nota < 9:
                letra = 'F'
            elif 9 <= nota < 13:
                letra = 'E'
            elif 13 <= nota < 14:
                letra = 'D'
            elif 14 <= nota < 17:
                letra = 'C'
            elif 17 <= nota < 19:
                letra = 'B'
            elif 19 <= nota <= 20:
                letra = 'A'
            else:
                letra = 'Nota fuera de rango.'
        except ValueError:
            error = "Por favor, ingrese una calificación válida."
    return render_template('convertir_calificacion.html', letra=letra, error=error)

@app.route('/calculo_precios', methods=['GET', 'POST'])
def calculo_precios():
    total_pesos = None
    error = None
    if request.method == 'POST':
        try:
            precios = [float(request.form[f'precio{i}']) for i in range(1, 6)]
            total_dolares = sum(precios)
            total_pesos = total_dolares * 18  
        except ValueError:
            error = "Por favor, ingrese precios válidos."
    return render_template('calculo_precios.html', total_pesos=total_pesos, error=error)

@app.route('/dobles_y_triples', methods=['GET', 'POST'])
def dobles_y_triples():
    doble = triple = None
    error = None
    if request.method == 'POST':
        try:
            numero = float(request.form['numero'])
            doble = numero * 2
            triple = numero * 3
        except ValueError:
            error = "Por favor, ingrese un número válido."
    return render_template('dobles_y_triples.html', doble=doble, triple=triple, error=error)

@app.route('/calcular_area', methods=['GET', 'POST'])
def calcular_area():
    figura = None
    area_calculada = None
    error = None
    if request.method == 'POST':
        figura = request.form['figura']
        try:
            if figura == 'circulo':
                radio = float(request.form['radio'])
                area_calculada = 3.14159 * (radio ** 2)
            elif figura == 'cuadrado':
                lado = float(request.form['lado'])
                area_calculada = lado ** 2
            elif figura == 'rectangulo':
                largo = float(request.form['largo'])
                ancho = float(request.form['ancho'])
                area_calculada = largo * ancho
            elif figura == 'triangulo':
                base = float(request.form['base'])
                altura = float(request.form['altura'])
                area_calculada = 0.5 * base * altura
            else:
                error = "Figura no válida."
        except ValueError:
            error = "Por favor, ingrese valores válidos."
    return render_template('calcular_area.html', figura=figura, area=area_calculada, error=error)

if __name__ == '__main__':
    app.run(debug=True)
