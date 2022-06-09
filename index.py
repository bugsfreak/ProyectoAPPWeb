#Se importa Flask
from flask import Flask, render_template,request,redirect,url_for

#inicializar variable
app = Flask(__name__, template_folder='templates')
#define la ruta

listaFarmacos = []
listaUsuarios = ['root', 'admin']
listaContrasenias = ['root123', 'admin123']
listaOperadores = []

listaOperadores.append({'usuario':listaUsuarios , 'contrasenia': listaContrasenias})




#Ruta que mostrará el login 
@app.route('/')
def login():
    '''
    Función para redireccionar a la página principal del login
    '''
    return redirect(url_for('paginaLogin'))


@app.route('/login')
def paginaLogin():
    '''
    Función que renderiza la página de login.html
    '''
    return render_template('login.html')


@app.route('/i1', methods=["POST","GET"])
def inicio():
    '''
    Función que redirecciona a la página de inicio
    '''
    if(request.method == "POST"):
        return redirect(url_for('paginaInicio'))

        
@app.route('/inicio', methods=["POST","GET"])
def paginaInicio():
    '''
    Función que renderiza la página de inicio.html
    '''
    if(request.method == "POST"):
        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']
        if((usuario in listaUsuarios) and (contrasenia in listaContrasenias)):
            return render_template('inicio.html')
        else:
            return redirect(url_for('paginaLogin'))



@app.route('/paginaFarmacos', methods=["POST","GET"])
def paginaFarmacos():
    '''
    Función que renderiza la página de farmacos.html
    '''
    return render_template('farmacos.html', listaFarmacos = listaFarmacos)


@app.route('/i2', methods=["POST","GET"])
def farmacos():
    '''
    Función que redirecciona a la pagina de fármacos
    '''
    if(request.method == "POST"):
        return redirect(url_for('paginaFarmacos'))



@app.route('/ingreso', methods=["POST","GET"])
def ingresoFarmaco():
    '''
    Función que realiza el ingreso de fármacos
    '''
    if(request.method == "POST"):
        idFarmaco = request.form['idFarmaco']
        farmaco = request.form['farmaco']
        proveedor = request.form['proveedor']
        precio = request.form['precio']
        stock = request.form['stock']
        listaFarmacos.append({'idFarmaco': idFarmaco, 'farmaco': farmaco , 'proveedor': proveedor, 'precio': precio, 'stock': stock})
        return redirect(url_for('paginaFarmacos'))


@app.route('/vaciar', methods=["POST","GET"])
def vaciar():
    '''
    Función para vaciar la lista de fármacos
    '''
    if(request.method == "POST"):
        listaFarmacos.clear()
        return redirect(url_for('paginaFarmacos'))



@app.route('/listar',methods=["POST","GET"])
def listar():
    return render_template('listaFarmacos.html', listaFarmacos2 = listaFarmacos)

@app.route('/i3',methods=["POST","GET"])
def listaFarm():
    if(request.method == "POST"):
        return redirect(url_for('listar'))

@app.route('/operadores', methods=["POST","GET"])
def usuarios():
    return render_template('listaOperadores.html', listaOperadores = listaOperadores)

@app.route('/proveedores', methods=["GET"])
def proveedores():
    return render_template('proveedores.html')
    
#Main, desde el que se ejecuta la aplicación

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=9696)