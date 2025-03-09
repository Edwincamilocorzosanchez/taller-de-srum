import os
import modulos.menus as mn
import main as ms
import modulos.utils.corefiles as cf
def agregar_producto(productos):

    # Selección del tipo de elemento
    while True:
        print("\nSeleccione el tipo de elemento:")
        print("1. aseo")
        print("2. despensa")
        print("3. frios")
        print("4. fruver")       
        print("5. regresar al menu principal")
        tipo_opcion = input("Ingrese el número de la opción: ")
        
        if tipo_opcion == "1":
            tipo = "aseo"
            break
        elif tipo_opcion == "2":
            tipo = "despensa"
            break
        elif tipo_opcion == "3":
            tipo = "frios"
            break
        elif tipo_opcion == "4":
            tipo = "fruver"
            break
        elif tipo_opcion == "4":
            return mn.menu_principal()
        else:
            print("opción no válida intente nuevamente.")
    os.system('cls')
    try:
        id = int(input('ingrese el id del producto: '))
    except ValueError:
        print('valor invalido')
        return agregar_producto()
    nombre = input('ingrese el nombre del producto:')
    try:
        precio= int(input('ingrese el precio del producto: '))
    except ValueError:
        print('valor invalido')
        return agregar_producto()
    fecha= input('Ingrese la fecha de entrada en formato DD/MM/AA:')
    try:
        cantidad =int(input('Ingrese la cantidad de producto ingresado:'))
    except ValueError:
        print('valor invalido')
        return agregar_producto()
    nuevo_producto={
        "id":id,
        "tipo":tipo,
        "nombre": nombre,
        "precio": precio,
        "fecha": fecha,
        "cantidad": cantidad
        
    }
    productos.append(nuevo_producto)
    cf.guardar_datos(productos)