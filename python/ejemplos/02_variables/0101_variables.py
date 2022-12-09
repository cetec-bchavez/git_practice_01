#!/usr/bin/env python
"""
---- TIPOS ----
Datos Inmutables (id()) y Simples
* int,float,bool,(str -> Ojo),char,datetime,bytes

Datos Mutables(id()) y Compuestos
* String,List[int],Set[int],Dict[str, float],Tuple[int, str, float]

Mutalbes por Valor --> Casi todos
Inmutables por Valor --> Tuplas,String
"""
#-------------------- General ---------------------
x = 5   #int(),x:int 
y = "John"  #str(),y:str
print(x)
print(y)
print(id(x))
print(id(y))
print("---------------------------------------------------")

#-------------------- Cambio Tipo Dinamico ------------

x = 4 # x is of type int, :int
x = "Sally" # x is now of type str
print(x)
print("-------------------------------")

#-------------------- General ---------------------
x = "awesome"   #str()
print("Python is " + x)
print("-------------------------------")

#-------------------- General ---------------------

x = "awesome"
y = "Python is " + x
print(y)
print("-------------------------------")


#-------------------- Calculo ---------------------

x = 5   #int()
y = 10  #int()
print(x + y)
print("-------------------------------")

#------------Error de Tipos --------------
"""
x = 5
y = "John"
print(x + y)
"""

#----------- Multiple -------------------
nota1,nota2,promedio = 6.5,8.5,0.0

promedio = (nota1 + nota2)/2

print("Promedio=",promedio)