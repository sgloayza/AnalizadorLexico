import ply.lex as lex

reserved = {
    "var":"VAR",
    "int":"INT",
    "double":"DOUBLE",
    "num":"NUM",
    "String":"STRING",
    "Bool":"BOOL",
    "Map":"MAP",
    "dynamic":"DYNAMIC",
    "if":"IF",
    "else":"ELSE",
    "for":"FOR",
    "while":"WHILE",
    "switch":"SWITCH",
    "as":"AS",
    "is":"IS",
    "print":"PRINT",
    "case":"CASE",
    "break":"BREAK",
    "return":"RETURN"

}

tokens = [
    "VARIABLE",
    "ENTERO",
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
    "SET",
    "LIST",
    "ELSEIF",
    "FUNCIONSTRING",
    "FUNCIONARR",
    "FUNCIONSTDIN",
    "FUNCIONSTDOUT",
    "FLECHA",
    "AND",
    "OR",
    "NOT"
]+list(reserved.values())

#--------------------------------------------------------------------------#
