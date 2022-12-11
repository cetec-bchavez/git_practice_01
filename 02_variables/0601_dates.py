#!/usr/bin/env python

import datetime

#-------------------------- Fecha/Hora --------------------------

x = datetime.datetime.now()     #:datetime
print(x)

print("----------------------------------------")


#-------------------------- Anio/Dia --------------------------

print(x.year)
print(x.strftime("%A"))

print("----------------------------------------")

#-------------------------- Fecha Manual --------------------------

x = datetime.datetime(2020, 5, 17)
print(x)

print("----------------------------------------")


#-------------------------- Mes --------------------------
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
