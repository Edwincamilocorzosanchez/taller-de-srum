import modulos.utils.corefiles as cf  # Módulo para manejar el archivo JSON
import main as mn  # Módulo del menú principal

def registrar_venta(productos):
    """
    Registra la venta de un producto, actualizando la cantidad disponible en la colección.
    Guarda automáticamente los cambios en el archivo JSON.
    """
    print("\n=== Registrar Venta ===")

    if not productos:
        print("La colección está vacía, no hay productos para vender.")
        return mn.mostrar_menu()

    # Mostrar productos disponibles
    print("\nProductos disponibles:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto['nombre']} - Precio: {producto['precio']} - Stock: {producto['cantidad']}")

    nombre_producto = input("\nIngrese el nombre del producto que desea vender: ").strip()

    # Buscar el producto en la colección
    for producto in productos:
        if producto["nombre"].lower() == nombre_producto.lower():
            try:
                cantidad_vendida = int(input(f"Ingrese la cantidad de '{producto['nombre']}' a vender: "))

                if cantidad_vendida <= 0:
                    print("La cantidad debe ser mayor a 0.")
                    return

                if cantidad_vendida > producto["cantidad"]:
                    print("No hay suficiente stock disponible.")
                    return

                # Restar la cantidad vendida del stock
                producto["cantidad"] -= cantidad_vendida

                # Guardar los cambios en el JSON
                cf.guardar_datos(productos)

                print(f"\nVenta registrada: {cantidad_vendida} unidades de '{producto['nombre']}' vendidas con éxito.")
                return mn.mostrar_menu()

            except ValueError:
                print("Error: Ingrese un número válido para la cantidad.")
                return

    print("\nProducto no encontrado en la colección.")
    return mn.mostrar_menu()

