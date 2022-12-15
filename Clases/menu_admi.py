from tkinter import *
from tkinter.messagebox import * 
import sqlite3 as sql

#Ventana del menú principal
def ventana_inicio():
    global ventana_principal
    
    ventana_principal=Tk()
    ventana_principal.geometry("300x300")
    ventana_principal.title("Supermark")
    ventana_principal['bg']='turquoise'
    
    Label(text="Menú", bg="turquoise", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Label(text="",bg="turquoise").pack()

    Button(text="Agregar artículo", height="2", width="30",cursor="hand2", bg="tan1", command=agregar_articulo).pack() #BOTÓN "Acceder" seria insertar
    Label(text="",bg="turquoise").pack()
    
    Button(text="Modificar artículo", height="2", width="30",cursor="hand2", bg="tan1", command=modificar_Articulo).pack() #BOTÓN "Acceder"
    Label(text="",bg="turquoise").pack()

    Button(text="Eliminar artículo", height="2", width="30",cursor="hand2", bg="tan1", command=eliminar_articulo).pack() #BOTÓN "Acceder"
    Label(text="",bg="turquoise").pack()


    ventana_principal.mainloop()

#Agregar artículo
def agregar_articulo():
        
        global ventana_agregar
        ventana_agregar = Toplevel(ventana_principal,bg="turquoise")
        ventana_agregar.title("Agregar artículo")
        ventana_agregar.geometry("310x310")
 
        
        global marca
        global categoria
        global nombre
        global precio
        global stock

        
        marca = StringVar()
        categoria = StringVar()
        nombre = StringVar()
        precio = StringVar()
        stock = StringVar()


        marca=Label(ventana_agregar,text="Marca: ",bg="turquoise")
        marca.pack()
        marca=Entry(ventana_agregar,textvariable=marca)
        marca.pack()
    
        categoria = Label(ventana_agregar,text="Categoría: ",bg="turquoise")
        categoria.pack()
        categoria=Entry(ventana_agregar,textvariable=categoria)
        categoria.pack()

        nombre = Label(ventana_agregar,text="Nombre: ",bg="turquoise")
        nombre.pack()
        nombre=Entry(ventana_agregar,textvariable=nombre)
        nombre.pack()
        
        precio = Label(ventana_agregar,text="Precio venta: ",bg="turquoise")
        precio.pack()
        precio=Entry(ventana_agregar,textvariable=precio)
        precio.pack()
        
        stock= Label(ventana_agregar,text="Stock: ",bg="turquoise")
        stock.pack()
        stock=Entry(ventana_agregar,textvariable=stock)
        stock.pack()

        Label(ventana_agregar, text="",bg="turquoise").pack()
        Button(ventana_agregar,text="Agregar", width=10, height=1,cursor="hand2",bg="tan1",command=insertar ).pack()
    

#Modificar artículo
def modificar_Articulo(): 
        global ventana_modificar
        ventana_modificar = Toplevel(ventana_principal,bg="turquoise")
        ventana_modificar.title("Modíficar artículo")
        ventana_modificar.geometry("310x310")
 
        global id
        global precio_venta
        global stock

        id= StringVar()
        precio_venta = StringVar()
        stock= StringVar()    

        id = Label(ventana_modificar,text="Id: ",bg="turquoise")
        id.pack()
        id=Entry(ventana_modificar,textvariable=id)
        id.pack()

        precio_venta = Label(ventana_modificar,text="Precio venta: ",bg="turquoise")
        precio_venta.pack()
        precio_venta=Entry(ventana_modificar,textvariable=precio_venta)
        precio_venta.pack()
        
        stock = Label(ventana_modificar,text="Stock: ",bg="turquoise")
        stock.pack()
        stock=Entry(ventana_modificar,textvariable=stock)
        stock.pack()
        

        Label(ventana_modificar, text="",bg="turquoise").pack()
        Button(ventana_modificar,text="Modíficar", width=10, height=1,cursor="hand2",bg="tan1",command=modificar).pack()


#Eliminar artículo
def eliminar_articulo():
        global ventana_eliminar
        ventana_eliminar = Toplevel(ventana_principal,bg="turquoise")
        ventana_eliminar.title("Eliminar artículo")
        ventana_eliminar.geometry("310x210")
 
        global id
        
        Label(ventana_eliminar, text="Ingrese el id del artículo a eliminar:", bg="turquoise", font=("Calibri", 11)).pack()
        Label(ventana_eliminar, text="", bg="turquoise").pack()

        id = Label(ventana_eliminar,text="Id: ",bg="turquoise")
        id.pack()
        id=Entry(ventana_eliminar,textvariable=id)
        id.pack()
    
        Label(ventana_eliminar, text="",bg="turquoise").pack()
        Button(ventana_eliminar,text="Eliminar", width=10, height=1,cursor="hand2",bg="tan1",command=eliminar).pack()



#BASE DE DATOS
#para agregar un artículo
def insertar():
    con = sql.connect("productos.db")
    cursor = con.cursor()

    marc= marca.get()
    cat = categoria.get()
    nomb = nombre.get()
    press = precio.get()
    stoc= stock.get()

    cursor.execute("INSERT INTO articulos VALUES (NULL,\'"+marc+"\',\'"+cat+"\',\'"+nomb+"\',\'"+press+"\',\'"+stoc+"\')")
    showinfo(title='Artículo agregado',message='El artículo se agregó correctamente')
    ventana_agregar.destroy()    
    con.commit()
    con.close()

#para modificar un artículo
def modificar():
    con = sql.connect("productos.db")
    cursor = con.cursor()

    cod= id.get()
    precio = precio_venta.get()
    stoc = stock.get()

   
    cursor.execute(f"UPDATE articulos SET precio='{precio}',stock='{stoc}' WHERE id='{cod}'")
    showinfo(title='Artículo modifica',message='El artículo se modifico correctamente')
    ventana_modificar.destroy()
    
    con.commit()
    con.close()

#para eliminar un artículo
def eliminar():
    con = sql.connect("productos.db")
    cursor = con.cursor()

    code = id.get()
    cursor.execute(f"DELETE FROM articulos WHERE id = {code} ")
    showinfo(title='Articulo eliminado',message='El artículo se elimino correctamente')
    ventana_eliminar.destroy()
    con.commit()
    con.close()

    
if __name__=="__main__":
    ventana_inicio()