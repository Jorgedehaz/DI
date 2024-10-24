from datetime import datetime
from dlgCalendar import *
import var
import eventos
from dlgGestion import Ui_dlgTipoprop


class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.uicalendar = Ui_dlgCalendar()
        var.uicalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year

        var.uicalendar.Calendar.setSelectedDate((QtCore.QDate(ano,mes,dia)))
        var.uicalendar.Calendar.clicked.connect(eventos.Eventos.cargaFecha)

class dlgGestionprop(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_dlgTipoprop, self).__init__()
        var.dlggestion = Ui_dlgTipoprop()
        var.dlggestion.setupUi(self)


