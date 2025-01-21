from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTableWidgetItem, QWidget, QVBoxLayout, QPushButton

import var
import conexion

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

        except Exception as e:
            print("error alta factura", e)

    @staticmethod
    def mostrarTablaFactura(self):
        try:
            listado = conexion.Conexion.listadoFacturas(self)
            var.ui.tablaFacturas.setRowCount(len(listado))
            index = 0
            for registro in listado:
                container = QWidget()
                layout = QVBoxLayout()
                var.botondel = QPushButton()
                var.botondel.setFixedSize(30, 20)
                var.botondel.setIcon(QIcon("./img/borrar.ico"))
                var.botondel.setStyleSheet("background-color: #efefef;")
                var.botondel.clicked.connect(Facturas.deleteFactura)
                layout.addWidget(var.botondel)
                layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(0)
                container.setLayout(layout)
                var.ui.tablaFacturas.setItem(index, 0, QTableWidgetItem(str(registro[0])))
                var.ui.tablaFacturas.setItem(index, 1, QTableWidgetItem(registro[1]))
                var.ui.tablaFacturas.setItem(index, 2, QTableWidgetItem(registro[2]))
                var.ui.tablaFacturas.setCellWidget(index, 3, container)

                var.ui.tablaFacturas.item(index, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaFacturas.item(index, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaFacturas.item(index, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                index += 1
            #eventos.Eventos.resizeTablaFacturas()
        except Exception as e:
            print("Error al cargar la tabla de facturas", e)

    def deleteFactura(self):
        try:
            sender = var.ui.tablaFacturas.sender(self)
            row = sender.property("row")

            if conexion.Conexion.delFactura(row[0]):
                msgbox = QtWidgets.QMessageBox()
                msgbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msgbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                msgbox.setWindowTitle("Aviso")
                msgbox.setText("Factura eliminada")
                msgbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msgbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText("Aceptar")
                msgbox.exec()

        except Exception as error:
            print ("eliminar factura", error)