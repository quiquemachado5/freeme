import re

cadena1 = "ARIAS CASTELLANO, DILIANA JOSE\nTRANSCANTÁBRICO, 11 - PORTAL\nCL DEL T\nL\n8 1-3\n28770 COLMENAR VIEJO\nCODIGO: 264459\nNIF : Y7729904D\nFECHA\nFACTURA\n31/08/22\n31/08/22\nCODIGO SAP: 000000050785779\nFACTURA\nNO.\n0224095856\n0224095857\nFECHA DE VENCIMIENTO: 07/09/22\nSEPA Direct Debit\nDIVISAS\nRESUMEN FACTURACION\nFECHA : 31/08/22\nNUMERO: 9643385430\nEUR\nEUR\nTOTAL\nDIVISAS\nB2M País de suministro: España\nB2Mobility GmbH\nWITTENER STRASSE 45\nTEL: 910 10 20 30\nFAX: 902 108 050\nNIF: ESN2765289J\nCONTACTO EN BP: tarjetasprofesionales@bp.com\nTOTAL\nEUR\nB2Mobility GmbH Inscrita en el R.M. de Bochum (Alemania) N.° de sociedad HRB 16999\nN.I.F.: N2765289J - NIF Intracomunitario ESN2765289J\nCR\nTOTAL\nEUR\nPag:\n96,11\n433,74\n529,85\nbp"

cadena2 = "19:14\nTotal\nDORTA ALVAREZ LUIS SEBASTIAN\nOtro importe x 1\nOtro importe x 1\nEfectivo\nsquareup.com\nCuéntale a DORTA ALVAREZ LUIS\nSEBASTIAN cómo fue tu experiencia\n132,65 €\n|||\nFactura simplificada 5A12AF39-13\nO\n|| 15% |\n99\nГ\nC\n92,00 €\n40,65 €\n6/10/2022, 19:13\nN.° rz76\n132,65 €\n|||"

cadena3 = "RESUMEN DEL PERIODO\nDe 08/01/22 a 08/14/22\nG48581671\nJosgreli Marin Colmenares\nES5921002282470200428575\n(1) Total facturas promociones y eventuales ajustes de Courier a Glovo\n(2) Total factura de Courier a Partner por servicio de delivery\n(3) Total Tasa de envío facturado a usuarios finales\n(4) Propinas recibidas de los usuarios finales\n(5) Suma total de los puntos anteriores (1) + (2) + (3) + (4)\n(6) Total efectivo retirado al final del periodo\n(7) Total efectivo retirado diariamente\n(8) Total efectivo recibido (6) + (7)\n(9) Ajuste de facturas anteriores\n(10) Ajustes de productos\n(11) Otros\n(12) Suma total de los ajustes anteriores (9) + (10) + (11)\n(13) Cuota por el uso de la plataforma\n(14) Importe líquido recibido por el courier (5) + (8) + (12) + (13)\n0.00 €\n557.73 €\n335.65 €\n17.00 €\n910.38 €\n0.00 €\n0.00 €\n0.00 €\n0.00 €\n0.00 €\n0.00 €\n0.00 €\n-3.03 €\n907.35 €"


patron_fecha = r"\d{1,2}/\d{1,2}/\d{2}"
patron_importe = r"\d+(?:,\d+)?(?:\.\d+)? €"


fecha_factura1 = re.findall(patron_fecha, cadena1)
if fecha_factura1:
    fecha_factura1 = fecha_factura1[-1]

importe_total1 = re.findall(patron_importe, cadena1)
if importe_total1:
    importe_total1 = importe_total1[-1]

fecha_factura2 = re.findall(patron_fecha, cadena2)
if fecha_factura2:
    fecha_factura2 = fecha_factura2[-1]

importe_total2 = re.findall(patron_importe, cadena2)
if importe_total2:
    importe_total2 = importe_total2[-1]

fecha_factura3 = re.findall(patron_fecha, cadena3)
if fecha_factura3:
    fecha_factura3 = fecha_factura3[-1]

importe_total3 = re.findall(patron_importe, cadena3)
if importe_total3:
    importe_total3 = importe_total3[-1]


print("Cadena 1:")
print("Fecha de la factura:", fecha_factura1)
print("Importe total:", importe_total1)

print("\nCadena 2:")
print("Fecha de la factura:", fecha_factura2)
print("Importe total:", importe_total2)

print("\nCadena 3:")
print("Fecha de la factura:", fecha_factura3)
print("Importe total:", importe_total3)
