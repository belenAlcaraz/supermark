from tkinter import *
from tkinter import ttk
from menu_admi import *

class Ventana(Frame): #--> Frame:contenedor de los demás widgets
    def __init__(self,master=None): # __init__ --> el contructor recibe ancho y alto de la ventana
        super().__init__(master,width=790,height=360)
        self.master = master 
        self.pack() #-->pack() permite mostrar los widgets 
        self.create_widgets()
        self.mostrar()

    #Funciones utilizando base de datos:
    def agregar(self):
        
        con = sql.connect("productos.db")
        cursor = con.cursor()

        marc = self.marca.get()
        cate= self.categoria.get()
        nomb = self.nombre.get()
        press = self.precio.get()
        stoc= self.stock.get()
        
        cursor.execute("INSERT INTO articulos VALUES (NULL,\'"+marc+"\',\'"+cate+"\',\'"+nomb+"\',\'"+press+"\',\'"+stoc+"\')")
        showinfo(title='Artículo agregado',message='El artículo se agregó correctamente')  
        con.commit()
        con.close()

    def modificar(self):
        con = sql.connect("productos.db")
        cursor = con.cursor()

        cod= self.id.get()
        stoc = self.stock.get()
        precio = self.precio.get()
    
        cursor.execute(f"UPDATE articulos SET precio='{precio}',stock='{stoc}' WHERE id='{cod}'")
        showinfo(title='Artículo modifica',message='El artículo se modificó correctamente')        
        con.commit()
        con.close()

    def eliminar(self):
        con = sql.connect("productos.db")
        cursor = con.cursor()

        code = self.id.get()

        cursor.execute(f"DELETE FROM articulos WHERE id = {code} ")
        showinfo(title='Articulo eliminado',message='El artículo se eliminó correctamente')
        con.commit()
        con.close()

    def mostrar(self): 
        con = sql.connect("productos.db")
        cursor = con.cursor()
        cursor.execute("SELECT * from articulos")
        datos = cursor
        for row in datos:
            self.grid.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
        
    ############# Otras funciones ###################
        
    def limpiar(self):
        """
        Para limpia los entry se usa el metodo delete.
        Se pasa como parametro 0 (a partir de donde empieza a borrar) hasta end (el final)
        """ 
        self.id.delete(0,END)
        self.marca.delete(0,END)
        self.categoria.delete(0,END)
        self.nombre.delete(0,END)
        self.stock.delete(0,END)
        self.precio.delete(0,END)
        
    def limpiaGrid(self):  
        """ doc oficial
        get_children()--> Devuelve la lista de hijos pertenecientes al elemento 
        """
        for item in self.grid.get_children():
            self.grid.delete(item)
    
    def actualizar(self):  
        self.limpiaGrid()
        self.mostrar()

    ############ widgets #################   
     
    def create_widgets(self): 
        #Elementos del Frame1
        frame1 = Frame (self, bg="turquoise")
        frame1.place(x=0,y=0,width=93,height=369)
        
        self.boton1=Button(frame1,text="Agregar", comman=self.agregar,bg="tan1",fg="black",cursor="hand2")
        self.boton1.place(x=5,y=50,width=80,height=30)  

        self.boton2=Button(frame1,text="Modificar",comman=self.modificar,bg="tan1",fg="black",cursor="hand2")
        self.boton2.place(x=5,y=90,width=80,height=30)

        self.boton3=Button(frame1,text="Eliminar",comman=self.eliminar,bg="tan1",fg="black",cursor="hand2")
        self.boton3.place(x=5,y=130,width=80,height=30)

        self.botonLimpiar=Button(frame1,text="Limpiar",command=self.limpiar,bg="tan1",fg="black",cursor="hand2")
        self.botonLimpiar.place(x=5,y=189,width=80,height=30)

        #Elementos del Frame2
        frame2 = Frame (self, bg="turquoise")
        frame2.place(x=95,y=0,width=150,height=369)

        lb1= Label(frame2,text="id: ",bg="turquoise") #label --> no lleva "self" por que no se va a modificar
        lb1.place(x=3,y=5)
        self.id=Entry(frame2) 
        self.id.place(x=3,y=23,width=100,height=20)

        lb2= Label(frame2,text="marca: ",bg="turquoise")  
        lb2.place(x=3,y=55)
        self.marca=Entry(frame2)
        self.marca.place(x=3,y=75,width=100,height=20)

        lb3= Label(frame2,text="categoria: ",bg="turquoise")  
        lb3.place(x=3,y=100)
        self.categoria=Entry(frame2)
        self.categoria.place(x=3,y=130,width=100,height=20)

        lb4=Label(frame2,text="nombre:",bg="turquoise")
        lb4.place(x=3,y=158)
        self.nombre=Entry(frame2)
        self.nombre.place(x=3,y=180,width=100,height=20)

        lb5=Label(frame2,text="cantidad: ",bg="turquoise")
        lb5.place(x=3,y=203)
        self.stock=Entry(frame2)
        self.stock.place(x=3,y=235,width=100,height=20)

        lb6=Label(frame2,text="precio: ",bg="turquoise")
        lb6.place(x=3,y=263)
        self.precio=Entry(frame2)
        self.precio.place(x=3,y=285,width=100,height=20)

        self.botonActualizar=Button(frame2,text="Actualizar",command=self.actualizar,bg="green",fg="black",cursor="hand2")
        self.botonActualizar.place(x=10,y=314,width=60,height=30)


        #Elemtentos del Frame3 --> donde se puede visualizar la tabla 
         
        frame3=Frame(self,bg="gold")
        frame3.place(x=247,y=0,width=530,height=369)

        """ 
        El widget ttk.Treeview muestra la informacion en tabla, dicha info se muestran en columnas
        se puede acceder a las columnas por número o nombres simbólicos enumerados 
        en las columnas de opciones del widget. 
        """        
        self.grid = ttk.Treeview(frame3,columns=("col1","col2","col3","col4","col5",))

        #Ancho de las columnas y ‘CENTER’, muestra el elemento centrado.
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=90,anchor=CENTER)
        self.grid.column("col2",width=90,anchor=CENTER)
        self.grid.column("col3",width=90,anchor=CENTER)
        self.grid.column("col4",width=90,anchor=CENTER)
        self.grid.column("col5",width=90,anchor=CENTER)
        #La columna #0 siempre hace referencia a la columna del árbol,seria el id, que se genera automaticamente
        
        # heading --> permite edicar el encabezados

        self.grid.heading("#0",text="Id",anchor=CENTER) 
        self.grid.heading("col1",text="marca",anchor=CENTER)
        self.grid.heading("col2",text="categoria",anchor=CENTER)
        self.grid.heading("col3",text="nombre",anchor=CENTER)
        self.grid.heading("col4",text="precio",anchor=CENTER)
        self.grid.heading("col5",text="stock",anchor=CENTER)
        
        self.grid.pack(side=LEFT)#--> coloca el grid a la izquierdda

        """Creacion del Scrollbar vertical:
         se crea la variable sbar que contiene el Scrollbar.
         Con pack() se coloca el Scrollbar del lado derecho y  
         fill indica al widget que crezca hasta la cantidad de espacio disponible 
         para él en la dirección especificada (Y).
         yscrollcommand: Se utiliza para comunicarse con las barras deslizantes verticales
        
        Para añadir la barra vertical se asigna la opción yscrollcommand al método set de la barra (sbar.set) y
        se configura la barra de desplazamiento con el comando yview 
        xview --> para barra de desplazamiento horizontal
        yview --> para barra de desplazamiento vertical

        set() --> Se utiliza para modificar el valor o estado de un widget:
        """

        sbar = Scrollbar(frame3,orient=VERTICAL) 
        sbar.pack(side=RIGHT,fill= Y)
        self.grid.config(yscrollcommand=sbar.set)
        sbar.config(command=self.grid.yview)