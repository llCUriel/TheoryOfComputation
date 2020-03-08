from colorama import Fore, init

def eliminarProduccion(P, N):
	P1 = dict() 
	D = [] 
	S = []
	j= ""
	for x in P: 
		for y in P[x]:
			for l in y:
				print  x,Fore.YELLOW+"----->",l
				if l == 'a'<=l<='z':
					if not S: 
						S.append(l)
					else:
						S = anadirterminalEnmiLista(S,l);
				if l in N:
					if not S:
						S.append(l)
						S.append('&')
					else:
						S = nanadirterminalEnmiLista(S,l);
				print S
			D = realizarUnion(D,S)
			S = []
		if '&' in D:
			D.remove('&')

		P1[x] = D
		D = []
	return P1

def nanadirterminalEnmiLista(miLista, Noterminal):
	variableAuxiliar = miLista
	miLista = anadirterminalEnmiLista(miLista,Noterminal)
	variableAuxiliar = realizarUnion(variableAuxiliar,miLista)
	return variableAuxiliar

def realizarUnion(A,B):
	variableAuxiliar= []
	for q in A:
		variableAuxiliar.append(q)
	for k in B:
		variableAuxiliar.append(k)
			
	return list(set(variableAuxiliar))
	
def anadirterminalEnmiLista(miLista, terminal):
	variableAuxiliar = []
	s = ""
	for q in miLista:
		for l in q:
			if l == '&':
				break
			s += l
		s += terminal
		variableAuxiliar.append(s)
		s =""
	return variableAuxiliar

def probadorDeAplicacion():
	P = {'S' : ['Aa','Ba','AB'],'A' : ['Aa','&'],'B' : ['aA','&']}
	NT = ['S','A','B'] 
	N= [] 
	variableAuxiliar = []
	for q in P:
		if '&' in P[q]:
			N.append(q)
	for q in NT:
		if q not in N:
			variableAuxiliar.append(q)
	for q in variableAuxiliar:
		for y in P[q]:
			for l in y:
				if l in N:
					bandera = True
				else:
					bandera = False
					break
			if bandera:
				N.append(q)
	print "N = ", N
	P1 = eliminarProduccion(P,N)
	for q in P1:
		print q, "----->", P1[q]

probadorDeAplicacion()