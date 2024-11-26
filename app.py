from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('index.html')


@app.route('/imagens')
def imagens():
    return render_template('imagens.html')

@app.route('/desabafo', methods=['GET', 'POST'])
def desabafo ():
    if request.method == 'POST':
        nome = request.form['nome']
        assunto = request.form['assunto']
        desabafo = request.form['desabafo']

        return render_template('desabafo.html', nome=nome, assunto=assunto, desabafo=desabafo)
    return render_template('desabafo.html', nome=None, assunto=None, desabafo=None)

if __name__ == '__main__':
    app.run(debug=True)
