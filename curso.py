#asignacion de variables

number_1 = 22
number_2 = 10
last_name = "lara"
LastName = "laraa"
#operaciones
suma = number_1 + number_2
resta = number_1 - number_2
multi = number_2 * number_1
div = number_1 / number_2

# #resultados
# print (suma)
# print (resta)
# print (multi)
# print (div)

print ("resultado de la resta: ", resta)
print (f"resultado de la resta es: {resta}")
#(de esta forma se ultiliza mas)
print (f"resultado de la multiplicacion es: {multi}")

#tipos de datos 
print (type(last_name))
print (type(suma))
print (type(multi))

#ingreso de datos por teclado 

name_1 = input ("nombre: ")
print ("hola", name_1)

#asignacion de variables
#cambio de datos de str a int, float
number_1 = input("ingrese numero 1:")
number_1 = float (number_1)

number_2 = input("ingrese numero 2:")
number_2 = float(number_2)

#operaciones
suma = number_1 + number_2

print (f"el resultado de la suma es:{suma}")