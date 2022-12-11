#!/usr/bin/env python


#-------------------- If Mayor ---------------------

a = 33    #:int
b = 200   #:int

if b > a: print("b is greater than a")

print("-----------------------------------------")


#-------------------- If Mayor ---------------------

a = 33
b = 200

if b > a:
  print("b is greater than a")

print("-----------------------------------------")


#a = 33
#b = 200

#if b > a:
#print("b is greater than a") # you will get an error

#print("-----------------------------------------")

#-------------------- If Mayor Else ---------------------

a = 200
b = 33

if b > a:
	print("b is greater than a")
else:
	print("b is not greater than a")
  

#-------------------- If Mayor Igual ---------------------

a = 33
b = 33

if b > a:
  print("b is greater than a")

elif a == b:
  print("a and b are equal")

print("-----------------------------------------")


#-------------------- If Mayor Igual Else ---------------------

a = 200
b = 33

if b > a:
  print("b is greater than a")

elif a == b:
  print("a and b are equal")

else:
  print("a is greater than b")

print("-----------------------------------------")



#-------------------- If Mayor And Mayor ---------------------
a = 200
b = 33
c = 500

if a > b and c > a:
	print("Both conditions are True")


#-------------------- If Mayor Or Mayor ---------------------
"""
a = 200
b = 33
c = 500
"""

a,b,c = 200,33,500

if a > b or a > c:
	print("At least one of the conditions is True")

#------------------------------- Ternario --------------------
impuesto = 0.0    #:float
tipo="NORMAL"     #:str

impuesto = 0.14 if tipo=="NORMAL" else 0.0

print("UPDATED: Impuesto Final",impuesto)
