import random



def generarNumeroAleatorio():
	return random.randint(0,255)


def generarTupla():

	for i in range(0,4):
		miNumero = generarNumeroAleatorio()
		cadena = str(miNumero)
		if miNumero<10:
			cadena = "00"+str(miNumero)
		if miNumero>=10 and miNumero <100:
			cadena = "0"+str(miNumero)
	return cadena

def generarDireccionIp():
	cadena = ""
	for i in range(0,4):
		cadena = cadena +"."+ generarTupla()



	return cadena[1:]

def probadorDeAplicacion():
	for i in range(0,10):
		print str(generarTupla())+"|"+generarDireccionIp()

probadorDeAplicacion()
