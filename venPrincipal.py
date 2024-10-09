# Form implementation generated from reading ui file '.\\templates\\venPrincipal.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(1177, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(venPrincipal.sizePolicy().hasHeightForWidth())
        venPrincipal.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\\\templates\\../img/iconoInmo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        venPrincipal.setWindowIcon(icon)
        venPrincipal.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(parent=venPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 6, 1, 1)
        self.panPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panPrincipal.sizePolicy().hasHeightForWidth())
        self.panPrincipal.setSizePolicy(sizePolicy)
        self.panPrincipal.setMinimumSize(QtCore.QSize(900, 700))
        self.panPrincipal.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.panPrincipal.setObjectName("panPrincipal")
        self.pesClientes = QtWidgets.QWidget()
        self.pesClientes.setObjectName("pesClientes")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pesClientes)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line = QtWidgets.QFrame(parent=self.pesClientes)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txtDnicli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDnicli.setMinimumSize(QtCore.QSize(150, 0))
        self.txtDnicli.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txtDnicli.setStyleSheet("background-color:rgb(246, 255, 187);")
        self.txtDnicli.setText("")
        self.txtDnicli.setObjectName("txtDnicli")
        self.gridLayout_2.addWidget(self.txtDnicli, 0, 2, 1, 1)
        self.txtDircli = QtWidgets.QLineEdit(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDircli.sizePolicy().hasHeightForWidth())
        self.txtDircli.setSizePolicy(sizePolicy)
        self.txtDircli.setMinimumSize(QtCore.QSize(300, 0))
        self.txtDircli.setMaximumSize(QtCore.QSize(300, 16777215))
        self.txtDircli.setObjectName("txtDircli")
        self.gridLayout_2.addWidget(self.txtDircli, 3, 2, 1, 3)
        self.lblMovilcli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblMovilcli.setObjectName("lblMovilcli")
        self.gridLayout_2.addWidget(self.lblMovilcli, 2, 5, 1, 1)
        self.lblNomcli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblNomcli.setObjectName("lblNomcli")
        self.gridLayout_2.addWidget(self.lblNomcli, 1, 5, 1, 1)
        self.lblDircli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblDircli.setObjectName("lblDircli")
        self.gridLayout_2.addWidget(self.lblDircli, 3, 1, 1, 1)
        self.txtMovilcli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtMovilcli.setMinimumSize(QtCore.QSize(150, 0))
        self.txtMovilcli.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txtMovilcli.setObjectName("txtMovilcli")
        self.gridLayout_2.addWidget(self.txtMovilcli, 2, 7, 1, 1)
        self.lblEmailcli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblEmailcli.setObjectName("lblEmailcli")
        self.gridLayout_2.addWidget(self.lblEmailcli, 2, 1, 1, 1)
        self.lblApelcli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblApelcli.setObjectName("lblApelcli")
        self.gridLayout_2.addWidget(self.lblApelcli, 1, 1, 1, 1)
        self.txtApelcli = QtWidgets.QLineEdit(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtApelcli.sizePolicy().hasHeightForWidth())
        self.txtApelcli.setSizePolicy(sizePolicy)
        self.txtApelcli.setMinimumSize(QtCore.QSize(300, 0))
        self.txtApelcli.setMaximumSize(QtCore.QSize(300, 16777215))
        self.txtApelcli.setObjectName("txtApelcli")
        self.gridLayout_2.addWidget(self.txtApelcli, 1, 2, 1, 1)
        self.cmbProvicli = QtWidgets.QComboBox(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProvicli.sizePolicy().hasHeightForWidth())
        self.cmbProvicli.setSizePolicy(sizePolicy)
        self.cmbProvicli.setMinimumSize(QtCore.QSize(150, 0))
        self.cmbProvicli.setObjectName("cmbProvicli")
        self.gridLayout_2.addWidget(self.cmbProvicli, 3, 7, 1, 1)
        self.txtAltacli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtAltacli.setMinimumSize(QtCore.QSize(120, 0))
        self.txtAltacli.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txtAltacli.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtAltacli.setObjectName("txtAltacli")
        self.gridLayout_2.addWidget(self.txtAltacli, 0, 7, 1, 1)
        self.lblProvcli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblProvcli.setMinimumSize(QtCore.QSize(0, 0))
        self.lblProvcli.setObjectName("lblProvcli")
        self.gridLayout_2.addWidget(self.lblProvcli, 3, 5, 1, 1)
        self.txtNomcli = QtWidgets.QLineEdit(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtNomcli.sizePolicy().hasHeightForWidth())
        self.txtNomcli.setSizePolicy(sizePolicy)
        self.txtNomcli.setMinimumSize(QtCore.QSize(250, 0))
        self.txtNomcli.setObjectName("txtNomcli")
        self.gridLayout_2.addWidget(self.txtNomcli, 1, 7, 1, 5)
        self.cmbMunicli = QtWidgets.QComboBox(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbMunicli.sizePolicy().hasHeightForWidth())
        self.cmbMunicli.setSizePolicy(sizePolicy)
        self.cmbMunicli.setMinimumSize(QtCore.QSize(180, 0))
        self.cmbMunicli.setObjectName("cmbMunicli")
        self.gridLayout_2.addWidget(self.cmbMunicli, 3, 9, 1, 1)
        self.btnAltacli = QtWidgets.QPushButton(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAltacli.sizePolicy().hasHeightForWidth())
        self.btnAltacli.setSizePolicy(sizePolicy)
        self.btnAltacli.setMinimumSize(QtCore.QSize(25, 25))
        self.btnAltacli.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\\\templates\\../img/calendar.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnAltacli.setIcon(icon1)
        self.btnAltacli.setIconSize(QtCore.QSize(24, 24))
        self.btnAltacli.setObjectName("btnAltacli")
        self.gridLayout_2.addWidget(self.btnAltacli, 0, 8, 1, 1)
        self.lblMunicli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblMunicli.setObjectName("lblMunicli")
        self.gridLayout_2.addWidget(self.lblMunicli, 3, 8, 1, 1)
        self.lblDni = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblDni.setObjectName("lblDni")
        self.gridLayout_2.addWidget(self.lblDni, 0, 1, 1, 1)
        self.txtEmailcli = QtWidgets.QLineEdit(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtEmailcli.sizePolicy().hasHeightForWidth())
        self.txtEmailcli.setSizePolicy(sizePolicy)
        self.txtEmailcli.setMinimumSize(QtCore.QSize(200, 0))
        self.txtEmailcli.setObjectName("txtEmailcli")
        self.gridLayout_2.addWidget(self.txtEmailcli, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 9, 1, 1)
        self.lblAltacli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblAltacli.setObjectName("lblAltacli")
        self.gridLayout_2.addWidget(self.lblAltacli, 0, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 3, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 13, 1, 1)
        self.chkHistoriacli = QtWidgets.QCheckBox(parent=self.pesClientes)
        self.chkHistoriacli.setObjectName("chkHistoriacli")
        self.gridLayout_2.addWidget(self.chkHistoriacli, 3, 10, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.btnGrabarcli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnGrabarcli.setObjectName("btnGrabarcli")
        self.horizontalLayout.addWidget(self.btnGrabarcli)
        self.btnModifcli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnModifcli.setObjectName("btnModifcli")
        self.horizontalLayout.addWidget(self.btnModifcli)
        self.btnDelecli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnDelecli.setObjectName("btnDelecli")
        self.horizontalLayout.addWidget(self.btnDelecli)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.tablaClientes = QtWidgets.QTableWidget(parent=self.pesClientes)
        self.tablaClientes.setObjectName("tablaClientes")
        self.tablaClientes.setColumnCount(0)
        self.tablaClientes.setRowCount(0)
        self.gridLayout_3.addWidget(self.tablaClientes, 4, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 2, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 3, 2, 1, 1)
        self.panPrincipal.addTab(self.pesClientes, "")
        self.tabConstruccion = QtWidgets.QWidget()
        self.tabConstruccion.setObjectName("tabConstruccion")
        self.label = QtWidgets.QLabel(parent=self.tabConstruccion)
        self.label.setGeometry(QtCore.QRect(260, 275, 381, 51))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.panPrincipal.addTab(self.tabConstruccion, "")
        self.gridLayout.addWidget(self.panPrincipal, 0, 2, 1, 1)
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=venPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1177, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        venPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(parent=venPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(venPrincipal)
        self.panPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "InmoTeis"))
        self.lblMovilcli.setText(_translate("venPrincipal", "Móvil:"))
        self.lblNomcli.setText(_translate("venPrincipal", "Nombre:"))
        self.lblDircli.setText(_translate("venPrincipal", "Dirección:"))
        self.lblEmailcli.setText(_translate("venPrincipal", "Email:"))
        self.lblApelcli.setText(_translate("venPrincipal", "Apellidos:"))
        self.lblProvcli.setText(_translate("venPrincipal", "Provincia:"))
        self.lblMunicli.setText(_translate("venPrincipal", "Municipio:"))
        self.lblDni.setText(_translate("venPrincipal", "DNI/CIF:"))
        self.lblAltacli.setText(_translate("venPrincipal", "Fecha Alta:"))
        self.chkHistoriacli.setText(_translate("venPrincipal", "Histórico"))
        self.btnGrabarcli.setText(_translate("venPrincipal", "Grabar"))
        self.btnModifcli.setText(_translate("venPrincipal", "Modificar"))
        self.btnDelecli.setText(_translate("venPrincipal", "Eliminar"))
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.pesClientes), _translate("venPrincipal", "CLIENTES"))
        self.label.setText(_translate("venPrincipal", "PANEL EN CONSTRUCCION"))
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.tabConstruccion), _translate("venPrincipal", "Tab 2"))
        self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
        self.actionSalir.setText(_translate("venPrincipal", "Salir"))
