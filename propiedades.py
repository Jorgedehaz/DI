from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QIcon
import clientes
import conexion
import conexionserver
import eventos
import propiedades
import var
from conexion import Conexion


class Propiedades():

    def altaTipopropiedad(self):
        try:
            tipo = var.dlggestion.ui.txtGestipoprop.text().title()
            registro = conexion.Conexion.altaTipoprop(tipo)
            #registro = conexionserver.ConexionServer.altaTipoProp(tipo)
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
            #if conexionserver.ConexionServer.bajaTipoProp():
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
            #registro = conexionserver.ConexionServer.cargarTipoProp(self)
            registro= conexion.Conexion.cargarTipoprop(self)
            var.ui.cmbTipoprop.clear()
            var.ui.cmbTipoprop.addItems(registro)
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
            #if conexionserver.ConexionServer.altaPropiedad(propiedad):
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

            #listado = conexionserver.ConexionServer.listadoPropiedades(self)
            listado = conexion.Conexion.listadoPropiedades(self)  # Obtén el listado completo
            inicio = (var.paginaprop - 1) * var.propiedadesxpagina
            fin = inicio + var.propiedadesxpagina
            propiedades_pagina = listado[inicio:fin]  # Filtra los clientes según la página actual
            var.ui.tablaPropiedades.setRowCount(0)

            for index, registro in enumerate(propiedades_pagina):
                var.ui.tablaPropiedades.setRowCount(index+1)
                var.ui.tablaPropiedades.setItem(index,0, QtWidgets.QTableWidgetItem("  " + str(registro[0]) + "  "))
                var.ui.tablaPropiedades.setItem(index,1, QtWidgets.QTableWidgetItem("  " + registro[5] + "  "))
                var.ui.tablaPropiedades.setItem(index,2, QtWidgets.QTableWidgetItem("  " + registro[6] + "  "))
                var.ui.tablaPropiedades.setItem(index,3, QtWidgets.QTableWidgetItem("  " + str(registro[7]) + "  "))
                var.ui.tablaPropiedades.setItem(index,4, QtWidgets.QTableWidgetItem("  " + str(registro[8]) + "  "))
                var.ui.tablaPropiedades.setItem(index,5, QtWidgets.QTableWidgetItem("  " + str(registro[10]) + " € "))
                var.ui.tablaPropiedades.setItem(index, 6, QtWidgets.QTableWidgetItem("  " + str(registro[11]) + " € "))
                var.ui.tablaPropiedades.setItem(index, 7, QtWidgets.QTableWidgetItem("  " + registro[14] + "  "))
                var.ui.tablaPropiedades.setItem(index, 8, QtWidgets.QTableWidgetItem("  " + str(registro[2]) + "  "))

            Propiedades.actualizarBotonesPaginacionProp(self)

        except Exception as e:
            print("error cargaTablaPropiedades", e)

    def modifPropiedad(self):
        try:
            modifProp = [var.ui.txtCodigoprop.text(),var.ui.txtAltaprop.text(),var.ui.txtBajaprop.text(),var.ui.txtDirprop.text().title(),
                       var.ui.cmbProviprop.currentText(),var.ui.cmbMuniprop.currentText(),var.ui.cmbTipoprop.currentText(),
                       var.ui.spinHabitaprop.value(),var.ui.spinBanosprop.value(), var.ui.txtSuperprop.text(),
                       var.ui.txtPrecioalquilerprop.text(),var.ui.txtPrecioventaprop.text(),
                       var.ui.txtCodigopostalprop.text(),var.ui.txtObservaprop.toPlainText()]

            tipooper = []
            if var.ui.chkVentaprop.isChecked():
                tipooper.append(var.ui.chkVentaprop.text())
            if var.ui.chkAlquilerprop.isChecked():
                tipooper.append(var.ui.chkAlquilerprop.text())
            if var.ui.chkIntercambioprop.isChecked():
                tipooper.append(var.ui.chkIntercambioprop.text())
            tipooper = "-".join(tipooper)
            modifProp.append(tipooper)

            if var.ui.radioDispoprop.isChecked():
                modifProp.append(var.ui.radioDispoprop.text())
            elif var.ui.radioAlquiladoprop.isChecked():
                modifProp.append(var.ui.radioAlquiladoprop.text())
            elif var.ui.radioVendidoprop.isChecked():
                modifProp.append(var.ui.radioVendidoprop.text())
            else:
                modifProp.append(None)

            modifProp.append(var.ui.txtPropietarioprop.text().title())
            modifProp.append(var.ui.txtMovilprop.text())

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
            print("Error modifPropiedad", error)

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
            print("Error baja de propiedad", e)


    def cargaOnePropiedad(self):
        try:
            var.ui.chkIntercambioprop.setChecked(False)
            var.ui.chkVentaprop.setChecked(False)
            var.ui.chkAlquilerprop.setChecked(False)

            fila = var.ui.tablaPropiedades.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOnePropiedad(str(datos[0]))
            #registro = conexionserver.ConexionServer.datosOnePropiedad(str(datos[0]))
            listado = [var.ui.txtCodigoprop,var.ui.txtAltaprop,var.ui.txtBajaprop,var.ui.txtDirprop,
                       var.ui.cmbProviprop,var.ui.cmbMuniprop,var.ui.cmbTipoprop,
                       var.ui.spinHabitaprop,var.ui.spinBanosprop, var.ui.txtSuperprop,
                       var.ui.txtPrecioalquilerprop,var.ui.txtPrecioventaprop,
                       var.ui.txtCodigopostalprop,var.ui.txtObservaprop]


            for i in range(len(listado)):
                if i == 4 or i == 5 or i==6:
                    listado[i].setCurrentText(str(registro[i]))
                elif i==7 or i==8:
                        listado[i].setValue(int(registro[i]))
                else:
                    listado[i].setText(str(registro[i]))
            if "Alquiler" in registro[14]:
                var.ui.chkAlquilerprop.setChecked(True)
            if "Venta" in registro[14]:
                var.ui.chkVentaprop.setChecked(True)
            if "Intercambio" in registro[14]:
                var.ui.chkIntercambioprop.setChecked(True)
            if registro [15] == "Disponible":
                var.ui.radioDispoprop.setChecked(True)
            elif registro [15] == "Alquilado":
                var.ui.radioAlquilerprop.setChecked(True)
            elif registro [15] == "Vendido":
                var.ui.radioVentaprop.setChecked(True)

            var.ui.txtPropietarioprop.setText(str(registro[16]))
            var.ui.txtMovilprop.setText(str(registro[17]))


            #Volcar datos propiedad a pag Ventas
            var.ui.txtDirFac.setText(str(registro[3]))
            var.ui.txtCodigoFac.setText(str(registro[0]))
            var.ui.txtTipoFac.setText(str(registro[6]))
            var.ui.txtLocalidadFac.setText(str(registro[5]))
            var.ui.txtPrecioFac.setText(str(registro[11]))

        except Exception as error:
            print("Error cargando datos de la Propiedad", error)

    def historicoProp(self):
        try:
            if var.ui.chkHosticoprop.isChecked():
                var.historico = 0
            else:
                var.historico = 1
            Propiedades.cargaTablaPropiedades(self)
        except Exception as e:
            print("checkbox historico", e)

    def filtrarProp(self):
        try:
            municipio = var.ui.cmbMuniprop.currentText()
            tipoprop = var.ui.cmbTipoprop.currentText()

            datos = [municipio,tipoprop]
            listado_filtrado = conexion.Conexion.buscarProp(datos)

            var.ui.tablaPropiedades.setRowCount(0)
            index = 0

            if len(listado_filtrado) == 0:
                var.ui.tablaPropiedades.setRowCount(index + 1)
                var.ui.tablaPropiedades.setItem(index, 2, QtWidgets.QTableWidgetItem("  No hay resultados  "))

            for registro in listado_filtrado:
                var.ui.tablaPropiedades.setRowCount(index + 1)
                var.ui.tablaPropiedades.setItem(index, 0, QtWidgets.QTableWidgetItem("  " + str(registro[0]) + "  "))
                var.ui.tablaPropiedades.setItem(index, 1, QtWidgets.QTableWidgetItem("  " + registro[5] + "  "))
                var.ui.tablaPropiedades.setItem(index, 2, QtWidgets.QTableWidgetItem("  " + registro[6] + "  "))
                var.ui.tablaPropiedades.setItem(index, 3, QtWidgets.QTableWidgetItem("  " + str(registro[7]) + "  "))
                var.ui.tablaPropiedades.setItem(index, 4, QtWidgets.QTableWidgetItem("  " + str(registro[8]) + "  "))
                var.ui.tablaPropiedades.setItem(index, 5, QtWidgets.QTableWidgetItem("  " + str(registro[10]) + " € "))
                var.ui.tablaPropiedades.setItem(index, 6, QtWidgets.QTableWidgetItem("  " + str(registro[11]) + " € "))
                var.ui.tablaPropiedades.setItem(index, 7, QtWidgets.QTableWidgetItem("  " + registro[14] + "  "))
                var.ui.tablaPropiedades.setItem(index, 8, QtWidgets.QTableWidgetItem("  " + str(registro[2]) + "  "))
                index += 1

        except Exception as e:
            print("Error al filtrar propiedades:", e)

    def checkVenta(self):
        try:
            var.ui.chkVentaprop.setChecked(True)
            if var.ui.txtPrecioventaprop.text() == "":
                var.ui.chkVentaprop.setChecked(False)
        except Exception as e:
            print(e)

    def checkAlquiler(self):
        try:
            var.ui.chkAlquilerprop.setChecked(True)
            if var.ui.txtPrecioalquilerprop.text() == "":
                var.ui.chkAlquilerprop.setChecked(False)
        except Exception as e:
            print(e)

    def checkMovil(movil):
        try:
            movil=str(movil).upper()
            var.ui.txtMovilprop.setText(str(movil))
            check=eventos.Eventos.validarMovil(movil)
            if check:
                var.ui.txtMovilprop.setStyleSheet('background-color: green;')
            else:
                var.ui.txtMovilprop.setStyleSheet('background-color: red')
                var.ui.txtMovilprop.setText(None)
                var.ui.txtMovilprop.setPlaceholderText("movil no válido")
                var.ui.txtMovilprop.setFocus()
        except Exception as e:
            print("error check movil propietario", e)

    def nextProp(self):
        try:
            listado = conexion.Conexion.listadoPropiedades(self)  # Obtén el listado completo
            total_paginas = (len(listado) + var.propiedadesxpagina - 1) // var.propiedadesxpagina
            if var.paginaprop < total_paginas:
                var.paginaprop += 1
                Propiedades.cargaTablaPropiedades(self)  # Llama al método de la instancia actual
        except Exception as e:
            print("Error en nextCli:", e)

    def prevProp(self):
        try:
            if var.paginaprop > 1:  # Verifica si puedes retroceder
                var.paginaprop -= 1  # Decrementa la página actual
                Propiedades.cargaTablaPropiedades(self)  # Recarga la tabla con la nueva página
        except Exception as e:
            print("Error en prevCli:", e)

    def actualizarBotonesPaginacionProp(self):
        try:
            listado = conexion.Conexion.listadoPropiedades(self)
            total_paginas = (len(listado) + var.propiedadesxpagina - 1) // var.propiedadesxpagina

            # Deshabilita el botón "Anterior" si estás en la primera página
            var.ui.btnAnteriorProp.setEnabled(var.paginaprop > 1)

            # Deshabilita el botón "Siguiente" si estás en la última página
            var.ui.btnSiguienteProp.setEnabled(var.paginaprop < total_paginas)
        except Exception as e:
            print("Error en actualizarBotonesPaginacion:", e)