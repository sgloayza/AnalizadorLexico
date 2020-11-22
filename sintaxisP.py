import ply.yacc as yacc

from lexico import tokens

#--------------------------------------------------------------------------#

def p_final(p):
    '''final : algoritmo PUNTOYCOMA
             | asignacion PUNTOYCOMA
             | expresionInt PUNTOYCOMA
             | expresionDouble PUNTOYCOMA
             | expresionString PUNTOYCOMA
             | expresionBool PUNTOYCOMA
    '''

def p_algoritmo(p):
    '''algoritmo : asignacion PUNTOYCOMA
                 | expresionInt PUNTOYCOMA
                 | expresionDouble PUNTOYCOMA
                 | expresionString PUNTOYCOMA
                 | expresionBool PUNTOYCOMA
                 | expresion
    '''

def p_asignacion(p):
    '''asignacion : INT VARIABLE IGUAL expresionInt
                  | DOUBLER VARIABLE IGUAL expresionDouble
                  | NUM VARIABLE IGUAL expresionDouble
                  | STRINGR VARIABLE IGUAL expresionString
                  | BOOLR VARIABLE IGUAL expresionBool
                  | DYNAMIC VARIABLE IGUAL expresion
                  | VAR VARIABLE IGUAL expresion

    '''





def p_valor(p):
    '''valor : ENTERO
             | VARIABLE
             | DOUBLE
             | STRING
    '''

def p_expresion(p):
    '''expresion : valor operadorMat expresion
                 | valor
                 | expresionString
                 | expresionInt
                 | expresionDouble
    '''





def p_valorBool(p):
    '''valorBool : BOOL
                   | VARIABLE
    '''

def p_expresionBool(p):
    '''expresionBool : valorInt comparadorMat expresionInt
                       | valorBool
    '''







def p_valorString(p):
    '''valorString : STRING
                   | VARIABLE
    '''

def p_expresion_aritmetica_String(p):
    '''expresionString : valorString operadorMat expresionString
                       | valorString
    '''







def p_valorInt(p):
    '''valorInt : ENTERO
                | VARIABLE
    '''

def p_expresion_aritmetica_Int(p):
    '''expresionInt : valorInt operadorMat expresionInt
                    | valorInt
    '''





def p_valorDouble(p):
    '''valorDouble : DOUBLE
                   | valorInt
    '''

def p_expresion_aritmetica_Double(p):
    '''expresionDouble : valorDouble operadorMat expresionDouble
                       | valorDouble
    '''







def p_operadorMat(p):
    '''operadorMat : SUMA
                   | RESTA
                   | MULTI
                   | DIV
                   | DIVENTERO
                   | MOD
    '''

def p_comparaedorMat(p):
    '''comparadorMat : DIGUAL
                   | NOIGUAL
                   | MAYOR
                   | MENOR
                   | MAYIGUAL
                   | MENIGUAL
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