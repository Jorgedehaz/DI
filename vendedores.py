from datetime import datetime, date
from operator import index

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QIcon
import conexion
import conexionserver
import eventos
import var
import vendedores


class Vendedores:
    def checkDNI(dni):
        try:
            dni=str(dni).upper()
            var.ui.txtDniVend.setText(str(dni))
            check=eventos.Eventos.validarDNI(dni)
            if check:
                var.ui.txtDniVend.setStyleSheet('background-color: green;')
            else:
                var.ui.txtDniVend.setStyleSheet('background-color: red')
                var.ui.txtDniVend.setText(None)
                var.ui.txtDniVend.setPlaceholderText("dni no válido")
                var.ui.txtDniVend.setFocus()
        except Exception as e:
            print("error check cliente", e)

    def checkMovil(movil):
        try:
            movil=str(movil).upper()
            var.ui.txtMovilVend.setText(str(movil))
            check=eventos.Eventos.validarMovil(movil)
            if check:
                var.ui.txtMovilVend.setStyleSheet('background-color: green;')
            else:
                var.ui.txtMovilVend.setStyleSheet('background-color: red')
                var.ui.txtMovilVend.setText(None)
                var.ui.txtMovilVend.setPlaceholderText("movil no válido")
                var.ui.txtMovilVend.setFocus()
        except Exception as e:
            print("error check movil cliente", e)

    def checkEmail(mail):
        try:
            mail = str(var.ui.txtEmailVend.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailVend.setStyleSheet('background-color: green;')
                var.ui.txtEmailVend.setText(mail.lower())

            else:
                var.ui.txtEmailVend.setStyleSheet('background-color:red; font-style: italic;')
                var.ui.txtEmailVend.setText(None)
                var.ui.txtEmailVend.setPlaceholderText("correo no válido")
                var.ui.txtEmailVend.setFocus()

        except Exception as error:
            print("error check cliente", error)

    def altaVendedor(self):
        try:
            nuevovend= [var.ui.txtDniVend.text(), var.ui.txtNombreVend.text(), var.ui.txtAltaVend.text(),
                    var.ui.txtMovilVend.text(), var.ui.txtEmailVend.text(), var.ui.cmbProviVend.currentText()]
            if (var.ui.txtDniVend.text()!=""):
                if conexion.Conexion.altaVendedor(nuevovend):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText("Vendedor dado de alta en la BBDD")
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()
                    Vendedores.cargaTablaVendedores(self)
            else:
                mbox= QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                mbox.setText("Error faltan datos o vendedor existe")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()

        except Exception as e:
            print("error alta vendedor", e)

    def modifVendedor(self):
        try:
            modifvend = [var.ui.txtNombreVend.text(), var.ui.txtAltaVend.text(),var.ui.txtBajaVend.text(),
                    var.ui.txtMovilVend.text(), var.ui.txtEmailVend.text(), var.ui.cmbProviVend.currentText()]

            if conexion.Conexion.modifCliente(modifvend):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/iconoInmo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Datos de vendedor modificados')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

                vendedores.Vendedores.cargaTablaVendedores(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/iconoInmo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error al modificar datos de vendedor')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

        except Exception as error:
            print("Error modificando vendedor", error)

    def bajaVendedor(self):
        try:
            op = True
            fecha= datetime.now().strftime("%d/%m/%Y")
            var.ui.txtBajaVend = str(fecha)

            print(str(fecha))

            datos = [var.ui.txtDniVend ,var.ui.txtBajaVend]


            if conexion.Conexion.bajaVendedor(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/house.svg'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Vendedor dado de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

                vendedores.Vendedores.cargaTablaVendedores(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/house.svg'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error Baja Vendedor: cliente no existe o ya ha sido dado de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

        except Exception as e:
            print("Error baja de vendedor", e)

    def cargaTablaVendedores(self):
        try:
            listado = conexion.Conexion.listadoVendedores(self)  # Obtén el listado completo
            inicio = (var.paginavend - 1) * var.vendpxpagina
            fin = inicio + var.vendpxpagina
            vendedores_pagina = listado[inicio:fin]  # Filtra los vendedores según la página actual

            var.ui.tablaVendedores.setRowCount(0)  # Limpia la tabla antes de cargar nuevos datos
            for index, registro in enumerate(vendedores_pagina):
                var.ui.tablaVendedores.setRowCount(index + 1)
                var.ui.tablaVendedores.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaVendedores.setItem(index, 1, QtWidgets.QTableWidgetItem(str("  " + registro[2] + "  ")))
                var.ui.tablaVendedores.setItem(index, 2, QtWidgets.QTableWidgetItem(str("  " + registro[5] + "  ")))
                var.ui.tablaVendedores.setItem(index, 3, QtWidgets.QTableWidgetItem(str("   " + registro[7] + "   ")))

        except Exception as e:
            print("Error en cargaTablaVendedores:", e)

    def cargaOneVendedor(self):
        try:
            fila = var.ui.tablaVendedores.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneVendedor(str(datos[0]))
            registro = [x if x != 'None' else '' for x in registro]
            listado = [var.ui.txtCodigoVend, var.ui.txtDniVend, var.ui.txtNombreVend, var.ui.txtAltaVend, var.ui.txtBajaVend,
                    var.ui.txtMovilVend, var.ui.txtEmailVend, var.ui.cmbProviVend]

            for i in range(len(listado)):
                if i == 7:
                    listado[i].setCurrentText(registro[i])
                else:
                    listado[i].setText(registro[i])

            # Volcar datos vendedor a pag Ventas
            var.ui.txtVendedorFac.setText(str(registro[0]))

            #Volvar datos vendedor a pag Alquileres
            var.ui.txtVendedoralqui.setText(str(registro[0]))

        except Exception as error:
            print("Error cargando datos del vendedor", error)



    def historicoVend(self):
        try:
            if var.ui.chkHistoriaVend.isChecked():
                var.historico = 0
            else:
                var.historico = 1
            Vendedores.cargaTablaVendedores(self)
        except Exception as e:
            print("checkbox historico", e)