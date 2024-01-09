numbers = [54, 102, 62, 177]
#Numbers es una lista que consta de 5 valores
#Numbers is a list consting of five values

#Nuevo valor en la lista
#New value in the list
numbers_1 = [102, 54, 56, 89, 1000]

numbers_1[0] = 1000

print(numbers_1)
print("La longitud de la lista número 1 es de:", len(numbers_1))

#Copiar el valor del quinto elemento al segundo elemento
#Copy the value of the fifth element to the second element

#Índice - index
numbers_2 = [500, 41, 65, 89, 100]

#Indexación - indexation
numbers_2[4] = numbers_2[1]

print(numbers_2)

#Acceso al contenido de las listas
#Access to the contents of the lists

print(numbers_2[0])
print(numbers_2[1])
print(numbers_2[2])
print(numbers_2[3])
print(numbers_2[4])

print("La longitud de la lista número 2 es de:", len(numbers_2))

#La función LEN nos permite saber el número de elementos de la lista
#The LEN fuction allows us to know the number of element in the list

numbers_3 = [200, 21, 32, 41, 51, 51, 32, 41, 100]
print("La longitud de la lista número 3 es de:", len(numbers_3))

#Eliminar elementos de una lista
#Delete elements from a list

numbers_4 = [10, 21, 32, 41, 561]
del numbers_4[0]

print(numbers_4)
print("La longitud de la lista número 4 es de:", len(numbers_4))

#Los índices negativos son legales
#Negatives rates are legal

numbers_5 = [100, 51, 21, 32, 45, 564]

#Un elemento con un índice igual a -1 es el último en la lista
#An element with an index equal to -1 is the last in the list

print(numbers_5[-1])
print(numbers_5[-2])
print(numbers_5[-3])