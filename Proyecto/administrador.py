from tkinter import *
from tkinter.messagebox import *
import sqlite3 as sql
from menu_admi2 import *


class Administrador():

    def __init__(self,usuario,gmail,contraseña):
        self.usuario = usuario
        self.gmail = gmail
        self.contraseña = contraseña

def admi():
        global entrada_login_usuario
        global entrada_login_contraseña
        global ventana_admi
        ventana_admi=Tk()
        ventana_admi.geometry("400x400")#--> Tamaño
        ventana_admi.title("Menú - Gestión de productos")#-->Título de la ventana
        ventana_admi['bg']='#FFF8DC'
        
       
        icono = PhotoImage(file="Proyecto/rcs/empleados.png") #--> se crea la imagen usando PhotoImage
        ventana_admi.iconphoto(True, icono) 


        entrada_login_usuario= StringVar()
        entrada_login_contraseña = StringVar()

        Label(ventana_admi, text="Usuario: ",bg="#FFF8DC", font="Monserrat",).pack()
        entrada_login_usuario =Entry(ventana_admi, textvariable=entrada_login_usuario, width=20, highlightthickness=1, highlightcolor="blue")   
        entrada_login_usuario.pack()
        Label(ventana_admi, text="",bg="#FFF8DC").pack()

        Label(ventana_admi, text="Contraseña: ",bg="#FFF8DC",font="Monserrat").pack()
        entrada_login_contraseña= Entry(ventana_admi, textvariable=entrada_login_contraseña, show= '*',width=20, highlightthickness=1, highlightcolor="blue")
        entrada_login_contraseña.pack()
        Label(ventana_admi, text="",bg="#FFF8DC").pack()

        Button(ventana_admi, text="Iniciar sesión",font=("Montserrat", 10),cursor="hand2",bg="#A6E441", width=10,height=1,command=login).pack()
        Label(ventana_admi, text="",bg="#FFFFFF").pack()
        Label(text="",bg="#FFFFFF").pack()

        Button(text="Registrarse", height="1", font=("Montserrat", 10), width="10", bg="tan1",cursor="hand2",command=fromulario).pack() # botón "Registrarse".
        Label(text="",bg="#FFFFFF").pack()

        Button(text="Cerrar ventana", font=("Montserrat", 10), height="1", width="15", bg="tan1",cursor="hand2",command=ventana_admi.destroy).pack()
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
    ventana_registro['bg']= "#FFF8DC"

    Label(ventana_registro, text="Complete los siguientes datos: ",font=("Calibri", 11),bg="#FFF8DC").pack()
    Label(ventana_registro, text="",bg="#FFF8DC").pack()

    usuario = StringVar()
    gmail = StringVar()
    contraseña = StringVar()

    usuario = Label(ventana_registro, text="Usuario: ",bg="#FFF8DC")
    usuario.pack()
    usuario= Entry(ventana_registro, textvariable=usuario,width=20, highlightthickness=1, highlightcolor="blue") # textvariable, es una variable que se mostrará como texto
    usuario.pack()

    gmail = Label(ventana_registro, text="Correo: ",bg="#FFF8DC")
    gmail.pack()
    gmail= Entry(ventana_registro, textvariable=gmail, width=20, highlightthickness=1, highlightcolor="blue")  
    gmail.pack()
    
    contraseña = Label(ventana_registro,text="Contraseña: ",bg="#FFF8DC")
    contraseña.pack()
    contraseña=Entry(ventana_registro,textvariable=contraseña, show='*',width=20, highlightthickness=1, highlightcolor="blue")
    contraseña.pack()
    Label(ventana_registro, text="",bg="#FFF8DC").pack()
    Button(ventana_registro,text="Finalizar", height="1", width="10", bg="tan1",cursor="hand2",command=registrarse).pack() 
    Label(text="",bg="#FFF8DC").pack()

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
    
    
    

