from PyQt6 import QtWidgets
from PyQt6.uic.properties import QtGui

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
            else:
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               QtWidgets.QMessageBox.StandardButton.Cancel)
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