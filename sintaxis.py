import ply.yacc as yacc

from lexico import tokens

#--------------------------------------------------------------------------#


def p_final(p):
    '''final : asignacion PUNTOYCOMA
             | asignacion PUNTOYCOMA final

             | expresionInt PUNTOYCOMA
             | expresionInt PUNTOYCOMA final

             | expresionDouble PUNTOYCOMA
             | expresionDouble PUNTOYCOMA final

             | expresionString PUNTOYCOMA
             | expresionString PUNTOYCOMA final

             | expresionBool PUNTOYCOMA
             | expresionBool PUNTOYCOMA final

             | expresionBoolFor PUNTOYCOMA
             | expresionBoolFor PUNTOYCOMA final

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

             | sentenciaFor PUNTOYCOMA final
             | sentenciaFor PUNTOYCOMA
             | sentenciaFor final
             | sentenciaFor

             | sentenciaSubstring PUNTOYCOMA final
             | sentenciaSubstring PUNTOYCOMA

             | VARIABLE DSUMA PUNTOYCOMA final
             | VARIABLE DSUMA PUNTOYCOMA
             | VARIABLE DRESTA PUNTOYCOMA final
             | VARIABLE DRESTA PUNTOYCOMA

             | expresionLista PUNTOYCOMA
             | expresionLista PUNTOYCOMA final
             | expresionNewList PUNTOYCOMA
             | expresionNewList PUNTOYCOMA final

             | expresionSet PUNTOYCOMA
             | expresionSet PUNTOYCOMA final

             | expresionMap PUNTOYCOMA
             | expresionMap PUNTOYCOMA final

             | expresionSwitch
             | expresionSwitch PUNTOYCOMA
             | expresionSwitch PUNTOYCOMA final

             | declaracionSimple PUNTOYCOMA
             | declaracionSimple PUNTOYCOMA final

             | sentenciaForEach
             | sentenciaForEach final
             | sentenciaForEach PUNTOYCOMA
             | sentenciaForEach PUNTOYCOMA final

             | funcionFirstWhere PUNTOYCOMA
             | funcionFirstWhere PUNTOYCOMA final

             | funcionSimple
             | funcionSimple final
             | funcionSimple PUNTOYCOMA
             | funcionSimple PUNTOYCOMA final

             | funcion
             | funcion final

             | funcionReturn
             | funcionReturn final
    '''

def p_algoritmoUnico(p):
    '''algoritmoUnico : asignacion PUNTOYCOMA
                      | expresionInt PUNTOYCOMA
                      | expresionDouble PUNTOYCOMA
                      | expresionString PUNTOYCOMA
                      | expresionBool PUNTOYCOMA
                      | expresionBoolFor PUNTOYCOMA
                      | sentenciaWhile
                      | sentenciaDoWhile PUNTOYCOMA
                      | sentenciaIf
                      | imprimir PUNTOYCOMA
                      | funcionStdin PUNTOYCOMA
                      | funcionStdout PUNTOYCOMA
                      | negacionBool PUNTOYCOMA
                      | comparacionBool PUNTOYCOMA
                      | sentenciaFor
                      | sentenciaSubstring PUNTOYCOMA
                      | VARIABLE DSUMA PUNTOYCOMA
                      | VARIABLE DRESTA PUNTOYCOMA
                      | expresionLista PUNTOYCOMA
                      | expresionNewList PUNTOYCOMA
                      | expresionSet PUNTOYCOMA
                      | expresionMap PUNTOYCOMA
                      | expresionSwitch
                      | declaracionSimple PUNTOYCOMA
                      | sentenciaForEach
                      | funcionFirstWhere PUNTOYCOMA
                      | funcionSimple
    '''









def p_funcionFirstWhere(p):
    '''funcionFirstWhere : VARIABLE FUNCIONFIRSTWHERE PIZQ PIZQ VARIABLE PDER FLECHA expresionBool PDER
    '''









def p_expresionSwitch(p):
    '''expresionSwitch : SWITCH PIZQ VARIABLE PDER LIZQ cases LDER
                       | SWITCH PIZQ VARIABLE PDER LIZQ cases DEFAULT DOSPUNTOS algoritmoUnico LDER
    '''
def p_cases(p):
    '''cases : caseString
             | caseInt
             | caseBool
    '''
def p_caseString(p):
    '''caseString : CASE STRING DOSPUNTOS final BREAK PUNTOYCOMA
                  | CASE STRING DOSPUNTOS final BREAK PUNTOYCOMA caseString
    '''
def p_caseInt(p):
    '''caseInt : CASE ENTERO DOSPUNTOS final BREAK PUNTOYCOMA
               | CASE ENTERO DOSPUNTOS final BREAK PUNTOYCOMA caseInt
    '''
def p_caseBool(p):
    '''caseBool : CASE BOOL DOSPUNTOS final BREAK PUNTOYCOMA
                | CASE BOOL DOSPUNTOS final BREAK PUNTOYCOMA caseBool
    '''








def p_expresionMap(p):
    '''expresionMap : MAP VARIABLE
                    | MAP VARIABLE IGUAL LIZQ LDER
                    | LIZQ LDER
                    | MAP VARIABLE IGUAL LIZQ expMap LDER
                    | LIZQ expMap LDER
                    | VARIABLE

    '''
def p_expMap(p):
    '''expMap : claveValor DOSPUNTOS claveValor
              | claveValor DOSPUNTOS claveValor COMA expMap
    '''
def p_claveValor(p):
    '''claveValor : VARIABLE
                  | STRING
                  | ENTERO
                  | DOUBLE
                  | BOOL

                  | CIZQ expListDynamic CDER
                  | CIZQ expListSet CDER
                  | expresionNewList

                  | SETFROM PIZQ CIZQ CDER PDER
                  | SETFROM PIZQ CIZQ expListDynamic CDER PDER

                  | LIZQ LDER
                  | LIZQ expMap LDER
    '''







def p_expresionSet(p):
    '''expresionSet : SET VARIABLE
                    | SETFROM PIZQ CIZQ CDER PDER
                    | SET VARIABLE IGUAL SETFROM PIZQ CIZQ CDER PDER
                    | SETFROM PIZQ CIZQ expListDynamic CDER PDER
                    | SET VARIABLE IGUAL SETFROM PIZQ CIZQ expListDynamic CDER PDER
                    | VARIABLE FUNCIONTAKE PIZQ ENTERO PDER
                    | VARIABLE
    '''








def p_expresionNewList(p):
    '''expresionNewList : NEWLIST PIZQ PDER
                        | NEWLIST PIZQ ENTERO PDER
                        | CIZQ CDER
    '''
def p_expresionLista(p):
    '''expresionLista : LIST MENOR STRINGR MAYOR VARIABLE
                      | funcionSplit
                      | LIST MENOR STRINGR MAYOR VARIABLE IGUAL funcionSplit
                      | LIST MENOR STRINGR MAYOR VARIABLE IGUAL CIZQ expListString CDER
                      | LIST MENOR STRINGR MAYOR VARIABLE IGUAL expresionNewList
                      | CIZQ expListString CDER

                      | LIST MENOR INT MAYOR VARIABLE
                      | LIST MENOR INT MAYOR VARIABLE IGUAL CIZQ expListInt CDER
                      | LIST MENOR INT MAYOR VARIABLE IGUAL expresionNewList
                      | CIZQ expListInt CDER

                      | LIST MENOR DOUBLER MAYOR VARIABLE
                      | LIST MENOR DOUBLER MAYOR VARIABLE IGUAL CIZQ expListNum CDER
                      | LIST MENOR DOUBLER MAYOR VARIABLE IGUAL expresionNewList
                      | CIZQ expListNum CDER

                      | LIST MENOR NUM MAYOR VARIABLE
                      | LIST MENOR NUM MAYOR VARIABLE IGUAL CIZQ expListNum CDER
                      | LIST MENOR NUM MAYOR VARIABLE IGUAL expresionNewList

                      | LIST MENOR BOOLR MAYOR VARIABLE
                      | LIST MENOR BOOLR MAYOR VARIABLE IGUAL CIZQ expListBool CDER
                      | LIST MENOR BOOLR MAYOR VARIABLE IGUAL expresionNewList
                      | CIZQ expListBool CDER

                      | LIST MENOR DYNAMIC MAYOR VARIABLE
                      | LIST MENOR DYNAMIC MAYOR VARIABLE IGUAL CIZQ expListDynamic CDER
                      | LIST MENOR DYNAMIC MAYOR VARIABLE IGUAL expresionNewList
                      | CIZQ expListDynamic CDER

                      | LIST MENOR SET MAYOR VARIABLE
                      | LIST MENOR SET MAYOR VARIABLE IGUAL CIZQ expListSet CDER
                      | LIST MENOR SET MAYOR VARIABLE IGUAL expresionNewList
                      | CIZQ expListSet CDER

                      | LIST MENOR MAP MAYOR VARIABLE
                      | LIST MENOR MAP MAYOR VARIABLE IGUAL CIZQ expListMap CDER
                      | LIST MENOR MAP MAYOR VARIABLE IGUAL expresionNewList
                      | CIZQ expListMap CDER

                      | VARIABLE CIZQ ENTERO CDER
                      | VARIABLE FUNCIONTAKE PIZQ ENTERO PDER
                      | VARIABLE FUNCIONRANGE PIZQ ENTERO COMA ENTERO PDER

                      | VARIABLE

    '''
def p_expListString(p):
    '''expListString : STRING
                     | STRING COMA expListString
                     | VARIABLE
                     | VARIABLE COMA expListString
    '''
def p_funcionSplit(p):
    '''funcionSplit : STRING FUNCIONSPLIT PIZQ STRING PDER'''
def p_expListInt(p):
    '''expListInt : ENTERO
                  | ENTERO COMA expListInt
                  | VARIABLE
                  | VARIABLE COMA expListInt
    '''
def p_expListNum(p):
    '''expListNum : ENTERO
                  | DOUBLE
                  | ENTERO COMA expListNum
                  | DOUBLE COMA expListNum
                  | VARIABLE
                  | VARIABLE COMA expListNum
    '''
def p_expListBool(p):
    '''expListBool : BOOL
                   | BOOL COMA expListBool
                   | VARIABLE
                   | VARIABLE COMA expListBool
    '''
def p_expListDynamic(p):
    '''expListDynamic : STRING
                      | ENTERO
                      | DOUBLE
                      | BOOL
                      | STRING COMA expListDynamic
                      | ENTERO COMA expListDynamic
                      | DOUBLE COMA expListDynamic
                      | BOOL COMA expListDynamic
                      | VARIABLE
                      | VARIABLE COMA expListDynamic
    '''
def p_expListSet(p):
    '''expListSet : SETFROM PIZQ CIZQ CDER PDER
                  | SETFROM PIZQ CIZQ expListDynamic CDER PDER
                  | SETFROM PIZQ CIZQ CDER PDER COMA expListSet
                  | SETFROM PIZQ CIZQ expListDynamic CDER PDER COMA expListSet
                  | VARIABLE
                  | VARIABLE COMA expListSet
    '''
def p_expListMap(p):
    '''expListMap : LIZQ LDER
                  | LIZQ expMap LDER
                  | LIZQ LDER COMA expListMap
                  | LIZQ expMap LDER COMA expListMap
                  | VARIABLE
                  | VARIABLE COMA expListMap
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

def p_declaracionSimple(p):
    '''declaracionSimple : STRINGR VARIABLE
                         | INT VARIABLE
                         | DOUBLER VARIABLE
                         | NUM VARIABLE
                         | VAR VARIABLE
                         | DYNAMIC VARIABLE
                         | BOOLR VARIABLE
    '''






def p_imprimir(p):
    '''imprimir : PRINT PIZQ expresion PDER
                | PRINT PIZQ asignacionSimple PDER'''










def p_funcionStdin(p):
    'funcionStdin : FUNCIONSTDIN'
def p_funcionStdout(p):
    '''funcionStdout : FUNCIONSTDOUT PIZQ expresion PDER
                     | FUNCIONSTDOUT PIZQ asignacionSimple PDER'''











def p_funcionSimple(p):
    '''funcionSimple : VOID VARIABLE PIZQ objeto VARIABLE PDER FLECHA algoritmoUnico
                     | VOID VARIABLE PIZQ PDER FLECHA algoritmoUnico
    '''
def p_funcion(p):
    '''funcion : VOID VARIABLE PIZQ PDER LIZQ LDER
               | VOID VARIABLE PIZQ PDER LIZQ final LDER

               | VOID VARIABLE PIZQ objeto VARIABLE PDER LIZQ LDER
               | VOID VARIABLE PIZQ objeto VARIABLE PDER LIZQ final LDER
    '''

def p_funcionReturn(p):
    '''funcionReturn : STRINGR VARIABLE PIZQ PDER LIZQ RETURN expresionString PUNTOYCOMA LDER
                     | STRINGR VARIABLE PIZQ PDER LIZQ final RETURN expresionString PUNTOYCOMA LDER
                     | STRINGR VARIABLE PIZQ objeto VARIABLE PDER LIZQ RETURN expresionString PUNTOYCOMA LDER
                     | STRINGR VARIABLE PIZQ objeto VARIABLE PDER LIZQ final RETURN expresionString PUNTOYCOMA LDER

                     | INT VARIABLE PIZQ PDER LIZQ RETURN expresionInt PUNTOYCOMA LDER
                     | INT VARIABLE PIZQ PDER LIZQ final RETURN expresionInt PUNTOYCOMA LDER
                     | INT VARIABLE PIZQ objeto VARIABLE PDER LIZQ RETURN expresionInt PUNTOYCOMA LDER
                     | INT VARIABLE PIZQ objeto VARIABLE PDER LIZQ final RETURN expresionInt PUNTOYCOMA LDER

                     | DOUBLER VARIABLE PIZQ PDER LIZQ RETURN expresionDouble PUNTOYCOMA LDER
                     | DOUBLER VARIABLE PIZQ PDER LIZQ final RETURN expresionDouble PUNTOYCOMA LDER
                     | DOUBLER VARIABLE PIZQ objeto VARIABLE PDER LIZQ RETURN expresionDouble PUNTOYCOMA LDER
                     | DOUBLER VARIABLE PIZQ objeto VARIABLE PDER LIZQ final RETURN expresionDouble PUNTOYCOMA LDER

                     | NUM VARIABLE PIZQ PDER LIZQ RETURN expresionDouble PUNTOYCOMA LDER
                     | NUM VARIABLE PIZQ PDER LIZQ final RETURN expresionDouble PUNTOYCOMA LDER
                     | NUM VARIABLE PIZQ objeto VARIABLE PDER LIZQ RETURN expresionDouble PUNTOYCOMA LDER
                     | NUM VARIABLE PIZQ objeto VARIABLE PDER LIZQ final RETURN expresionDouble PUNTOYCOMA LDER

                     | VAR VARIABLE PIZQ PDER LIZQ RETURN expresion PUNTOYCOMA LDER
                     | VAR VARIABLE PIZQ PDER LIZQ final RETURN expresion PUNTOYCOMA LDER
                     | VAR VARIABLE PIZQ objeto VARIABLE PDER LIZQ RETURN expresion PUNTOYCOMA LDER
                     | VAR VARIABLE PIZQ objeto VARIABLE PDER LIZQ final RETURN expresion PUNTOYCOMA LDER

                     | DYNAMIC VARIABLE PIZQ PDER LIZQ RETURN expresion PUNTOYCOMA LDER
                     | DYNAMIC VARIABLE PIZQ PDER LIZQ final RETURN expresion PUNTOYCOMA LDER
                     | DYNAMIC VARIABLE PIZQ objeto VARIABLE PDER LIZQ RETURN expresion PUNTOYCOMA LDER
                     | DYNAMIC VARIABLE PIZQ objeto VARIABLE PDER LIZQ final RETURN expresion PUNTOYCOMA LDER

                     | BOOLR VARIABLE PIZQ PDER LIZQ RETURN expresionBool PUNTOYCOMA LDER
                     | BOOLR VARIABLE PIZQ PDER LIZQ final RETURN expresionBool PUNTOYCOMA LDER
                     | BOOLR VARIABLE PIZQ objeto VARIABLE PDER LIZQ RETURN expresionBool PUNTOYCOMA LDER
                     | BOOLR VARIABLE PIZQ objeto VARIABLE PDER LIZQ final RETURN expresionBool PUNTOYCOMA LDER

                     | LIST VARIABLE PIZQ PDER LIZQ RETURN expresionLista PUNTOYCOMA LDER
                     | LIST VARIABLE PIZQ PDER LIZQ final RETURN expresionLista PUNTOYCOMA LDER
                     | LIST VARIABLE PIZQ objeto VARIABLE PDER LIZQ RETURN expresionLista PUNTOYCOMA LDER
                     | LIST VARIABLE PIZQ objeto VARIABLE PDER LIZQ final RETURN expresionLista PUNTOYCOMA LDER

                     | MAP VARIABLE PIZQ PDER LIZQ RETURN expresionMap PUNTOYCOMA LDER
                     | MAP VARIABLE PIZQ PDER LIZQ final RETURN expresionMap PUNTOYCOMA LDER
                     | MAP VARIABLE PIZQ objeto VARIABLE PDER LIZQ RETURN expresionMap PUNTOYCOMA LDER
                     | MAP VARIABLE PIZQ objeto VARIABLE PDER LIZQ final RETURN expresionMap PUNTOYCOMA LDER

                     | SET VARIABLE PIZQ PDER LIZQ RETURN expresionSet PUNTOYCOMA LDER
                     | SET VARIABLE PIZQ PDER LIZQ final RETURN expresionSet PUNTOYCOMA LDER
                     | SET VARIABLE PIZQ objeto VARIABLE PDER LIZQ RETURN expresionSet PUNTOYCOMA LDER
                     | SET VARIABLE PIZQ objeto VARIABLE PDER LIZQ final RETURN expresionSet PUNTOYCOMA LDER
    '''










def p_sentenciaForEach(p):
    '''sentenciaForEach : FOR PIZQ STRINGR VARIABLE IN VARIABLE PDER algoritmoUnico
                        | FOR PIZQ INT VARIABLE IN VARIABLE PDER algoritmoUnico
                        | FOR PIZQ DOUBLER VARIABLE IN VARIABLE PDER algoritmoUnico
                        | FOR PIZQ NUM VARIABLE IN VARIABLE PDER algoritmoUnico
                        | FOR PIZQ DYNAMIC VARIABLE IN VARIABLE PDER algoritmoUnico
                        | FOR PIZQ BOOLR VARIABLE IN VARIABLE PDER algoritmoUnico
                        | FOR PIZQ MAP VARIABLE IN VARIABLE PDER algoritmoUnico
                        | FOR PIZQ SET VARIABLE IN VARIABLE PDER algoritmoUnico

                        | FOR PIZQ STRINGR VARIABLE IN VARIABLE PDER LIZQ final LDER
                        | FOR PIZQ INT VARIABLE IN VARIABLE PDER LIZQ final LDER
                        | FOR PIZQ DOUBLER VARIABLE IN VARIABLE PDER LIZQ final LDER
                        | FOR PIZQ NUM VARIABLE IN VARIABLE PDER LIZQ final LDER
                        | FOR PIZQ DYNAMIC VARIABLE IN VARIABLE PDER LIZQ final LDER
                        | FOR PIZQ BOOLR VARIABLE IN VARIABLE PDER LIZQ final LDER
                        | FOR PIZQ MAP VARIABLE IN VARIABLE PDER LIZQ final LDER
                        | FOR PIZQ SET VARIABLE IN VARIABLE PDER LIZQ final LDER
    '''
def p_objetoForEach(p):
    '''objetoForEach : STRINGR
                     | INT
                     | DOUBLER
                     | NUM
                     | DYNAMIC
                     | BOOLR
                     | MAP
                     | SET
    '''






















def p_sentenciaIf(p):
    '''sentenciaIf : IF PIZQ expresionBool PDER algoritmoUnico
                   | IF PIZQ expresionBool PDER algoritmoUnico sentenciasElseIf
                   | IF PIZQ expresionBool PDER algoritmoUnico sentenciasElseIf sentenciaElse
                   | IF PIZQ expresionBool PDER LIZQ final LDER
                   | IF PIZQ expresionBool PDER LIZQ final LDER sentenciasElseIf
                   | IF PIZQ expresionBool PDER LIZQ final LDER sentenciasElseIf sentenciaElse
    '''
def p_sentenciasElseIf(p):
    '''sentenciasElseIf : sentenciaElseIf
                        | sentenciaElseIf sentenciasElseIf
    '''
def p_sentenciaElseIf(p):
    '''sentenciaElseIf : ELSEIF PIZQ expresionBool PDER algoritmoUnico
                       | ELSEIF PIZQ expresionBool PDER LIZQ final LDER
    '''
def p_sentenciaElse(p):
    '''sentenciaElse : ELSE algoritmoUnico
                     | ELSE LIZQ final LDER
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
                 | funcionFirstWhere
    '''









def p_expresionFor(p):
    '''asignacionFor : INT VARIABLE IGUAL expresionInt
                    | DOUBLER VARIABLE IGUAL expresionDouble
                    | NUM VARIABLE IGUAL expresionDouble
                    | DYNAMIC VARIABLE IGUAL expresionInt
                    | DYNAMIC VARIABLE IGUAL expresionDouble
                    | VAR VARIABLE IGUAL expresionInt
                    | VAR VARIABLE IGUAL expresionDouble
                    | VARIABLE IGUAL expresionInt
                    | VARIABLE IGUAL expresionDouble
                    '''
def p_expresionBoolFor(p):
    '''expresionBoolFor : valorDouble comparadorMat expresionDouble
                        | VARIABLE comparadorMat expresionDouble
                        | VARIABLE comparadorMat VARIABLE
                        | valorDouble comparadorMat VARIABLE
                        | valorBool
                        | negacionBool
                        | comparacionBool
    '''
def p_sentenciaFor(p):
    '''sentenciaFor : FOR PIZQ asignacionFor PUNTOYCOMA expresionBoolFor PUNTOYCOMA VARIABLE DSUMA PDER LIZQ final LDER
                    | FOR PIZQ asignacionFor PUNTOYCOMA expresionBoolFor PUNTOYCOMA VARIABLE DSUMA PDER algoritmoUnico
                    | FOR PIZQ asignacionFor PUNTOYCOMA expresionBoolFor PUNTOYCOMA VARIABLE DRESTA PDER LIZQ final LDER
                    | FOR PIZQ asignacionFor PUNTOYCOMA expresionBoolFor PUNTOYCOMA VARIABLE DRESTA PDER algoritmoUnico
    '''









def p_sentenciaWhile(p):
    '''sentenciaWhile : WHILE PIZQ expresionBool PDER LIZQ final LDER
                      | WHILE PIZQ expresionBool PDER algoritmoUnico
    '''
def p_sentenciaDoWhile(p):
    'sentenciaDoWhile : DO LIZQ final LDER WHILE PIZQ expresionBool PDER'









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
                   | sentenciaSubstring
                   | STRING CIZQ ENTERO CDER
    '''
def p_expresion_aritmetica_String(p):
    '''expresionString : valorString SUMA expresionString
                       | valorString
    '''
def p_expresion_index_String(p):
    'expresionIndexString : valorString CIZQ ENTERO CDER'
def p_sentenciaSubstring(p):
    '''sentenciaSubstring : VARIABLE FUNCIONSUBSTRING PIZQ ENTERO PDER
                         | VARIABLE FUNCIONSUBSTRING PIZQ ENTERO COMA ENTERO PDER
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
              | BOOLR
              | MAP
              | SET
    '''



#--------------------------------------------------------------------------#

confirmacion = [False]
def p_error(p):
    print("Syntax error in input!")
    confirmacion[0]=True

#--------------------------------------------------------------------------#


parser = yacc.yacc()
def analisisSintactico(data):
    lista=[]
    contador = 0
    for linea in data:
        contador+=1
        print("> "+linea)
        r = parser.parse(linea)
        if confirmacion[0]==False:
            print("None")
            lista.append("None")
        if confirmacion[0]==True:
            print("error en linea "+str(contador))
            lista.append("error en linea "+str(contador))
            confirmacion[0]=False
    print(lista)
    return lista


'''
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)

    print(result)





archivo = open("algoritmoLoayza.txt")
for linea in archivo:
    try:
        s = linea.rstrip('\n')
        print("> "+s)
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)


f=open("algoritmoLoayza.txt")
s = f.read()
print(s)
result = parser.parse(s)
print(result)
f.close()
'''