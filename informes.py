from reportlab.pdfgen import canvas
from datetime import datetime
from PIL import Image
import os, shutil
import var
import sqlite3
from PyQt6 import QtSql, QtWidgets, QtCore

class Informes:
    @staticmethod
    #Informe de clientes
    def reportClientes(self):
        try:
            rootPath = '.\\informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            nomepdfcli = fecha + "_listadoclientes.pdf"
            pdf_path = os.path.join(rootPath, nomepdfcli)   #también esto
            var.report = canvas.Canvas(pdf_path)
            titulo = "Listado Clientes"
            query0=QtSql.QSqlQuery()
            query0.exec("select count(*) from clientes")
            if query0.next():
                print(query0.value(0))
                registros = int(query0.value(0))
                paginas = int (registros/ 20) + 1 # quitar 1 porque si es exacto suma 1 más
            Informes.topInforme(titulo)
            Informes.footInforme(titulo, paginas)
            items = ['DNI', 'APELLIDOS', 'NOMBRE', 'MOVIL', 'PROVINCIA', 'MUNICIPIO']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 650, str(items[0]))
            var.report.drawString(100, 650, str(items[1]))
            var.report.drawString(190, 650, str(items[2]))
            var.report.drawString(280, 650, str(items[3]))
            var.report.drawString(355, 650, str(items[4]))
            var.report.drawString(440, 650, str(items[5]))
            var.report.line(50, 645, 525, 645)
            query = QtSql.QSqlQuery()
            query.prepare("SELECT dnicli, apelcli, nomecli, movilcli, provcli, municli from"
                          " clientes order by apelcli")
            if query.exec():
                registros= query.value(0)
                print(registros)
                x = 55
                y = 630
                while query.next():
                    if y <= 90:
                        var.report.setFont('Helvetica-Oblique', size=8)
                        var.report.drawString(450, 70, 'Página siguiente...')
                        var.report.showPage() #Crea una pag nueva
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo,paginas)
                        items = ['DNI', 'APELLIDOS', 'NOMBRE', 'MOVIL', 'PROVINCIA', 'MUNICIPIO']
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(55, 650, str(items[0]))
                        var.report.drawString(100, 650, str(items[1]))
                        var.report.drawString(190, 650, str(items[2]))
                        var.report.drawString(280, 650, str(items[3]))
                        var.report.drawString(355, 650, str(items[4]))
                        var.report.drawString(440, 650, str(items[5]))
                        var.report.line(50, 645, 525, 645)
                        x = 55
                        y = 630

                    var.report.setFont('Helvetica', size=8)
                    dni = '****' + str(query.value(0)[4:7] + '***')
                    var.report.drawCentredString(x + 10, y, str(dni))
                    var.report.drawString(x + 50 , y, str(query.value(1)))
                    var.report.drawString(x + 140, y, str(query.value(2)))
                    var.report.drawString(x + 220, y, str(query.value(3)))
                    var.report.drawString(x + 305, y, str(query.value(4)))
                    var.report.drawString(x + 390, y, str(query.value(5)))
                    y = y - 25

            var.report.save()
            for file in os.listdir(rootPath):
                if file.endswith(nomepdfcli):
                    os.startfile(pdf_path)

        except Exception as error:
            print(error)

    def topInforme(titulo):
        try:
            ruta_logo = '.\\img\\iconoInmo.ico'
            logo = Image.open(ruta_logo)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Inmobiliaria Teis')
                var.report.drawString(230, 675, titulo)
                var.report.line(50, 665, 525, 665)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: cartesteisr@mail.com')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera informe:', error)

    def footInforme(titulo,paginas):
        try:
            total_pages = 0
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber() + '/' + str(paginas)))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)


    @staticmethod
    #informePropiedades
    def reportPropiedades(localidad):
        try:
            rootPath = '.\\informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            nomepdfProp = fecha + "_listadopropiedades.pdf"
            pdf_path = os.path.join(rootPath, nomepdfProp)
            var.report = canvas.Canvas(pdf_path)
            titulo = "Listado Propiedades de " + str(localidad)
            Informes.topInforme(titulo)

            # Calculate total pages
            paginas = 1
            query0 = QtSql.QSqlQuery()
            query0.exec("select count(*) from propiedades where muniProp = :localidad")
            query0.bindValue(':localidad', localidad)
            if (query0.next()):
                registros = int(query0.value(0))
                paginas = int(registros / 20) + 1
            Informes.footInforme(titulo, paginas)
            items = ['CODIGO', 'DIRECCION', 'TIPO', 'OPERACION', 'VENTA €', 'ALQUILER €']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 650, str(items[0]))  # CODIGO
            var.report.drawString(110, 650, str(items[1]))  # DIRECCION
            var.report.drawString(260, 650, str(items[2]))  # TIPO
            var.report.drawString(310, 650, str(items[3]))  # TIPO OPERACION
            var.report.drawString(415, 650, str(items[4]))  # PRECIO VENTA
            var.report.drawString(470, 650, str(items[5]))  # PRECIO ALQUILER
            var.report.line(50, 645, 525, 645)
            query0.prepare(
                "SELECT codigo, dirprop, tipoprop, tipooper, prevenprop, prealquiprop from propiedades where muniProp = :localidad order by codigo")
            query0.bindValue(':localidad', localidad)
            if query0.exec():
                x = 60
                y = 630
                while query0.next():
                    if y <= 90:
                        var.report.setFont('Helvetica-Oblique', size=8)  # HELVETICA OBLIQUE PARA LA FUENTE ITALIC
                        var.report.drawString(450, 80, 'Página siguiente...')
                        var.report.showPage()  # CREAMOS UNA PAGINA NUEVA
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo, paginas)
                        items = ['CODIGO', 'DIRECCION', 'TIPO', 'OPERACION', 'VENTA €', 'ALQUILER €']
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(55, 650, str(items[0]))  # CODIGO
                        var.report.drawString(120, 650, str(items[1]))  # DIRECCION
                        var.report.drawString(250, 650, str(items[2]))  # TIPO
                        var.report.drawString(325, 650, str(items[3]))  # TIPO OPERACION
                        var.report.drawString(405, 650, str(items[4]))  # PRECIO VENTA
                        var.report.drawString(475, 650, str(items[5]))  # PRECIO ALQUILER
                        var.report.line(50, 645, 525, 645)
                        x = 60
                        y = 630

                    var.report.setFont('Helvetica', size=8)
                    dni = str(query0.value(0))
                    var.report.drawCentredString(x + 5, y, str(dni))  # CODIGO
                    var.report.drawString(x + 60, y, str(query0.value(1)))  # DIRECCION
                    var.report.drawString(x + 205, y, str(query0.value(2)))  # TIPO
                    var.report.drawString(x + 250, y, str(query0.value(3)))  # TIPO OPERACION
                    var.report.drawString(x + 370, y, str(query0.value(4)))  # PRECIO VENTA
                    var.report.drawString(x + 420, y, str(query0.value(5)))  # PRECIO ALQUILER
                    y = y - 25.

            var.report.save()
            for file in os.listdir(rootPath):
                if file.endswith(nomepdfProp):
                    os.startfile(pdf_path)
        except Exception as error:
            print(error)

    @staticmethod
    # Informe de ventas
    def reportVentas(self):
        try:
            rootPath = '.\\informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            nomepdfcli = fecha + "_listadoventas.pdf"
            pdf_path = os.path.join(rootPath, nomepdfcli)  # también esto
            var.report = canvas.Canvas(pdf_path)
            titulo = "Listado Ventas Factura" + var.ui.txtidfac.text()

            paginas = 1
            query0 = QtSql.QSqlQuery()
            query0.prepare("SELECT COUNT(*) FROM facturas WHERE id = :id")
            query0.bindValue(":id", var.ui.txtidfac.text())
            if query0.exec() and query0.next():
                print(query0.value(0))
                registros = int(query0.value(0))
                paginas = int(registros / 20) + 1  # quitar 1 porque si es exacto suma 1 más
            Informes.topInforme(titulo)
            Informes.footInforme(titulo, paginas)
            items = ['ID VENTA', 'ID PROPIEDAD', "DIRECCION", 'LOCALIDAD', 'TIPO', 'PRECIO VENTA']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 650, str(items[0]))
            var.report.drawString(110, 650, str(items[1]))
            var.report.drawString(210, 650, str(items[2]))
            var.report.drawString(300, 650, str(items[3]))
            var.report.drawString(390, 650, str(items[4]))
            var.report.drawString(450, 650, str(items[5]))
            var.report.line(50, 645, 525, 645)
            query = QtSql.QSqlQuery()
            query.prepare("""
                SELECT v.idventa, p.codigo, p.dirprop, p.muniprop, p.tipoprop, p.prevenprop
                FROM ventas AS v
                INNER JOIN propiedades AS p ON v.codprop = p.codigo
                WHERE v.facventa = :factura
            """)
            query.bindValue(":factura", var.ui.txtidfac.text())

            if query.exec():
                registros = query.value(0)
                print(registros)
                x = 55
                y = 630
                while query.next():
                    if y <= 90:
                        var.report.setFont('Helvetica-Oblique', size=8)
                        var.report.drawString(450, 70, 'Página siguiente...')
                        var.report.showPage()  # Crea una pag nueva
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo, paginas)
                        items = ['ID VENTA', 'ID PROPIEDAD', "DIRECCION", 'LOCALIDAD', 'TIPO', 'PRECIO VENTA']
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(50, 650, str(items[0]))
                        var.report.drawString(110, 650, str(items[1]))
                        var.report.drawString(210, 650, str(items[2]))
                        var.report.drawString(300, 650, str(items[3]))
                        var.report.drawString(390, 650, str(items[4]))
                        var.report.drawString(450, 650, str(items[5]))
                        var.report.line(50, 645, 525, 645)
                        x = 55
                        y = 630

                    var.report.setFont('Helvetica', size=8)
                    var.report.drawCentredString(70, y, str(query.value(0)))
                    var.report.drawString(150, y, str(query.value(1)))
                    var.report.drawString(210, y, str(query.value(2)))
                    var.report.drawString(300, y, str(query.value(3)))
                    var.report.drawString(390, y, str(query.value(4)))
                    var.report.drawString(470, y, str(query.value(5)))
                    var.report.drawString(430, 130, "Precio: ")
                    var.report.drawString(430, 110, "Impuestos: ")
                    var.report.drawString(430, 90, "Total: ")
                    var.report.drawString(490, 130, str(var.ui.txtPrecioVentaFac.text()))
                    var.report.drawString(490, 110, str(var.ui.txtImpuestos.text()))
                    var.report.drawString(490, 90, str(var.ui.txtPrecioTotal.text()))
                    y = y - 25

            var.report.save()
            for file in os.listdir(rootPath):
                if file.endswith(nomepdfcli):
                    os.startfile(pdf_path)

        except Exception as error:
            print(error)
