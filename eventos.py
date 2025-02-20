import csv
import json
import os
import shutil
import sys
import time
import zipfile

import conexionserver
import eventos
import clientes
import var

from PyQt6.QtGui import QIcon
from datetime import datetime

import conexion
import re

from PyQt6 import QtWidgets, QtGui


class Eventos():


    def mensajeSalir(self=None):
        mbox=QtWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))

        mbox.setWindowTitle('Salir')
        mbox.setText('Desea salir?')
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')

        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            mbox.hide()

    def cargarProv(self):
        var.ui.cmbProvicli.clear()
        listado=conexion.Conexion.listaProv(self)
        #listado=conexionserver.ConexionServer.listaProv(self)
        var.ui.cmbProvicli.addItems(listado)

    def cargaMunicli(self):
        provincia= var.ui.cmbProvicli.currentText()
        listado= conexion.Conexion.listaMuniprov(provincia)
        #listado= conexionserver.ConexionServer.listaMuniProv(provincia)
        var.ui.cmbMunicli.clear()
        var.ui.cmbMunicli.addItems(listado)

    def cargarProvprop(self):
        var.ui.cmbProviprop.clear()
        listado=conexion.Conexion.listaProv(self)
        var.ui.cmbProviprop.addItems(listado)

    def cargaMuniprop(self):
        provincia= var.ui.cmbProviprop.currentText()
        listado= conexion.Conexion.listaMuniprov(provincia)
        var.ui.cmbMuniprop.clear()
        var.ui.cmbMuniprop.addItems(listado)

    def cargarProviVend(self):
        var.ui.cmbProviVend.clear()
        listado=conexion.Conexion.listaProv(self)
        var.ui.cmbProviVend.addItems(listado)

    def validarDNI(dni):
        try:
            dni = str(dni).upper()
            var.ui.txtDnicli.setText(str(dni))
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:
                    dig_control = dni[8]
                    dni = dni[:8]
                    if dni[0] in dig_ext:
                        dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                    if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                        return True
                    else:
                        return False
            else:
                return False
        except Exception as error:
            print("error en validar dni ", error)


    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            if var.ui.panPrincipal.currentIndex() == 0 and var.btn==0:
                var.ui.txtAltacli.setText(str(data))
            elif var.ui.panPrincipal.currentIndex() == 0 and var.btn==1:
                var.ui.txtBajacli.setText(str(data))
            elif var.ui.panPrincipal.currentIndex() == 1 and var.btn==2:
                var.ui.txtAltaprop.setText(str(data))
            elif var.ui.panPrincipal.currentIndex() == 1 and var.btn==3:
                var.ui.txtBajaprop.setText(str(data))
            elif var.ui.panPrincipal.currentIndex () == 2 and var.btn==4:
                var.ui.txtAltaVend.setText(str(data))
            elif var.ui.panPrincipal.currentIndex() == 3 and var.btn==5:
                var.ui.txtFechafac.setText(str(data))
            elif var.ui.panPrincipal.currentIndex() == 4 and var.btn==6:
                var.ui.txtfechaalquiler.setText(str(data))
            elif var.ui.panPrincipal.currentIndex() == 4 and var.btn==7:
                var.ui.txtFechaini.setText(str(data))
            elif var.ui.panPrincipal.currentIndex() == 4 and var.btn==8:
                var.ui.txtFechafin.setText(str(data))
            time.sleep(0.5)
            var.uiCalendar.hide()
            return data
        except Exception as error:
            print("error en cargar fecha: ", error)

    def validarMail(mail):
        mail = mail.lower()
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(regex, mail):
            return True
        else:
            return False

    def validarMovil(movil):
        if re.fullmatch(r'\d{9}', movil):  # Valida si son exactamente 9 dígitos
            return True
        else:
            return False

    def resizeTablaClientes(self):
        try:
            header = var.ui.tablaClientes.horizontalHeader()
            for i in range(header.count()):
                if (i==0 or i==1 or i==3 or i==4):
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_items =var.ui.tablaClientes.horizontalHeaderItem(i)
                font=header_items.font()
                font.setBold(True)
                header_items.setFont(font)



        except Exception as e:
            print("error en resize tabla clientes: ", e)

    def resizeTablaPropiedades(self):
        try:
            header = var.ui.tablaPropiedades.horizontalHeader()
            for i in range(header.count()):
                if (i==1 or i==2):
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_items =var.ui.tablaPropiedades.horizontalHeaderItem(i)
                font=header_items.font()
                font.setBold(True)
                header_items.setFont(font)



        except Exception as e:
            print("error en resize tabla clientes: ", e)

    def resizeTablaVendedores(self):
        try:
            header = var.ui.tablaVendedores.horizontalHeader()
            for i in range(header.count()):
                if (i==1 or i==2 or i==3):
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_items =var.ui.tablaPropiedades.horizontalHeaderItem(i)
                font=header_items.font()
                font.setBold(True)
                header_items.setFont(font)



        except Exception as e:
            print("error en resize tabla clientes: ", e)

    def resizeTablaFacturas(self):
        try:
            header = var.ui.tablaFacturas.horizontalHeader()
            for i in range(header.count()):
                if (i==1 or i==2):
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_items =var.ui.tablaFacturas.horizontalHeaderItem(i)
                font=header_items.font()
                font.setBold(True)
                header_items.setFont(font)



        except Exception as e:
            print("error en resize tabla facturas: ", e)

    def resizeTablaVentas(self):
        try:
            header = var.ui.tablaVentas.horizontalHeader()
            for i in range(header.count()):
                if (i==2 or i==3 or i==4 or i==5):
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_items =var.ui.tablaVentas.horizontalHeaderItem(i)
                font=header_items.font()
                font.setBold(True)
                header_items.setFont(font)



        except Exception as e:
            print("error en resize tabla facturas: ", e)

    def resizeTablaAlquileres(self):
        try:
            header = var.ui.tablaContrato.horizontalHeader()
            for i in range(header.count()):
                if (i==1 or i==2):
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_items =var.ui.tablaContrato.horizontalHeaderItem(i)
                font=header_items.font()
                font.setBold(True)
                header_items.setFont(font)



        except Exception as e:
            print("error en resize tabla Alquileres: ", e)

    def resizeTablaMensualidades(self):
        try:
            header = var.ui.tablaMensualidades.horizontalHeader()
            for i in range(header.count()):
                if (i == 1 or i == 2 or i == 3):
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_items = var.ui.tablaMensualidades.horizontalHeaderItem(i)
                font = header_items.font()
                font.setBold(True)
                header_items.setFont(font)



        except Exception as e:
            print("error en resize tabla Alquileres: ", e)

    def abrirTipoprop(self):
        try:
            var.dlggestion.show()
        except Exception as error:
            print("error en abrir gestión propiedades: ", error)

    def abrirTipoprop(self):
        try:
            var.dlggestion.show()
        except Exception as error:
            print("error en abrir gestión propiedades: ", error)





    '''
    BACKUPS
    '''
    def crearBackup(self):
        try:
            fecha = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            copia = str(fecha) + "_backup.zip"

            directorio, fichero = var.dlgabrir.getSaveFileName(None, "Guardar Copia Seguridad", copia, '.zip')
            if var.dlgabrir.accept and fichero:
                fichezip = zipfile.ZipFile(fichero, 'w')
                fichezip.write('bbdd.sqlite', os.path.basename('bbdd.sqlite'), zipfile.ZIP_DEFLATED)
                fichezip.close()
                shutil.move(fichero, directorio)

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/house.svg'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Copia de seguridad')
                mbox.setText('Copia de seguridad creada')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

        except Exception as error:
            print("error en crear backup: ", error)

    def restauraraBackup(self):
        try:
            filename = var.dlgabrir.getOpenFileName(None, "Restaurar Copia Seguridad", '', '*.zip;;All Files (*)')
            file = filename[0]
            if file:
                with zipfile.ZipFile(file, 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/iconoInmo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Copia de seguridad')
                mbox.setText('Copia de seguridad restaurada')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()
                conexion.Conexion.db_conexion(self)
                eventos.Eventos.cargarProvincias(self)
                clientes.Clientes.cargaTablaCientes(self)

        except Exception as e:
            print("error en restaurar backup: ", e)

    '''
    EXPORTS
    '''

    def exportCSVprop(self):
        try:
            var.historico = 0
            fecha=datetime.today()
            fecha=fecha.strftime("%Y_%m_%d_%H_%M_%S")
            file=(str(fecha) + 'Datospropiedades.csv')
            directorio,fichero= var.dlgabrir.getSaveFileName(None, "Exportar CSV", file, '.csv')
            if fichero:
                registros=conexion.Conexion.listadoPropiedades(self)
                with open(fichero, 'w', newline='') as csvfile:
                    writer=csv.writer(csvfile) #creo el puntero de almacenamiento
                    writer.writerow(["Codigo","Alta","Baja","Dirección","Provincia","Municipio","Tipo",
                                     "Nº Habitaciones", "Nº Baños","Superficie", "Precio Alquiler", "Precio Compra",
                                     "Código Postal","Observaciones","Operación","Estado","Propietario","Móvil"])
                    for registro in registros:
                        writer.writerow(registro)
                shutil.move(fichero, directorio)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/iconoInmo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Copia de seguridad')
                mbox.setText('Error Exportación de Datos Propiedades')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
        except Exception as e:
            print(e)

    def exportJSONprop(self):
        try:
            var.historico = 0
            fecha=datetime.today()
            fecha=fecha.strftime("%Y_%m_%d_%H_%M_%S")
            file=(str(fecha) + 'Datospropiedades.json')
            directorio,fichero = var.dlgabrir.getSaveFileName(None, "Exportar JSON", file, '.json')
            if fichero:
                keys = ["Codigo","Alta","Baja","Dirección","Provincia","Municipio","Tipo",
                                     "Nº Habitaciones", "Nº Baños","Superficie", "Precio Alquiler", "Precio Compra",
                                     "Código Postal","Observaciones","Operación","Estado","Propietario","Móvil"]
                registros = conexion.Conexion.listadoPropiedades(self)
                lista_propiedades= [dict(zip(keys,registro))for registro in registros]
                with open(fichero, 'w', newline='',encoding='utf-8') as jsonfile:
                    json.dump(lista_propiedades, jsonfile,ensure_ascii=False, indent=4)
                shutil.move(fichero, directorio)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/iconoInmo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Copia de seguridad')
                mbox.setText('Error Exportación de Datos Propiedades')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

        except Exception as e:
            print(e)


    '''
    OTROS
    '''

    def abrirCalendar(btn):
        try:
            var.btn = btn
            var.uiCalendar.show()
        except Exception as error:
            print("error en abrir calendar ", error)


    def limpiarPanel(self):
        camposPanel = [var.ui.txtDnicli, var.ui.txtAltacli, var.ui.txtApelcli,
                       var.ui.txtNomcli, var.ui.txtEmailcli, var.ui.txtMovilcli,
                       var.ui.txtDircli, var.ui.cmbProvicli, var.ui.cmbMunicli, var.ui.txtBajacli]
        for i, dato in enumerate(camposPanel):
            if i == 7 or i == 8:
                pass
            else:
                dato.setText("")

            eventos.Eventos.cargarProv(self)

        camposPanel2 = [var.ui.txtCodigoprop,var.ui.txtAltaprop,var.ui.txtBajaprop,var.ui.txtDirprop,
                       var.ui.cmbProviprop,var.ui.cmbMuniprop,var.ui.cmbTipoprop, var.ui.txtSuperprop,
                       var.ui.txtPrecioalquilerprop,var.ui.txtPrecioventaprop,
                       var.ui.txtCodigopostalprop,var.ui.txtObservaprop,var.ui.txtPropietarioprop,var.ui.txtMovilprop]
        for i, dato in enumerate(camposPanel2):
            if i == 4 or i == 5 or i == 6:
                pass
            else:
                dato.setText("")

            eventos.Eventos.cargarProv(self)

    def abrirTipoprop(self):
        try:
            var.dlggestion.show()
        except Exception as error:
            print("error en abrir tipoprop: ", error)

    def cargarTipoprop(self):
        registro=conexion.Conexion.cargarTipoprop(self)
        var.ui.cmbTipoprop.clear()
        var.ui.cmbTipoprop.addItems(registro)

    def abrirAbout(self):
        try:
            var.dlgabout.show()
        except Exception as error:
            print ("error en abrir About", error)

    def abrirBuscarProp(self):
        try:
            var.dlgbuscarprop.show()
        except Exception as error:
            print("error abriendo BuscarProp : ", error)

    def limpiarPanFacturas(self):
        camposPanelFac=[var.ui.txtidfac, var.ui.txtFechafac, var.ui.txtdnifac, var.ui.txtApellidoFac, var.ui.txtNombreFac,
                        var.ui.txtDirFac, var.ui.txtCodigoFac, var.ui.txtTipoFac, var.ui.txtLocalidadFac, var.ui.txtPrecioFac,
                        var.ui.txtVendedorFac]

        for i, dato in enumerate(camposPanelFac):
            dato.setText("")