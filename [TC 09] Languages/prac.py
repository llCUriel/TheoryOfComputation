# -*- coding: utf-8 -*-
#!/usr/bin/python
import itertools
SIGMA=['1','0']


##
Q1=['A','B']
Sa1='A'
SaF=['B']
DELTAuno={('A','0'):'A',
		  ('A','1'):'B',
		  ('B','1'):'A',
		  ('B','0'):'A'}
##
Q2=['C','D']
Sb1='C'
SbF=['C']
DELTAdos={('C','1'):'C',
		  ('C','0'):'D',
		  ('D','1'):'C',
		  ('D','0'):'D'}



#ESTADOS
Q=list(itertools.product(Q1,Q2))
# ESTADO INICIAL
S=(Sa1,Sb1)
#ESTADOS FINALES
estaFinalesunion=[]

for q in Q:
		if q[0] in SaF and q[1] in SbF:
			estaFinalesunion.append(q)

estaFinalesinterseccion=[]

for q in Q:
		if q[0] in SaF or q[1] in SbF:
			estaFinalesinterseccion.append(q)



delta={}
#DELTA
for m in Q:
	for i in SIGMA:
		delta[m,i] = (DELTAuno[m[0],i],DELTAdos[m[1],i])
		print("-------------------------")
		print "("+str(m[0])+" , "+str(i)+")"
		print "("+str(m[1])+ " , "+str(i)+")"
		print("-------------------------")
	

print(Q)
print(S)
print("Interseccion: "+str(estaFinalesunion))
print("Union: "+str(estaFinalesinterseccion))
print (str(delta))
