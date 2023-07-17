from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import Label
from tkinter import ttk
from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import W
from tkinter import E
from tkinter import ttk
from modelo import crud

"""
                    VISTA DE MI APLICACIÓN
        """

class vistaDeApp():
    def __init__(self, window, ) -> None:

        self.entrada = window
        self.entrada.title("Trabajo Final Nivel Intermedio")
        self.entrada.geometry("1020x600")
        self.entrada.config(background='#E3E4E4')
        self.obj = crud()

        self.titulo = Label(self.entrada, text="BOLSAS DE ECOLÓGICAS Y PRODUCTOS DE DISEÑO", font="Arial", justify="center", bg="#56CAC2", fg="#F8F9F9", height=3, width=115)
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

        self.producto = Label(self.entrada, text="Producto")
        self.producto.grid(row=1, column=0, sticky=W)
        self.cantidad=Label(self.entrada, text="Cantidad")
        self.cantidad.grid(row=2, column=0, sticky=W)
        self.precio=Label(self.entrada, text="Precio")
        self.precio.grid(row=3, column=0, sticky=W)
        self.producto.config(bg='#E3E4E4', font='Arial', fg='black')
        self.cantidad.config(bg='#E3E4E4', font='Arial', fg='black')
        self.precio.config(bg='#E3E4E4', font='Arial', fg='black')


        """
                    VARIABLES
        """
        self.mi_id_var, self.pro_var, self.cant_var, self.pre_var = StringVar(), StringVar(), DoubleVar(), DoubleVar()
        mi_ancho = 40

        self.entrada1 = Entry(self.entrada, textvariable = self.pro_var, width = mi_ancho) 
        self.entrada1.grid(row = 1, column = 1, sticky=W)
        self.entrada2 = Entry(self.entrada, textvariable = self.cant_var, width = mi_ancho) 
        self.entrada2.grid(row = 2, column = 1, sticky=W)
        self.entrada3 = Entry(self.entrada, textvariable = self.pre_var, width = mi_ancho) 
        self.entrada3.grid(row = 3, column = 1, sticky=W)
        
        """
                    BOTONES
        """
        self.boton_alta = Button(self.entrada, text="Agregar", command=lambda: self.dar_alta())
        self.boton_alta.grid(row=6, column=1)
        self.boton_alta.config(height=1, width=20)
        
        self.boton_alta = Button(self.entrada, text="Borrar", command=lambda: self.borrar())
        self.boton_alta.grid(row=7, column=1)
        self.boton_alta.config(height=1, width=20)
        
        self.boton_alta = Button(self.entrada, text="Actualizar", command=lambda: self.actualizar())
        self.boton_alta.grid(row=8, column=1)
        self.boton_alta.config(height=1, width=20)
        
        self.boton_alta = Button(self.entrada, text="Modificar", command=lambda: self.modificar())
        self.boton_alta.grid(row=9, column=1)
        self.boton_alta.config(height=1, width=20)


        """
                    TREEVIEW
        """

        self.tree = ttk.Treeview()
        self.tree["columns"]=("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor=W)
        self.tree.column("col1", width=400, minwidth=80)
        self.tree.column("col2", width=150, minwidth=80)
        self.tree.column("col3", width=150, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Producto")
        self.tree.heading("col2", text="Cantidad")
        self.tree.heading("col3", text="Precio")
        self.tree.grid(row=15, column=0, columnspan=4)
    """
    Función dar de alta un nuevo producto
    """     
    def dar_alta(
            self,
        ):
            self.obj.dar_alta(self.pro_var, self.cant_var, self.pre_var, self.tree)
    """
    Función dar de baja un producto
    """    
    def borrar(
            self,
        ):
            self.obj.borrar(self.tree)
    """
    Función para modificar un producto, precio y cantidad
    """  
    def modificar(
            self,
        ):
            self.obj.modificar(self.pro_var, self.pre_var, self.tree)
    """
    Función para actualizar el árbol
    """          
    def actualizar(
            self,
        ):
            self.obj.actualizar_tree(self.tree)




  

        

    