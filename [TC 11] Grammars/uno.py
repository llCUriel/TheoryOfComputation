tokens = ('a','b')
t_a = r'a'
t_b = r'b'
def t_error(t):
	print('caracter ilegal', t.value[0])
	t.lexer.skip(1)

import ply.lex as lex
lex.lex()

def p_S(p):
	'''S : b A'''
	pass

def p_A(p):
	'''A : a a a A
		| b
		| empty '''
	pass

def p_empty(p):
	'empty : '
	pass

S = ' '

def p_error(p):
	global s
	if p:
		print('error de sintaxis en', p.value)
	else:
		print('error de sintaxis en EOF')
		print(s, 'no esta en el lenguaje')
import ply.yacc as yacc
yacc.yacc()
while(1):
	try:
		s = input('> ')
	except EOFError:
		break;
	if not s:
		continue
	t = yacc.parse(s)