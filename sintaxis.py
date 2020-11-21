import ply.yacc as yacc

from lexico import tokens

#--------------------------------------------------------------------------#

def p_final(p):
    '''final : expresion PUNTOYCOMA
             | asignacion PUNTOYCOMA
             | imprimir PUNTOYCOMA
             | sentenciaIf PUNTOYCOMA
             | sentenciaIf
             | sentenciaWhile
             | sentenciaWhile PUNTOYCOMA
             | sentenciaDoWhile PUNTOYCOMA
    '''

def p_algoritmo(p):
    '''algoritmo : imprimir PUNTOYCOMA
                 | asignacion PUNTOYCOMA
                 | expresion PUNTOYCOMA
                 | comparacion PUNTOYCOMA
                 | sentenciaWhile
                 | sentenciaWhile PUNTOYCOMA
                 | sentenciaIf PUNTOYCOMA
                 | sentenciaIf
                 | sentenciaDoWhile PUNTOYCOMA
    '''

def p_sentenciaIf(p):
    '''sentenciaIf : IF PIZQ comparacion PDER algoritmo
                   | IF PIZQ comparacion PDER LIZQ algoritmo LDER
    '''

#****************************************#

def p_sentenciaWhile(p):
    '''sentenciaWhile : WHILE PIZQ comparacion PDER LIZQ algoritmo LDER
                      | WHILE PIZQ comparacion PDER algoritmo
    '''

def p_sentenciaDoWhile(p):
    'sentenciaDoWhile : DO LIZQ algoritmo LDER WHILE PIZQ comparacion PDER'

def p_imprimir(p):
    'imprimir : PRINT PIZQ expresion PDER'

#****************************************#

def p_asignacion(p):
    'asignacion : VARIABLE IGUAL expresion'

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


def p_expresion(p):
    '''expresion : valor
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