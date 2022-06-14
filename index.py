#Se importa Flask
from crypt import methods
from csv import writer
from flask import Flask, render_template,request,redirect, send_file,url_for
#Condigo experimental
#Importar librerias tanto de BytesIO y Pandas
from io import BytesIO
import pandas as pd
#inicializar variable
app = Flask(__name__, template_folder='templates')
#define la ruta

listaFarmacos = []
listaUsuarios = ['root', 'admin']
listaContrasenias = ['root123', 'admin123']

listaOperadores = {'usuario':listaUsuarios , 'contrasenia': listaContrasenias}
listaIdFarmaco = []
listaFarmaco = []
listaProveedor = []
listaPrecio = []
listaStock = []



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
        listaIdFarmaco.append(idFarmaco)
        listaFarmaco.append(farmaco)
        listaProveedor.append(proveedor)
        listaPrecio.append(precio)
        listaStock.append(stock)

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
    '''
    Lista los fármacos
    '''
    return render_template('listaFarmacos.html', listaFarmacos2 = listaFarmacos)

@app.route('/i3',methods=["POST","GET"])
def listaFarm():
    if(request.method == "POST"):
        return redirect(url_for('listar'))

@app.route('/operadores', methods=["POST","GET"])
def usuarios():
    '''
    Lista los operadores de la farmacia
    '''
    return render_template('listaOperadores.html', listaOperadores = listaOperadores)

@app.route('/proveedores', methods=["GET"])
def proveedores():
    '''
    Renderiza la página de proveedores
    '''
    return render_template('proveedores.html')


@app.route('/facturacion', methods=["POST","GET"])
def facturacion():
    '''
    Renderiza la página de facturacion
    '''
    return render_template('facturacion.html')


@app.route('/exportar', methods=["POST"])
def exportar():
    '''
    Exportar la lista de farmacos como archivo de excel mediante el uso de pandas

    '''

    listaFarmas = {'idFarmaco': listaIdFarmaco, 'Farmaco': listaFarmaco, 'Proveedor': listaProveedor, 'Precio': listaPrecio, 'Stock': listaStock}
    datos = pd.DataFrame.from_dict(listaFarmas)
    salida = BytesIO()
    #El escritor se usa para establecer una escritor sobre xlsx para ello se importa también xlsxwriter
    writer = pd.ExcelWriter(salida, engine='xlsxwriter')
    #Se emite los datos a excel agregandolo en una hoja llamada Hoja1
    datos.to_excel(writer, startrow=0, merge_cells=False, sheet_name="Hoja1")
    libro = writer.book
    hojaLibro = writer.sheets["Hoja1"]
    format = libro.add_format()
    format.set_bg_color('#eeeeee')
    hojaLibro.set_column(0,9,28)
    writer.close()
    salida.seek(0)

    return send_file(salida,attachment_filename="ReporteFarmacos.xlsx", as_attachment=True) 
    
#Main, desde el que se ejecuta la aplicación

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=9696)