
from Model.Connection import Connection


class ProductosIngresos_BD:
    conection=Connection()

    def Create_producto(self, datos):
        cone = self.conection.abrir()
        cursor = cone.cursor()
        sql = "INSERT INTO Productos(Nombre, Categoria, Color, Modelo, Precio) VALUES (?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def Read_producto(self):
        try:
            cone = self.conection.abrir()
            cursor = cone.cursor()
            sql = "SELECT * FROM Productos ORDER BY Nombre ASC"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def Update_producto(self, datos):
        try:
            cone =  self.conection.abrir()
            cursor = cone.cursor()
            sql = "UPDATE Productos SET Categoria=?, Color=?, Modelo=?, Precio=? WHERE codigo=? AND nombre=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount  # retornamos la cantidad de filas modificadas
        except:
            cone.close()

    def Delete_producto(self, datos):
        try:
            cone = self.conection.abrir()
            cursor = cone.cursor()
            sql = "DELETE FROM Productos WHERE codigo=? AND nombre=? "
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount  # retornamos la cantidad de filas borradas
        except:
            cone.close()


    def Consular_producto(self, datos):
        try:
            cone = self.conection.abrir()
            cursor = cone.cursor()
            sql = "SELECT Categoria, Color, Modelo, Precio FROM Productos WHERE codigo=? AND nombre=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
