import modulos.utils.corefiles as cf
from tabulate import tabulate
import main as mn

def eliminar_elemento(productos):
    """
    Permite eliminar un elemento de la colección buscando por nombre, precio, fecha o cantidad.
    Guarda automáticamente los cambios en el archivo JSON.
    """
    print("\n=== Eliminar un Elemento ===")

    if not productos:
        print("La colección está vacía, no hay elementos para eliminar.")
        return

    # Mostrar lista de elementos con índice
    print("\nElementos en la colección:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto['nombre']} - {producto['precio']} ({producto['fecha']}) [{producto['cantidad']}]")

    print("\nSeleccione el criterio de eliminación:")
    print("1. Eliminar por nombre")
    print("2. Eliminar por precio")
    print("3. Eliminar por fecha")
    print("4. Eliminar por cantidad")
    print("5. Regresar al menú principal")

    opcion = input("Ingrese el número de la opción: ").strip()

    criterios = {"1": "nombre", "2": "precio", "3": "fecha", "4": "cantidad"}
    
    if opcion == "5":
        mn.mostrar_menu()
        return
    elif opcion not in criterios:
        print("\nOpción no válida. Intente nuevamente.")
        return

    criterio = criterios[opcion]
    valor = input(f"\nIngrese el {criterio} del elemento a eliminar: ").strip()

    # Convertir el valor ingresado al tipo correcto
    if criterio in ["precio", "cantidad"]:
        try:
            valor = float(valor) if "." in valor else int(valor)
        except ValueError:
            print(f"\nError: El {criterio} debe ser un número válido.")
            return

    # Filtrar elementos que NO coincidan para eliminarlos
    elementos_filtrados = [e for e in productos if e[criterio] != valor]

    if len(elementos_filtrados) == len(productos):
        print(f"\nNo se encontró ningún elemento con {criterio}: {valor}")
        return

    # Actualizar la colección y guardar cambios
    productos.clear()
    productos.extend(elementos_filtrados)

    cf.guardar_datos(productos)
    print(f"\nLos elementos con {criterio} '{valor}' han sido eliminados y la colección ha sido actualizada.")
