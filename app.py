from flask import Flask, render_template

app = Flask(__name__)

users = [
    {
        'nome': 'João Silva',
        'email': 'joao.silva@email.com',
        'role': 'admin',
        'gastos': [
            {
                'tipo': 'Alimentação',
                'valor': 450.75
            },
            {
                'tipo': 'Transporte',
                'valor': 180.50
            }
        ],
        'renda': [
            {
                'fonte': 'Salário',
                'valor': 5200.00
            },
            {
                'fonte': 'Freelance',
                'valor': 850.00
            }
        ]
    },
    {
        'nome': 'Maria Oliveira',
        'email': 'maria.oliveira@email.com',
        'role': 'member',
        'gastos': [
            {
                'tipo': 'Moradia',
                'valor': 1200.00
            },
            {
                'tipo': 'Lazer',
                'valor': 320.40
            }
        ],
        'renda': [
            {
                'fonte': 'Salário',
                'valor': 4300.00
            }
        ]
    },
    {
        'nome': 'Carlos Santos',
        'email': 'carlos.santos@email.com',
        'role': 'member',
        'gastos': [
            {
                'tipo': 'Educação',
                'valor': 650.00
            },
            {
                'tipo': 'Saúde',
                'valor': 210.90
            }
        ],
        'renda': [
            {
                'fonte': 'Bolsa de Estudos',
                'valor': 1800.00
            },
            {
                'fonte': 'Estágio',
                'valor': 1400.00
            }
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/quadros', methods=['GET', 'POST'])
def quadros():
    return render_template('quadros.html')

@app.route('/quadros/quadro')
def quadro():
    return render_template('quadro.html', secao=1)


@app.route('/quadros/quadro/gastos')
def gastos():
    return render_template('gastos.html', secao=2, users=users)


@app.route('/quadros/quadro/renda')
def renda():
    return render_template('renda.html', secao=3, users=users)


@app.route('/quadros/quadro/membros')
def membros():
    return render_template('membros.html', secao=4, users=users)


@app.route('/quadros/quadro/configuracoes')
def config():
    return render_template('config.html', secao=5)