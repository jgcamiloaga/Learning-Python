print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
#En break se rompe la secuencia
#Hasta el valor que no cumpla la restriccion


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
#En continue sigue la secuencia 
#Pero se omite el valor que no cumple la restriccion