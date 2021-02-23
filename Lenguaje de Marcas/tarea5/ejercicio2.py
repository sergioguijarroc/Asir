from random import randint
a=randint(2,10)
b=randint(2,10)
num_mul=int(input("¿Cúantas multiplicaciones vas a hacer? "))
contador=0
acertadas=0
acum=0

while contador!=num_mul:
    contador=contador+1
    
    a=randint(2,10)
    b=randint(2,10)
    multiplicacion=a*b
    print(f"¿Cual es el resultado de {a}x{b}?")
    resultado=int(input("Dime el resultado de esa multiplicación "))
    if resultado==multiplicacion:
        acertadas=acertadas+1
        print("¡Respuesta correcta!")
    else:
        print("Respuesta incorrecta")
total=acertadas/contador*10
if total>=9:
    print(f"Enhorabuena, ha sacado un pedazo de {total}")
else:
    print(f"Su nota es de {total}")