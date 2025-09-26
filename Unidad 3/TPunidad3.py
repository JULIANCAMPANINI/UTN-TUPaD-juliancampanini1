# 1
for i in range(101):
    print (i)

# 2 
num = int(input("Ingrese un número entero: "))
contador = len(str(abs(num)))
print("Cantidad de dígitos:", contador)

# 3 
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))
suma= 0

for i in range(num1, num2 + 1):
    suma += i 
print(f"La suma de entre los enteros es de {suma} ")

# 4
suma = 0

while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    suma += num

print("La suma total es:", suma)

# 5
import random

secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivine el número (0 a 9): "))
    intentos += 1
    if intento == secreto:
        break

print("¡Correcto! El número era", secreto)
print("Intentos realizados:", intentos)

#6
for i in range(100,-1,-2):
    print (i)

# 7
num = int(input("Ingrese un numero positivo: ")) 
suma = 0

for i in range(num + 1):
    suma += i 

print("la suma es de: ", suma)

# 8 
pares = impares = positivos = negativos = 0

for i in range(100):
    n = int(input(f"Ingrese el número {i+1}: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)


#9 
suma = 0 

for i in range(100):
    n = int(input(f"Ingrese el numero {i+1}: "))
    suma += n

media = suma / 100
print("La media es: ",media)


#10 
num = int(input("Ingrese un número: "))
invertido = int(str(num)[::-1])
print("Número invertido:", invertido)
