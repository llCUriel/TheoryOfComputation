def definirNuevoEstado():
	global count
	aux = 'estado' + str(count)
	count += 1
	return aux
def armarKleene(s0, F0):
	global estado
	global DELTA
	global count
	s = definirNuevoEstado()
	F = definirNuevoEstado()
	estado.append(s)
	estado.append(F)
	DELTA[(s, 'e')] = [s0,F]
	DELTA[(F0, 'e')] = [s0,F]
	return s, F
def realizarConcatenacion(s1, F1, s2, F2):
	global estado
	global DELTA
	DELTA[(F1, 'e')] = [s2]
	return s1, F2
def definirSimbolo(simb):
	global estado
	global DELTA
	global count
	s = definirNuevoEstado()
	F = definirNuevoEstado()
	estado.append(s)
	estado.append(F)
	DELTA[(s, simb)] = [F]
	return s, F
def leerRegex(regex):
	global estado
	global DELTA
	global count
	if ( regex.strip()[-1] == ')'):
		regex = regex[1:-1]
	if(len(regex) == 1):
			return definirSimbolo(regex[0])
	else:
		flag = False
		pila = []
		for i in range(len(regex)):

			if( regex[i] == '|' and len(pila) == 0):
				flag = True
				s1, F1 = leerRegex( regex[:i] )
				s2, F2 = leerRegex( regex[i + 1:] )
				return realizarUnion(s1,F1,s2,F2)
				
			elif( regex[i] == '(' ):
				pila.append( regex[i] )

			elif( regex[i] == ')' ):
				pila.pop()
		if(not flag):
			pila = []
			for i in range(len(regex)):
				if( regex[i] == '.' and len(pila) == 0):
					flag = True
					s1, F1 = leerRegex( regex[:i] )
					s2, F2 = leerRegex( regex[i + 1:] )
					return realizarConcatenacion(s1, F1, s2, F2)				
				elif( regex[i] == '(' ):
					pila.append(regex[i])
				elif( regex[i] == ')' ):
					pila.pop()
		s, F = leerRegex(regex[:-1])
		return armarKleene(s, F)
def realizarUnion(s1, F1, s2, F2):
	global estado
	global DELTA
	global count
	s = definirNuevoEstado()
	F = definirNuevoEstado()
	estado.append(s)
	estado.append(F)
	DELTA[(s, 'e')] = [s1,s2]
	DELTA[(F1, 'e')] = [F]
	DELTA[(F2, 'e')] = [F]
	return s, F

rgx = raw_input()
regex = ""
for x in range(len(rgx) - 1):
	if((rgx[x] != '(') and (rgx[x] != '|')):
		if((rgx[x + 1] != '|') and (rgx[x + 1] != '*') and (rgx[x + 1] != ')')):		
			regex += rgx[x]			
			regex += '.'
		else:
			regex += rgx[x]	
	else:
		regex += rgx[x]	
regex += rgx.strip()[-1]
Sigma = ['a', 'b']
DELTA = {}
estado = []
s = ''
F = ''
count = 0
s, F = leerRegex(regex)
print "estado = ", estado
print "s = ", s
print "F = ", F 
print "DELTA = "
aux = sorted(DELTA)
for i in aux:
	if(len(DELTA[i]) == 1):
		print i, "-", DELTA[i]
	else:
		for j in range(len(DELTA[i])):
			print i, "-", "['" + DELTA[i][j] + "']"


