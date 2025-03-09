import modulos.utils.corefiles as cf
from tabulate import tabulate
def editar_elemento(productos):
    print("\n=== Editar un Elemento de la Colección ===")

    if not productos:
        print("\nLa colección está vacía.")
        return

    nombre_buscar = input("Ingrese el nombre del producto a editar: ").strip().lower()

    # Buscar el elemento por título (ignorando mayúsculas y minúsculas)
    productos_encontrados = [e for e in productos if e.get("nombre", "").lower() == nombre_buscar]

    if not productos_encontrados:
        print("\nNo se encontró ningún elemento con ese título.")
        return

    producto = productos_encontrados[0]  # Se asume que no hay títulos repetidos

    print("\nElemento encontrado:")
    tabla = [[
            producto.get("id", "N/A"),
            producto.get("tipo", "N/A"),
            producto.get("nombre", "N/A"),
            producto.get("precio", "N/A"),
            producto.get("fecha", "N/A"),
            producto.get("cantidad", "N/A")

    ]]
    headers = ["id","tipo","nombre", "precio", "fecha","cantidad"]
    print(tabulate(tabla, headers=headers, tablefmt="grid"))

    # Confirmar si el usuario quiere editar
    confirmar = input("\n¿Desea editar este producto? (s/n): ").strip().lower()
    if confirmar != "s":
        print("Edición cancelada.")
        return

    # Pedir nuevos valores (presionar Enter para mantener los actuales)
    nuevo_nombre = input(f"Nuevo nombre [{producto['nombre']}]: ").strip() or producto["nombre"]
    while True:
        nuevo_precio = input(f"Nuevo precio [{producto['precio']}]: ").strip() or producto["precio"]
        if not nuevo_precio:  # Si no ingresa nada, mantiene la actual
            nuevo_precio = producto["cantidad"]
            break
        elif nuevo_precio.isdigit()  :
            nuevo_precio = int(nuevo_precio)
            break
        else:
            print("precio no válida. Ingrese un número valido")
    nueva_fecha = input(f"Nueva fecha [{producto['fecha']}]: ").strip() or producto["fecha"]

    # Manejo de la valoración opcional
    while True:
        nueva_cantidad = input(f"Nueva cantidad [{producto['cantidad']}]: ").strip()
        if not nueva_cantidad:  # Si no ingresa nada, mantiene la actual
            nueva_cantidad = producto["cantidad"]
            break
        elif nueva_cantidad.isdigit():
            nueva_cantidad = int(nueva_cantidad)
            break
        else:
            print("cantidad no válida. Ingrese un número valido")

    # Actualizar los valores del producto
    producto["nombre"] = nuevo_nombre
    producto["precio"] = nuevo_precio
    producto["fecha"] = nueva_fecha
    producto["cantidad"] = nueva_cantidad

    # Guardar los cambios en el archivo JSON
    cf.guardar_datos(productos)
    print("\n¡Elemento actualizado con éxito!")