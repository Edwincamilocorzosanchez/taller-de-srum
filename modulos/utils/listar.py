from tabulate import tabulate
import json
ARCHIVO_JSON="data/datos.json"
def cargar_datos():
    """
    Carga la colección desde el archivo JSON.
    Si el archivo no existe o tiene errores, retorna una lista vacía.
    """
    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def guardar_datos(productos):
    """
    Guarda la colección en el archivo JSON.
    """
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)
def listar_productos(productos):
    print("\n=== Listar productos ===")

    if not productos:
        print("\nNo hay productos guardados.")
        return

    # Convertimos la colección en formato tabular
    tabla = []
    for producto in productos:
        tabla.append([
            producto.get("id", "N/A"),
            producto.get("tipo", "N/A"),
            producto.get("nombre", "N/A"),
            producto.get("precio", "N/A"),
            producto.get("fecha", "N/A"),
            producto.get("cantidad", "N/A")

        ])

    # Encabezados de la tabla
    headers = ["id","tipo","nombre", "precio", "fecha","cantidad"]


    # Mostramos la tabla con tabulate
    print(tabulate(tabla, headers=headers, tablefmt="grid"))
