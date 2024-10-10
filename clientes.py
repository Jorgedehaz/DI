from operator import index

from PyQt6 import QtWidgets, QtGui, QtCore


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