A = input("Ingresa un número:")
New_A = float(A)
if (New_A != 10):
    print("El numero no es 10\n""El numero es", New_A)
elif (New_A == 1):
    print("El numero es 1")
else: 
    print("El numero es", New_A)


A1 = input("Ingrese el número 1:")
A2 = input("Ingrese el número 2:")
New_A1 = float(A1)
New_A2 = float(A2)
Answer_1 = New_A1 > New_A2
Answer_2 = New_A1 < New_A2
Answer_3 = New_A1 == New_A2
QUESTION = input("Ingrese la pregunta:")
New_Q = str(QUESTION)
if(New_Q == "Quien es mayor?"):
    print("El numero",New_A1,"es mayor, la respuesta es",Answer_1)
elif (New_Q == "Quien es menor?"):
    print(("El numero",New_A1,"es menor, la respuesta es",Answer_2))
elif ((New_Q == "Son iguales?")):
    print("Los números son iguales, respuesta es",Answer_3)
else:
    print("Datos mal ingresados")

n = float(input("Ingrese los datos:"))
print(n >= 100)
