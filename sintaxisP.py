import ply.yacc as yacc

from lexico import tokens

#--------------------------------------------------------------------------#

def p_final(p):
    '''final : algoritmo PUNTOYCOMA
             | asignacion PUNTOYCOMA
             | expresionInt PUNTOYCOMA
             | expresionDouble PUNTOYCOMA
             | expresionString PUNTOYCOMA
    '''

def p_algoritmo(p):
    '''algoritmo : asignacion PUNTOYCOMA
                 | expresionInt PUNTOYCOMA
                 | expresionDouble PUNTOYCOMA
                 | expresionString PUNTOYCOMA
    '''

def p_asignacion(p):
    '''asignacion : INT VARIABLE IGUAL expresionInt
                  | DOUBLER VARIABLE IGUAL expresionDouble
                  | NUM VARIABLE IGUAL expresionDouble
                  | STRINGR VARIABLE IGUAL expresionString
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