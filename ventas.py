from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTableWidgetItem, QWidget, QVBoxLayout, QPushButton

import propiedades
import var
import conexion

class Ventas:

    def altaVenta(self):
        try:
            nuevaVenta = [var.ui.txtidfac.text(),var.ui.txtCodigoFac.text(),var.ui.txtVendedorFac.text(),var.ui.txtCodigoFac.text()]
            if conexion.Conexion.altaVenta(nuevaVenta):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText("Venta dado de alta en la BBDD")
                    mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()


            else:
                mbox= QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                mbox.setText("Error faltan datos o venta existe")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()

            Ventas.cargarTablaVentas(self)
            propiedades.Propiedades.cargaTablaPropiedades(self)

        except Exception as e:
            print("error alta factura", e)

    @staticmethod
    def cargarTablaVentas(self):
        try:
            var.ui.tablaVentas.clearContents()
            var.ui.tablaVentas.setRowCount(0)
            listado = conexion.Conexion.listadoVentas(var.ui.txtidfac.text())
            var.ui.tablaVentas.setRowCount(len(listado))
            index = 0

            for registro in listado:

                # Llenar las celdas de la tabla
                var.ui.tablaVentas.setItem(index, 0, QTableWidgetItem(str(registro[0])))
                var.ui.tablaVentas.setItem(index, 1, QTableWidgetItem(str(registro[1])))
                var.ui.tablaVentas.setItem(index, 2, QTableWidgetItem(str(registro[2])))
                var.ui.tablaVentas.setItem(index, 3, QTableWidgetItem(str(registro[3])))
                var.ui.tablaVentas.setItem(index, 4, QTableWidgetItem(str(registro[4])))
                var.ui.tablaVentas.setItem(index, 5, QTableWidgetItem(str(registro[5])))

                # Alinear el texto de las celdas
                var.ui.tablaVentas.item(index, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaVentas.item(index, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaVentas.item(index, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaVentas.item(index, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaVentas.item(index, 4).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaVentas.item(index, 5).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                index += 1

        except Exception as e:
            print("Error al cargar la tabla de ventas:", e)

    def cargarOneVenta(self):

            fila = var.ui.tablaVentas.selectedItems()

            datos = [dato.text() for dato in fila]

            precio_venta = float(datos[5].replace(",", ".").strip())
            impuestos = precio_venta * 0.10
            precio_total = precio_venta + impuestos

            var.ui.txtPrecioVentaFac.setText(f"{precio_venta:.2f}")
            var.ui.txtImpuestos.setText(f"{impuestos:.2f}")
            var.ui.txtPrecioTotal.setText(f"{precio_total:.2f}")


