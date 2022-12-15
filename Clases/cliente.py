from usuario import Usuario
from tkinter import *
from tkinter.messagebox import *
import sqlite3


class Cliente(Usuario):
    def __init__(self,nombre,apellido,edad,usuario,gmail,contraseña,documento,telefono):
     super().__init__(nombre,apellido,edad,usuario,gmail,contraseña,documento,telefono) 
     """
     super()--> la función super() de  nos permite referirnos a la superclase (usuario). 
     Además,o solo puede referirse a la __init__()función, 
     sino que también puede llamar a todas las demás funciones de la superclase.(usuario,no tiene funciones) 
     """

#Ventana principal
def ventana_inicio():
        global entrada_login_usuario
        global entrada_login_contraseña
        global ventana_inicio
        ventana_inicio=Tk()
        ventana_inicio.geometry("400x400")#-->Tamaño
        ventana_inicio.title("Supermark")#-->Titulo de la ventana
        ventana_inicio['bg']='turquoise'
        Label(text="Bienvenido", bg="turquoise", width="300", height="2", font=("Calibri", 13)).pack() 
        Label(text="",bg="turquoise").pack()

        entrada_login_usuario= StringVar()
        entrada_login_contraseña = StringVar()

        Label(ventana_inicio, text="Usuario: ",bg="turquoise").pack()
        entrada_login_usuario =Entry(ventana_inicio, textvariable=entrada_login_usuario)
        entrada_login_usuario.pack()
        Label(ventana_inicio, text="",bg="turquoise").pack()

        Label(ventana_inicio, text="Contraseña: ",bg="turquoise").pack()
        entrada_login_contraseña= Entry(ventana_inicio, textvariable=entrada_login_contraseña, show= '*')
        entrada_login_contraseña.pack()
        Label(ventana_inicio, text="",bg="turquoise").pack()

        Button(ventana_inicio, text="Iniciar sesión",cursor="hand2",bg="tan1", width=10, height=1,command=login).pack()
        Label(ventana_inicio, text="",bg="turquoise").pack()
        Label(text="",bg="turquoise").pack()

        Button(text="Registrarse", height="1", width="10", bg="tan1",cursor="hand2",command=registro).pack() # botón "Registrarse".
        Label(text="",bg="turquoise").pack()

        Button(text="Cerrar ventana", height="1", width="15", bg="tan1",cursor="hand2",command=ventana_inicio.destroy).pack()
        ventana_inicio.mainloop()

# Registro
def registro():
    #variables globales
    global ventana_registro
    global nombre
    global apellido
    global edad
    global gmail
    global documento
    global usuario
    global contraseña
    global repetir_contraseña

    
    """
    StringVar()--> viene de tkinter,es usada para algunos widgets,son variable de control y al  mismo tiempo la usamos con textvariable,
    a la que se le asigna la variable que tiene la StrinVar()
    Las variables de control se declaran de forma diferente en función al tipo de dato que almacenan:
    StringVar() --> Declara variable de tipo cadena
    """ 

    nombre = StringVar()
    apellido=  StringVar()
    edad=  StringVar()
    gmail= StringVar()
    documento=  StringVar()
    usuario=  StringVar()
    contraseña =  StringVar()
    repetir_contraseña= StringVar()

    ventana_registro = Tk()
    ventana_registro.title("Registro")
    ventana_registro.geometry("400x500")
    ventana_registro['bg']='turquoise'

    Label(ventana_registro, text="Para un registro exitoso,complete los siguientes datos: ",font=("Calibri", 11),bg="turquoise").pack()
    Label(ventana_registro, text="",bg="turquoise").pack()

    nombre = Label(ventana_registro, text="Nombre: ",bg="turquoise")
    nombre.pack()
    nombre= Entry(ventana_registro, textvariable=nombre) # textvariable ---> es una variable que se mostrará como texto
    nombre.pack()

    apellido = Label(ventana_registro, text="Apellido: ",bg="turquoise")
    apellido.pack()
    apellido= Entry(ventana_registro,textvariable=apellido)
    apellido.pack()

    edad =Label(ventana_registro,text="Edad: ",bg="turquoise")
    edad.pack()
    edad=Entry(ventana_registro,textvariable=edad)
    edad.pack()

    gmail = Label(ventana_registro,text="Gmail: ",bg="turquoise")
    gmail.pack()
    gmail=Entry(ventana_registro,textvariable=gmail)
    gmail.pack()

    documento = Label(ventana_registro,text="Documento: ",bg="turquoise")
    documento.pack()
    documento=Entry(ventana_registro,textvariable=gmail)
    documento.pack()

    usuario = Label(ventana_registro,text="Nombre de usuario: ",bg="turquoise")
    usuario.pack()
    usuario=Entry(ventana_registro,textvariable=usuario)
    usuario.pack()

    contraseña = Label(ventana_registro,text="Contraseña: ",bg="turquoise")
    contraseña.pack()
    contraseña=Entry(ventana_registro,textvariable=contraseña, show='*')
    contraseña.pack()

    repetir_contraseña = Label(ventana_registro,text="Repetir contraseña: ",bg="turquoise")
    repetir_contraseña.pack()
    repetir_contraseña=Entry(ventana_registro,textvariable=repetir_contraseña, show='*')
    repetir_contraseña.pack()

    Label(ventana_registro, text="",bg="turquoise").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="tan1",cursor="hand2",command=registrarse).pack()

#Base de datos
def crearBD():
    con =sqlite3.connect('clientes.db')
    con.commit()
    con.close()

def crear_tabla(): 
    con =sqlite3.connect('clientes.db')
    cursor= con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTEGER NOT NULL,nombre TEXT NOT NULL ,apellido TEXT,edad INTEGER NOT NULL,correo TEXT,documento INTEGER NOT NULL,usuario TEXT,contraseña TEXT, repetir contraseña TEXT,PRIMARY KEY(id AUTOINCREMENT))")
    con.commit()
    con.close()

#Funciones con base de datos
#Login
def login():
    if validar():
        con =sqlite3.connect('clientes.db')
        cursor = con.cursor()
        
        usuario = entrada_login_usuario.get()
        contra  = entrada_login_contraseña.get()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ? ", (usuario,contra))
        
        if cursor.fetchall():
            showinfo(title='Login exitoso',message='Sesion iniciada correctamente')
        else:
            showerror(title='ups, algo ha salido mal', message='usuario o contraseña incorrectos')
        con.close()

        """
        El método get() obtiene el valor que tenga, las variable de control. 
        Se utiliza cuando es necesario leer el valor de un control
        """

#Registro
def registrarse():
    if validacion():
        con = sqlite3.connect("clientes.db")
        cursor = con.cursor()

        nomb= nombre.get()
        appe= apellido.get()
        eda= edad.get()
        correo1 = gmail.get()
        doc= documento.get()
        usua = usuario.get()
        contra = contraseña.get()
        repe= repetir_contraseña.get()

        if(contra==repe):
            cursor.execute("INSERT INTO usuarios VALUES(NULL,\'"+nomb+"\',\'"+appe+"\', \'"+eda+"\',\'"+correo1+"\',\'"+doc+"\',\'"+usua+"\',\'"+contra+"\',\'"+repe+"\')")
            showinfo(title='Registro exitoso',message='Se registró correctamente.')
            ventana_registro.destroy()#--> destroy(): permite destruir la ventana despues de que el showinfo
        else:
            showerror(title='Error en la contraseña',message='Las contraseñas no coinciden.')
        con.commit()
        con.close()


##### Otras funciones #####
def validar(): #--> validacion para login
    return len(entrada_login_usuario.get())!=0 and len(entrada_login_contraseña.get())!=0
     
def validacion(): #--> validacion para registro
    return len(nombre.get()) !=0 and len(apellido.get())!=0 and len(edad.get()) !=0 and len(gmail.get()) !=0 and len(documento.get()) !=0 and len(usuario.get())!=0 and len(contraseña.get())!=0 and len(repetir_contraseña.get())!=0

ventana_inicio()

if __name__=="__main__":#--> permite poder escribir o llamar las funciones sin perjudicar el codígo
 #crearBD() -->se llama a la función y se crea la base de datos 
 #crear_tabla() -->se llama a la función crea las tablas en la base
 pass
