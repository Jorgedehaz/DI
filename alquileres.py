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
            nuevoAlquiler = [var.ui.txtPropiedadalqui.text(),var.ui.txtdniclialqui.text(),var.ui.txtVendedoralqui.text(),
                             var.ui.txtfechaalquiler.text()]
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

    @staticmethod
    def cargarTablaAlquileres(self):
            try:
                var.ui.tablaContrato.clearContents()
                var.ui.tablaContrato.setRowCount(0)
                listado = conexion.Conexion.listadoAlquileres(self)
                var.ui.tablaContrato.setRowCount(len(listado))
                index = 0
                for registro in listado:
                    # Crear un botón con una propiedad 'row' que almacena el índice de la fila
                    container = QWidget()
                    layout = QVBoxLayout()
                    var.botondel = QPushButton()
                    var.botondel.setFixedSize(30, 20)
                    var.botondel.setIcon(QIcon("./img/borrar.ico"))
                    var.botondel.setStyleSheet("background-color: #efefef;")

                    # Asignar la fila actual como propiedad 'row' del botón
                    var.botondel.setProperty("row", int(registro[0]))

                    # Conectar el botón a la función deleteFactura
                    var.botondel.clicked.connect(Alquileres.deleteFactura)

                    layout.addWidget(var.botondel)
                    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    layout.setContentsMargins(0, 0, 0, 0)
                    layout.setSpacing(0)
                    container.setLayout(layout)

                    # Llenar las celdas de la tabla
                    var.ui.tablaContrato.setItem(index, 0, QTableWidgetItem(str(registro[0])))
                    var.ui.tablaContrato.setItem(index, 1, QTableWidgetItem(registro[2]))
                    var.ui.tablaContrato.setCellWidget(index, 2, container)

                    # Alinear el texto de las celdas
                    var.ui.tablaContrato.item(index, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    var.ui.tablaContrato.item(index, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    var.ui.tablaContrato.item(index, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                    # Incrementar el índice de la fila
                    index += 1

            except Exception as e:
                print("Error al cargar la tabla de contratos de alquiler:", e)