print("--------------------------- DEFINIR VARIABLES -----------------------------")

# Definicion de variables

#Constantes
IVA = 0.14 #float(, IVA:float

#Ingresados por Usuario
producto = ""   #str(, producto:str
cantidad = 0    #int(, cantidad:int
precio = 0.0    #precio:float

#Automaticas
sutotal = 0.0
total = 0.0


print("--------------------------- INGRESO DE DATOS -----------------------------")

# Ingreso de Datos

# Siempre son Textos o String
producto = input("Ingrese Producto: ")
cantidad = input("Ingrese Cantidad: ")
precio = input("Ingrese Precio: ")

print("--------------------------- PROCESAR DATOS -----------------------------")

# Procesar Calculos

#Convertir cantidad y precio a entero y decimal respectivamente
subtotal= int(cantidad) * float(precio);

total = subtotal + (subtotal * IVA)

# Mostrar Resultados

print("--------------------------- MOSTRAR TOTALES -----------------------------")

print("Producto:",producto)
print("Cantidad:",cantidad)
print("Precio:",precio)
print("Total:",total)