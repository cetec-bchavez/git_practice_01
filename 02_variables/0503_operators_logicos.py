#!/usr/bin/env python

#----------------------------COMPARACION------------------------

#-------------------------- Igualdad --------------------------
x = 5   #:int
y = 3   #:int
print(x == y)
# returns False because 5 is not equal to 3
print("-----------------------------------------")

#-------------------------- Desigualdad --------------------------
x = 5
y = 3
print(x != y)
# returns True because 5 is not equal to 3
print("-----------------------------------------")

"""
x = 5
y = 3
print(x <> y)
# returns True because 5 is not equal to 3
print("-----------------------------------------")
"""

#-------------------------- Mayor --------------------------
x = 5
y = 3
print(x > y)
# returns True because 5 is greater than 3
print("-----------------------------------------")

#-------------------------- Menor --------------------------
x = 5
y = 3
print(x < y)
# returns False because 5 is not less than 3
print("-----------------------------------------")

#-------------------------- Mayor Igual --------------------------

x = 5
y = 3
print(x >= y)
# returns True because five is greater, or equal, to 3
print("-----------------------------------------")

#-------------------------- Menor Igual --------------------------
x = 5
y = 3
print(x <= y)
# returns False because 5 is neither less than or equal to 3
print("-----------------------------------------")


#---------------------------- Mayor/Menor and LOGICAL------------------------

x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10
print("-----------------------------------------")

#---------------------------- Mayor/Menor or LOGICAL------------------------
x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
print("-----------------------------------------")

#---------------------------- NOT Mayor/Menor & LOGICAL------------------------

x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result
print("-----------------------------------------")


#----------------------------IDENTITY (is) ------------------------

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have thew same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print("-----------------------------------------")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

"""
print(x <> y)
# to demonstrate the difference betweeen "is not" and "<>": this comparison returns False because x is equal to y
print("-----------------------------------------")
"""

#----------------------------MIEMBROS LIST/ARRAY (in) ------------------------

x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
print("-----------------------------------------")

x = ["apple", "banana"]
print("UPDATED: pineapple" not in x)
# returns True because a sequence with the value "pineapple" is noot in the list
print("-----------------------------------------")

