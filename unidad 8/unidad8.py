NOMBRE_ARCHIVO = "productos.txt"

def cargar_y_mostrar_productos():
    productos = []
    print("--- Mostrando Productos Actuales (Act 2) ---")
    
    with open(NOMBRE_ARCHIVO, 'r') as f:
        for linea in f:
            linea_limpia = linea.strip() 
            
            if linea_limpia:
                partes = linea_limpia.split(",") 
                
                nombre = partes[0]
                precio = float(partes[1])
                cantidad = int(partes[2])
                
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
                
                producto_dict = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
                productos.append(producto_dict)

    print("\n--- Carga en lista de diccionarios completada (Act 4) ---")
    return productos

def agregar_producto(lista_productos):
    print("\n--- Agregar Nuevo Producto (Act 3) ---")
    
    nombre = input("Ingrese nombre del nuevo producto: ")
    precio = float(input("Ingrese precio: "))
    cantidad = int(input("Ingrese cantidad: "))
    
    with open(NOMBRE_ARCHIVO, 'a') as f:
        f.write(f"\n{nombre},{precio},{cantidad}")
        
    lista_productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    
    print("¡Producto agregado correctamente!")

def buscar_producto(lista_productos):
    print("\n--- Buscar Producto (Act 5) ---")
    nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ")
    
    encontrado = False
    for producto in lista_productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print("¡Producto encontrado!")
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: ${producto['precio']}")
            print(f"  Cantidad: {producto['cantidad']}")
            encontrado = True
            break 
            
    if not encontrado:
        print(f"Error: El producto '{nombre_buscar}' no existe.")

def guardar_productos_actualizados(lista_productos):
    print("\n--- Guardando Productos Actualizados (Act 6) ---")
    
    with open(NOMBRE_ARCHIVO, 'w') as f:
        for i, producto in enumerate(lista_productos):
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}"
            f.write(linea)
            if i < len(lista_productos) - 1:
                f.write("\n")
    
    print(f"Archivo '{NOMBRE_ARCHIVO}' actualizado exitosamente.")

def main():
    lista_prods = cargar_y_mostrar_productos()
    
    agregar_producto(lista_prods)
    
    buscar_producto(lista_prods)
    
    guardar_productos_actualizados(lista_prods)
    
    print("\n--- Práctica Finalizada ---")

main()
