from tkinter import Tk
import vista

"""
CONTROLADOR

A partir del controlador, es posible ejecutar la APP de Registro de Ventas
"""

class Controlador:

    def __init__(self, root_w):
        self.root_controlador = root_w
        self.objeto_vista = vista.vistaDeApp(self.root_controlador)
    
if __name__ == "__main__":
    entrada_tk = Tk()
    application = Controlador(entrada_tk)

    application.objeto_vista.actualizar()
    
    entrada_tk.mainloop()