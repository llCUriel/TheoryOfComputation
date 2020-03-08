#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AutomataFinitoN:


    def obtenerCerraduraEpsilon(estado, DELTA):
		miLista=[]
		miLista.append(estado)
		for i in DELTA:
			if (estado == i[0] and i[1]=='e'):	
				cadena = str(DELTA.get(i))[2:-2]
				miLista.append(cadena)
				obtenerCerraduraEpsilon(cadena,DELTA)
		return miLista

#def Ecerradura(q,d):
#	aux = []
#	q = list(q)
#	d = dict(d)
#	i =0
#	for x in q:
#		aux.append(q[i])
#		P = []
#		P.append(x)
#		P.append('e')
#		Ptuple = tuple(P)
#		i+=1

#		if d.has_key(Ptuple):
#			aux.append(d[Ptuple][0])

#	return aux


    def convertiraAutomataFinitoDeterminista(argumento):

        argumento.AFD =[]

        estadosTemporales= argumento.obtenerEstadoInicialPrima()

        while len(estadosTemporales) <> 0:

            argumento.AFD.append( estadosTemporales[0])

            for estado in argumento.obtEstado_():

                obtenerTransicionDelAFD=[]

                for mysimbol in argumento.mysimbolsDelLenguaje:

                    nuevoEstado=[]

                    for e in estado:

                        for t in argumento.obtenerTransicion([e],mysimbol):

                            if t not in nuevoEstado:

                                nuevoEstado.append(t)

                        nuevoEstado.sort()

                    obtenerTransicionDelAFD.append([mysimbol,nuevoEstado])

                estadosTemporales.append([estado]+obtenerTransicionDelAFD)

            estadosTemporales.pop(0)

        estasdosDeAceptacion = [l[0][0] for l in filter(lambda s:len(s)>=4 and s[-1]=='*',argumento.AFN)]

        for e in argumento.AFD:

            Aceptacion = False

            for ea in estasdosDeAceptacion :

                        if not Aceptacion:

                            Aceptacion =  ea in e[0]

            if Aceptacion and '*' not in e: e.append('*')

        return argumento.AFD


    def __init__(argumento,AFN):

        argumento.AFN = AFN

        argumento.mysimbolsDelLenguaje =  argumento.getLenguajeDeAFN()

        argumento.AFD = argumento.convertiraAutomataFinitoDeterminista()
		
    def obtenerTransicion(argumento,e,t):

	return filter(lambda s:s[0]==t,filter(lambda s:s[0]==e,argumento.AFN)[0])[0][1]

    def obtenerEstadoInicialPrima(argumento):

        return filter(lambda s:len(s)>=4 and s[3]=='>',argumento.AFN) # Función encargada de obtener el nuevo estado inicial, es decir el estado inicial prima.

    def getLenguajeDeAFN(argumento):

        return [l[0] for l in  filter(lambda s:len(s)==2,argumento.AFN[-1])];  # Esta función es opcional, ya que se podria definir el lenguaje como usualmente se realiza en clase o bien, definirlo cuando se llama al obj

    def obtEstado(argumento):   

        return [e[0] for e in  argumento.AFD] # Nuevos estados.

    def obtEstado_(argumento):

        return map(lambda e:e[1],filter(lambda s:s[0] in argumento.mysimbolsDelLenguaje and s[1] not in argumento.obtEstado(),argumento.AFD[-1]))
# Tabla de transición donde "->" indica el estado inicial de nuestro automata.


# DefiniciÃ³n de nuestro automata donde ">" indica el estado inicial, y 'e' las transiciones epsilon.
Atma = AutomataFinitoN(                      [ [ [1], ['a',[1]] , ['b',[1,2]],'>']
							    , [ [2], ['b',[1] ] ,['a',[3]  ]],
							      [ [3], ['a',[3]] ,['b',[3]  ]], 
							       [ [4], ['b',[4]] ,['a',[4]  ],'e'],
							       [ [5], ['a',[5]] ,['b',[4]  ],'e']
							      ] )
							      
for m in  Atma.AFD:

    print ("[**********]  \033[92m"+str(m))
