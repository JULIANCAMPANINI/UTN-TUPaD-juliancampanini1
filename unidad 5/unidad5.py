#1 
notas = [10, 9, 8, 5, 6, 3, 2, 4, 5, 1]
print("las notas son: ")
promedio = sum(notas) / len(notas)
print("El promedio de las notas es de: ", promedio)

print("La nota mas alta es de: ", max(notas))
print("La nota mas baja es de: ", min(notas))

#2 
productos = []


for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)


productos_ordenados = sorted(productos)
print("Lista de productos ordenada alfabéticamente:", productos_ordenados)


eliminar = input("Ingrese el nombre del producto que desea eliminar: ")


if eliminar in productos:
    productos.remove(eliminar)
    print("Producto eliminado. Lista actualizada:", productos)
else:
    print("El producto no se encuentra en la lista.")


#3 
import random

numeros= [random.randint(1,100) for _ in range(15)]

print(numeros)

pares = []
impares = []

for numero in numeros:
    if numero % 2==0: 
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Números impares:", impares)
print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))

#4 

datos = [1, 3, 5, 3, 7, 1,9,5,3]
lista_sinrepetidos = []

for numero in datos:
    if numero not in lista_sinrepetidos:
        lista_sinrepetidos.append(numero)

print(lista_sinrepetidos)


#5 
estudiantes = ["Julian", "Agustin", "Paula", "Milagros", "Diego", "Carla", "Joaquin", "Thiago"]
menu = (int(input("1para agregar estudiantes o 2 para eliminar")))
                       
if menu == 1:
  est1 = (str(input("Ingrese el nombre del estudiante que quiere agregar: ")))
  if est1 in estudiantes: 
      print("El estudiante ya esta en la lista")
  else:
      estudiantes.append(est1)
else:
 est2=  (str(input("Ingrese el nombre del estudiante que quiere eliminar: ")))
 if est2 in estudiantes:
     estudiantes.remove(est2)

print(estudiantes)
     
# 6
numeros = [1,2,3,4,5,6,7]

ultimo = numeros[-1]
numeros=[ultimo] + numeros[:-1]

print(numeros)

#7 

temperaturas = [
    [20, 25],
    [24, 28],
    [24, 20],
    [21, 26],
    [15, 24],
    [26, 28],
]

minimas= [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]

minimas_prom = sum(minimas) / len(minimas)
maximas_prom = sum(maximas) / len(minimas)

print("Promedio de temperaturas mínimas:", minimas_prom)
print("Promedio de temperaturas máximas:", maximas_prom)

amplitudes = [dia[0] - dia[1] for dia in temperaturas] 

mayor_amplitud = max(amplitudes)
dia_mayor_amplitud = amplitudes.index(mayor_amplitud)

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("La mayor amplitud térmica fue de", mayor_amplitud, "°C y ocurrió el día", dias_semana[dia_mayor_amplitud])


# 8

notas = [
    [7, 8, 6],   
    [9, 6, 7],  
    [5, 7, 8],   
    [8, 9, 9],   
    [6, 5, 7]    
]


print("Promedio de cada estudiante:")
for i, estudiante in enumerate(notas, start=1):
    promedio_est = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i}: {promedio_est:.2f}")

print("\nPromedio de cada materia:")
num_materias = len(notas[0])
for j in range(num_materias):
    suma = sum(notas[i][j] for i in range(len(notas)))
    promedio_mat = suma / len(notas)
    print(f"Materia {j+1}: {promedio_mat:.2f}")


# 9 

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()


turno = "X"
for _ in range(5):  
    mostrar_tablero()
    print(f"Turno del jugador {turno}")
    fila = int(input("Ingrese la fila (0-2): "))
    col = int(input("Ingrese la columna (0-2): "))
    
    if tablero[fila][col] == "-":
        tablero[fila][col] = turno
        turno = "O" if turno == "X" else "X"  
    else:
        print("Esa casilla ya está ocupada, intente de nuevo.")

mostrar_tablero()

#10
ventas = [
    [10, 12, 8, 9, 15, 7, 11],   
    [5, 7, 6, 10, 9, 8, 12],     
    [20, 18, 22, 25, 19, 21, 23],
    [8, 9, 7, 6, 10, 12, 11]     
]


print("Total vendido por producto:")
for i, producto in enumerate(ventas, start=1):
    total_prod = sum(producto)
    print(f"Producto {i}: {total_prod}")


ventas_por_dia = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
dia_max = ventas_por_dia.index(max(ventas_por_dia)) + 1
print("\nEl día con mayores ventas fue el día", dia_max, "con", max(ventas_por_dia), "ventas")


totales = [sum(prod) for prod in ventas]
producto_max = totales.index(max(totales)) + 1
print("El producto más vendido en la semana fue el Producto", producto_max)
