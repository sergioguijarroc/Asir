an1=int(input("Escribe el año actual "))
an2=int(input("Escribe el segundo año "))
if an1>an2:
    resto=an1-an2
    print(f"Desde el año {an2} al año {an1} han pasado {resto} años")
elif an2>an1:
    resto=an2-an1
    print(f"quedan {resto} años para llegar al año {an2}")
elif an1-1==an2 or an1+1==an2:
    print("Hay un año de diferencia entre los dos años")
else:
    print("Error, introduce de nuevo los valores")
    

