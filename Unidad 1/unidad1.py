#Trabajo practico unidad 1


#1
print("hola mundo!")


#2
nombre = input("hola ingrese su nombre ")

print(f"Hola {nombre}!")


#3
nombre=input("ingrese su nombre: ")
edad=input("ingrese su edad: ")
residencia=input("ingrese su recidencia: ")
apellido=input("ingrese su apellido: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#4
radio=float(input("ingrese radio: "))
pi = 3.14
area = pi * radio ** 2
perimetro=2*pi*radio

print(f"el perimetro es de {perimetro}, y el area de {area}")


#5
segundos=float(input("ingrese la cantidad de segundos: "))
hora = segundos / 3600

print(f"La cantidad de horas es de: {hora}")


#6
numero=float(input("ingrese un numero: "))

print(f"{numero} * 1 = {numero * 1}")
print(f"{numero} * 2 = {numero * 2}")
print(f"{numero} * 3 = {numero * 3}")
print(f"{numero} * 4 = {numero * 4}")
print(f"{numero} * 5= {numero * 5}")
print(f"{numero} * 6 = {numero * 6}")
print(f"{numero} * 7 = {numero * 7}")
print(f"{numero} * 8 = {numero * 8}")
print(f"{numero} * 9 = {numero * 9}")
print(f"{numero} * 10= {numero *10}")


#7
numerouno=float(input("ingrese un numero: "))
numerodos=float(input("ingrese otro numero: "))

numerouno != 0
numerodos != 0

print(f"la suma entre los numeros es de {numerouno+numerodos}")
print(f"la resta entre los numeros es de {numerouno-numerodos}")
print(f"la multiplicion entre los numeros es de {numerouno*numerodos}")
print(f"la division entre los numeros es de {numerouno/numerodos}")


#8
altura=float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc= peso / (altura ** 2)

print(f"El indice de masa corporal es de {imc}")


#9
tempcelcius=float(input("ingrese la temperatura en grados celcius: "))
tempfare=(9/5*tempcelcius)+32
print(f"La temperatura en grados Fahrenheit es de: {tempfare}")


#10
numerouno= float(input("ingrese el primer numero: "))
numerodos= float(input("ingrese el segundo numero: "))
numerotres= float(input("ingrese el tercer numero: "))
promedio = (numerouno+numerodos+numerotres)/3

print(f"el promedio es de {promedio}")