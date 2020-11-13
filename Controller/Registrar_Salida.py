
from tkinter import messagebox as mb #
from Model.Reigstro import RegistroSalida
from Model.ProductoSalida import ProductosSalidas_BD



class LogicaSalidas(RegistroSalida):

    def __init__(self):

        self.Instancia_salida=ProductosSalidas_BD()


    #######Validar si existen datos para guardar#########
    def Validacion_create(self):
        return len(self.codigoV.get()) != 0 and\
               len(self.nombreV.get()) != 0 and\
               len(self.categoriaV.get() != 0 and\
               len(self.colorV.get())) != 0 and\
               len(self.modeloV.get()) != 0 and\
               len(self.precioV.get()) != 0

    def Create_salida(self):
        if self.Validacion_create():
            self.datos = (self.codigoV.get(),
                          self.nombreV.get(),
                          self.categoriaV.get(),
                          self.colorV.get(),
                          self.modeloV.get(),
                          self.precioV.get())
            self.Instancia_salida.CreateProductos_venta(self.datos)
            mb.showinfo("Información", "Los datos fueron guardados")
            self.codigoV.set(' ')
            self.nombreV.set(' ')
            self.categoriaV.set(' ')
            self.colorV.set(' ')
            self.modeloV.set(' ')
            self.precioV.set(' ')
            #self.totalV.set(' ')
        else:
            mb.showinfo("Error","Rellene todos los campos")


    def Read_salida(self):  # Obtener los usuarios
        Records = self.tabla2.get_children()  # Mostrar datos de la tabla
        for element in Records:  # ciclo para limpiarla en caso de que tenga información
            self.tabla2.delete(element)  # comando delete

        DbRows = self.Instancia_salida.ReadProductos_venta()  # hacer que las filas vayan aumentando atuomáticamente
        for row in DbRows:  # Rellenar los datos
            self.tabla2.insert("", 0,text=row[0],
                                  values=(row[1],
                                          row[2],
                                          row[3],
                                          row[4],
                                          row[5]))  # Espacios para ingresar los nuevos datos

