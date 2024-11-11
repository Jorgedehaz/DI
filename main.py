from calendar import Calendar

import conexionserver
from venPrincipal import *
from venAux import *

import var
import clientes
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
        var.dlggestion = dlgGestionprop()
        conexion.Conexion.db_conexion(self)
        var.historico = 1
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
        var.ui.tablaClientes.clicked.connect(clientes.Clientes.cargaOneCliente)
        var.ui.tablaPropiedades.clicked.connect(propiedades.Propiedades.cargaOnePropiedad)

        '''
        zona de eventos del menubar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionCrear_Backup.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(eventos.Eventos.restauraraBackup)
        var.ui.actionTipo_Propiedades.triggered.connect(eventos.Eventos.abrirTipoprop)

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
        var.ui.btnGrabarprop.clicked.connect(propiedades.Propiedades.altaPropiedad)
        var.ui.btnModificarprop.clicked.connect(propiedades.Propiedades.modifPropiedad)
        var.ui.btnDeleteprop.clicked.connect(propiedades.Propiedades.bajaPropiedades)
        var.ui.btnBuscar.clicked.connect(propiedades.Propiedades.filtrarProp)



        '''
        eventos de cajas de texto
        '''

        var.ui.txtDnicli.editingFinished.connect(lambda:clientes.Clientes.checkDNI(var.ui.txtDnicli.text()))
        var.ui.txtEmailcli.editingFinished.connect(lambda: clientes.Clientes.checkEmail(var.ui.txtEmailcli.text()))

        '''
        eventos de comobox
        '''
        eventos.Eventos.cargarProv(self)
        eventos.Eventos.cargaMunicli(self)
        eventos.Eventos.cargarProvprop(self)
        eventos.Eventos.cargaMuniprop(self)
        var.ui.cmbProvicli.currentIndexChanged.connect(eventos.Eventos.cargaMunicli)
        var.ui.cmbProviprop.currentIndexChanged.connect(eventos.Eventos.cargaMuniprop)
        eventos.Eventos.cargarTipoprop(self)

        '''
        Eventos ToolBar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionBorrar.triggered.connect(eventos.Eventos.limpiarPanel)

        '''
        Eventos Checkbox
        '''
        var.ui.chkHistoriacli.stateChanged.connect(clientes.Clientes.historicoCli)
        var.ui.chkHosticoprop.stateChanged.connect(propiedades.Propiedades.historicoProp)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window=Main()
    window.showMaximized()
    sys.exit(app.exec())