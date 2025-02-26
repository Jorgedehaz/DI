from PyQt6 import QtWidgets, QtGui, QtCore, QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTableWidgetItem, QWidget, QVBoxLayout, QCheckBox, QPushButton

import conexion
import informes  # Asegúrate de importar el módulo informes
import var

class Mensualidades:

    @staticmethod
    def cargaTablaMensualidades(self):
        """
        Obtiene el ID del contrato actual, llama al método de la clase Conexion para
        obtener los datos de las mensualidades y los carga en la tabla 'tablaMensualidades'.
        Las columnas serán:
          0: Recibo (codmes)
          1: id propiedad
          2: Precio (importe)
          3: Mes (mensualidad)
          4: Gestión (checkbox que refleja y permite actualizar el campo 'pago')
          5: Reporte (botón para generar el reporte de la mensualidad)
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
                # Se espera que 'registro' contenga: (codmes, propiedad_id, mes, importe, pago)
                codmes, propiedad_id, mes, importe, pago = registro

                # Columna 0: Recibo (codmes)
                item_recibo = QTableWidgetItem(str(codmes))
                item_recibo.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaMensualidades.setItem(index, 0, item_recibo)

                # Columna 1: id propiedad
                item_id_propiedad = QTableWidgetItem(str(propiedad_id))
                item_id_propiedad.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaMensualidades.setItem(index, 1, item_id_propiedad)

                # Columna 2: Precio (importe)
                item_importe = QTableWidgetItem(str(importe))
                item_importe.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaMensualidades.setItem(index, 2, item_importe)

                # Columna 3: Mes (mensualidad)
                item_mes = QTableWidgetItem(str(mes))
                item_mes.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaMensualidades.setItem(index, 3, item_mes)

                # Columna 4: Gestión (checkbox para el campo 'pago')
                checkbox = QCheckBox()
                checkbox.setChecked(str(pago) == "1")
                # Conectar el cambio del checkbox para actualizar el valor en la BD.
                # Usamos lambda con parámetro por defecto para capturar el valor de codmes en esta iteración.
                checkbox.stateChanged.connect(lambda state, cod=codmes: conexion.Conexion.actualizarPago(cod, state))
                container = QWidget()
                layout = QVBoxLayout(container)
                layout.addWidget(checkbox)
                layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                var.ui.tablaMensualidades.setCellWidget(index, 4, container)

                # Columna 5: Reporte (botón para llamar a reportMensualidad de informes)
                btnReport = QPushButton()
                btnReport.setFixedSize(30, 20)
                btnReport.setIcon(QIcon("./img/recibo.ico"))
                btnReport.setStyleSheet("background-color: #efefef;")
                btnReport.clicked.connect(lambda checked, cod=codmes: informes.Informes.reportMensualidad(cod))

                containerReport = QWidget()
                layoutReport = QtWidgets.QHBoxLayout(containerReport)
                layoutReport.addWidget(btnReport)
                layoutReport.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layoutReport.setContentsMargins(0, 0, 0, 0)
                var.ui.tablaMensualidades.setCellWidget(index, 5, containerReport)

                index += 1

        except Exception as e:
            print("Error al cargar la tabla de mensualidades (Mensualidades):", e)