from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    # Aqui você pode passar dados para o template
    # Por enquanto, vamos deixar simples
    return render_template('index.html')

# Rota para a página de projetos
@app.route('/projetos')
def projetos():
    # Dados de exemplo para seus projetos (vamos detalhar isso depois)
    meus_projetos = [
        {
            'titulo': 'Sistema de Monitoramento de Linha de Produção',
            'setor': 'Manufatura',
            'descricao': 'Desenvolvimento de um sistema em Flask e MQTT para monitoramento em tempo real de KPIs de produção, resultando em 20% de redução de tempo de inatividade.',
            'imagem': 'projeto1.png',
            'link_detalhes': '#' # Link para uma página de detalhes, se houver
        },
        {
            'titulo': 'Automação de Relatórios de Qualidade',
            'setor': 'Petroquímica',
            'descricao': 'Script Python que automatiza a geração de relatórios de qualidade diários, integrando dados de diferentes fontes e economizando 4 horas/dia de trabalho manual.',
            'imagem': 'projeto2.png',
            'link_detalhes': '#'
        }
    ]
    return render_template('projetos.html', projetos=meus_projetos)

# Rota para a página de contato
@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    # Para rodar no Termux, pode ser necessário especificar o host
    # 0.0.0.0 torna o servidor acessível de outros dispositivos na mesma rede
    app.run(host='0.0.0.0', port=5000, debug=True)

