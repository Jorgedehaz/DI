import os
import sqlite3
from logging import exception
from datetime import datetime, timedelta
from datetime import date
import calendar
from PyQt6 import QtSql, QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTableWidgetItem, QCheckBox, QWidget, QVBoxLayout

import var


class Conexion:

    '''
    método de una clase que no depende de una instancia específica de esa clase. 
    Se puede llamarlo directamente a través de la clase, sin necesidad de crear un objeto de esa clase. 
    Es útil en comportamientos o funcionalidades que son más a una clase en general que a una instancia en particular.
    '''


    '''
    BLOQUE METODOS CONEXION CLIENTES 
    '''

    @staticmethod
    def db_conexion(self):

        """

        :param self: None
        :type self: None
        :return: False or True
        :rtype: bool

        Módulo de conexion con la base de datos.
        Si éxito devuelve true , en caso  contrario devuelve False.

        """

        # Verifica si el archivo de base de datos existe
        if not os.path.isfile('bbdd.sqlite'):
            QtWidgets.QMessageBox.critical(None, 'Error', 'El archivo de la base de datos no existe.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
        # Crear la conexión con la base de datos SQLite
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bbdd.sqlite')

        if db.open():
            # Verificar si la base de datos contiene tablas
            query = QtSql.QSqlQuery()
            query.exec("SELECT name FROM sqlite_master WHERE type='table';")

            if not query.next():  # Si no hay tablas
                QtWidgets.QMessageBox.critical(None, 'Error', 'Base de datos vacía o no válida.',
                                               QtWidgets.QMessageBox.StandardButton.Cancel)
                return False
            else:
                QtWidgets.QMessageBox.information(None, 'Aviso', 'Conexión Base de Datos realizada',
                                               QtWidgets.QMessageBox.StandardButton.Ok)
                return True
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', 'No se pudo abrir la base de datos.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False

    @staticmethod
    def listaProv(self):

        """

        :param self: None
        :type self: None
        :return: lista provincias
        :rtype: bytearray

        Metodo que obtiene listado de provincias en la base de datos.

        """

        listaprov = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM provincias")
        if query.exec():
            while query.next():
                listaprov.append(query.value(1))

        return listaprov

    def listaMuniprov(provincia):
        """

        :param provincia: nombre provincia
        :type provincia: str
        :return: lista municipios
        :rtype: bytearray

        Módulo de conexion con la base de datos.
        Si éxito devuelve true , en caso  contrario devuelve False.

        """

        listamunicipios = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM municipios where idprov = (select idprov from provincias  where provincia = ?)")
        query.bindValue(0, provincia)
        if query.exec():
            while query.next():
                listamunicipios.append(query.value(1))
        return listamunicipios

    def altaCliente(nuevocli):
        """

        :param nuevocli: array con datos cliente
        :type nuevocli: list
        :return: true o false
        :rtype: bool

        Metodo que inserta datos nuevo cliente en la bbdd

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into CLIENTES (dnicli,altacli,apelcli,nomecli,emailcli,movilcli,dircli,"
                          " provcli,municli) VALUES (:dnicli,:altacli,:apelcli,:nomecli,:emailcli,:movilcli,:dircli,"
                          " :provcli,:municli)")
            query.bindValue(":dnicli", str(nuevocli[0]))
            query.bindValue(":altacli", str(nuevocli[1]))
            query.bindValue(":apelcli", str(nuevocli[2]))
            query.bindValue(":nomecli", str(nuevocli[3]))
            query.bindValue(":emailcli",str(nuevocli[4]))
            query.bindValue(":movilcli",str(nuevocli[5]))
            query.bindValue(":dircli",str(nuevocli[6]))
            query.bindValue(":provcli",str(nuevocli[7]))
            query.bindValue(":municli", str(nuevocli[8]))

            if query.exec():
                print("Cliente añadido")
                return True

            else:
                return False

        except Exception as e:
            print("error alta cliente", e)
        except sqlite3.IntegrityError:
            return False

    def listadoClientes(self):
        """

        :return: devuelve listado clientes
        :rtype: list

        Metodo que devuelve todos los clientes ordenados por apellidos y nombre

        """
        try:
            listado = []
            if var.historico == 1:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM CLIENTES WHERE bajacli is NULL ORDER BY apelcli, nomecli ASC")

                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                    return listado
            else:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM CLIENTES ORDER BY apelcli, nomecli ASC")

                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                    return listado
        except Exception as e:
            print("error listado cliente", e)

        except Exception as e:
            print("error listado en conexión", e)

    def datosOneCliente(dni):
        """
        :param dni: dni cliente
        :type dni: str
        :return: datos cliente
        :rtype: list

        Metodo que devuelve los datos de un cliente cuyo dni coincida con el dado

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM clientes WHERE dnicli = :dni")

            query.bindValue(":dni", str(dni).strip())

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))

            return registro

        except Exception as e:
            print("Error recuperando datos de clientes", e)

    def modifCliente(registro):
        """
        :param registro: array con datos cliente
        :type registro: list
        :return: true o false
        :rtype: bool

        Metodo que modifica los datos del cliente pasados por parametro

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select count(*) from clientes where dnicli = :dni")
            query.bindValue(":dni", str(registro[0]))
            if query.exec():
                if query.next() and query.value(0) > 0:
                    if query.exec():
                        query = QtSql.QSqlQuery()
                        query.prepare("UPDATE clientes set altacli = :altacli, apelcli = :apelcli, nomecli = :nomecli, "
                                      " emailcli = :emailcli, movilcli = :movilcli, dircli = :dircli, provcli = :provcli, "
                                      " municli = :municli, bajacli = :bajacli where dnicli = :dni")
                        query.bindValue(":dni", str(registro[0]))
                        query.bindValue(":altacli", str(registro[1]))
                        query.bindValue(":apelcli", str(registro[2]))
                        query.bindValue(":nomecli", str(registro[3]))
                        query.bindValue(":emailcli", str(registro[4]))
                        query.bindValue(":movilcli", str(registro[5]))
                        query.bindValue(":dircli", str(registro[6]))
                        query.bindValue(":provcli", str(registro[7]))
                        query.bindValue(":municli", str(registro[8]))
                        query.bindValue(":bajacli", str(registro[9]))
                        if registro[9] == "":
                            query.bindValue(":bajacli", QtCore.QVariant())
                        else:
                            query.bindValue(":bajacli", str(registro[9]))


                        if query.exec():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except Exception as error:
            print("error modificar cliente", error)

    def bajaCliente(datos):
        """

        :param datos: array con datos de cliente
        :type datos: list
        :return: true o false
        :rtype: bool

        Metodo que elimina a un cliente en funcion de los datos pasados por parametro

        """
        try:

            query = QtSql.QSqlQuery()
            query.prepare("UPDATE clientes SET bajacli =:bajacli WHERE dnicli = :dni")
            query.bindValue(":dni", str(datos[0]).strip())
            query.bindValue(":bajacli", str(datos[1]))

            if query.exec():
                return True
            else:
                return False

        except Exception as e:
            print("Error baja cliente bd", e)

    def buscarCliente(datos):
        """

        :param datos: array con datos de cliente
        :type datos: list
        :return: true o false
        :rtype: bool

        Metodo que devuelve los datos de un lciente cuyo dni coincida con el dado

        """
        try:
            registro=[]
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM clientes WHERE dnicli = :dnicli")
            query.bindValue(":dnicli",str(datos[0]))
            if query.exec():
                while query.next():
                    prop=[]
                    for i in range(query.record().count()):
                        prop.append(str(query.value(i)))
                    registro.append(prop)
            return registro
        except Exception as e:
            print("Error buscar cliente", e)


    '''
    BLOQUE METODOS CONEXION PROPIEDADES
    '''
    def altaTipoprop(tipo):
        """

        :param tipo: array con datos tipo propiedad
        :type tipo: list
        :return: true o false
        :rtype: bool

        Metodo que inserta un nuevo tipo propiedad en la bbdd

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into TIPOPROPIEDAD (TIPO) VALUES (:tipo)")
            query.bindValue(":tipo", str(tipo))
            if query.exec():
                registro=Conexion.cargarTipoprop(self = None)
                return registro
            else:
                return registro
        except Exception as error:
            print("error alta tipoprop", error)

    def bajaTipoprop(tipo):
        """
        :param tipo: array con datos tipo propiedad
        :type tipo: list
        :return: true or false
        :rtype: bool

        Metodo que borra un tipo propiedad en la bbdd

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT count(*) from TIPOPROPIEDAD WHERE tipo = :tipo")
            query.bindValue(":tipo", str(tipo))
            if query.exec():
                if query.next() and query.value(0) > 0:
                    query = QtSql.QSqlQuery()
                    query.prepare("DELETE from TIPOPROPIEDAD where tipo = :tipo")
                    query.bindValue(":tipo", str(tipo))
                    if query.exec():
                        return True
                else:
                    return False

        except Exception as e:
            print("Error baja tipoprop", e)

    def cargarTipoprop(self):
        """
        :return: devuelve listado de tipos propiedad
        :rtype: list

        Metodo que devuelve todos los tipos de propiedad

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * from TIPOPROPIEDAD ASC")
            if query.exec():
                while query.next():
                    registro.append(str(query.value(0)))
            return registro
        except Exception as error:
            print("Error cargar tipoprop", error)

    def altaPropiedad(propiedad):
        """
        :param propiedad: array con datos de propiedad
        :type propiedad: list
        :return: true o false
        :rtype: bool

        Metodo que da de alta una propiedad pasando su datos a la bbdd

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into PROPIEDADES (altaprop,dirprop,provprop,muniprop,tipoprop, "
                          " habitaprop,banprop,superprop,prealquiprop,prevenprop,cpprop,observaprop, "
                          " tipooper,estadoprop,nombreprop,movilprop)"
                          " VALUES (:altaprop,:dirprop,:provprop,:muniprop,:tipoprop, "
                          " :habitaprop,:banprop,:superprop,:prealquiprop,:prevenprop,:cpprop,:observaprop, "
                          " :tipooper,:estadoprop,:nombreprop,:movilprop)")
            query.bindValue(":altaprop", str(propiedad[0]))
            query.bindValue(":dirprop", str(propiedad[1]))
            query.bindValue(":provprop", str(propiedad[2]))
            query.bindValue(":muniprop", str(propiedad[3]))
            query.bindValue(":tipoprop", str(propiedad[4]))
            query.bindValue(":habitaprop", int(propiedad[5]))
            query.bindValue(":banprop", int(propiedad[6]))
            query.bindValue(":superprop", float(propiedad[7]))
            query.bindValue(":prealquiprop", float(propiedad[8]))
            query.bindValue(":prevenprop", float(propiedad[9]))
            query.bindValue(":cpprop", str(propiedad[10]))
            query.bindValue(":observaprop", str(propiedad[11]))
            query.bindValue(":tipooper", str(propiedad[12]))
            query.bindValue(":estadoprop", str(propiedad[13]))
            query.bindValue(":nombreprop", str(propiedad[14]))
            query.bindValue(":movilprop", str(propiedad[15]))

            if query.exec():
                print("Propiedad añadida")
                return True

            else:
                return False

        except Exception as error:
            print("Error alta propiedad en conexion", error)

    def listadoPropiedades(self):
        """

        :return: devuelve listado propiedades
        :rtype: list

        Metodo que devuelve todas las propiedades ordenadas por municipio

        """
        try:
            listado = []
            if var.historico == 1:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM PROPIEDADES WHERE bajaprop is NULL ORDER BY muniprop ASC")

                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                    return listado
            else:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM PROPIEDADES ORDER BY muniprop ASC")

                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                    return listado

        except Exception as e:
            print("error listado en conexión", e)

    def modifPropiedad(registro):
        """

        :param registro: array con datos de propiedad
        :type registro: list
        :return: true o false
        :rtype: bool

        Metodo que modifica propiedad pasando su datos a la bbdd

        """
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
        """

        :param datos: array con datos de propiedad
        :type datos: list
        :return: true o false
        :rtype: bool

        Metodo que elimina una propiedad pasando su datos a la bbdd

        """

        try:

            query = QtSql.QSqlQuery()
            query.prepare("UPDATE propiedades SET bajaprop =:bajaprop WHERE codigo = :codigo")
            query.bindValue(":codigo", str(datos[0]).strip())
            query.bindValue(":bajaprop", str(datos[1]))


            if query.exec():
                return True
            else:
                return False

        except Exception as e:
            print("Error baja propiedad bd", e)

    def datosOnePropiedad(id):
        """
        :param id: array con datos de propiedad
        :type id: list
        :return: true o false
        :rtype: bool

        Metodo que elimina una propiedad pasando su datos a la bbdd

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM propiedades WHERE codigo = :codigo")

            query.bindValue(":codigo", str(id))

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as e:
            print("Error recuperando datos de clientes", e)

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

    def cargaBuscarProp(self):
        registros = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT municipio FROM municipios")
        if query.exec():
            while query.next():
                registros.append(str(query.value(0)))
        return registros

    '''
    VENDEDORES
    '''

    def altaVendedor(nuevovend):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into COMENTARIOS (dniVendedor,nombreVendedor,altaVendedor,movilVendedor,mailVendedor,"
                          " delegacionVendedor) VALUES (:dniVendedor,:nombreVendedor,:altaVendedor,:movilVendedor,:mailVendedor,"
                          ":delegacionVendedor)")
            query.bindValue(":dniVendedor", str(nuevovend[0]))
            query.bindValue(":nombreVendedor", str(nuevovend[1]))
            query.bindValue(":altaVendedor", str(nuevovend[2]))
            query.bindValue(":movilVendedor", str(nuevovend[3]))
            query.bindValue(":mailVendedor", str(nuevovend[4]))
            query.bindValue(":delegacionVendedor", str(nuevovend[5]))

            if query.exec():
                print("Vendedor añadido")
                return True

            else:
                return False

        except Exception as e:
            print("error alta vendedor", e)
        except sqlite3.IntegrityError:
            return False

    def listadoVendedores(self):
        try:
            listado = []
            if var.historico == 1:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM COMENTARIOS WHERE bajaVendedor is NULL ORDER BY idVendedor ASC")

                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                    return listado
            else:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM COMENTARIOS ORDER BY idVendedor ASC")

                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                    return listado
        except Exception as e:
            print("error listado vendedores", e)

        except Exception as e:
            print("error listado en conexión", e)

    def datosOneVendedor(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM comentarios WHERE idVendedor = :idVendedor")

            query.bindValue(":idVendedor", int(id))

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))

            return registro

        except Exception as e:
            print("Error recuperando datos de vendedor", e)


    def modifVendedor(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select count(*) from coemntarios where idVendedor = :id")
            query.bindValue(":id", int(registro[0]))
            if query.exec():
                if query.next() and query.value(0) > 0:
                    if query.exec():
                        query = QtSql.QSqlQuery()
                        query.prepare("UPDATE comentarios set nombreVendedor = :nombreVendedor,"
                                      "altaVendedor = :altaVendedor,bajaVendedor = :bajaVendedor, movilVendedor = :movilVendedor,"
                                      "mailVendedor =: mailVendedor,"
                                      "delegacionVendedor = :delegacionVendedor where idVendedor = :idVendedor")
                        query.bindValue(":nombreVendedor", str(registro[0]))
                        query.bindValue(":altaVendedor", str(registro[1]))
                        if registro[2] == "":
                            query.bindValue(":bajaVendedor", QtCore.QVariant())
                        else:
                            query.bindValue(":bajaVendedor", str(registro[2]))

                        query.bindValue(":movilVendedor", str(registro[3]))
                        query.bindValue(":mailVendedor", str(registro[4]))
                        query.bindValue(":delegacionVendedor", str(registro[5]))


                        if query.exec():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except Exception as error:
            print("error modificar vendedor", error)

    def bajaVendedor(datos):
        try:

            query = QtSql.QSqlQuery()
            query.prepare("UPDATE COMENTARIOS SET bajaVendedor =:bajaVend WHERE dniVendedor =:dniVendedor")

            query.bindValue(":dniVendedor", str(datos[0]).strip())
            query.bindValue(":bajaVend", str(datos[1]))

            if query.exec():
                return True
            else:
                return False

        except Exception as e:
            print("Error baja vendedor bd", e)

    '''
    ZONA FACTURACION
    '''

    def altaFactura(nuevafactura):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into FACTURAS (fechafac,dnifac) VALUES (:fechafac,:dnifac)")
            query.bindValue(":fechafac", str(nuevafactura[0]))
            query.bindValue(":dnifac", str(nuevafactura[1]))
            if query.exec():
                return True
            else:
                return False
        except Exception as e:
            print("Error alta factura", e)

    def listadoFacturas(self):
        try:
            registros = []

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM facturas")
            if query.exec():
                while query.next():
                    # Crear una lista para la fila completa
                    fila = [str(query.value(i)) for i in range(query.record().count())]
                    registros.append(fila)  # Agregar la fila completa como un elemento

            return registros

        except Exception as e:
            print("Error listado factura", e)
            return []

    def delFactura(idfactura):
        try:
            print(idfactura)
            query = QtSql.QSqlQuery()
            query.prepare("DELETE FROM facturas WHERE id = :idfactura")
            query.bindValue(":idfactura", idfactura)

            if query.exec():
                return True
            else:
                return False
        except Exception as e:
            print("Error eliminando factura:", e)

    def datosOneFactura(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM facturas WHERE id = :idFactura")

            query.bindValue(":idFactura", int(id))

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))

            return registro

        except Exception as e:
            print("Error recuperando datos de vendedor", e)



    '''
    ZONA VENTAS
    '''

    def altaVenta(nuevaVenta):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO VENTAS (facventa, codprop, agente) VALUES (:fechaventa, :codprop, :agente)")
            query.bindValue(":fechaventa", str(nuevaVenta[0]))
            query.bindValue(":codprop", str(nuevaVenta[1]))
            query.bindValue(":agente", str(nuevaVenta[2]))

            # Obtener la fecha de hoy sin la hora
            fechabaja = date.today().strftime("%d/%m/%Y")  # Formato estándar YYYY-MM-DD

            query2 = QtSql.QSqlQuery()
            query2.prepare("UPDATE propiedades SET bajaprop = :bajaprop WHERE codigo = :codigo")
            query2.bindValue(":bajaprop", fechabaja)
            query2.bindValue(":codigo", str(nuevaVenta[3]))

            if query.exec() and query2.exec():
                return True
            else:
                return False

        except Exception as e:
            print("Error alta venta:", e)

    def listadoVentas(factura):
        try:
            registros = []

            query = QtSql.QSqlQuery()
            query.prepare("""
                SELECT v.idventa AS "ID Venta",
                       p.codigo AS "ID Propiedad",
                       p.dirprop AS "Dirección de la propiedad",
                       p.muniprop AS "Localidad",
                       p.tipoprop AS "Tipo propiedad",
                       p.prevenprop AS "Precio de venta"
                FROM ventas AS v
                INNER JOIN propiedades AS p ON v.codprop = p.codigo
                WHERE v.facventa = :factura
            """)
            query.bindValue(":factura", factura)

            if query.exec():
                while query.next():
                    fila = []
                    for i in range(query.record().count()):
                        valor = query.value(i)
                        # Convertir valores nulos a cadena vacía para evitar errores en la UI
                        fila.append("" if valor is None else str(valor))
                    registros.append(fila)

            return registros

        except Exception as e:
            print("Error listado ventas:", e)
            return []


    '''
    ZONA ALQUILERES
    '''

    def add_one_month(fecha):
        """Suma un mes a la fecha dada, ajustando el día si es necesario."""
        year, month, day = fecha.year, fecha.month, fecha.day
        if month == 12:
            new_year = year + 1
            new_month = 1
        else:
            new_year = year
            new_month = month + 1

        last_day = calendar.monthrange(new_year, new_month)[1]
        new_day = min(day, last_day)

        return fecha.replace(year=new_year, month=new_month, day=new_day)

    def altaAlquiler(nuevoAlquiler):
        try:
            # 1. Guardar el alquiler en la tabla ALQUILERES
            query = QtSql.QSqlQuery()
            query.prepare(
                "INSERT INTO ALQUILERES (propiedadid, clientedni, agenteid, fechainicio, fechafin, preciodealquiler, fecha) "
                "VALUES (:propiedadid, :clientedni, :agenteid, :fechainicio, :fechafin, :preciodealquiler, :fecha)")
            query.bindValue(":propiedadid", str(nuevoAlquiler[0]))
            query.bindValue(":clientedni", str(nuevoAlquiler[1]))
            query.bindValue(":agenteid", str(nuevoAlquiler[2]))
            query.bindValue(":fechainicio", str(nuevoAlquiler[3]))
            query.bindValue(":fechafin", str(nuevoAlquiler[4]))
            query.bindValue(":preciodealquiler", int(str(nuevoAlquiler[5])))
            query.bindValue(":fecha", str(nuevoAlquiler[6]))

            if not query.exec():
                print("Error dando de alta alquiler:", query.lastError().text())
                return False

            # 2. Obtener el ID del contrato insertado
            contrato_id = query.lastInsertId()
            if contrato_id is None:
                # En caso de no funcionar, consulta la tabla correcta (asegúrate de usar ALQUILERES y no contratos)
                query_contrato = QtSql.QSqlQuery()
                query_contrato.prepare("SELECT max(idalquiler) FROM ALQUILERES")

                if query_contrato.next():
                    contrato_id = query_contrato.value(0)

            # 3. Convertir las fechas usando el formato correcto (con barras '/')
            fecha_inicio = datetime.strptime(nuevoAlquiler[3], "%d/%m/%Y")
            fecha_fin = datetime.strptime(nuevoAlquiler[4], "%d/%m/%Y")

            # 4. Calcular las mensualidades
            mensualidades = []
            while fecha_inicio <= fecha_fin:
                mensualidades.append(fecha_inicio.strftime("%d/%m/%Y"))
                fecha_inicio = Conexion.add_one_month(fecha_inicio)
            print("Mensualidades calculadas:", mensualidades)

            # 5. Guardar las mensualidades en la tabla correspondiente
            for fecha in mensualidades:
                query_mensualidad = QtSql.QSqlQuery()
                query_mensualidad.prepare(
                    "INSERT INTO MENSUALIDADES (propiedad, contrato, mensualidad, importe, pago) "
                    "VALUES (:propiedad, :contrato, :mensualidad, :importe, :pago)")
                query_mensualidad.bindValue(":propiedad", str(nuevoAlquiler[0]))
                query_mensualidad.bindValue(":contrato", str(contrato_id))
                query_mensualidad.bindValue(":mensualidad", fecha)
                query_mensualidad.bindValue(":importe", str(nuevoAlquiler[5]))
                query_mensualidad.bindValue(":pago", "0")  # Por defecto, no pagado
                if not query_mensualidad.exec():
                    print("Error al insertar mensualidad:", query_mensualidad.lastError().text())
                    return False

            return True

        except Exception as e:
            print("Error alta alquiler:", e)
            return False

    def listadoAlquileres(self):
        try:
            registros = []

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM alquileres")
            if query.exec():
                while query.next():
                    fila = []
                    for i in range(query.record().count()):
                        valor = query.value(i)
                        # Convertir valores nulos a cadena vacía para evitar errores en la UI
                        fila.append("" if valor is None else str(valor))
                    registros.append(fila)

            return registros

        except Exception as e:
            print("Error listado alquileres", e)
            return []

    @staticmethod
    def delAqluiler(idAlquiler):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                "DELETE FROM ALQUILERES WHERE idalquiler = :idalquiler")
            query.bindValue(":idalquiler", idAlquiler)
            return query.exec()
        except Exception as exec:
            print("Error eliminando el alquiler", exec)

    def datosOneAlquiler(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM alquileres WHERE idalquiler = :idalquiler")

            if not id.isdigit():
                print("ID de alquiler no válido")
                return []

            query.bindValue(":idalquiler", int(id))

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))

            return registro

        except Exception as e:
            print("Error recuperando datos de alquiler", e)
            return []


    '''
    ZONA MENSUALIDADES
    '''

    @staticmethod
    def cargarTablaMensualidades(contrato_id):
        """
        Consulta en la base de datos las mensualidades para el contrato indicado y
        retorna una lista de tuplas con los siguientes datos:
          (codmes, propiedad_id, mensualidad, importe, pago)
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("""
                SELECT codmes, propiedad, mensualidad, importe, pago 
                FROM MENSUALIDADES 
                WHERE contrato = :contrato
                ORDER BY codmes
            """)
            query.bindValue(":contrato", int(contrato_id))
            if not query.exec():
                print("Error en consulta de mensualidades:", query.lastError().text())
                return []

            registros = []
            while query.next():
                codmes = query.value(0)
                propiedad_id = query.value(1)
                mes = query.value(2)
                importe = query.value(3)
                pago = query.value(4)
                registros.append((codmes, propiedad_id, mes, importe, pago))

            return registros

        except Exception as e:
            print("Error en cargarTablaMensualidades (Conexion):", e)
            return []

    @staticmethod
    def actualizarPago(codmes, state):
        """
        Actualiza el campo 'pago' de la mensualidad con id 'codmes' según el estado del checkbox.
        Si el checkbox está marcado (state == 2), se pone 1; si no, se pone 0.
        """
        try:
            # En PyQt6, state es un entero: 0 (Unchecked), 2 (Checked)
            pago = 1 if state == 2 else 0
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE MENSUALIDADES SET pago = :pago WHERE codmes = :codmes")
            query.bindValue(":pago", pago)
            query.bindValue(":codmes", codmes)
            if not query.exec():
                print("Error al actualizar el pago:", query.lastError().text())
        except Exception as e:
            print("Error en actualizarPago:", e)




