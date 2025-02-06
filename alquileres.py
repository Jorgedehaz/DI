from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTableWidgetItem, QWidget, QVBoxLayout, QPushButton

import propiedades
import var
import conexion

class Alquileres:

    def altaAlquiler(self):
        try:
            nuevoAlquiler = [var.ui.txtidfac.text(),var.ui.txtCodigoFac.text(),var.ui.txtVendedorFac.text(),var.ui.txtCodigoFac.text()]
            if conexion.Conexion.altaAlquiler(nuevoAlquiler):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText("Alquiler dado de alta en la BBDD")
                    mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()


            else:
                mbox= QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                mbox.setText("Error faltan datos o alquiler existe")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()

            Alquileres.cargarTablaAlquileres(self)
            propiedades.Propiedades.cargaTablaPropiedades(self)

        except Exception as e:
            print("error alta Alquiler", e)