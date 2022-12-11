#!/usr/bin/env python

#--------------------- General ------------------

x = 1    # int,:int
y = 2.8  # float,:float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
print("----------------------------------")

#--------------------- Enteros -----------------------

x = 1 #:int
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
print("----------------------------------")

#----------------------- Decimales -------------------------

x = 1.10 			#:float
y = 1.0		#:float
z = -35.59	#:float

print(type(x))
print(type(y))
print(type(z))
print("----------------------------------")

#------------------------- Decimales 2 -----------------------------


x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
print("----------------------------------")

#------------------------- Complejos -------------------

x = 3+5j	#:complex
y = 5j		#:complex
z = -5j		#:complex

print(type(x))
print(type(y))
print(type(z))

#------------------------- Error Nombre (@*/) -------------------
#7name=10

if(isinstance(5, int)):
	print("5 es int")
