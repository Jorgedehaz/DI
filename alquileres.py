from PyQt6 import QtWidgets, QtGui, QtCore, QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTableWidgetItem, QWidget, QVBoxLayout, QPushButton

import alquileres
import mensualidades
import propiedades
import var
import conexion

class Alquileres:

    def altaAlquiler(self):
        try:
            nuevoAlquiler = [var.ui.txtPropiedadalqui.text(),var.ui.txtdniclialqui.text(),var.ui.txtVendedoralqui.text(),
                             var.ui.txtFechaini.text(), var.ui.txtFechafin.text(),
                             var.ui.txtPrecioalquilerprop.text(),var.ui.txtfechaalquiler.text()]
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
                var.botondel.clicked.connect(Alquileres.deleteAlquiler)

                layout.addWidget(var.botondel)
                layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(0)
                container.setLayout(layout)

                # Llenar las celdas de la tabla
                # Crear un QTableWidgetItem para cada celda
                item1 = QTableWidgetItem(str(registro[0]))
                item2 = QTableWidgetItem(registro[2])

                var.ui.tablaContrato.setItem(index, 0, item1)
                var.ui.tablaContrato.setItem(index, 1, item2)
                var.ui.tablaContrato.setCellWidget(index, 2, container)

                # Alinear el texto de las celdas
                item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                # Incrementar el índice de la fila
                index += 1

        except Exception as e:
            print("Error al cargar la tabla de contratos de alquiler:", e)

    @staticmethod
    def deleteAlquiler(self):
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
            if conexion.Conexion.delAqluiler(row):  # Pasar el ID directamente
                msgbox = QtWidgets.QMessageBox()
                msgbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msgbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                msgbox.setWindowTitle("Aviso")
                msgbox.setText("Alquiler eliminado")
                msgbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msgbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText("Aceptar")
                msgbox.exec()
            else:
                print(f"Error al eliminar el alquiler con ID {row}.")

            Alquileres.cargarTablaAlquileres(self)

        except Exception as error:
            print("Error al eliminar factura:", error)

    def cargarOneAlquiler(self):
        try:
            fila = var.ui.tablaContrato.selectedItems()
            if not fila:
                print("No se ha seleccionado ninguna fila")
                return

            datos = [dato.text() for dato in fila]

            if not datos:
                print("No hay datos en la fila seleccionada")
                return

            registro = conexion.Conexion.datosOneAlquiler(str(datos[0]))

            if not registro:
                print("No se encontraron datos del alquiler con ese ID")
                return

            # Validación para evitar desbordamiento de índice
            while len(registro) < 8:
                registro.append("")

            listado = [var.ui.txtidalquiler, var.ui.txtPropiedadalqui, var.ui.txtdniclialqui,
                       var.ui.txtVendedoralqui, var.ui.txtFechaini, var.ui.txtFechafin,
                       var.ui.txtfechaalquiler]

            for i in range(len(listado)):
                if i == 6:
                    listado[i].setText(registro[7])
                else:
                    listado[i].setText(registro[i])

            alquileres.Alquileres.cargarTablaAlquileres(self)
            mensualidades.Mensualidades.cargaTablaMensualidades(self)

        except Exception as error:
            print("Error cargando datos del alquiler", error)
