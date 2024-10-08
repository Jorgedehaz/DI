import clientes
from venPrincipal import*
from venAux import *
import sys
import var
import eventos
import conexion
import styles



class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main,self).__init__()
        var.ui=Ui_venPrincipal()
        var.ui.setupUi(self)
        var.uicalendar = Calendar()
        conexion.Conexion.db_conexion(self)
        eventos.Eventos.cargarProv(self)




        '''
        zona de eventos del menubar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)


        '''
        eventos de botones
        '''

        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.btnAltacli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0))

        '''
        eventos de cajas de texto
        '''

        var.ui.txtDnicli.editingFinished.connect(lambda:clientes.Clientes.checkDNI(var.ui.txtDnicli.text()))
        var.ui.txtEmailcli.editingFinished.connect(lambda: clientes.Clientes.checkEmail(var.ui.txtEmailcli.text()))

        '''
        eventos de comobox
        '''

        var.ui.cmbProvcli.currentIndexChanged.connect(eventos.Eventos.cargaMunicli)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window=Main()
    window.showMaximized()
    sys.exit(app.exec())
