from calendar import Calendar

import alquileres
import conexionserver
import informes
import mensualidades
import vendedores
import ventas
from venPrincipal import *
from venAux import *

import var
import clientes
import facturas
import conexion
import eventos
import styles
import sys
import propiedades

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main,self).__init__()
        var.ui=Ui_venPrincipal()
        var.ui.setupUi(self)
        var.uiCalendar = Calendar()
        var.dlgabrir = FileDialogAbrir()
        var.dlggestion = dlgGestionprop()
        var.dlgabout = dlgAbout()
        conexion.Conexion.db_conexion(self)
        var.dlgbuscarprop = dlgBuscarProp(conexion.Conexion.cargaBuscarProp(self))
        #conexionserver.ConexionServer.crear_conexion(self)
        var.historico = 1
        var.paginacli = 1
        var.paginaprop = 1
        var.paginavend = 1
        var.long= 10
        var.clientesxpagina= 15
        var.propiedadesxpagina = 12
        var.vendpxpagina = 10
        eventos.Eventos.cargarProv(self)
        clientes.Clientes.cargaTablaClientes(self)
        self.setStyleSheet(styles.load_stylesheet())


        '''
        Eventos de Tablas
        '''
        clientes.Clientes.cargaTablaClientes(self)
        propiedades.Propiedades.cargaTablaPropiedades(self)
        eventos.Eventos.resizeTablaClientes(self)
        eventos.Eventos.resizeTablaPropiedades(self)
        eventos.Eventos.resizeTablaFacturas(self)
        eventos.Eventos.resizeTablaVentas(self)
        eventos.Eventos.resizeTablaAlquileres(self)
        eventos.Eventos.resizeTablaMensualidades(self)
        var.ui.tablaClientes.clicked.connect(clientes.Clientes.cargaOneCliente)
        var.ui.tablaPropiedades.clicked.connect(propiedades.Propiedades.cargaOnePropiedad)
        var.ui.tablaFacturas.clicked.connect(facturas.Facturas.cargarOneFactura)
        var.ui.tablaVentas.clicked.connect(ventas.Ventas.cargarOneVenta)
        var.ui.tablaContrato.clicked.connect(alquileres.Alquileres.cargarOneAlquiler)

        vendedores.Vendedores.cargaTablaVendedores(self)
        eventos.Eventos.resizeTablaVendedores(self)
        var.ui.tablaVendedores.clicked.connect(vendedores.Vendedores.cargaOneVendedor)

        facturas.Facturas.mostrarTablaFactura(self)
        alquileres.Alquileres.cargarTablaAlquileres(self)


        '''
        zona de eventos del menubar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionCrear_Backup.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(eventos.Eventos.restauraraBackup)
        var.ui.actionTipo_Propiedades.triggered.connect(eventos.Eventos.abrirTipoprop)
        var.ui.actionListado_Clientes.triggered.connect(informes.Informes.reportClientes)
        var.ui.actionListado_Propiedades.triggered.connect(eventos.Eventos.abrirBuscarProp)
        var.ui.actionListado_Ventas.triggered.connect(informes.Informes.reportVentas)

        '''
        eventos de botones
        '''

        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifCliente)
        var.ui.btnDelecli.clicked.connect(clientes.Clientes.bajaCliente)
        var.ui.btnAltacli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0))
        var.ui.btnBajacli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(1))
        var.ui.btnPubliprop.clicked.connect(lambda: eventos.Eventos.abrirCalendar(2))
        var.ui.btnBajaprop.clicked.connect(lambda: eventos.Eventos.abrirCalendar(3))
        var.ui.btnAltavend.clicked.connect(lambda: eventos.Eventos.abrirCalendar(4))
        var.ui.btnfechafac.clicked.connect(lambda: eventos.Eventos.abrirCalendar(5))
        var.ui.btnAltacontrato.clicked.connect(lambda: eventos.Eventos.abrirCalendar(6))
        var.ui.btnIniciomens.clicked.connect(lambda: eventos.Eventos.abrirCalendar(7))
        var.ui.btnFinmens.clicked.connect(lambda: eventos.Eventos.abrirCalendar(8))
        var.ui.btnGrabarprop.clicked.connect(propiedades.Propiedades.altaPropiedad)
        var.ui.btnModificarprop.clicked.connect(propiedades.Propiedades.modifPropiedad)
        var.ui.btnDeleteprop.clicked.connect(propiedades.Propiedades.bajaPropiedades)
        var.ui.btnBuscar.clicked.connect(propiedades.Propiedades.filtrarProp)
        var.ui.btnBuscarCli_2.clicked.connect(clientes.Clientes.filtrarCliente)
        var.ui.btnAnteriorCli.clicked.connect(clientes.Clientes.prevCli)
        var.ui.btnSiguienteCli.clicked.connect(clientes.Clientes.nextCli)
        var.ui.btnAnteriorProp.clicked.connect(propiedades.Propiedades.prevProp)
        var.ui.btnSiguienteProp.clicked.connect(propiedades.Propiedades.nextProp)

        #Botones ventas

        var.ui.btnGrabarVend.clicked.connect(vendedores.Vendedores.altaVendedor)
        var.ui.btnModificarVend.clicked.connect(vendedores.Vendedores.modifVendedor)
        var.ui.btnDeleteVend.clicked.connect(vendedores.Vendedores.bajaVendedor)

        # Botones ventas

        var.ui.btnGrabarFactura.clicked.connect(facturas.Facturas.altaFactura)
        var.ui.btnlimpiarfac.clicked.connect(eventos.Eventos.limpiarPanFacturas)

        # Botones ventas

        var.ui.btnGrabarVenta.clicked.connect(ventas.Ventas.altaVenta)

        # Botones ventas

        var.ui.btnGrabarContrato.clicked.connect(alquileres.Alquileres.altaAlquiler)







        '''
        eventos de cajas de texto
        '''
        var.ui.txtDnicli.editingFinished.connect(lambda: clientes.Clientes.checkDNI(var.ui.txtDnicli.text()))
        var.ui.txtEmailcli.editingFinished.connect(lambda: clientes.Clientes.checkEmail(var.ui.txtEmailcli.text()))
        var.ui.txtMovilcli.editingFinished.connect(lambda : clientes.Clientes.checkMovil(var.ui.txtMovilcli.text()))
        var.ui.txtDniVend.editingFinished.connect(lambda: vendedores.Vendedores.checkDNI(var.ui.txtDniVend.text()))
        var.ui.txtEmailVend.editingFinished.connect(lambda: vendedores.Vendedores.checkEmail(var.ui.txtEmailVend.text()))
        var.ui.txtMovilVend.editingFinished.connect(lambda: vendedores.Vendedores.checkMovil(var.ui.txtMovilVend.text()))
        var.ui.txtMovilprop.editingFinished.connect(lambda: propiedades.Propiedades.checkMovil(var.ui.txtMovilprop.text()))
        var.ui.txtPrecioventaprop.textChanged.connect(propiedades.Propiedades.checkVenta)
        var.ui.txtPrecioalquilerprop.textChanged.connect(propiedades.Propiedades.checkAlquiler)

        '''
        eventos de comobox
        '''
        eventos.Eventos.cargarProv(self)
        eventos.Eventos.cargaMunicli(self)
        eventos.Eventos.cargarProvprop(self)
        eventos.Eventos.cargaMuniprop(self)
        eventos.Eventos.cargarProviVend(self)
        var.ui.cmbProvicli.currentIndexChanged.connect(eventos.Eventos.cargaMunicli)
        var.ui.cmbProviprop.currentIndexChanged.connect(eventos.Eventos.cargaMuniprop)
        eventos.Eventos.cargarTipoprop(self)

        '''
        Eventos ToolBar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionBorrar.triggered.connect(eventos.Eventos.limpiarPanel)
        var.ui.actionBuscar.triggered.connect(propiedades.Propiedades.filtrarProp)
        var.ui.actionGestion.triggered.connect(eventos.Eventos.abrirTipoprop)
        var.ui.actionExportar_Propiedades_CSV.triggered.connect(eventos.Eventos.exportCSVprop)
        var.ui.actionExportar_Propiedades_Json.triggered.connect(eventos.Eventos.exportJSONprop)
        var.ui.action_Acercade.triggered.connect(eventos.Eventos.abrirAbout)



        '''
        Eventos Checkbox
        '''
        var.ui.chkHistoriacli.stateChanged.connect(clientes.Clientes.historicoCli)
        var.ui.chkHosticoprop.stateChanged.connect(propiedades.Propiedades.historicoProp)
        var.ui.chkVentaprop.setEnabled(False)
        var.ui.chkAlquilerprop.setEnabled(False)

        var.ui.chkHistoriaVend.stateChanged.connect(vendedores.Vendedores.historicoVend)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window=Main()
    window.showMaximized()
    sys.exit(app.exec())