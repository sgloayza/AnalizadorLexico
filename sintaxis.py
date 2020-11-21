import ply.yacc as yacc

from lexico import tokens

#--------------------------------------------------------------------------#

def p_sentencias(p):
    '''sentencias : algoritmo
                 | algoritmo sentencias
    '''

def p_algoritmo(p):
    '''algoritmo : imprimir
                 | asignacion
                 | expresion
                 | comparacion
                 | sentenciaIf
    '''

#****************************************#

def p_sentenciaIf(p):
    'sentenciaIf : IF PIZQ comparacion PDER DOSPUNTOS algoritmo'

def p_imprimir(p):
    'imprimir : PRINT PIZQ expresion PDER'

def p_asignacion(p):
    'asignacion : VARIABLE IGUAL expresion'

#****************************************#

def p_expresion(p):
    '''expresion : valor
    '''

def p_valor(p):
    '''valor : ENTERO
             | VARIABLE
    '''

#****************************************#

def p_expresion_comparacion(p):
    'comparacion : expresion operadorComp expresion'

def p_operadorComp(p):
    '''operadorComp : DIGUAL
                    | NOIGUAL
                    | MAYOR
                    | MENOR
                    | MAYIGUAL
                    | MENIGUAL
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