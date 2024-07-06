# #asignacion de variables

# number_1 = 22
# number_2 = 10
# last_name = "lara"
# LastName = "laraa"
# #operaciones
# suma = number_1 + number_2
# resta = number_1 - number_2
# multi = number_2 * number_1
# div = number_1 / number_2

# # #resultados
# # print (suma)
# # print (resta)
# # print (multi)
# # print (div)

# print ("resultado de la resta: ", resta)
# print (f"resultado de la resta es: {resta}")
# #(de esta forma se ultiliza mas)
# print (f"resultado de la multiplicacion es: {multi}")

# #tipos de datos 
# print (type(last_name))
# print (type(suma))
# print (type(multi))

# #ingreso de datos por teclado 

# name_1 = input ("nombre: ")
# print ("hola", name_1)

# #asignacion de variables
# #cambio de datos de str a int, float
# number_1 = input("ingrese numero 1:")
# number_1 = float (number_1)

#number_2 = input("ingrese numero 2:")
#number_2 = float(number_2)

##operaciones
#suma = number_1 + number_2

# print (f"el resultado de la suma es:{suma}")

# #listas, nueva estructura de datos 
# #de izquierda a derecha comienza con 0 y de derecha a izquierda -1)
# list_1 = ["jose", "maria", "juan", 'ruperto', 12, 14, 15, 90.2, 78.5, 1.2]

# print (list_1)

# #la forma de acceder a la lista, com el indice

# print (list_1 [2])

#extraer los datos que quiera, varios datos
#[star:stop] stop se come una asi que hay que agragar una mas
# print (list_1 [0:4])

# #extraer lo que hay en la lista
# name_list = (list_1 [0:4])
# int_list = (list_1 [4:7])
# float_list = (list_1 [-3:])
# # print(int_list)

# # operaciones basicas hechsas con listas
# #agregar elemento a litas
# float_list.append(55.5)

# # print(float_list)

# #limpiar lista
# int_list.clear()

# #copiar lista
# name_list_2 = name_list.copy()

# #cantida de elementos de la lita
# len(name_list_2)

# #
# print(name_list_2)




#condicionales
#sintaxis de un condicional simple
#if condicion: 
# #operacion
#mayor que >
# menor que<
# igual =
#mayor igual que >=
#menor igual que <=
#difierente que !=
#igual a ==

# day = input("dia de la semana: ")
# if day == 'lunes':
#     print ("no, hoy es lunes, a trabajar")
# else:
#     print("no es lunes, a mimir")


#operadores logivcos
#and y or
#con and las dos condiciones se debn cumplis si o si
#or es para que se cumpla uno de los dos
day = input("dia de la semana: ")
momento = input("ingrese momento del dia:") 
if (day == 'lunes') or (momento == 'noche'):
    print ("a ver pelis")
else:
    print("no es lunes, a mimir")
    



#TAREA DOS JUGADORES, PLAYER UNO PLAYER DOS, PIEDRA PAPEL O TIJERA