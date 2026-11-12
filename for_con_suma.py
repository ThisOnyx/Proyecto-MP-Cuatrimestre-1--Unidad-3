suma = 0 #si no definimos la suma como 0 el programa no sabra que numero tiene y no podra hacer la suma y al final siempre tomara el ultimo valor 

for i in range(1, 6): #inicia en el 1 y termina en el 6 pero no lo incluye, por eso en la terminal solo terminaria en 5
    suma = suma + i #la suma de cada numero se guarda en suma y se le va agregando el nuevo con "i"

print(suma) #el resultado de esa suma 