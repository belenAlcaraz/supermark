import tkinter as tk
import sqlite3 as sql

def kiwi():
    #Para añadir un producto al carrito de compras
    def agregar_producto():
        pass
    """ 
    con = sqlite3.connect('productos.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    producto = cursor
     """

    # Para vaciar el carrito de compras
    def vaciar_carrito():
        pass

    # Ventana principal
    ventana = tk.Tk()
    ventana.title("Kiwi Market")

    icono = tk.PhotoImage(file="Proyecto/rcs/kiwi.png") #--> se crea la imagen usando PhotoImage
    ventana.iconphoto(True, icono) 
    """
    --> El método iconphoto() de la instancia de la ventana. 
    Este método toma dos argumentos: el primero es True para indicar que el icono es para la ventana principal,
    y el segundo es el objeto PhotoImage que contiene la imagen del icono.
    """

    #Conexion a la base de datos
    def mostrar_productos():
     con = sql.connect("productos.db")
     cursor = con.cursor()
     cursor.execute("SELECT nombre,precio,stock FROM articulos") #Obtener los productos de la bd
     datos = cursor
        # Insertar los productos en la lista de productos disponibles
     #for row in datos:
      #  lista_disponibles.insert(tk.END, "{:<20s}{:<10s}{:<10s}".format(row[0], str(row[1]), str(row[2])))
        
     con.close()

    # Marco principal de la ventana
    marco_principal = tk.Frame(ventana, bg="#FFF8DC", padx=20, pady=20)
    marco_principal.pack(expand=True, fill="both")

    # Crear el marco para el carrito de compras
    marco_carrito = tk.Frame(marco_principal, bg="#FFF8DC", padx=10, pady=10)
    marco_carrito.pack(side="right", fill="y")

   
    etiqueta_carrito = tk.Label(marco_carrito, text="Carrito de Compras", font=("Helvetica", 14, "bold"))
    etiqueta_carrito.pack(side="top")

    # Crear el Listbox para mostrar los productos disponibles
    #lista_disponibles = tk.Listbox(ventana, width=40, height=20)
    #lista_disponibles.pack(side="left", fill="both", expand=True)

    
    boton_vaciar = tk.Button(marco_carrito, text="Vaciar Carrito", command=vaciar_carrito)
    boton_vaciar.pack(side="bottom")

    # Crear el marco para la lista de productos disponibles
    marco_productos = tk.Frame(marco_principal, bg="white", padx=10, pady=10)
    marco_productos.pack(side="left", fill="both", expand=True)

   
    etiqueta_productos = tk.Label(marco_productos, text="Productos Disponibles", font=("Helvetica", 14, "bold"))
    etiqueta_productos.pack(side="top")

    # Crear la lista de productos disponibles
    #lista_disponibles = tk.Listbox(marco_productos, width=40, height=20)
    #lista_disponibles.pack(side="left", fill="both", expand=True)

    # Crear el botón para añadir productos al carrito de compras
    boton_agregar = tk.Button(marco_productos, text="Agregar al Carrito", command=agregar_producto)
    boton_agregar.pack(side="bottom", pady=10)

    #llamar funcion
    mostrar_productos()

    # Iniciar el bucle principal de la ventana
    ventana.mainloop()

if __name__ == '__main__':
  kiwi()