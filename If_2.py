ingreso = float(input("Inserta tu número de ingresos:"))
if (ingreso <= 85528):
    INP = (ingreso*18)/100
    INP_FINAL = INP - 556.2
else:
    INP = ingreso - 85528
    INP_FINAL = ((INP*32)/100 + 14839.2)

RESULTADO = round(INP_FINAL,0)
if(RESULTADO <=0):
    RESULTADO = 0

print("El impuesto a pagar es",RESULTADO) 