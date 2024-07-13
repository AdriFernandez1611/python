
#TUPLAS
#es un dato inmutable, no se puee cambiar ss datos
tupla_1 = (1, 2, 3, 4, 5)
tupla_2 = ("a", "e", "i", "o", "u")

#diccionario
# es una combinacion clave\valor

dict_1 = {
    "luis": 1234,
    "pedro" : 5678,
    "juan" : 8910,
}

#acceder diccionarios es
print( dict_1 ["luis"] )

dict_2 = {
    "frutas": ["manzana", "pera", "melon"],
    'numeros' : [12, 13, 23],
    "pesos": [1.5, 2, 3.7, 4, 5]
}

#CICLOS FINITOS FOR

# sintaxis:
#for variable in [secuencia]:
#        cuerpo del ciclo


name_list =  ["jose", "maria", "juan", 'ruperto']
# for name in name_list:
#     print (name)
    

for name in name_list: 
     if (name == "jose"):
         print (f'"{name}" es el papa')
     else:
         print (f"{name} no es papa")

#funciones
#sintaxis de una fincion en pytohn

# def name function (parametros):
#             documenta cion de la funcio
#   codigo de ka funcion

#FUNCION PARA SUMAR DOS NUMEROS

def suma_dos(num_1, num_2):
    """_esta funcion suma dos numeros enteros
    Args:
        num_1 (_type_): int
        num_2 (_type_): int
        return salida: int
    """
    result = num_1 = num_2
    return result

suma_dos(12, 12)

def resta_dos (num_1, num_2):
    result = num_1 - num_2
    return result

resta_dos(num_2=23, num_1=20)

print 