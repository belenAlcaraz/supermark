from tkinter import *
from tkinter.messagebox import *
import sqlite3 as sql
from usuario import Usuario
from menu_admi2 import *


class Administrador(Usuario):

    def __init__(self,usuario,gmail,contraseña):
     super().__init__(usuario,gmail,contraseña)
     """
     super()--> la función super() de  nos permite referirnos a la superclase (usuario). 
     Además,o solo puede referirse a la __init__()función, 
     sino que también puede llamar a todas las demás funciones de la superclase.(usuario,no tiene funciones) 
     """

def admi():
        global entrada_login_usuario
        global entrada_login_contraseña
        global ventana_admi
        ventana_admi=Tk()
        ventana_admi.geometry("400x400")#--> Tamaño
        ventana_admi.title("Inicio")#-->Título de la ventana
        ventana_admi['bg']='turquoise'
        Label(text="Bienvenido administrador", bg="turquoise", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
        Label(text="",bg="turquoise").pack()
    
        entrada_login_usuario= StringVar()
        entrada_login_contraseña = StringVar()

        Label(ventana_admi, text="Usuario: ",bg="turquoise").pack()
        entrada_login_usuario =Entry(ventana_admi, textvariable=entrada_login_usuario)   
        entrada_login_usuario.pack()
        Label(ventana_admi, text="",bg="turquoise").pack()

        Label(ventana_admi, text="Contraseña: ",bg="turquoise").pack()
        entrada_login_contraseña= Entry(ventana_admi, textvariable=entrada_login_contraseña, show= '*')
        entrada_login_contraseña.pack()
        Label(ventana_admi, text="",bg="turquoise").pack()

        Button(ventana_admi, text="Iniciar sesión",cursor="hand2",bg="tan1", width=10, height=1,command=login).pack()
        Label(ventana_admi, text="",bg="turquoise").pack()
        Label(text="",bg="turquoise").pack()

        Button(text="Registrarse", height="1", width="10", bg="tan1",cursor="hand2",command=fromulario).pack() # botón "Registrarse".
        Label(text="",bg="turquoise").pack()

        Button(text="Cerrar ventana", height="1", width="15", bg="tan1",cursor="hand2",command=ventana_admi.destroy).pack()
        ventana_admi.mainloop()

#ventana para rellenar el registro
def fromulario():
    global ventana_registro
    global usuario
    global gmail
    global contraseña

    ventana_registro = Tk()
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x330")
    ventana_registro['bg']='turquoise'

    Label(ventana_registro, text="Complete los siguientes datos: ",font=("Calibri", 11),bg="turquoise").pack()
    Label(ventana_registro, text="",bg="turquoise").pack()

    usuario = StringVar()
    gmail = StringVar()
    contraseña = StringVar()

    usuario = Label(ventana_registro, text="Usuario: ",bg="turquoise")
    usuario.pack()
    usuario= Entry(ventana_registro, textvariable=usuario) # textvariable, es una variable que se mostrará como texto
    usuario.pack()

    gmail = Label(ventana_registro, text="Correo: ",bg="turquoise")
    gmail.pack()
    gmail= Entry(ventana_registro, textvariable=gmail)  
    gmail.pack()
    
    contraseña = Label(ventana_registro,text="Contraseña: ",bg="turquoise")
    contraseña.pack()
    contraseña=Entry(ventana_registro,textvariable=contraseña, show='*')
    contraseña.pack()
    Label(ventana_registro, text="",bg="turquoise").pack()
    Button(ventana_registro,text="Finalizar", height="1", width="10", bg="tan1",cursor="hand2",command=registrarse).pack() 
    Label(text="",bg="turquoise").pack()

#Base de dato
def base_admi():
    con = sql.connect("usuarios.db")
    con.commit()
    con.close()

   
# Login
def login():
    if val1():
        con = sql.connect("usuarios.db")
        cursor = con.cursor()

        usuario = entrada_login_usuario.get()
        contra  = entrada_login_contraseña.get()
        cursor.execute("SELECT * FROM usuario WHERE usuario = ? AND contraseña = ? ", (usuario,contra))

        if cursor.fetchall():
            showinfo(title='Login exitoso',message='Sesion iniciada correctamente')
            ventana_admi.destroy()
            main()
            
        else:
            showerror(title='ups, algo ha salido mal', message='usuario o contraseña incorrectos')
        con.close()


def registrarse(): 
    if val2():
        con = sql.connect("usuarios.db")
        cursor = con.cursor()

        usua = usuario.get()
        correo1 = gmail.get()
        contra = contraseña.get()
        
        cursor.execute("INSERT INTO usuario VALUES(NULL,\'"+usua+"\',\'"+correo1+"\',\'"+contra+"\')")
        showinfo(title='Registro exitoso',message='Se registró correctamente')
        ventana_registro.destroy()
        con.commit()
        con.close()

###### Otras funciones ######

def val1(): #---> para login
    return len(entrada_login_usuario.get())!=0 and len(entrada_login_contraseña.get())!=0

def val2():#-->para registro
    return len(usuario.get())!=0 and len(gmail.get())!=0 and len(contraseña.get()) !=0 



if __name__=="__main__":
    admi()
    #base_admi() --> se llama a la funcion para crea la base 
    
    
    

