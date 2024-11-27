from datetime import datetime

import mysql.connector
from PyQt6.uic.properties import QtCore
from mysql.connector import Error
import os
from PyQt6 import QtSql, QtWidgets
import var

class ConexionServer():
    def crear_conexion(self):

        try:
            conexion = mysql.connector.connect(
            host='192.168.10.66', # Cambia esto a la IP de tu servidor user='dam', # Usuario creado
            #host='192.168.1.49',
            user='dam',
            password='dam2425',
            database='bbdd',
            charset="utf8mb4",
            collation="utf8mb4_general_ci"  # Asegúrate de que aquí esté configurado
            # Contraseña del usuario database='bbdd' # Nombre de la base de datos
            )
            if conexion.is_connected():
                pass
                #print("Conexión exitosa a la base de datos")
            return conexion
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
        return None

    @staticmethod
    def listaProv(self=None):
        listaprov = []
        conexion = ConexionServer().crear_conexion()

        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM provincias")
                resultados = cursor.fetchall()
                for fila in resultados:
                    listaprov.append(fila[1])  # Asumiendo que el nombre de la provincia está en la segunda columna
                cursor.close()
                conexion.close()
            except Error as e:
                print(f"Error al ejecutar la consulta: {e}")
        return listaprov

    @staticmethod
    def listaMuniProv(provincia):
        try:
            conexion = ConexionServer().crear_conexion()
            listamunicipios = []
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT * FROM municipios WHERE idprov = (SELECT idprov FROM provincias WHERE provincia = %s)",
                (provincia,)
            )
            resultados = cursor.fetchall()
            for fila in resultados:
                listamunicipios.append(fila[1])  # Asumiendo que el nombre de la provincia está en la segunda columna
            cursor.close()
            conexion.close()
            return listamunicipios
        except Exception as error:
            print("error lista muni", error)

    def listadoClientes(self):
        try:
            conexion = ConexionServer().crear_conexion()
            listadoclientes = []
            cursor = conexion.cursor()
            if var.historico == 1:
                cursor.execute("SELECT * FROM clientes WHERE bajacli is NULL or bajacli='' ORDER BY apelcli, nomecli ASC")
                resultados = cursor.fetchall()
                # Procesar cada fila de los resultados
                for fila in resultados:
                    # Crear una lista con los valores de la fila
                    listadoclientes.append(list(fila))  # Convierte la tupla en una lista y la añade a listadoclientes

                # Cerrar el cursor y la conexión si no los necesitas más
                cursor.close()
                conexion.close()
                return listadoclientes
            else:
                cursor.execute("SELECT * FROM clientes ORDER BY apelcli, nomecli ASC")
                resultados = cursor.fetchall()
                # Procesar cada fila de los resultados
                for fila in resultados:
                    # Crear una lista con los valores de la fila
                    listadoclientes.append(list(fila))  # Convierte la tupla en una lista y la añade a listadoclientes

                # Cerrar el cursor y la conexión si no los necesitas más
                cursor.close()
                conexion.close()
                return listadoclientes

        except Exception as e:
            print("error listado en conexion", e)

    def altaCliente(cliente):
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                # Definir la consulta de inserción
                query = """
                INSERT INTO clientes (dnicli, altacli, apelcli, nomecli, dircli, emailcli, movilcli, provcli, municli)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, cliente)  # Ejecutar la consulta pasando la lista directamente
                conexion.commit()  # Confirmar la transacción
                cursor.close()  # Cerrar el cursor y la conexión
                conexion.close()
                return True
        except Error as e:
            print(f"Error al insertar el cliente: {e}")

    def datosOneCliente(dni):
        registro = []  # Inicializa la lista para almacenar los datos del cliente
        try:
            conexion = ConexionServer().crear_conexion()  # Crear la conexión

            if not conexion:
                raise Exception("No se pudo establecer la conexión a la base de datos.")

            with conexion.cursor() as cursor:
                # Definir la consulta de selección
                query = '''SELECT * FROM clientes WHERE dnicli = %s'''
                cursor.execute(query, (dni,))  # Pasar 'dni' como parámetro en una tupla

                # Recuperar los datos de la consulta
                resultados = cursor.fetchall()

                # Verificar si hay resultados
                if not resultados:
                    print(f"No se encontraron datos para el DNI: {dni}")
                    return None  # Retornar None si no hay datos

                # Procesar las filas encontradas
                for row in resultados:
                    for col in row:
                        registro.append(str(col))  # Convertir cada columna a string y agregarla a la lista

            return registro

        except Exception as e:
            print("Error al obtener datos de un cliente:", e)
            return None  # Devolver None en caso de error

    def modifCliente(registro):
        conexion = ConexionServer().crear_conexion()
        cursor = conexion.cursor()
        try:
            query = '''SELECT count(*) FROM clientes WHERE dnicli = %s'''
            cursor.execute(query, (str(registro[0]),))
            count = cursor.fetchone()[0]
            if count > 0:
                query_update = """
                                   UPDATE clientes
                                   SET altacli = %s, apelcli = %s, nomecli = %s, emailcli = %s, movilcli = %s, 
                                       dircli = %s, provcli = %s, municli = %s, bajacli = %s
                                   WHERE dnicli = %s
                               """
                # Verificar que el parámetro bajacli esté correctamente formateado
                params = (
                    str(registro[1]), str(registro[2]), str(registro[3]), str(registro[4]),
                    str(registro[5]), str(registro[6]), str(registro[7]), str(registro[8]),
                    str(registro[9]) if registro[9] != "" else None,
                    str(registro[0])
                )

                # Verificar que la cantidad de parámetros sea correcta
                if len(params) == 10:
                    cursor.execute(query_update, params)
                    conexion.commit()
                    return True
            else:
                return False
        except Exception as error:
            print("error modificar cliente", error)
        finally:
            cursor.close()
            conexion.close()

    import mysql.connector
    from mysql.connector import Error

    def bajaCliente(datos):
        conexion = ConexionServer().crear_conexion()
        cursor = conexion.cursor()
        try:

                # Consulta SQL para dar de baja al cliente
                consulta = "UPDATE clientes SET bajacli = %s WHERE dnicli = %s"
                valores = (str(datos[1]), str(datos[0]).strip())

                # Ejecutar la consulta
                cursor.execute(consulta, valores)
                conexion.commit()  # Confirmar los cambios

                if cursor.rowcount > 0:
                    print(f"Cliente con DNI {datos[0]} dado de baja correctamente.")
                    return True
                else:
                    print(f"No se encontró un cliente con DNI {datos[0]}.")
                    return False

        except Error as e:
            print("Error al dar de baja al cliente:", e)
            return False

    '''PROPIEDADES'''

    def altaPropiedad(propiedad):
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                # Definir la consulta de inserción
                query = """
                INSERT INTO propiedades (altaprop, dirprop, provprop, muniprop, tipoprop, habprop, banprop, superprop, 
                prealquiprop, prevenprop, cpprop, obserprop, tipooper, estadoprop, nomeprop, movilprop)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, propiedad)  # Ejecutar la consulta pasando la lista directamente
                conexion.commit()  # Confirmar la transacción
                cursor.close()  # Cerrar el cursor y la conexión
                conexion.close()
                return True
        except Error as e:
            print(f"Error al insertar propiedad: {e}")



    def listadoPropiedades(self):
        try:
            conexion = ConexionServer().crear_conexion()
            listado = []
            cursor = conexion.cursor()
            if var.historico == 1:
                cursor.execute("SELECT * FROM propiedades WHERE bajaprop is NULL ORDER BY muniprop ASC ")

            elif var.historico == 0:
                cursor.execute("SELECT * FROM propiedades ORDER BY muniprop ASC ")

            resultados = cursor.fetchall()
            for fila in resultados:  # Procesar cada fila de los resultados y crea una lista con valores de la fila
                listado.append(list(fila))  # Convierte la tupla en una lista y la añade a listadoclientes
            cursor.close()  # Cerrar el cursor y la conexión si no los necesitas más
            conexion.close()
            return listado

        except Exception as e:
            print("error listado en conexión", e)

    def modifPropiedad(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare( "UPDATE propiedades set altaprop = :altaprop, bajaprop = :bajaprop, dirprop = :dirprop, provprop = :provprop,"
                "muniprop = :muniprop, tipoprop = :tipoprop, habitaprop = :habitaprop, banprop = :banprop,"
                "superprop = :superprop, prealquiprop = :prealquiprop, prevenprop = :prevenprop,"
                "cpprop = :cpprop, observaprop = :observaprop, tipooper = :tipooper, estadoprop = :estadoprop,"
                "nombreprop = :nombreprop, movilprop = :movilprop where codigo = :codigo")

            query.bindValue(":codigo", int(registro[0]))
            query.bindValue(":altaprop", str(registro[1]))
            if str(registro[2]) == "":
                query.bindValue(":bajaprop", QtCore.QVariant())
            else:
                query.bindValue(":bajaprop", str(registro[2]))
            query.bindValue(":dirprop", str(registro[3]))
            query.bindValue(":provprop", str(registro[4]))
            query.bindValue(":muniprop", str(registro[5]))
            query.bindValue(":tipoprop", str(registro[6]))
            query.bindValue(":habitaprop", int(registro[7]))
            query.bindValue(":banprop", int(registro[8]))
            query.bindValue(":superprop", str(registro[9]))
            query.bindValue(":prealquiprop", str(registro[10]))
            query.bindValue(":prevenprop", str(registro[11]))
            query.bindValue(":cpprop", str(registro[12]))
            query.bindValue(":observaprop", str(registro[13]))
            query.bindValue(":tipooper", str(registro[14]))
            query.bindValue(":estadoprop", str(registro[15]))
            query.bindValue(":nombreprop", str(registro[16]))
            query.bindValue(":movilprop", str(registro[17]))

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error modificar propiedad", error)

    def bajaPropiedad(datos):
        conexion = ConexionServer().crear_conexion()
        cursor = conexion.cursor()
        try:

            # Consulta SQL para dar de baja al cliente
            consulta = "UPDATE clientes SET bajacli = %s WHERE dnicli = %s"
            valores = (str(datos[1]), str(datos[0]).strip())

            # Ejecutar la consulta
            cursor.execute(consulta, valores)
            conexion.commit()  # Confirmar los cambios

            if cursor.rowcount > 0:
                print(f"Cliente con DNI {datos[0]} dado de baja correctamente.")
                return True
            else:
                print(f"No se encontró un cliente con DNI {datos[0]}.")
                return False

        except Error as e:
            print("Error al dar de baja al cliente:", e)
            return False

    def datosOnePropiedad(codigo):
        registro = []
        try:
            conexion = ConexionServer().crear_conexion()  # Crear la conexión

            if not conexion:
                raise Exception("No se pudo establecer la conexión a la base de datos.")

            with conexion.cursor() as cursor:
                query = '''SELECT * FROM propiedades WHERE codigo = %s'''
                cursor.execute(query, (codigo,))

                resultados = cursor.fetchall()

                if not resultados:
                    print(f"No se encontraron datos para el Codigo: {codigo}")
                    return None

                for row in resultados:
                    for col in row:
                        registro.append(str(col))

            return registro

        except Exception as e:
            print("Error al obtener datos de una propiedad:", e)
            return None

    def buscarProp(datos):
        try:
            registro=[]
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM propiedades WHERE muniprop = :muniprop and tipoprop = :tipoprop ORDER BY codigo")
            query.bindValue(":muniprop",str(datos[0]))
            query.bindValue(":tipoprop", str(datos[1]))
            if query.exec():
                while query.next():
                    prop=[]
                    for i in range(query.record().count()):
                        prop.append(str(query.value(i)))
                    registro.append(prop)
            return registro
        except Exception as e:
            print("Error buscar propiedad", e)

    @staticmethod
    def cargarTipoProp(self):
        try:
            registro = []
            conexion = ConexionServer().crear_conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT tipo FROM tipopropiedad")
            resultados = cursor.fetchall()
            for fila in resultados:
                registro.append(fila[0])
            return registro
        except Exception as e:
            print("error cargarTipoProp en conexionServer", e)

    def altaTipoProp(tipo):
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                query = "INSERT INTO tipopropiedad (tipo) VALUES (%s)"
                cursor.execute(query, (tipo,))
                conexion.commit()
                cursor.close()
                conexion.close()
                return True
        except Error as e:
            print("error altaTipoPropiedad en conexionServer", e)
            return False

    def bajaTipoProp(tipo):
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                query = "DELETE FROM tipopropiedad WHERE tipo = %s"
                cursor.execute(query, (tipo,))
                conexion.commit()
                cursor.close()
                conexion.close()
                return True
        except Error as e:
            print("error bajaTipoPropiedad en conexionServer", e)
            return False


