i= 0    #:int
j= 0    #:int

print("--------------------- GLOBAL ---------------")

def sumar_global() :    #-> None
    #global i,j
    k = 0   #:int
    k = i + j

    print("Resultado", k)


i=100
j=200

sumar_global()


print("--------------------- LOCAL ---------------")

def sumar_local(x,y) :  #:int, -> None 
    r=0
    r = x + y + i

    print("Resultado", r)

sumar_local(10,20)