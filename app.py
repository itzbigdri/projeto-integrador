from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/quadros/')
def quadros():
    return render_template('quadros.html')

@app.route('/quadros/quadro')
def quadro():
    return render_template('quadro.html')


@app.route('/quadros/quadro/gastos')
def gastos():
    return render_template('gastos.html')


@app.route('/quadros/quadro/renda')
def renda():
    return render_template('renda.html')


@app.route('/quadros/quadro/membros')
def membros():
    return render_template('membros.html')


@app.route('/quadros/quadro/configuracao')
def config():
    return render_template('config.html')