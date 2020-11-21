import ply.yacc as yacc

from lexico import tokens

#--------------------------------------------------------------------------#

def p_asignacion(p):
    'asignacion : VARIABLE IGUAL expresion'

#****************************************#

def p_expresion(p):
    '''expresion : valor PUNTOYCOMA
    '''

def p_valor(p):
    '''valor : ENTERO
             | VARIABLE
    '''

#****************************************#

def p_expresion_aritmetica(p):
    'expresion : valor operadorMat expresion'

def p_operadorMat(p):
    '''operadorMat : SUMA
                   | RESTA
                   | MULTI
                   | DIV
                   | DIVENTERO
                   | MOD
    '''

#--------------------------------------------------------------------------#

def p_error(p):
    print("Syntax error in input!")

#--------------------------------------------------------------------------#

parser = yacc.yacc()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)