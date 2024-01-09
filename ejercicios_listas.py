"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas
, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje 
Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
"""

asignaturas_1 = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for asignatura_1 in asignaturas_1:
    print("Yo estudio " + asignatura_1)

"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha 
sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura>
has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> 
cada una de las correspondientes notas introducidas por el usuario.
""" 
asignaturas_2 = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for asignatura_2 in asignaturas_2:
    nota = int(input("Que nota sacaste en " + asignatura_2 + "?\n"))
    print("En " + asignatura_2 + " has sacado", nota)