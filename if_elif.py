temperatura = 85

if temperatura < 60:
    print("Motor frío")
elif temperatura <= 90: #elif sirve para poner otro mensaje en caso de que el if no se cumpla, es como decir "si pero".
    print("Temperatura normal")
else:
    print("Sobrecalentamiento")