from PyQt6 import QtWidgets, QtGui, QtCore, QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTableWidgetItem, QWidget, QVBoxLayout, QPushButton

import alquileres
import propiedades
import var
import conexion

class Mensualidades:

    @staticmethod
    def cargarTablaMensualidades(self):
        try:
            var.ui.tablaMensualidades.clearContents()
            var.ui.tablaMensualidades.setRowCount(0)
            listado = conexion.Conexion.listadoAlquileres(self)
            var.ui.tablaMensualidades.setRowCount(len(listado))
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
