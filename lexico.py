import ply.lex as lex

reserved = {
    "var":"VAR",
    "int":"INT",
    "void":"VOID",
    "in":"IN",
    "double":"DOUBLER",
    "num":"NUM",
    "String":"STRINGR",
    "bool":"BOOLR",
    "Map":"MAP",
    "Set":"SET",
    "List":"LIST",
    "dynamic":"DYNAMIC",
    "if":"IF",
    "do":"DO",
    "else":"ELSE",
    "for":"FOR",
    "while":"WHILE",
    "switch":"SWITCH",
    "is":"IS",
    "print":"PRINT",
    "case":"CASE",
    "break":"BREAK",
    "do":"DO",
    "default":"DEFAULT",
    "return":"RETURN"
}

tokens = [
    "BOOL",
    "VARIABLE",
    "ENTERO",
    "DOUBLE",
    "STRING",
    "SUMA",
    "RESTA",
    "MULTI",
    "DIV",
    "DIVENTERO",
    "MOD",
    "IGUAL",
    "DIGUAL",
    "NOIGUAL",
    "MAYOR",
    "MENOR",
    "MAYIGUAL",
    "MENIGUAL",
    "ISNEGADO",
    "PUNTOYCOMA",
    "DSUMA",
    "DRESTA",
    "LIZQ",
    "LDER",
    "CIZQ",
    "CDER",
    "PIZQ",
    "PDER",
    "COMILLAS",
    "COMILLAD",
    "DOSPUNTOS",
    "COMA",
    "SETFROM",
    "NEWLIST",
    "ELSEIF",
    "FUNCIONSUBSTRING",
    "FUNCIONSTDIN",
    "FUNCIONSTDOUT",
    "FUNCIONTAKE",
    "FUNCIONRANGE",
    "FUNCIONSPLIT",
    "FUNCIONFIRSTWHERE",
    "FLECHA",
    "AND",
    "OR",
    "NOT"
]+list(reserved.values())

#--------------------------------------------------------------------------#

t_STRING = r'("[^"]*"|\'[^\']*\')'
t_SUMA = r"\+"
t_RESTA = r"-"
t_MULTI = r"\*"
t_DIV = r"/"
t_DIVENTERO = r"\~/"
t_MOD = r"%"
t_IGUAL = r"="
t_DIGUAL = r"=="
t_NOIGUAL = "!="
t_MAYOR = r">"
t_MENOR = r"<"
t_MAYIGUAL = r">="
t_MENIGUAL = r"<="

t_PUNTOYCOMA = r";"
t_DSUMA= r"\+\+"
t_DRESTA= r"--"
t_CIZQ = r"\["
t_CDER = r"\]"
t_LIZQ = r"\{"
t_LDER = r"\}"
t_PIZQ = r"\("
t_PDER = r"\)"
t_DOSPUNTOS = r":"
t_COMA = r","
t_FLECHA = r"=>"
t_AND = r"&&"
t_OR = r"\|\|"
t_NOT = r"!"
#--------------------------------------------------------------------------#

t_ignore = " \t"
t_ignore_CM1 = r"//.*"
t_ignore_CM2 = r"^(\/\*).*(\*\/)$"

#--------------------------------------------------------------------------#

def t_BOOL(t):
    r"(true|false)"
    return t

def t_ISNEGADO(t):
    r"is\!"
    return t

def t_NEWLIST(t):
    r"(new\sList)"
    return t

def t_SETFROM(t):
    r"(Set\.from)"
    return t

def t_ELSEIF(t):
    r"else\sif"
    return t

def t_FUNCIONSUBSTRING(t):
    r"(\.substring)"
    return t

def t_FUNCIONSPLIT(t):
    r"(\.split)"
    return t

def t_FUNCIONSTDIN(t):
    r"stdin\.readLineSync\(\)"
    return t

def t_FUNCIONSTDOUT(t):
    r"stdout\.write"
    return t

def t_FUNCIONTAKE(t):
    r"\.take"
    return t

def t_FUNCIONRANGE(t):
    r"\.getRange"
    return t

def t_FUNCIONFIRSTWHERE(t):
    r"\.firstWhere"
    return t

def t_VARIABLE(t):
    r"[a-zA-Z][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value,"VARIABLE")
    return t

def t_DOUBLE(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r"\d+"
    t.value = int(t.value)
    return t

#--------------------------------------------------------------------------#

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("No es reconocido '"+t.value[0]+"'")
    t.lexer.skip(1)

lexer = lex.lex()

def analisisLexico(data):
    resultado = []
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        resultado.append(tok)
    lexer.lineno = 1
    return resultado

'''
print("Mi primer analizador léxico :)")
archivo = open("algoritmoLoayza.txt")
for linea in archivo:
    print(">>"+linea)
    analizar(linea)
    if len(linea)==0:
        break

while True:
    data = input("> ")
    analizar(data)
    if len(data)==0: break
'''