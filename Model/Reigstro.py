

class RegistroIngreso:

    def __init__(self, codigo, nombre, categoria, color, modelo, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.color = color
        self.modelo = modelo
        self.precio = precio

    def setCodigo(self, codigo):
        self.codigo = codigo
    def getcodigo(self,codigo):
        return codigo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCategoria(self, categoria):
        self.categoria = categoria

    def setColor(self, color):
        self.color = color

    def setModelo(self, modelo):
        self.modelo = modelo

    def setPrecio(self, precio):
        self.precio = precio

    def setTabla1(self, tabla1):
        self.tabla1 = tabla1

class RegistroSalida:
    def __init__(self, codigoV, nombreV, categoriaV, colorV, modeloV, precioV):
        self.codigoV = codigoV
        self.nombreV = nombreV
        self.categoriaV = categoriaV
        self.colorV = colorV
        self.modeloV = modeloV
        self.precioV = precioV

    def setCodigoV(self, codigoV):
        self.codigoV = codigoV

    def setNombreV(self, nombreV):
        self.nombreV = nombreV

    def setCategoriaV(self, categoriaV):
        self.categoriaV = categoriaV

    def setColorV(self, colorV):
        self.colorV = colorV

    def setModeloV(self, modeloV):
        self.modeloV = modeloV

    def setPrecioV(self, precioV):
        self.precioV = precioV

    def setTabla2(self, tabla2):

        self.tabla2 = tabla2







