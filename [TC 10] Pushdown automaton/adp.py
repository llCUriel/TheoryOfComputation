# -*- coding: utf-8 -*-
#!/usr/bin/python

import os 

Q={'q1','q2','q3'}
s='q1'
f='q3'
Sigma = ['a','b']
DELTA={('q1','a','z'): ('q1',['A','Z']),
               ('q1','b','A'): ('q2',['e']),
	       ('q2','b','A'): ('q2',['e']),
	       ('q2','e','z'): ('q3',['z']),
	       ('q1','a','A'):('q1',['A','A'])}
GAMMA={'e','z','A'}
pila=['z']
pila.append('A')
gamma=pila.pop()


def probadorDeAplicacion():
	valores = raw_input("Escriba los valores:")
	validar(valores)
	automata_de_pila(valores)
	
def validar(val):
	flag = 0
	for x in val:
		if x != Sigma[0] and x != Sigma[1]:
			flag = 1
	if flag == 1:
		print "Esta palabra no es valida tiene que ser de la forma: "
		print "{a^n b^n | n >= 0}"
		exit()
	else :
		poscicion = val.find("b")
		recorre_unos = val[poscicion: ]
		recorre_ceros = val[:poscicion]
		for y in recorre_unos:
			if y == "a":
				print "Esta palabra no es valida tiene que ser de la forma: "
				print "{a°n b°n | n >= 0}"
				exit()
		if len(recorre_unos) != len(recorre_ceros):
			print "Esta palabra no es valida tiene que ser de la forma: "
			print "{a°n b°n | n >= 0}"
			exit()
		

def automata_de_pila(val):
	pila = ["#"]
	alfabeto_pila = "z"
#	print "Palabra del alfabeto: ",val	
#	print "Estado inicial de la pila: ",pila	
	print 
	print
	for i in val:
		if i == "a":
			pila.append(alfabeto_pila)
			print "pila: ",pila
			print
		if i == "b":
			pila.pop()
			print "pila: ",pila
			print
	print "La cadena es aceptada"
	
probadorDeAplicacion()