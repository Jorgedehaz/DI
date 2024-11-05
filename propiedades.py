from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QIcon
import clientes
import conexion
import eventos
import propiedades
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
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                mbox.setText("Propiedad Dada de Alta")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()

            print(propiedad)
        except Exception as e:
            print("error alta propiedad" + str(e))

    def cargaTablaPropiedades(self):
        try:
            listado = conexion.Conexion.listadoPropiedades(self)
            index=0
            for registro in listado:
                var.ui.tablaPropiedades.setRowCount(index+1)
                var.ui.tablaPropiedades.setItem(index,0, QtWidgets.QTableWidgetItem("  " + str(registro[0]) + "  "))
                var.ui.tablaPropiedades.setItem(index,1, QtWidgets.QTableWidgetItem("  " + registro[5] + "  "))
                var.ui.tablaPropiedades.setItem(index,2, QtWidgets.QTableWidgetItem("  " + registro[6] + "  "))
                var.ui.tablaPropiedades.setItem(index,3, QtWidgets.QTableWidgetItem("  " + str(registro[7]) + "  "))
                var.ui.tablaPropiedades.setItem(index,4, QtWidgets.QTableWidgetItem("  " + str(registro[8]) + "  "))
                var.ui.tablaPropiedades.setItem(index,5, QtWidgets.QTableWidgetItem("  " + str(registro[10]) + " € "))
                var.ui.tablaPropiedades.setItem(index, 6, QtWidgets.QTableWidgetItem("  " + str(registro[11]) + " € "))
                var.ui.tablaPropiedades.setItem(index, 7, QtWidgets.QTableWidgetItem("  " + registro[14] + "  "))

                index+=1

        except Exception as e:
            print("error cargaTablaPropiedades", e)

    def modifPropiedad(self):
        try:
            modifProp = [var.ui.txtAltaprop.text(),var.ui.txtDirprop.text(),
                       var.ui.cmbProviprop.currentText(),var.ui.cmbMuniprop.currentText(),var.ui.cmbTipoprop.currentText(),
                       var.ui.spinHabitaprop.value(),var.ui.spinBanosprop.value(), var.ui.txtSuperprop.text(),
                       var.ui.txtPrecioalquilerprop.text(),var.ui.txtPrecioventaprop.text(),
                       var.ui.txtCodigopostalprop.text(),var.ui.txtObservaprop.toPlainText()]

            if conexion.Conexion.modifPropiedad(modifProp):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/iconoInmo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Datos de propiedad modificados')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

                propiedades.Propiedades.cargaTablaPropiedades(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/iconoInmo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error al modificar datos de la propiedad')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

        except Exception as error:
            print("Error cargando la tabla de clientes", error)

    def bajaPropiedades(self):
        try:
            op = True
            datos = [var.ui.txtCodigoprop.text(), var.ui.txtBajaprop.text()]

            if conexion.Conexion.bajaPropiedad(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/house.svg'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad dada de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

                propiedades.Propiedades.cargaTablaPropiedades(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/house.svg'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error Baja Propiedad: propiedad no existe o ya ha sido dada de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

        except Exception as e:
            print("Error baja de clientes", e)