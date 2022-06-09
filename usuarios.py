
class usuarios:

    def __init__(self):
        self.usuario = ''
        self.contrasenia = ''

    def setUsuario(self,usuario):
        self.usuario = usuario
    
    def setContrasenia(self,contrasenia):
        self.contrasenia = contrasenia

    def getUsuario(self):
        return self.usuario

    def getContrasenia(self):
        return self.contrasenia