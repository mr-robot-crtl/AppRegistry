
from Model.Connection import Connection


class ProductosSalidas_BD():
    conection=Connection()
    def CreateProductos_venta(self, datos):
        cone =  self.conection.abrir()
        cursor = cone.cursor()
        sql = "INSERT INTO Ventas(CodigoV, NombreV, CategoriaV, ColorV, ModeloV, PrecioV) VALUES (?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def ReadProductos_venta(self):
        try:
            cone =  self.conection.abrir()
            cursor = cone.cursor()
            sql = "SELECT * FROM Ventas ORDER BY NombreV ASC"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()



