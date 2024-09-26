import sys
from PyQT6 import QtWidgets


class Eventos(): new*
    def mensajeSalir(self=None): new*
        mbox=QTabWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        mbox.setWindowTitle('Salir')
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes|QtWidgets.QMessageBox.StandardButton.No)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('No')

        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            mbox.hide()