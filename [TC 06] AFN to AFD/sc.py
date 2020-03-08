#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain,combinations
from time import sleep
from colorama import Cursor, init, Fore

def powerset(iterable):
		s=list(iterable)
		return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

def obtenerConjuntoDeEstadosF(Qprima):
			F=['q1']
			cnt = 0
			Fprima=[]
			print("\033[1;33m"+"¿Qué conjuntos contiene, por lo menos, un estado de F?"+'\033[0;m') 
			for q in Qprima:
				cnt = cnt + 1
				cadena = "Conjunto "+str(cnt)
				print cadena.center(70, "=") 
				if cnt == 1:
					print("Vacio")
				for x in q:
					if x in F:
						print(x+"\033[1;33m"+" Es un estado de aceptación, por lo que el conj "+str(cnt)+ " es parte de F''"+'\033[0;m') 
						Fprima.append(q)
					else:
						print(x + " No es un estado de aceptación.")
			return Fprima


def agregarTransicAVacio(Sigma, Q, DELTA):
	Dprima = {}

	for r in range(len(Sigma)):
		Dprima[('E', Sigma[r])] = 'E'
		print("\n------ "+Sigma[r]+" ------")
		for i in range(len(Q)):
			val = DELTA.get((Q[i], Sigma[r]))
			if(val is not None):
				print("("+Q[i]+","+Sigma[r]+")" +"->"+str(val))
			else:
				Dprima[(Q[i], Sigma[r])] = 'E'
				print("("+Q[i]+","+Sigma[r]+")"+ "->"+str(val))
	return Dprima


def obtDeltaEstrella(Dprima, Q, Fprima, Sigma, DELTA):
	print("\n"+str(Dprima)+"\n")
	miDiccionario = {}
	for j in range(len(Q)):
		miDiccionario[str(Q[j])]=0
		
	for j in DELTA:
		llave = DELTA[j][0]
		miDiccionario[llave] = miDiccionario[llave] + 1


	for t in range(len(Q)):
		if(miDiccionario.has_key(Q[t])):
			if((miDiccionario[Q[t]]==len(Q)) and 1==1):
				Dprima[(Q[t], Sigma[t])] = Fprima[len(Q)-1]
			
	print(miDiccionario)

def probadorDeAplicacion():
	F=['q1']
	Q=['q0','q1']
	s='q0'
	DELTA={ ('q0','a'):['q0'],
		      ('q0','b'):['q1'],
		      ('q1','a'):['q1'] }
	Sigma=['a','b']
	Qprima=list(powerset(Q))
	print("\033[1;33m"+"Conjunto potencia"+'\033[0;m') 
	print("\n")
	print("S' = P(S) = "+str(Qprima))
	print("\n")
	Fprima= obtenerConjuntoDeEstadosF(Qprima)
	print("\n")
	print("\033[1;33m"+"Colección de subconjuntos de S que contienen, por lo menos, un estado de F"+'\033[0;m') 
	print("\n")
	print ("F' = "+str(Fprima))
	print("\n")
	print("\033[1;33mAl estado vacio se le dibujan tantos arcos que salen e inciden en el estado, como simbolos del alfabeto haya-")
	Dprima = agregarTransicAVacio(Sigma,Q,DELTA)
	obtDeltaEstrella(Dprima,Q,Fprima,Sigma,DELTA)
	
	

	
probadorDeAplicacion()
