num1 = int(input("Dime un número entero"))
num2 = int(input("Dime otro número entero"))
while num1 <= num2:
    print(f"el número {num2} es mayor que {num1} , inténtalo de nuevo ")
    num1 = int(input("Dime otra vez un número entero"))
    num2 = int(input("Dime otro número entero"))
for i in range(num1,num2):
    print(f"Estos son los números que están comprendidos entre{num1} y {num2} {i})

