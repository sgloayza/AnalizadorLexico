
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS BOOL BREAK CASE CDER CIZQ COMA COMILLAD COMILLAS DIGUAL DIV DIVENTERO DOSPUNTOS DOUBLE DRESTA DSUMA DYNAMIC ELSE ELSEIF ENTERO FLECHA FOR FUNCIONARR FUNCIONRANGE FUNCIONSTDIN FUNCIONSTDOUT FUNCIONSTRING FUNCIONTAKE IF IGUAL INT IS ISNEGADO LDER LIST LIZQ MAP MAYIGUAL MAYOR MENIGUAL MENOR MOD MULTI NOIGUAL NOT NUM OR PDER PIZQ PRINT PUNTOYCOMA RESTA RETURN SET STRING SUMA SWITCH VAR VARIABLE WHILEfinal : expresion PUNTOYCOMA\n             | asignacion PUNTOYCOMA\n             | imprimir PUNTOYCOMA\n             | sentenciaIf PUNTOYCOMA\n             | sentenciaIf\n    algoritmo : imprimir PUNTOYCOMA\n                 | asignacion PUNTOYCOMA\n                 | expresion PUNTOYCOMA\n                 | comparacion PUNTOYCOMA\n                 | sentenciaIf PUNTOYCOMA\n                 | sentenciaIf\n    sentenciaIf : IF PIZQ comparacion PDER algoritmo\n                   | IF PIZQ comparacion PDER LIZQ algoritmo LDER\n    imprimir : PRINT PIZQ expresion PDERasignacion : VARIABLE IGUAL expresioncomparacion : expresion operadorComp expresionoperadorComp : DIGUAL\n                    | NOIGUAL\n                    | MAYOR\n                    | MENOR\n                    | MAYIGUAL\n                    | MENIGUAL\n    expresion : valor\n    valor : ENTERO\n             | VARIABLE\n    expresion : valor operadorMat expresionoperadorMat : SUMA\n                   | RESTA\n                   | MULTI\n                   | DIV\n                   | DIVENTERO\n                   | MOD\n    '
    
_lr_action_items = {'VARIABLE':([0,15,16,17,18,19,20,21,22,23,24,32,33,34,35,36,37,38,39,42,],[7,26,-27,-28,-29,-30,-31,-32,26,26,26,7,26,-17,-18,-19,-20,-21,-22,7,]),'PRINT':([0,32,42,],[8,8,8,]),'IF':([0,32,42,],[9,9,9,]),'ENTERO':([0,15,16,17,18,19,20,21,22,23,24,32,33,34,35,36,37,38,39,42,],[10,10,-27,-28,-29,-30,-31,-32,10,10,10,10,10,-17,-18,-19,-20,-21,-22,10,]),'$end':([1,5,11,12,13,14,41,46,48,50,51,52,53,54,],[0,-5,-1,-2,-3,-4,-12,-11,-9,-6,-7,-8,-10,-13,]),'PUNTOYCOMA':([2,3,4,5,6,7,10,25,26,27,31,40,41,43,44,45,46,47,48,50,51,52,53,54,],[11,12,13,14,-23,-25,-24,-26,-25,-15,-14,48,-12,50,51,52,53,-16,-9,-6,-7,-8,-10,-13,]),'PDER':([6,10,25,26,28,29,47,],[-23,-24,-26,-25,31,32,-16,]),'DIGUAL':([6,7,10,25,26,30,45,],[-23,-25,-24,-26,-25,34,34,]),'NOIGUAL':([6,7,10,25,26,30,45,],[-23,-25,-24,-26,-25,35,35,]),'MAYOR':([6,7,10,25,26,30,45,],[-23,-25,-24,-26,-25,36,36,]),'MENOR':([6,7,10,25,26,30,45,],[-23,-25,-24,-26,-25,37,37,]),'MAYIGUAL':([6,7,10,25,26,30,45,],[-23,-25,-24,-26,-25,38,38,]),'MENIGUAL':([6,7,10,25,26,30,45,],[-23,-25,-24,-26,-25,39,39,]),'SUMA':([6,7,10,26,],[16,-25,-24,-25,]),'RESTA':([6,7,10,26,],[17,-25,-24,-25,]),'MULTI':([6,7,10,26,],[18,-25,-24,-25,]),'DIV':([6,7,10,26,],[19,-25,-24,-25,]),'DIVENTERO':([6,7,10,26,],[20,-25,-24,-25,]),'MOD':([6,7,10,26,],[21,-25,-24,-25,]),'IGUAL':([7,],[22,]),'PIZQ':([8,9,],[23,24,]),'LIZQ':([32,],[42,]),'LDER':([41,46,48,49,50,51,52,53,54,],[-12,-11,-9,54,-6,-7,-8,-10,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'final':([0,],[1,]),'expresion':([0,15,22,23,24,32,33,42,],[2,25,27,28,30,45,47,45,]),'asignacion':([0,32,42,],[3,44,44,]),'imprimir':([0,32,42,],[4,43,43,]),'sentenciaIf':([0,32,42,],[5,46,46,]),'valor':([0,15,22,23,24,32,33,42,],[6,6,6,6,6,6,6,6,]),'operadorMat':([6,],[15,]),'comparacion':([24,32,42,],[29,40,40,]),'operadorComp':([30,45,],[33,33,]),'algoritmo':([32,42,],[41,49,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> final","S'",1,None,None,None),
  ('final -> expresion PUNTOYCOMA','final',2,'p_final','sintaxis.py',8),
  ('final -> asignacion PUNTOYCOMA','final',2,'p_final','sintaxis.py',9),
  ('final -> imprimir PUNTOYCOMA','final',2,'p_final','sintaxis.py',10),
  ('final -> sentenciaIf PUNTOYCOMA','final',2,'p_final','sintaxis.py',11),
  ('final -> sentenciaIf','final',1,'p_final','sintaxis.py',12),
  ('algoritmo -> imprimir PUNTOYCOMA','algoritmo',2,'p_algoritmo','sintaxis.py',16),
  ('algoritmo -> asignacion PUNTOYCOMA','algoritmo',2,'p_algoritmo','sintaxis.py',17),
  ('algoritmo -> expresion PUNTOYCOMA','algoritmo',2,'p_algoritmo','sintaxis.py',18),
  ('algoritmo -> comparacion PUNTOYCOMA','algoritmo',2,'p_algoritmo','sintaxis.py',19),
  ('algoritmo -> sentenciaIf PUNTOYCOMA','algoritmo',2,'p_algoritmo','sintaxis.py',20),
  ('algoritmo -> sentenciaIf','algoritmo',1,'p_algoritmo','sintaxis.py',21),
  ('sentenciaIf -> IF PIZQ comparacion PDER algoritmo','sentenciaIf',5,'p_sentenciaIf','sintaxis.py',25),
  ('sentenciaIf -> IF PIZQ comparacion PDER LIZQ algoritmo LDER','sentenciaIf',7,'p_sentenciaIf','sintaxis.py',26),
  ('imprimir -> PRINT PIZQ expresion PDER','imprimir',4,'p_imprimir','sintaxis.py',32),
  ('asignacion -> VARIABLE IGUAL expresion','asignacion',3,'p_asignacion','sintaxis.py',37),
  ('comparacion -> expresion operadorComp expresion','comparacion',3,'p_expresion_comparacion','sintaxis.py',42),
  ('operadorComp -> DIGUAL','operadorComp',1,'p_operadorComp','sintaxis.py',45),
  ('operadorComp -> NOIGUAL','operadorComp',1,'p_operadorComp','sintaxis.py',46),
  ('operadorComp -> MAYOR','operadorComp',1,'p_operadorComp','sintaxis.py',47),
  ('operadorComp -> MENOR','operadorComp',1,'p_operadorComp','sintaxis.py',48),
  ('operadorComp -> MAYIGUAL','operadorComp',1,'p_operadorComp','sintaxis.py',49),
  ('operadorComp -> MENIGUAL','operadorComp',1,'p_operadorComp','sintaxis.py',50),
  ('expresion -> valor','expresion',1,'p_expresion','sintaxis.py',56),
  ('valor -> ENTERO','valor',1,'p_valor','sintaxis.py',60),
  ('valor -> VARIABLE','valor',1,'p_valor','sintaxis.py',61),
  ('expresion -> valor operadorMat expresion','expresion',3,'p_expresion_aritmetica','sintaxis.py',67),
  ('operadorMat -> SUMA','operadorMat',1,'p_operadorMat','sintaxis.py',70),
  ('operadorMat -> RESTA','operadorMat',1,'p_operadorMat','sintaxis.py',71),
  ('operadorMat -> MULTI','operadorMat',1,'p_operadorMat','sintaxis.py',72),
  ('operadorMat -> DIV','operadorMat',1,'p_operadorMat','sintaxis.py',73),
  ('operadorMat -> DIVENTERO','operadorMat',1,'p_operadorMat','sintaxis.py',74),
  ('operadorMat -> MOD','operadorMat',1,'p_operadorMat','sintaxis.py',75),
]
