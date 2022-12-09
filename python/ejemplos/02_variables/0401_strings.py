#!/usr/bin/env python

#--------------------------- Caracter ------------------------

a = "hello"     #:str
print(a[1])
print("---------------------------------------------------")
#--------------------------- Substring (Slice/Rebanada) ------------------------
#inicio: indice Inicio, incluyente
#fin: indice Fin, no incluyente

b = "world"     #:str
print(b[2:5])
print(b[2:])
print(b[:5])
print(b[:]) #Copia
print(b[2:5:1]) #:salto
print("---------------------------------------------------")
#---------------------------- Caracteres -----------------------

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
print("---------------------------------------------------")

#----------------------------- Tamanio ----------------------
a = "Hello, World!"
print(len(a))
print("---------------------------------------------------")

#------------------------------ Minusculas (Copia) ---------------------
a = "Hello, World!"
print(a.lower())
print("---------------------------------------------------")

#------------------------------- Mayusculas (Copia) --------------------
a = "Hello, World!"
print(a.upper())
print("---------------------------------------------------")

#------------------------------- Capitalize (Copia) --------------------
a = "Hello, World!"
print(a.capitalize())
print("---------------------------------------------------")

#-------------------------------- Reemplazar -------------------
a = "Hello, World!"
print(a.replace("H", "J"))
print("---------------------------------------------------")

#--------------------------------- A Arreglo/Lista ------------------
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
print("---------------------------------------------------")
#---------------------------------------------------

#-------------------------------- Ingresar por Pantalla -------------------
#Ingresar ByDan
print("Enter your name:")
x = input()
print(type(x))
print("Hello, " + x)

#-------------------------------- Strip -------------------
a = "    abc def     hgq asdfaf     "
b = a.strip()
print(b)

#find
#index
#isdigit
#isdedimal
#isalnum
#islower

