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




class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main,self).__init__()
        var.ui=Ui_venPrincipal()
        var.ui.setupUi(self)
        var.uiCalendar = Calendar()
        conexion.Conexion.db_conexion(self)
        var.historico = 1
        eventos.Eventos.cargarProv(self)
        clientes.Clientes.cargaTablaClientes(self)
        self.setStyleSheet(styles.load_stylesheet())

        '''
        Eventos de Tablas
        '''
        clientes.Clientes.cargaTablaClientes(self)
        eventos.Eventos.resizeTablaClientes(self)
        var.ui.tablaClientes.clicked.connect(clientes.Clientes.cargaOneCliente)

        '''
        zona de eventos del menubar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionCrear_Backup.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(eventos.Eventos.restauraraBackup)

        '''
        eventos de botones
        '''

        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.btnAltacli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0,0))
        var.ui.btnBajacli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0,1))
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifCliente)
        var.ui.btnDelecli.clicked.connect(clientes.Clientes.bajaCliente)


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
        var.ui.cmbProvicli.currentIndexChanged.connect(eventos.Eventos.cargaMunicli)

        '''
        Eventos ToolBar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionBorrar.triggered.connect(eventos.Eventos.limpiarPanel)

        '''
        Eventos Checkbox
        '''
        var.ui.chkHistoriacli.stateChanged.connect(clientes.Clientes.historicoCli)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window=Main()
    window.showMaximized()
    sys.exit(app.exec())