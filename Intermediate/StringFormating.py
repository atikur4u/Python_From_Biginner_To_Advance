import math

me = "Harry"
a1 = 3

"""First Format string example"""
# a = "THis is {1} {0}"  # Here {num} indicate what to print first
# b = a.format(me, a1)
# print(b)

"""second format string example"""
a = f"this is {me} {a1} {math.cos(65)}"
print(a)
