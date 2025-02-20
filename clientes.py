from operator import index

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QIcon
import clientes
import conexion
import conexionserver
import eventos
import var

class Clientes:
    def checkDNI(dni):
        try:
            dni=str(dni).upper()
            var.ui.txtDnicli.setText(str(dni))
            check=eventos.Eventos.validarDNI(dni)
            if check:
                var.ui.txtDnicli.setStyleSheet('background-color: green;')
            else:
                var.ui.txtDnicli.setStyleSheet('background-color: red')
                var.ui.txtDnicli.setText(None)
                var.ui.txtDnicli.setPlaceholderText("dni no válido")
                var.ui.txtDnicli.setFocus()
        except Exception as e:
            print("error check cliente", e)

    def checkMovil(movil):
        try:
            movil=str(movil).upper()
            var.ui.txtMovilcli.setText(str(movil))
            check=eventos.Eventos.validarMovil(movil)
            if check:
                var.ui.txtMovilcli.setStyleSheet('background-color: green;')
            else:
                var.ui.txtMovilcli.setStyleSheet('background-color: red')
                var.ui.txtMovilcli.setText(None)
                var.ui.txtMovilcli.setPlaceholderText("movil no válido")
                var.ui.txtMovilcli.setFocus()
        except Exception as e:
            print("error check movil cliente", e)

    def checkEmail(mail):
        try:
            mail = str(var.ui.txtEmailcli.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailcli.setStyleSheet('background-color: green;')
                var.ui.txtEmailcli.setText(mail.lower())

            else:
                var.ui.txtEmailcli.setStyleSheet('background-color:red; font-style: italic;')
                var.ui.txtEmailcli.setText(None)
                var.ui.txtEmailcli.setPlaceholderText("correo no válido")
                var.ui.txtEmailcli.setFocus()

        except Exception as error:
            print("error check cliente", error)

    def altaCliente(self):
        try:
            nuevocli= [var.ui.txtDnicli.text(), var.ui.txtAltacli.text(), var.ui.txtApelcli.text().title(), var.ui.txtNomcli.text().title(),
                    var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text().title(), var.ui.cmbProvicli.currentText(),
                    var.ui.cmbMunicli.currentText()]
            if (var.ui.txtDnicli.text()!=""):
                if conexion.Conexion.altaCliente(nuevocli):
                #if conexionserver.ConexionServer.altaCliente(nuevocli):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText("Cliente dado de alta en la BBDD")
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()
                    Clientes.cargaTablaClientes(self)
            else:
                mbox= QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/iconoInmo.ico'))
                mbox.setText("Error faltan datos o cliente existe")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()

        except Exception as e:
            print("error alta cliente", e)

    def modifCliente(self):
        try:
            modifCli = [var.ui.txtDnicli.text(), var.ui.txtAltacli.text(), var.ui.txtApelcli.text(),
                        var.ui.txtNomcli.text(), var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(),
                        var.ui.txtDircli.text(),
                        var.ui.cmbProvicli.currentText(), var.ui.cmbMunicli.currentText(),var.ui.txtBajacli.text()]

            if conexion.Conexion.modifCliente(modifCli):
            #if conexionserver.ConexionServer.modifCliente(modifCli):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/iconoInmo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Datos de cliente modificados')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

                clientes.Clientes.cargaTablaClientes(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/iconoInmo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error al modificar datos de cliente')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

        except Exception as error:
            print("Error cargando la tabla de clientes", error)

    def bajaCliente(self):
        try:
            op = True
            datos = [var.ui.txtDnicli.text(), var.ui.txtBajacli.text()]

            if conexion.Conexion.bajaCliente(datos):
            #if conexionserver.ConexionServer.bajaCliente(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/house.svg'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Cliente dado de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

                clientes.Clientes.cargaTablaClientes(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowIcon(QIcon('./img/house.svg'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error Baja Cliente: cliente no existe o ya ha sido dado de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')

                mbox.exec()

        except Exception as e:
            print("Error baja de clientes", e)


    '''
    def cargaTablaClientes(self):
        try:
            listado = conexion.Conexion.listadoClientes(self)
            #listado = conexionserver.ConexionServer.listadoClientes(self)
            index=0
            for registro in listado:
                var.ui.tablaClientes.setRowCount(index+1)
                var.ui.tablaClientes.setItem(index,0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaClientes.setItem(index,1, QtWidgets.QTableWidgetItem(str("  " + registro[2] + "  ")))
                var.ui.tablaClientes.setItem(index,2, QtWidgets.QTableWidgetItem(str("  " + registro[3] + "  ")))
                var.ui.tablaClientes.setItem(index,3, QtWidgets.QTableWidgetItem(str("   " + registro[5] + "   ")))
                var.ui.tablaClientes.setItem(index,4, QtWidgets.QTableWidgetItem(str("  " + registro[7] + "  ")))
                var.ui.tablaClientes.setItem(index,5, QtWidgets.QTableWidgetItem(str("  " + registro[8] + "  ")))
                var.ui.tablaClientes.setItem(index,6, QtWidgets.QTableWidgetItem(registro[9]))

                index+=1

        except Exception as e:
            print("error cargaTablaClientes", e)
    '''

    def cargaTablaClientes(self):
        try:
            listado = conexion.Conexion.listadoClientes(self)  # Obtén el listado completo
            inicio = (var.paginacli - 1) * var.clientesxpagina
            fin = inicio + var.clientesxpagina
            clientes_pagina = listado[inicio:fin]  # Filtra los clientes según la página actual

            var.ui.tablaClientes.setRowCount(0)  # Limpia la tabla antes de cargar nuevos datos
            for index, registro in enumerate(clientes_pagina):
                var.ui.tablaClientes.setRowCount(index + 1)
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str("  " + registro[2] + "  ")))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str("  " + registro[3] + "  ")))
                var.ui.tablaClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str("   " + registro[5] + "   ")))
                var.ui.tablaClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str("  " + registro[7] + "  ")))
                var.ui.tablaClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(str("  " + registro[8] + "  ")))
                var.ui.tablaClientes.setItem(index, 6, QtWidgets.QTableWidgetItem(registro[9]))

            Clientes.actualizarBotonesPaginacion(self)

        except Exception as e:
            print("Error en cargaTablaClientes:", e)

    def cargaOneCliente(self):
        try:
            fila = var.ui.tablaClientes.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneCliente(str(datos[0]))
            #registro = conexionserver.ConexionServer.datosOneCliente(str(datos[0]))
            registro = [x if x != 'None' else '' for x in registro]
            listado = [var.ui.txtDnicli, var.ui.txtAltacli, var.ui.txtApelcli,
                       var.ui.txtNomcli, var.ui.txtEmailcli, var.ui.txtMovilcli,
                       var.ui.txtDircli,
                       var.ui.cmbProvicli, var.ui.cmbMunicli,var.ui.txtBajacli]

            #Carga de datos en la pag Ventas
            var.ui.txtdnifac.setText(str(datos[0]))
            var.ui.txtApellidoFac.setText(str(datos[1]))
            var.ui.txtNombreFac.setText(str(datos[2]))

            for i in range(len(listado)):
                if i == 7 or i == 8:
                    listado[i].setCurrentText(registro[i])
                else:
                    listado[i].setText(registro[i])


            #Cargar datos en pag Alquileres
            var.ui.txtdniclialqui.setText(str(datos[0]))

        except Exception as error:
            print("Error cargando datos del cliente", error)



    def historicoCli(self):
        try:
            if var.ui.chkHistoriacli.isChecked():
                var.historico = 0
            else:
                var.historico = 1
            Clientes.cargaTablaClientes(self)
        except Exception as e:
            print("checkbox historico", e)

    def nextCli(self):
        try:
            listado = conexion.Conexion.listadoClientes(self)  # Obtén el listado completo
            total_paginas = (len(listado) + var.clientesxpagina - 1) // var.clientesxpagina
            if var.paginacli < total_paginas:
                var.paginacli += 1
                Clientes.cargaTablaClientes(self)  # Llama al método de la instancia actual
        except Exception as e:
            print("Error en nextCli:", e)

    def prevCli(self):
        try:
            if var.paginacli > 1:  # Verifica si puedes retroceder
                var.paginacli -= 1  # Decrementa la página actual
                Clientes.cargaTablaClientes(self)  # Recarga la tabla con la nueva página
        except Exception as e:
            print("Error en prevCli:", e)

    def actualizarBotonesPaginacion(self):
        try:
            listado = conexion.Conexion.listadoClientes(self)
            total_paginas = (len(listado) + var.clientesxpagina - 1) // var.clientesxpagina

            # Deshabilita el botón "Anterior" si estás en la primera página
            var.ui.btnAnteriorCli.setEnabled(var.paginacli > 1)

            # Deshabilita el botón "Siguiente" si estás en la última página
            var.ui.btnSiguienteCli.setEnabled(var.paginacli < total_paginas)
        except Exception as e:
            print("Error en actualizarBotonesPaginacion:", e)


    def filtrarCliente(self):
        try:
            dni = var.ui.txtDnicli.text()

            datos = [dni]
            listado_filtrado = conexion.Conexion.buscarCliente(datos)

            var.ui.tablaClientes.setRowCount(0)
            index = 0

            if len(listado_filtrado) == 0:
                var.ui.tablaClientes.setRowCount(index + 1)
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem("  No hay resultados  "))

            for registro in listado_filtrado:
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str("  " + registro[2] + "  ")))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str("  " + registro[3] + "  ")))
                var.ui.tablaClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str("   " + registro[5] + "   ")))
                var.ui.tablaClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str("  " + registro[7] + "  ")))
                var.ui.tablaClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(str("  " + registro[8] + "  ")))
                var.ui.tablaClientes.setItem(index, 6, QtWidgets.QTableWidgetItem(registro[9]))
                index += 1

        except Exception as e:
            print("Error al filtrar clientes:", e)

