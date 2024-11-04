from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QIcon
import clientes
import conexion
import eventos
import var
from conexion import Conexion


class Propiedades():

    def altaTipopropiedad(self):
        try:
            tipo = var.dlggestion.ui.txtGestipoprop.text().title()
            registro = conexion.Conexion.altaTipoprop(tipo)
            if registro:
                var.ui.cmbTipoprop.clear()
                var.ui.cmbTipoprop.addItems(registro)
            elif not registro:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                mbox.setText("Propiedad Existe")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()
            var.dlggestion.ui.txtGestipoprop.setText("")
        except Exception as e:
            print(f"Error: {e}")

    def bajaTipopropiedad(self):
        try:
            tipo = var.dlggestion.ui.txtGestipoprop.text().title()
            if conexion.Conexion.bajaTipoprop(tipo):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                mbox.setText("Tipo Propiedad Eliminada")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                mbox.setText("Propiedad No Existe")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()
            registro= conexion.Conexion.cargarTipoprop(self)
            var.ui.cmbTipoprop.clear()
            var.ui.cmbTipoprop.addItem(registro)
        except Exception as e:
            print(f"Error: {e}")

    def altaPropiedad(self):
        try:
            propiedad=[var.ui.txtAltaprop.text(),var.ui.txtDirprop.text(),
                       var.ui.cmbProviprop.currentText(),var.ui.cmbMuniprop.currentText(),var.ui.cmbTipoprop.currentText(),
                       var.ui.spinHabitaprop.value(),var.ui.spinBanosprop.value(), var.ui.txtSuperprop.text(),
                       var.ui.txtPrecioalquilerprop.text(),var.ui.txtPrecioventaprop.text(),
                       var.ui.txtCodigopostalprop.text(),var.ui.txtObservaprop.toPlainText()]

            tipooperacion = []
            if var.ui.chkAlquilerprop.isChecked():
                tipooperacion.append(var.ui.chkAlquilerprop.text())
            if var.ui.chkVentaprop.isChecked():
                tipooperacion.append(var.ui.chkVentaprop.text())
            if var.ui.chkIntercambioprop.isChecked():
                tipooperacion.append(var.ui.chkIntercambioprop.text())
            tipooperacion = "-".join(tipooperacion)
            propiedad.append(tipooperacion)

            if var.ui.radioDispoprop.isChecked():
                propiedad.append(var.ui.radioDispoprop.text())
            elif var.ui.radioAlquiladoprop.isChecked():
                propiedad.append(var.ui.radioAlquiladoprop.text())
            elif var.ui.radioVendidoprop.isChecked():
                propiedad.append(var.ui.radioVendidoprop.text())

            propiedad.append(var.ui.txtPropietarioprop.text())
            propiedad.append(var.ui.txtMovilprop.text())
            if conexion.Conexion.altaPropiedad(propiedad):
                mbox = QtWidgets.QMessageBox(self)
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                mbox.setText("Propiedad Dada de Alta")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()

            print(propiedad)
        except Exception as e:
            print("error alta propiedad" + str(e))