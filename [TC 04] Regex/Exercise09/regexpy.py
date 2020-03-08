import re


def sobreescribirFichero(ruta, contenido):
	outfile = open(ruta, 'w')
	outfile.write(contenido)
	outfile.close()

def abrirFichero(ruta):
	cadena = ""
	infile = open(ruta, 'r')
	for line in infile:
		cadena = cadena +line
	infile.close()
	return cadena


def probadorDeAplicacion():
	ruta = "a.txt"
	patron = re.compile(r'([a-z]|[A-Z]|[0-9])*.@.([a-z]|[A-Z]|[0-9])*.*')
	cadena = abrirFichero(ruta)
	print patron.findall(cadena)


probadorDeAplicacion()
