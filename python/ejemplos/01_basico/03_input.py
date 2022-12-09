#entered data treated as string with or without ''
#SIEMPRE retorna String o Caracteres

#-------------------------- General --------------------------
x = input("something:")

print(type(x))

print(x)



#-------------------------- Enteros --------------------------

lado = input("Lado:")
alto = input("Alto:")

perimetro = 2*lado + 2*alto

#lado= int(slado)
#alto= int(salto)

#sperimetro = str(perimetro)

print("Perimetro =",perimetro)