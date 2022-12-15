class Usuario:
    def __init__(self,nombre,apellido,edad,tipo_usuario,usuario,gmail,contraseña,confirmar_contraseña,documento,telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__tipo_usuario = tipo_usuario
        self.__usuario = usuario
        self.__gmail = gmail
        self.__contraseña = contraseña
        self.__confirmar_contraseña = confirmar_contraseña
        self.__documento = documento
        self.__telefono = telefono
        

    def __str__(self) -> str:
        cadena='Nombre: ' +self.__nombre
        cadena+='\nApellido: ' + self.__apellido
        cadena+='\nEdad: ' + str(self.__edad)
        cadena+='\nTipo Usuario: '+ self.__tipo_usuario
        cadena+='\nUsuario: '+ self.__usuario
        cadena+='\nGmail: '+self.__gmail
        cadena+='\nContraseña: '+self.__contraseña
        cadena+='\nConfirmar Contraseña: ' + self.__confirmar_contraseña
        cadena+='\nDocumento: '+ str(self.__documento)
        cadena+='\nTelefono: '+ str(self.__telefono)
        return cadena

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self,nuevo_apellido):
        self.__apellido = nuevo_apellido

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,nueva_edad):
        self.__edad = nueva_edad 

    @property
    def tipo_usuario(self):
        return self.__tipo_usuario

    @tipo_usuario.setter
    def tipo_usuario(self,nueva_usuario):
        self.__tipo_usuario = nueva_usuario

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self,usuario):
        self.__usuario = usuario

    @property
    def gmail(self):
        return self.__gmail

    @gmail.setter
    def gmail(self,nuevo_gmail):
        self.__gmail = nuevo_gmail
    
    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self,nueva_contraseña):
        self.__contraseña = nueva_contraseña

    @property
    def confirmar_contraseña(self):
        return self.__confirmar_contraseña

    @confirmar_contraseña.setter
    def confirmar_contraseña(self,confirmar_contraseña):
        self.__confirmar_contraseña = confirmar_contraseña

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self,nuevo_documento):
        self.__documento = nuevo_documento

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self,nuevo_telefono):
        self.__telefono = nuevo_telefono


