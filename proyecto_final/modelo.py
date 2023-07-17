import sqlite3
from tkinter import *
from peewee import *
from tkinter import messagebox
import validacion_re
from observador import Sujeto
import datetime

db = SqliteDatabase("mi_baseapp2.db")

class BaseModel(Model):
    class Meta:
        database = db

class Registro(BaseModel):
    producto = CharField(unique=False)
    cantidad = CharField()
    precio = CharField()
    
    def __str__(self,):
        return f"El título es: {self.producto} con descripción: {self.precio}"

db.connect()
db.create_tables([Registro])

"""
        DECORADORES
"""

def decorador_alta(funcion):
    def envoltura(*args):
        funcion(*args)
        print(datetime.date.today())
        mi_fecha=datetime.date.today()
        print(funcion.__name__)
        mi_producto = f" El usuario ha ejecutado {funcion.__name__}"
        print(mi_producto)
        mi_texto=str(mi_fecha)+", "+mi_producto
        
        argumentos = (
            "Producto" + str(args[1].get()),
            "Cantidad" + str(args[2].get()),
            "Precio" + str(args[3].get())
        )
        
        for valor in args:
            print(valor)
            print(type(valor))
            mi_texto=mi_texto + ", " + str(argumentos)

        mi_texto=mi_texto + "\n "
        archivo = open("decoradores.txt", "a")
        archivo.write(mi_texto)
        archivo.close()
        funcion(*args)
        
    return envoltura 

def decorador_borrar(funcion):
    def envoltura(*args):
        funcion(*args)
        mi_producto = f"El usuario ha ejecutado {funcion.__name__}"
        print(mi_producto)
        
    return envoltura

def decorador_modificar(funcion):
    def envoltura(*args):
        funcion(*args)
        mi_producto = funcion.__name__
        print(f"Modificado {mi_producto}")
        
    return envoltura

def decorador_actualizar(funcion):
    def envoltura(*args):
        funcion(*args)
        mi_producto = funcion.__name__
        print(f"El cliente ha ejecutado actualizar {mi_producto}")
        
        
    return envoltura

class crud(Sujeto):
    
    def __init__(
        self, 
    ): pass
        
    @decorador_alta
    def dar_alta(self, producto, cantidad, precio, tree):
        noticia=Registro()
        noticia.producto = producto.get()
        noticia.cantidad = cantidad.get()
        noticia.precio = precio.get()
        noticia.save()
        
        self.actualizar_tree(tree)
        self.notificar(producto.get(), cantidad.get(), precio.get())
    
    @decorador_actualizar    
    def actualizar_tree(self, tree):
        records = tree.get_children()
        try:
            for element in records:
                tree.delete(element)
        finally:
            for fila in Registro.select():
                tree.insert("", 0, text=fila.id, values=(fila.producto, fila.cantidad, fila.precio))
              
    @decorador_borrar          
    def borrar(self, tree):
        item_seleccionado = tree.focus()
        valor_id = tree.item(item_seleccionado)
        borrar=Registro.get(Registro.id==valor_id["text"])
        borrar.delete_instance()
        self.actualizar_tree(tree)
        
    @decorador_modificar    
    def modificar(self, pro_var, pre_var, tree):
        item_seleccionado = tree.focus()
        valor_id = tree.item(item_seleccionado)
        actualizar = Registro.update(producto = pro_var.get(), precio = pre_var.get()).where(Registro.id == valor_id["text"])
        actualizar.execute()

        self.actualizar_tree(tree)    
        



            
    
    
        
        

            

    