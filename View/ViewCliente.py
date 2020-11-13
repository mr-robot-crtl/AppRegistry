


from tkinter import *
import tkinter as tk
from tkinter import ttk
from Controller.Registrar_Ingreso import  LogicaIngresos
from Controller.Registrar_Salida import LogicaSalidas

class FormularioArticulos:
    def __init__(self):
        self.Control_ingreso = LogicaIngresos()
        self.Control_salida = LogicaSalidas()
        self.ventana1=tk.Tk()
        self.ventana1.title("Registros IONSAC")
        self.cuaderno1 = ttk.Notebook()
        self.Estilo_ventana1()
        self.Estilo_cuaderno1()
        self.Formulario_ingreso()
        self.ListadoCompleto_ingreso()
        self.Formulario_salida()
        self.ListadoCompleto_salida()
        self.ventana1.mainloop()

    def Estilo_ventana1(self):
        self.ventana1.iconbitmap("image/icono1.ico")
        self.ventana1.resizable(1,1)
    def Estilo_cuaderno1(self):
        self.cuaderno1.grid(column=0,columnspan = 20,padx=180, row=0, pady=180,sticky=W+E)#
        self.cuaderno1.config(width=1000, height=650)
        self.cuaderno1.pack(side="bottom")



    ########### CREACION DEL FORMULARIO DE INGRESOS ###############
    def Formulario_ingreso(self):
        self.pagina1 = tk.Frame(self.cuaderno1,background="#9ec7c6")
       #self.imagenRegistro= tk.PhotoImage(file="imageZ/01.jpg")
        self.cuaderno1.add(self.pagina1, text="Registrar Productos")#,image=self.imagenRegistro,compound=tk.LEFT,padding=10)

        #####################LABEL###################
        ######LABELFRAME1######
        self.labelframe1=tk.LabelFrame(self.pagina1, text="Productos",bg="#9fd1d3",fg="Black")
        self.labelframe1.grid(column=0,columnspan = 2, row=0, pady=10) #padx=5,
        self.labelframe1.configure(font=("@DengXian Light", 13,"roman")) #Yu Gothic ,Yu Gothic UI Semibold,Yu Gothic Medium

        ######LABEL1######
        self.label1 = tk.Label(self.labelframe1, text="Codigo",bg="#9fd1d3")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.label1.configure(font=("@DengXian Light", 10, "roman"))
        ######ENTRY1######
        self.codigo=tk.StringVar()
        self.Control_ingreso.setCodigo(self.codigo)
        self.entrycodigo = tk.Entry(self.labelframe1, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.entrycodigo.configure(font=("@DengXian Light", 9, "roman"))

        ######LABEL2######
        self.label2=tk.Label(self.labelframe1, text="Nombre",bg="#9fd1d3")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.label2.configure(font=("@DengXian Light", 10, "roman"))
        ######ENTRY2######
        self.nombre = tk.StringVar()
        self.Control_ingreso.setNombre(self.nombre)
        self.entrynombre=tk.Entry(self.labelframe1, textvariable=self.nombre)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        self.entrynombre.configure(font=("@DengXian Light", 9, "roman"))

        ######LABEL3######
        self.label3=tk.Label(self.labelframe1, text="Categoria",bg="#9fd1d3")
        self.label3.grid(column=0, row=2, padx=4, pady= 4)
        self.label3.configure(font=("@DengXian Light", 10, "roman"))
        ######COMBOBOX3######
        self.categoria = tk.StringVar()
        self.Control_ingreso.setCategoria(self.categoria)
        self.comboxcategoria=ttk.Combobox(self.labelframe1,width=18,textvariable=self.categoria)
        self.comboxcategoria.grid(column=1, row=2, padx=4, pady=4)
        self.opsionesCategoria = ["Accesorios","Comunicacion"]
        self.comboxcategoria['values']=self.opsionesCategoria
        self.comboxcategoria.configure(font=("@DengXian Light", 9, "roman"))

        ######LABEL4######
        self.label4 = tk.Label(self.labelframe1, text="Color",bg="#9fd1d3")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.label4.configure(font=("@DengXian Light", 10, "roman"))
        ######COMBOBOX4######
        self.color = tk.StringVar()
        self.Control_ingreso.setColor(self.color)
        self.comboxcolor = ttk.Combobox(self.labelframe1, width=18, textvariable=self.color)
        self.comboxcolor.grid(column=1, row=3, padx=4, pady=4)
        self.opsionesColor=["Green","Black","Pink","White","SkyBlue","Sky"]
        self.comboxcolor['values']=self.opsionesColor
        self.comboxcolor.configure(font=("@DengXian Light", 9, "roman"))

        ######LABEL5######
        self.label5 = tk.Label(self.labelframe1, text="Modelo",bg="#9fd1d3")
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.label5.configure(font=("@DengXian Light", 10, "roman"))
        ######COMBOBOX5######
        self.modelo = tk.StringVar()
        self.Control_ingreso.setModelo(self.modelo)
        self.comboxmodelo = ttk.Combobox(self.labelframe1, width=18, textvariable=self.modelo)
        self.comboxmodelo.grid(column=1, row=4, padx=4, pady=4)
        self.opsionesModelo=["Hawei","Samsung","Nokia","LG","Apple","Gamer"]
        self.comboxmodelo['values']=self.opsionesModelo
        self.comboxmodelo.configure(font=("@DengXian Light", 9, "roman"))

        ######LABEL6######
        self.label6 = tk.Label(self.labelframe1, text="Precio",bg="#9fd1d3")
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.label6.configure(font=("@DengXian Light", 10, "roman"))
        ######ENTRY6######
        self.precio = tk.StringVar()
        self.Control_ingreso.setPrecio(self.precio)
        self.entryprecio = ttk.Entry(self.labelframe1, textvariable=self.precio)
        self.entryprecio.grid(column=1, row=5, padx=4, pady=4)
        self.entryprecio.configure(font=("@DengXian Light", 9, "roman"))



       ############################### BOTONES ################################

        ######BOTON1######
        self.boton1=tk.Button(self.labelframe1, text="Create",bg="skyblue",fg="black", command=self.Control_ingreso.Create_ingresos)
        self.boton1.grid(row = 22, column=0,columnspan=2,pady=5,padx=30,sticky=W+E) #(column=1, row=8, padx=4, pady=4)
        self.boton1.configure(font=("@DengXian Light", 10, "roman"))
        self.boton1.config(cursor="hand2")

        ######BOTON1######
        self.boton2=tk.Button(self.labelframe1, text="Read",bg="skyblue",fg="black",command=self.Control_ingreso.Read_ingresos)
        self.boton2.grid(row = 23, column=0,columnspan=2,pady=5,padx=30,sticky=W+E) #(column=1, row=9, padx=4, pady=4)
        self.boton2.configure(font=("@DengXian Light", 10, "roman"))
        self.boton2.config(cursor="hand2")

        ######BOTON1######
        self.boton3=tk.Button(self.labelframe1, text="Update",bg="skyblue",fg="black", command=self.Control_ingreso.Update_ingresos)
        self.boton3.grid(row = 24, column=0,columnspan=2,pady=5,padx=30,sticky=W+E) #(column=1, row=10, padx=4, pady=4)
        self.boton3.configure(font=("@DengXian Light", 10, "roman"))
        self.boton3.config(cursor="hand2")

        ######BOTON1######
        self.boton4=tk.Button(self.labelframe1, text="Delete",bg="skyblue",fg="black", command=self.Control_ingreso.Delete_ingresos)
        self.boton4.grid(row = 25, column=0,columnspan=2,pady=5,padx=30,sticky=W+E) #(column=1, row=11, padx=4, pady=4)
        self.boton4.configure(font=("@DengXian Light", 10, "roman"))
        self.boton4.config(cursor="hand2")

        ######BOTON1######
        self.boton5=tk.Button(self.labelframe1, text="Consultar",bg="skyblue",fg="black", command=self.Control_ingreso.Consultar_ingresos)
        self.boton5.grid(row = 26, column=0,columnspan=2,pady=5,padx=30,sticky=W+E) #(column=1, row=12, padx=4, pady=4)
        self.boton5.configure(font=("@DengXian Light", 10, "roman"))
        self.boton5.config(cursor="hand2")



######################## CREACION DEL TREEVIEW INGRESOS ##########################
    def ListadoCompleto_ingreso(self):
        #### TABLA 1 #####
        self.tabla1=ttk.Treeview(self.pagina1, height=9,columns=2)
        self.Control_ingreso.setTabla1(self.tabla1)
        self.tabla1.grid(row=30,column=0 ,columnspan=2,pady=8,padx=72)
        ########### COLUMNAS #############
        self.tabla1["columns"] = ("1", "2", "3","4", "5")
        self.tabla1.column("#0", width=140, minwidth=140, stretch=tk.NO)
        self.tabla1.column("1", width=140, minwidth=140, stretch=tk.NO)
        self.tabla1.column("2", width=140, minwidth=140)
        self.tabla1.column("3", width=140, minwidth=140, stretch=tk.NO)
        self.tabla1.column("4", width=140, minwidth=140, stretch=tk.NO)
        self.tabla1.column("5", width=140, minwidth=140, stretch=tk.NO)

        ############## NOMBRE DE CADA COLUMNA ############
        self.tabla1.heading("#0", text="Codigo", anchor=tk.W)
        self.tabla1.heading("1", text="Nombre", anchor=tk.W)
        self.tabla1.heading("2", text="Categoria", anchor=tk.W)
        self.tabla1.heading("3", text="Color", anchor=tk.W)
        self.tabla1.heading("4", text="Modelo", anchor=tk.W)
        self.tabla1.heading("5", text="Precio", anchor=tk.W)




#################################### VENDER ##########################################

    def Formulario_salida(self):
        #######PAGINA2#######
        self.pagina2 =tk.Frame(self.cuaderno1,background="#9ec7c6")
        self.cuaderno1.add(self.pagina2, text="Vender Productos")

        ###########LABELS##############
        ###### LABELFRAME2 ####
        self.labelframe2 = tk.LabelFrame(self.pagina2, text="Productos",bg="#9fd1d3",fg="Black")
        self.labelframe2.config(font=("@DengXian Light", 13, "roman"))
        self.labelframe2.grid(column=0,columnspan=2, row=0, pady=10)
        self.labelframe2.configure(height=700,width=500)

        ###### LABEL1 #####
        self.label1 = tk.Label(self.labelframe2, text="Codigo",bg="#9fd1d3",fg="Black")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.label1.configure(font=("@DengXian Light", 10, "roman"))
        ###### ENTRY1 ######
        self.codigoV = tk.StringVar()
        self.Control_salida.setCodigoV(self.codigoV)
        self.entrycodigo = tk.Entry(self.labelframe2, textvariable=self.codigoV)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        ###### LABEL2 #####
        self.label2 = tk.Label(self.labelframe2, text="Nombre",bg="#9fd1d3",fg="Black")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.label2.configure(font=("@DengXian Light", 10, "roman"))
        ###### ENTRY2 ######
        self.nombreV = tk.StringVar()
        self.Control_salida.setNombreV(self.nombreV)
        self.entrynombre = ttk.Entry(self.labelframe2, textvariable=self.nombreV)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)

        ###### LABEL3 #####
        self.label3 = tk.Label(self.labelframe2, text="Categoria",bg="#9fd1d3",fg="Black")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.label3.configure(font=("@DengXian Light", 10, "roman"))
        ###### ENTRY3 ######
        self.categoriaV = tk.StringVar()
        self.Control_salida.setCategoriaV(self.categoriaV)
        self.entrycategoria = ttk.Entry(self.labelframe2, textvariable=self.categoriaV)
        self.entrycategoria.grid(column=1, row=2, padx=4, pady=4)

        ###### LABEL4 #####
        self.label4 = tk.Label(self.labelframe2, text="Color",bg="#9fd1d3",fg="Black")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.label4.configure(font=("@DengXian Light", 10, "roman"))
        ###### ENTRY4 ######
        self.colorV = tk.StringVar()
        self.Control_salida.setColorV(self.colorV)
        self.entrycolor = ttk.Entry(self.labelframe2, textvariable=self.colorV)
        self.entrycolor.grid(column=1, row=3, padx=4, pady=4)

        ###### LABEL5 #####
        self.label5 = tk.Label(self.labelframe2, text="Modelo",bg="#9fd1d3",fg="Black")
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.label5.configure(font=("@DengXian Light", 10, "roman"))
        ###### ENTRY5 ######
        self.modeloV = tk.StringVar()
        self.Control_salida.setModeloV(self.modeloV)
        self.entrymodelo = ttk.Entry(self.labelframe2, textvariable=self.modeloV)
        self.entrymodelo.grid(column=1, row=4, padx=4, pady=4)

        ###### LABEL6 #####
        self.label6 = tk.Label(self.labelframe2, text="Precio",bg="#9fd1d3",fg="Black")
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.label6.configure(font=("@DengXian Light", 10, "roman"))
        ###### ENTRY6 ######
        self.precioV = tk.StringVar()
        self.Control_salida.setPrecioV(self.precioV)
        self.entryprecio = ttk.Entry(self.labelframe2, textvariable=self.precioV)
        self.entryprecio.grid(column=1, row=5, padx=4, pady=4)

        ############################# BOTONES ###############################
        self.boton1 = tk.Button(self.labelframe2, text="Read",bg="#9fd1d3",fg="Black", command=self.Control_salida.Read_salida)
        self.boton1.grid(column=0,columnspan=2, row=8, padx=30, pady=4,sticky=W+E)
        self.boton1.configure(font=("@DengXian Light", 10, "roman"))
        self.boton1.config(cursor="hand2")

        self.boton2 = tk.Button(self.labelframe2, text="Vender",bg="#9fd1d3",fg="Black", command=self.Control_salida.Create_salida)
        self.boton2.grid(column=0,columnspan=2, row=9, padx=30, pady=4,sticky=W+E)
        self.boton2.configure(font=("@DengXian Light", 10, "roman"))
        self.boton2.config(cursor="hand2")


########################### CREACION DE LA TREEVIEW SALIDA #####################################
    def ListadoCompleto_salida(self):
        ##### TABLA 2 #####
        self.tabla2=ttk.Treeview(self.pagina2,height=10,columns=2)
        self.Control_salida.setTabla2(self.tabla2)
        self.tabla2.grid(row=2,column=0 ,columnspan=2,pady=10,padx=72,sticky=W+E)
        ###### COLUMNAS ######
        self.tabla2["columns"] = ("1", "2", "3","4", "5")
        self.tabla2.column("#0", width=140, minwidth=140, stretch=tk.NO)
        self.tabla2.column("1", width=140, minwidth=140, stretch=tk.NO)
        self.tabla2.column("2", width=140, minwidth=140)
        self.tabla2.column("3", width=140, minwidth=140, stretch=tk.NO)
        self.tabla2.column("4", width=140, minwidth=140, stretch=tk.NO)
        self.tabla2.column("5", width=140, minwidth=140, stretch=tk.NO)
        ############## NOMBRE DE CADA COLUMNA ############
        self.tabla2.heading("#0", text="Nombre", anchor=tk.W)
        self.tabla2.heading("1", text="Categoria", anchor=tk.W)
        self.tabla2.heading("2", text="Color", anchor=tk.W)
        self.tabla2.heading("3", text="Codigo", anchor=tk.W)
        self.tabla2.heading("4", text="Modelo", anchor=tk.W)
        self.tabla2.heading("5", text="Precio", anchor=tk.W)






















