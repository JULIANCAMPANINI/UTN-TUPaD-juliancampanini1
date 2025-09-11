# 1 

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")

# 2

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Esta aprobado")
else:
    print("Esta desaprobado")

# 3

num = int(print("Ingrese un numero"))
if num % 2 == 0:
    print("Su numero es par")
else:
    print("Ingrese un numero par")

# 4 
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto joven")
elif edad >= 30:
    print("Adulto")


# 5 

contrasenia = input("Ingrese contraseña de 8 a 14 caracteres: ")

if 8 <= len(contrasenia) <= 14:
    print("HA ingresado una contraseña correcta")
else:
    print("Ha ingresado una contraseña incorrecta")


# 6 
import random
from statistics import mode, mean, median
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

print(f"moda: {moda}")
print(f"media: {media}")
print(f"mediana: {mediana}")

if media > mediana and mediana > moda:
    print("Su sezgo es  positivo")
elif media < mediana and mediana < moda:
    print("Su sezgo es negativo")
elif media == moda == mediana:
    print("Sin sezgo")
else:
    print("La distribución no cumple con los criterios de sesgo definidos")


# 7 
frase = input("Ingrese la frase")
vocales = "aeiouAEIOU"

ultima_letra = frase[-1]

if ultima_letra in vocales:
    frase = frase + "!"

print(f"Resultado: {frase}")


# 8

nombre = input("ingrese su nombre: ")
num = int(input("Ingrese un numero del 1 al 3: "))

if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
elif num == 3:
    print(nombre.title())
else:
    print("Ingrese un numero del 1 al 3")


# 9

magnitud = float(input("Ingrese el numero de magnitud del terremoto: "))

if magnitud <3:
    print("Muy leve (imperceptible)") 
elif magnitud >= 3 and magnitud < 4:
    print("Leve (Ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (Sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5  and magnitud < 6:
    print("Fuerte (Puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (Puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (Puede causar  graves daños a gran escala)")

#10
hemisferio = input("Ingrese en que hemisferio se encuentra N/S: ").upper
dia = int(input("ingrese el dia del mes: "))
mes = int(input("Ingrese el mes: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2  or ( mes == 3 and dia <= 20 ):
        print("Estas en invierno")
    elif (mes == 3 and dia >= 21 ) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("estas en primavera")
    elif (mes == 6 and dia >= 21 ) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Estas en verano")
    else:
        print("Estas en otoño")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2  or ( mes == 3 and dia <= 20 ):
        print("Estas en verano")
    elif (mes == 3 and dia >= 21 ) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("estas en otoño")
    elif (mes == 6 and dia >= 21 ) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Estas en invierno")
    else:
        print("Estas en primavera")