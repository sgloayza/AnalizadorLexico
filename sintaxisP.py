import ply.yacc as yacc

from lexico import tokens

#--------------------------------------------------------------------------#

def p_final(p):
    '''final : algoritmo PUNTOYCOMA
             | algoritmo PUNTOYCOMA final

             | asignacion PUNTOYCOMA
             | asignacion PUNTOYCOMA final

             | expresionInt PUNTOYCOMA
             | expresionInt PUNTOYCOMA final

             | expresionDouble PUNTOYCOMA
             | expresionDouble PUNTOYCOMA final

             | expresionString PUNTOYCOMA
             | expresionString PUNTOYCOMA final

             | expresionBool PUNTOYCOMA
             | expresionBool PUNTOYCOMA final

             | sentenciaWhile
             | sentenciaWhile final
             | sentenciaWhile PUNTOYCOMA
             | sentenciaWhile PUNTOYCOMA final

             | sentenciaDoWhile PUNTOYCOMA
             | sentenciaDoWhile PUNTOYCOMA final

             | sentenciaIf PUNTOYCOMA
             | sentenciaIf PUNTOYCOMA final
             | sentenciaIf
             | sentenciaIf final

             | sentenciaElse PUNTOYCOMA
             | sentenciaElse PUNTOYCOMA final
             | sentenciaElse
             | sentenciaElse final

             | imprimir PUNTOYCOMA
             | imprimir PUNTOYCOMA final
             | funcionStdin PUNTOYCOMA
             | funcionStdin PUNTOYCOMA final
             | funcionStdout PUNTOYCOMA
             | funcionStdout PUNTOYCOMA final

             | negacionBool PUNTOYCOMA
             | negacionBool PUNTOYCOMA final

             | comparacionBool PUNTOYCOMA final
             | comparacionBool PUNTOYCOMA

             | sentenciaElseIf PUNTOYCOMA final
             | sentenciaElseIf final
             | sentenciaElseIf PUNTOYCOMA
             | sentenciaElseIf
    '''

def p_algoritmo(p):
    '''algoritmo : asignacion PUNTOYCOMA
                 | expresionInt PUNTOYCOMA
                 | expresionDouble PUNTOYCOMA
                 | expresionString PUNTOYCOMA
                 | expresionBool PUNTOYCOMA
                 | expresion

                 | sentenciaWhile
                 | sentenciaWhile PUNTOYCOMA

                 | sentenciaDoWhile PUNTOYCOMA

                 | sentenciaIf PUNTOYCOMA
                 | sentenciaIf

                 | sentenciaElse PUNTOYCOMA
                 | sentenciaElse

                 | imprimir PUNTOYCOMA
                 | funcionStdin PUNTOYCOMA
                 | funcionStdout PUNTOYCOMA
                 | negacionBool PUNTOYCOMA
                 | comparacionBool PUNTOYCOMA

                 | sentenciaElseIf
                 | sentenciaElseIf PUNTOYCOMA
    '''








def p_asignacion(p):
    '''asignacion : INT VARIABLE IGUAL expresionInt
                  | DOUBLER VARIABLE IGUAL expresionDouble
                  | NUM VARIABLE IGUAL expresionDouble
                  | STRINGR VARIABLE IGUAL expresionString
                  | BOOLR VARIABLE IGUAL expresionBool
                  | DYNAMIC VARIABLE IGUAL expresion
                  | VAR VARIABLE IGUAL expresion
                  | asignacionSimple

    '''

def p_asignacionSimple(p):
    'asignacionSimple : VARIABLE IGUAL expresion'








def p_imprimir(p):
    '''imprimir : PRINT PIZQ expresion PDER
                | PRINT PIZQ asignacionSimple PDER'''







def p_funcionStdin(p):
    'funcionStdin : FUNCIONSTDIN'

def p_funcionStdout(p):
    '''funcionStdout : FUNCIONSTDOUT PIZQ expresion PDER
                | FUNCIONSTDOUT PIZQ asignacionSimple PDER'''




def p_sentenciaIf(p):
    '''sentenciaIf : IF PIZQ expresionBool PDER algoritmo
                   | IF PIZQ expresionBool PDER LIZQ algoritmo LDER
    '''


def p_sentenciaElse(p):
    '''sentenciaElse : ELSE algoritmo
                     | ELSE LIZQ algoritmo LDER
    '''

def p_sentenciaElseIf(p):
    '''sentenciaElseIf : ELSEIF PIZQ expresionBool PDER algoritmo
                       | ELSEIF PIZQ expresionBool PDER LIZQ algoritmo LDER
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
                 | expresionBool
    '''







def p_sentenciaWhile(p):
    '''sentenciaWhile : WHILE PIZQ expresionBool PDER LIZQ algoritmo LDER
                      | WHILE PIZQ expresionBool PDER algoritmo
    '''

def p_sentenciaDoWhile(p):
    'sentenciaDoWhile : DO LIZQ algoritmo LDER WHILE PIZQ expresionBool PDER'






def p_valorBool(p):
    '''valorBool : BOOL
                 | VARIABLE
    '''

def p_expresionBool(p):
    '''expresionBool : valorDouble comparadorMat expresionDouble
                     | VARIABLE comparadorMat expresionDouble
                     | VARIABLE comparadorMat VARIABLE
                     | valorDouble comparadorMat VARIABLE
                     | valorBool
                     | negacionBool
                     | comparacionBool
                     | valor IS objeto
                     | valor ISNEGADO objeto
    '''

def p_negacionBool(p):
    'negacionBool : NOT PIZQ expresionBool PDER'

def p_comparacionBool(p):
    '''comparacionBool : expresionBool operadorLogico expresionBool
                       | expresionBool operadorLogico comparacionBool
    '''












def p_valorString(p):
    '''valorString : STRING
                   | VARIABLE
                   | FUNCIONSTDIN
                   | expresionIndexString
    '''

def p_expresion_aritmetica_String(p):
    '''expresionString : valorString SUMA expresionString
                       | valorString
    '''

def p_expresion_index_String(p):
    'expresionIndexString : valorString CIZQ ENTERO CDER'






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

def p_comparadorMat(p):
    '''comparadorMat : DIGUAL
                     | NOIGUAL
                     | MAYOR
                     | MENOR
                     | MAYIGUAL
                     | MENIGUAL
    '''

def p_operadorLogico(p):
    '''operadorLogico : AND
                      | OR
    '''

def p_objeto(p):
    '''objeto : STRINGR
            | INT
            | DOUBLER
            | NUM
            | VAR
            | DYNAMIC
            | LIST
            | BOOL
            | MAP
            | SET
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