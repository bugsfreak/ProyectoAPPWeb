#Se importa Flask
from flask import Flask, render_template,request,redirect,url_for

#inicializar variable
app = Flask(__name__, template_folder='templates')
#define la ruta

listaFarmacos = []

#Ruta que mostrará el login 
@app.route('/')
def login():

    return redirect(url_for('paginaLogin'))


@app.route('/login')
def paginaLogin():

    return render_template('login.html')


@app.route('/i1', methods=["POST","GET"])
def inicio():
    if(request.method == "POST"):
        return redirect(url_for('paginaInicio'))

        

@app.route('/inicio', methods=["POST","GET"])
def paginaInicio():
    return render_template('inicio.html')

#Main, desde el que se ejecuta la aplicación

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=9696)