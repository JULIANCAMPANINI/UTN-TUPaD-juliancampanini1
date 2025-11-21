# ==============================================================================
# EJERCICIO 1: FACTORIAL (Recursividad)
# Función para calcular el factorial usando llamadas recursivas
def calcular_factorial(num):
    # Caso base: El factorial de 0 es 1.
    return 1 if num == 0 else num * calcular_factorial(num - 1)

# Programa principal: Muestra el factorial de los números hasta el límite N.
limite_n = int(input("Ingrese un número límite N: "))
print(f"\nCalculando factoriales hasta {limite_n}:")
for i in range(1, limite_n + 1):
    # Llama a la función y muestra el resultado en lazo (loop)
    print(f"El factorial de {i} es: {calcular_factorial(i)}")
# ==============================================================================


# ==============================================================================
# EJERCICIO 2: SERIE DE FIBONACCI (Recursividad)
# Función recursiva para obtener el valor de Fibonacci en la posición 'n'
def serie_fibo(n):
    # Caso base 1: Posición 0 es 0.
    if n == 0:
        return 0
    # Caso base 2: Posición 1 es 1.
    elif n == 1:
        return 1
    # Paso recursivo: La suma de las dos posiciones anteriores.
    else:
        return serie_fibo(n - 1) + serie_fibo(n - 2)
    
pos_final = int(input("\nIngrese la posición final para la serie de Fibonacci: "))

print(f"Serie completa hasta la posición {pos_final}:")
for i in range(pos_final + 1):
    # Itera e imprime cada valor de la serie.
    print(f"{i}: {serie_fibo(i)}")
# ==============================================================================


# ==============================================================================
# EJERCICIO 3: POTENCIA (Recursividad)
# Función recursiva para calcular la potencia (base^exponente)
def calc_potencia(base, exponente):
    # Caso base: Cualquier número elevado a la 0 es 1.
    if exponente == 0:     
        return 1
    # Paso recursivo: Multiplica la base por la potencia de (exponente - 1).
    else:           
        return base * calc_potencia(base, exponente - 1)

# Algoritmo principal
valor_base = int(input("\nIngrese la base numérica: "))
valor_exp = int(input("Ingrese el exponente: "))

res_potencia = calc_potencia(valor_base, valor_exp)
print(f"{valor_base} elevado a la {valor_exp} da como resultado: {res_potencia}")
# ==============================================================================


# ==============================================================================
# EJERCICIO 4: DECIMAL A BINARIO (Recursividad)
# Función recursiva para la conversión de base 10 a base 2
def decimal_a_bin(numero_dec):
    # Casos base para 0 y 1.
    if numero_dec == 0:
        return "0"
    elif numero_dec == 1:
        return "1"
    # Paso recursivo: Llama a la función con la división entera (cociente) y concatena el resto (residuo).
    else:
        cociente = numero_dec // 2
        residuo = numero_dec % 2
        return decimal_a_bin(cociente) + str(residuo)

# Inicia el programa
n_dec = int(input("\nIngrese un número entero positivo para convertir a binario: "))
if n_dec < 0:
    print("Error: Ingrese un número positivo.")
else:
    conversion_binaria = decimal_a_bin(n_dec)
    print(f"El valor {n_dec} en formato binario es: {conversion_binaria}")
# ==============================================================================


# ==============================================================================
# EJERCICIO 5: PALÍNDROMO (Recursividad)
# Función recursiva para verificar si una palabra es palíndromo
def verificar_palindromo(palabra_check):
    # Caso base 1: Si la longitud es 0 o 1, siempre es palíndromo (la recursión se detiene).
    if len(palabra_check) <= 1:
        return True
    # Caso base 2: Si los caracteres de los extremos no coinciden, no es palíndromo.
    elif palabra_check[0] != palabra_check[-1]:
        return False
    # Paso recursivo: Llama a la función con la subcadena que excluye el primer y último carácter.
    else:
        return verificar_palindromo(palabra_check[1:-1])

# Ejecución
texto_entrada = input("\nIngrese una palabra para verificar si es palíndromo: ").lower()

if verificar_palindromo(texto_entrada):
    print(f'"{texto_entrada}" es un palíndromo (se lee igual al derecho y al revés).')
else:
    print(f'"{texto_entrada}" no es un palíndromo.')
# ==============================================================================


# ==============================================================================
# EJERCICIO 6: SUMA DE DÍGITOS (Recursividad Matemática)
# Función recursiva para sumar los dígitos de un número entero (solo con aritmética)
def sumar_digitos_num(numero):
    # Caso base: Si el número es menor a 10 (un solo dígito), el resultado es el número mismo.
    if numero < 10:
        return numero
    # Paso recursivo: Suma el último dígito (residuo) y llama a la función con el resto del número (cociente).
    else:
        ultimo_digito = numero % 10
        resto_del_numero = numero // 10
        return ultimo_digito + sumar_digitos_num(resto_del_numero)

# Lógica principal
valor_input = int(input("\nIngrese un valor para sumar sus dígitos: "))
suma_total = sumar_digitos_num(valor_input)
print(f"La suma total de los dígitos de {valor_input} es: {suma_total}")
# ==============================================================================


# ==============================================================================
# EJERCICIO 7: PIRÁMIDE DE BLOQUES (Recursividad Suma Progresiva)
# Función recursiva para calcular el total de bloques
def calcular_total_bloques(nivel_n):
    # Caso base: El último nivel siempre tiene 1 bloque.
    if nivel_n == 1:
        return 1
    # Paso recursivo: Suma el nivel actual y llama a la función para el nivel superior (n - 1).
    else:
        return nivel_n + calcular_total_bloques(nivel_n - 1)

niveles_piramide = int(input("\nIngrese la cantidad de bloques en el nivel más bajo (Niveles totales): "))
total_bloques = calcular_total_bloques(niveles_piramide)

print(f"Para construir una pirámide con {niveles_piramide} niveles se necesitan {total_bloques} bloques en total.")
# ==============================================================================


# ==============================================================================
# EJERCICIO 8: CONTAR DÍGITO ESPECÍFICO (Recursividad)
# Función recursiva para contar un dígito dentro de un número
def contar_coincidencias(numero, digito_buscado):
    # Caso base: Cuando queda un solo dígito.
    if numero < 10:
        # Retorna 1 si el único dígito coincide, 0 si no.
        return 1 if numero == digito_buscado else 0
    # Paso recursivo:
    else:
        ultimo_digito = numero % 10
        # Determina si el último dígito coincide (1 o 0).
        coincidencia_actual = 1 if ultimo_digito == digito_buscado else 0
        # Suma la coincidencia actual y llama a la función con el resto del número (n // 10).
        resto_del_numero = numero // 10
        return coincidencia_actual + contar_coincidencias(resto_del_numero, digito_buscado)

# Bloque de ejecución principal
valor_num = int(input("\nIngrese el número grande para buscar: "))
valor_digito = int(input("Ingrese el dígito a contar (0-9): "))

contador_final = contar_coincidencias(valor_num, valor_digito)
print(f"El dígito {valor_digito} aparece un total de {contador_final} veces en el número {valor_num}.")
# ==============================================================================
