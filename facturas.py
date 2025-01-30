from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTableWidgetItem, QWidget, QVBoxLayout, QPushButton

import var
import conexion
import ventas


class Facturas:
    def altaFactura(self):
        try:
            nuevafactura = [var.ui.txtFechafac.text(),var.ui.txtdnifac.text()]
            if conexion.Conexion.altaFactura(nuevafactura):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText("Factura dado de alta en la BBDD")
                    mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()

                    #Vendedores.cargaTablaVendedores(self)
            else:
                mbox= QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                mbox.setText("Error faltan datos o factura existe")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()

            Facturas.mostrarTablaFactura(self)

        except Exception as e:
            print("error alta factura", e)

    @staticmethod
    def mostrarTablaFactura(self):
        try:
            var.ui.tablaFacturas.clearContents()
            var.ui.tablaFacturas.setRowCount(0)
            listado = conexion.Conexion.listadoFacturas(self)
            var.ui.tablaFacturas.setRowCount(len(listado))
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
                var.botondel.clicked.connect(Facturas.deleteFactura)

                layout.addWidget(var.botondel)
                layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(0)
                container.setLayout(layout)

                # Llenar las celdas de la tabla
                var.ui.tablaFacturas.setItem(index, 0, QTableWidgetItem(str(registro[0])))
                var.ui.tablaFacturas.setItem(index, 1, QTableWidgetItem(registro[2]))
                var.ui.tablaFacturas.setItem(index, 2, QTableWidgetItem(registro[1]))
                var.ui.tablaFacturas.setCellWidget(index, 3, container)

                # Alinear el texto de las celdas
                var.ui.tablaFacturas.item(index, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaFacturas.item(index, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaFacturas.item(index, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                # Incrementar el índice de la fila
                index += 1

        except Exception as e:
            print("Error al cargar la tabla de facturas:", e)

    @staticmethod
    def deleteFactura(self):
        try:
            sender = QtWidgets.QApplication.instance().focusWidget()  # Obtener el botón que disparó la acción
            if sender is None:
                raise Exception("No se pudo identificar el botón que disparó la acción.")

            row = sender.property("row")  # Obtener el ID de la factura
            if row is None:
                raise Exception("No se encontró la propiedad 'row' en el botón.")

            if not isinstance(row, int):
                raise Exception(f"Se esperaba un entero para 'row', pero se obtuvo {type(row)}.")

            # Eliminar la factura de la base de datos
            if conexion.Conexion.delFactura(row):  # Pasar el ID directamente
                msgbox = QtWidgets.QMessageBox()
                msgbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msgbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                msgbox.setWindowTitle("Aviso")
                msgbox.setText("Factura eliminada")
                msgbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msgbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText("Aceptar")
                msgbox.exec()
            else:
                print(f"Error al eliminar la factura con ID {row}.")

            Facturas.mostrarTablaFactura(self)

        except Exception as error:
            print("Error al eliminar factura:", error)

    def cargarOneFactura(self):
        try:
            fila = var.ui.tablaFacturas.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneFactura(str(datos[0]))
            listado = [var.ui.txtidfac, var.ui.txtFechafac, var.ui.txtdnifac]

            for i in range(len(listado)):
                listado[i].setText(str(registro[i]))

            ventas.Ventas.cargarTablaVentas(self)

        except Exception as error:
            print("Error cargando datos de la factura", error)
