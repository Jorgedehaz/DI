import os
import sqlite3
from logging import exception

from PyQt6 import QtSql, QtWidgets, QtCore


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
        listaprov = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM provincias")
        if query.exec():
            while query.next():
                listaprov.append(query.value(1))
        print(listaprov)
        return listaprov

    def listaMuniprov(provincia):
        listamunicipios = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM municipios where idprov = (select idprov from provincias  where provincia = ?)")
        query.bindValue(0, provincia)
        if query.exec():
            while query.next():
                listamunicipios.append(query.value(1))
        return listamunicipios

    def altaCliente(nuevocli):
        try:

            query = QtSql.QSqlQuery()
            query.prepare("INSERT into CLIENTES (dnicli,altacli,apelcli,nomecli,emailcli,movilcli,dircli,"
                          " provcli,municli,bajacli) VALUES (:dnicli,:altacli,:apelcli,:nomecli,:emailcli,:movilcli,:dircli,"
                          " :provcli,:municli,:bajacli)")
            query.bindValue(":dnicli", str(nuevocli[0]))
            query.bindValue(":altacli", str(nuevocli[1]))
            query.bindValue(":apelcli", str(nuevocli[2]))
            query.bindValue(":nomecli", str(nuevocli[3]))
            query.bindValue(":emailcli",str(nuevocli[4]))
            query.bindValue(":movilcli",str(nuevocli[5]))
            query.bindValue(":dircli",str(nuevocli[6]))
            query.bindValue(":provcli",str(nuevocli[7]))
            query.bindValue(":municli", str(nuevocli[8]))
            query.bindValue(":bajacli", str(nuevocli[9]))

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


    '''
    BLOQUE METODOS CONEXION PROPIEDADES
    '''
    def altaTipoprop(tipo):
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
            print(registro)
            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error modificar propiedad", error)

    def bajaPropiedad(datos):
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
            query.prepare("SELECT * FROM propiedades WHERE tipoprop = :tipoprop and muniprop = :muniprop ORDER BY codigo")
            query.bindValue("tipoprop",str(datos[0]))
            query.bindValue("muniprop", str(datos[1]))
            if query.exec():
                while query.next():
                    prop= []
                    for i in range(query.record().count()):
                        prop.append(str(query.value(i)))
                    registro.append(prop)
            print (registro)
            return registro
        except Exception as e:
            print("Error buscar propiedad", e)

