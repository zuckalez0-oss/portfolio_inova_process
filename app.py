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
            'titulo': 'Gerador de desenhos DXF para formas simples',
            'setor': 'Engenharia',
            'descricao': 'Um app para geração de DXF e PDF, otimizando o fluxo de trabalho permitindo criação de multiplos desenhos de formas simples com poucos cliques, tirando a necessidade da utilização do Software CAD para criação desses desenhos.',
            'imagem1': 'projeto1.png',
            'link_detalhes': 'https://github.com/zuckalez0-oss/gerador_de_desenhos_pdf' # Link para uma página de detalhes, se houver
        },
        {
            'titulo': 'App para contagem de diagonais e montantes de Treliças',
            'setor': 'Engenharia',
            'descricao': 'Script Python para automação do processo de análise de montantes e diagonais de treliças, o processo era feito manualmente antes e com esse script foi possivel ter um ganho significativo de tempo e redução dos erros humanos.',
            'imagem1': 'projeto2.png',
            'link_detalhes': 'https://github.com/zuckalez0-oss/analisador-de-trelicas'
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

