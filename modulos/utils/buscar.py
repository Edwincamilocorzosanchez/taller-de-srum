from tabulate import tabulate
import main as mn

# Función para buscar elementos en la colección (Opción 3)
def buscar_elemento(productos):
    print("\n=== Buscar Elemento en la Colección ===")
    
    if not productos:
        print("La colección está vacía.")
        return

    # Seleccionar el criterio de búsqueda
    print("Buscar por:")
    print("1. nombre")
    print("2. precio")
    print("3. fecha")
    print("4. cantidad")
    print("5. regresar al menu")
    criterio = input("Seleccione el criterio (1-5): ").strip()

    if criterio == "1":
        termino = input("Ingrese el nombre a buscar: ").strip().lower()
        resultados = [e for e in productos if termino in e.get("nombre", "").lower()]
    elif criterio == "2":
        termino = input("Ingrese el precio a buscar: ").strip().lower()
        resultados = [e for e in productos if termino in e.get("precio", "").lower()]
    elif criterio == "3":
        termino = input("Ingrese el fecha a buscar: ").strip().lower()
        resultados = [e for e in productos if termino in e.get("fecha", "").lower()]
    elif criterio == "4":
        termino = input("Ingrese la cantidad a buscar: ").strip().lower()
        resultados = [e for e in productos if termino in e.get("cantidad", "").lower()]
    elif criterio == "5":
        return mn.mostrar_menu()
    else:
        print("Criterio no válido.")
        return

    # Mostrar los resultados
    if resultados:
        print("\nResultados encontrados:")
        tabla = []
        for producto in resultados:
            tabla.append([
            producto.get("id", "N/A"),
            producto.get("tipo", "N/A"),
            producto.get("nombre", "N/A"),
            producto.get("precio", "N/A"),
            producto.get("fecha", "N/A"),
            producto.get("cantidad", "N/A")
            ])
        headers = ["id","tipo","nombre", "precio", "fecha","cantidad"]
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        print("\nNo se encontraron elementos que coincidan con la búsqueda.")