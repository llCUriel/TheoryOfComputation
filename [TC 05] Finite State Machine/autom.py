Q=['q0','q1','q2']
S='q0'
Sigma = ['A','B','C']
F=['q0','q1']
delta = {
	('q0', 'B'):'q0',
	('q0', 'C'):'q0',
	('q0', 'A'):'q1',
	('q1', 'B'):'q1',
	('q1', 'A'):'q1',
	('q1', 'C'):'q2',
	('q2', 'A'):'q2',
	('q2', 'B'):'q2',
	('q2', 'C'):'q2'
}
def transicion(estado, sigma):
	global Sigma, delta
	STATUS = True
	if (sigma not in Sigma):
		STATUS = False
		return '', STATUS
	if(estado, sigma) not in delta.keys():
		STATUS = False
		return '', STATUS
	estado_siguiente = delta[(estado, sigma)]
	print ('Transicion(', estado, ',' , sigma ,')->', estado_siguiente)
	return estado_siguiente, STATUS

w = 'AB'
estado = S
for sigma in w:
	estado, STATUS = transicion(estado, sigma)
	if not STATUS:
		break
if (STATUS and (estado in F)):
	print (w, 'si esta en el lenguaje')
else:
	print (w, 'no esta en el lenguaje')
