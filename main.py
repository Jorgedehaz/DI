import clientes
from venPrincipal import*
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

        '''
        zona de eventos del menubar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)

        '''
        eventos de botones
        '''

        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaCliente)

        '''
        eventos de cajas de texto
        '''

        var.ui.txtDnicli.editingFinished.connect(lambda:clientes.Clientes.checkDNI(var.ui.txtDnicli.text()))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window=Main()
    window.showMaximized()
    sys.exit(app.exec())
