AÑO = int(input("Ingresa el año:"))
if (AÑO < 1582):
    print("No esta dentro del período del calendario Gregoriano")
else:
    if(AÑO%4 != 0):
        print("El año",AÑO,"es un año común.")
    elif(AÑO%100 !=0):
        print("El",AÑO,"es un año bisiesto.")
    elif(AÑO%400 != 0):
        print("El año",AÑO,"es un año común.")
    else:
        print("El año",AÑO,"es bisiesto.")