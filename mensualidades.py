from PyQt6 import QtWidgets, QtGui, QtCore, QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTableWidgetItem, QWidget, QVBoxLayout, QPushButton, QCheckBox

import alquileres
import propiedades
import var
import conexion

class Mensualidades:

    @staticmethod
    def cargaTablaMensualidades(self):
        """
        Obtiene el ID del contrato actual, llama al método de la clase Conexion para
        obtener los datos de las mensualidades y los carga en la tabla 'tablaMensualidades'.
        Las columnas serán:
          0: Recibo (codmes)
          1: Propiedad (dirección)
          2: id propiedad
          3: Precio (importe)
          4: Mes (mensualidad)
          5: Gestión (checkbox que refleja el campo 'pago')
        """
        try:
            # Limpiar la tabla
            var.ui.tablaMensualidades.clearContents()
            var.ui.tablaMensualidades.setRowCount(0)

            # Obtener el ID del contrato actual (se asume que está en txtidalquiler)
            contrato = var.ui.txtidalquiler.text()
            if not contrato.isdigit():
                print("ID de contrato inválido")
                return

            # Llamar al método de Conexion para obtener los registros de mensualidades
            registros = conexion.Conexion.cargarTablaMensualidades(contrato)

            var.ui.tablaMensualidades.setRowCount(len(registros))
            index = 0
            for registro in registros:
                codmes, direccion, propiedad_id, importe, mes, pago = registro

                # Columna 0: Recibo (codmes)
                item_recibo = QTableWidgetItem(str(codmes))
                item_recibo.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaMensualidades.setItem(index, 0, item_recibo)

                # Columna 1: Propiedad (dirección)
                item_direccion = QTableWidgetItem(str(direccion))
                item_direccion.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaMensualidades.setItem(index, 1, item_direccion)

                # Columna 2: id propiedad
                item_id_propiedad = QTableWidgetItem(str(propiedad_id))
                item_id_propiedad.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaMensualidades.setItem(index, 2, item_id_propiedad)

                # Columna 3: Precio (importe)
                item_importe = QTableWidgetItem(str(importe))
                item_importe.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaMensualidades.setItem(index, 3, item_importe)

                # Columna 4: Mes (mensualidad)
                item_mes = QTableWidgetItem(str(mes))
                item_mes.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaMensualidades.setItem(index, 4, item_mes)

                # Columna 5: Gestión (checkbox para el campo 'pago')
                checkbox = QCheckBox()
                checkbox.setChecked(str(pago) == "1")
                # Opcional: Conectar el cambio del checkbox para actualizar el campo en la base de datos
                container = QWidget()
                layout = QVBoxLayout(container)
                layout.addWidget(checkbox)
                layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                var.ui.tablaMensualidades.setCellWidget(index, 5, container)

                index += 1

        except Exception as e:
            print("Error al cargar la tabla de mensualidades (Mensualidades):", e)


