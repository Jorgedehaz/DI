from operator import index

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QIcon

import conexion
import eventos
import var

class Clientes:
    def checkDNI(dni):
        try:
            dni=str(dni).upper()
            var.ui.txtDnicli.setText(str(dni))
            check=eventos.Eventos.validarDNI(dni)
            if check:
                var.ui.txtDnicli.setStyleSheet('background-color: green;')
            else:
                var.ui.txtDnicli.setStyleSheet('background-color: red')
                var.ui.txtDnicli.setText(None)
                var.ui.txtDnicli.setFocus()
        except Exception as e:
            print("error check cliente", e)



    def altaCliente(self):
        try:
            nuevocli= [var.ui.txtDnicli.text(), var.ui.txtAltacli.text(), var.ui.txtApelcli.text(), var.ui.txtNomcli.text(),
                    var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text(), var.ui.cmbProvicli.currentText(),
                    var.ui.cmbMunicli.currentText()]
            if (var.ui.txtDnicli.text()!=""):
                if conexion.Conexion.altaCliente(nuevocli):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText("Cliente dado de alta en la BBDD")
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()
                    Clientes.cargaTablaClientes(self)
            else:
                mbox= QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                mbox.setText("Error faltan datos o cliente existe")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()

        except Exception as e:
            print("error alta cliente", e)

    def checkEmail(mail):
        try:
            mail = str(var.ui.txtEmailcli.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailcli.setStyleSheet('background-color: green;')
                var.ui.txtEmailcli.setText(mail.lower())

            else:
                var.ui.txtEmailcli.setStyleSheet('background-color:red; font-style: italic;')
                var.ui.txtEmailcli.setText(None)
                var.ui.txtEmailcli.setText("correo no válido")
                var.ui.txtEmailcli.setFocus()

        except Exception as error:
            print("error check cliente", error)

    def cargaTablaClientes(self):
        try:
            listado = conexion.Conexion.listadoClientes(self)
            index=0
            print(listado)
            for registro in listado:
                var.ui.tablaClientes.setRowCount(index + 1)
                var.ui.tablaClientes.setItem(index,0, QtWidgets.QTableWidgetItem(registro[2]))
                var.ui.tablaClientes.setItem(index,1, QtWidgets.QTableWidgetItem(registro[3]))
                var.ui.tablaClientes.setItem(index,2, QtWidgets.QTableWidgetItem("  " + registro[5] + "  "))
                var.ui.tablaClientes.setItem(index,3, QtWidgets.QTableWidgetItem(registro[7]))
                var.ui.tablaClientes.setItem(index,4, QtWidgets.QTableWidgetItem(registro[8]))
                var.ui.tablaClientes.setItem(index,5, QtWidgets.QTableWidgetItem(registro[9]))
                var.ui.tablaClientes.item(index,0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index,1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index,2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaClientes.item(index,3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index,4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index,5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)

                index+=1

        except Exception as e:
            print("error cargaTablaClientes", e)

    def cargaOneCliente(self):
        try:
            fila = var.ui.tabClientes.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneCliente(str(datos[0]))
            listado = [var.ui.txtDnicli, var.ui.txtAltacli, var.ui.txtApelcli,
                       var.ui.txtNomcli, var.ui.txtEmailcli, var.ui.txtMovilcli,
                       var.ui.txtDircli,
                       var.ui.cmbProvicli, var.ui.cmbMunicli]

            for i in range(len(listado)):
                if i == 7 or i == 8:
                    listado[i].setCurrentText(registro[i])
                else:
                    listado[i].setText(registro[i])

        except Exception as error:
            print("Error cargando datos del cliente", error)

    def modifCliente(self):
        try:
            modifCli = [var.ui.txtDnicli.text(), var.ui.txtAltacli.text(), var.ui.txtApelcli.text(),
                        var.ui.txtNomcli.text(), var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(),
                        var.ui.txtDircli.text(),
                        var.ui.cmbProvicli.currentText(), var.ui.cmbMunicli.currentText()]

            if conexion.Conexion.modifCliente(modifCli):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/iconoInmo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Datos de cliente modificados')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

                clientes.Clientes.cargaTablaClientes(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/iconoInmo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error al modificar datos de cliente')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

        except Exception as error:
            print("Error cargando la tabla de clientes", error)

    def bajaCliente(self):
        try:
            datos = [var.ui.txtDniCliente.text(), var.ui.txtBajaCliente.text()]

            if conexion.Conexion.bajaCliente(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/house.svg'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Cliente dado de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

                clientes.Clientes.cargaTablaClientes(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/house.svg'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error Baja Cliente: cliente no existe o ya ha sido dado de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

        except Exception as e:
            print("Error baja de clientes", e)