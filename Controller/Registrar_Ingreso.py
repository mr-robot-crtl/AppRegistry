
from tkinter import messagebox as mb #
from Model.Reigstro import RegistroIngreso
from Model.ProductoIngreso import ProductosIngresos_BD



class LogicaIngresos(RegistroIngreso):


   def __init__(self):
      self.Instancia_ingreso = ProductosIngresos_BD()

   ##########CREATE PRODUCTOS##############
   def validacionCreate(self):
      return len(self.nombre.get()) != 0 and \
             len(self.categoria.get()) != 0 and\
             len(self.color.get()) != 0 and \
             len(self.modelo.get()) != 0 and \
             len(self.precio.get()) != 0

   def Create_ingresos(self):
      if self.validacionCreate():

         self.datos = (self.nombre.get(),
                       self.categoria.get(),
                       self.color.get(),
                       self.modelo.get(),
                       self.precio.get())
         self.Instancia_ingreso.Create_producto(self.datos)
         mb.showinfo("Información", "Los datos fueron guardados")
         self.LimpiarRegistro_ingresos()

      else:
         mb.showerror("Error","Por favor rellene todas las opsiones")


   ##########READ PRODUCTOS##############
   def Read_ingresos(self):  # Obtener los usuarios
      Records = self.tabla1.get_children()  # Mostrar datos de la tabla
      for element in Records:  # ciclo para limpiarla en caso de que tenga información
         self.tabla1.delete(element)  # comando delete
      DbRows = self.Instancia_ingreso.Read_producto()  # hacer que las filas vayan aumentando atuomáticamente
      for self.row in DbRows:  # Rellenar los datos
         self.tabla1.insert("", 0,  text=self.row[0],
                                 values=(self.row[1],
                                         self.row[2],
                                         self.row[3],
                                         self.row[4],
                                         self.row[5]))  # , self.row[6]))  # Espacios para ingresar los nuevos datos


   ##########UPDATE PRODUCTOS##############
   def Update_ingresos(self):

      if self.validacionCreate():
         datos = (self.categoria.get(), self.color.get(), self.modelo.get(), self.precio.get(), self.codigo.get(),
                  self.nombre.get())  # ,self.total.get()
         cantidad = self.Instancia_ingreso.Update_producto(datos)
         if cantidad == 1:
            self.LimpiarRegistro_ingresos()
            mb.showinfo("Información", "Se modificó el artículo")
         else:
            mb.showinfo("Error", "No existe un Producto con dicho valor")
      else:
         mb.showerror("Error", "Por favor rellene todas las opsiones")



   ##########DELETE PRODUCTOS##############
   def Delete_ingresos(self):
      if self.validacionCreate():
         datos = (self.codigo.get(), self.nombre.get(),)
         cantidad = self.Instancia_ingreso.Delete_producto(datos)
         if cantidad == 1:
            self.LimpiarRegistro_ingresos()
            mb.showinfo("Información", "Se borró el artículo con dicho valor")
         else:
            mb.showinfo("Error", "No existe un artículo con dicho valor")
      else:
         mb.showerror("Error", "Por favor rellene todas las opsiones")






   ##########CONSULTAR PRODUCTOS##############
   def ValidacionConsulta_ingresos(self):
      return len(self.codigo.get()) != 0 and len(self.nombre.get()) != 0

   def Consultar_ingresos(self):
      if self.ValidacionConsulta_ingresos():
         datos = (self.codigo.get(), self.nombre.get())
         respuesta = self.Instancia_ingreso.Consular_producto(datos)
         if len(respuesta) > 0:
            self.categoria.set(respuesta[0][0])
            self.color.set(respuesta[0][1])
            self.modelo.set(respuesta[0][2])
            self.precio.set(respuesta[0][3])
            # self.total.set(respuesta[0][4])
         else:
            self.categoria.set('')
            self.color.set(' ')
            self.modelo.set(' ')
            self.precio.set(' ')
            # self.total.set(' ')
            mb.showinfo("Información", "No existe un artículo con dicho valor")
      else:
         mb.showerror("Error", "Por favor rellene todas las opsiones")

   ##########LIMPIAR REGISTRO##############
   def LimpiarRegistro_ingresos(self):
      self.codigo.set("")
      self.nombre.set("")
      self.categoria.set("")
      self.color.set("")
      self.modelo.set("")
      self.precio.set("")







