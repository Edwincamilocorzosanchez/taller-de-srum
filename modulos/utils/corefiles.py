import json
ARCHIVO_JSON="data/productos.json"
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