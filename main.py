import modulos.menus as mn
import modulos.utils.agregar as ag
import os
import modulos.utils.corefiles as cf
import modulos.utils.listar as li
def mostrar_menu():
    productos= cf.cargar_datos()
    print(mn.MENU)
    try:
        opcion= int(input('Escoje al opcion que deseas implementar: '))
    except ValueError:
        print('opcion invalida')
        os.system('cls')
        return mostrar_menu()
    else:
        match opcion:
            case 1:
                os.system('cls')
                ag.agregar_producto(productos)
                os.system('pause')
                return mostrar_menu()
            case 2:
                os.system('cls')
                li.listar_productos(productos)
                os.system('pause')
                return mostrar_menu()
            case 3:
                return mostrar_menu()
            case 4:
                return mostrar_menu()
            case 5:
                return mostrar_menu()
            case 6:
                os.system('cls')
                print('saliendo del programa')
                os.system('pause')
            case _:
                os.system('cls')
                print('opcion invalida')
                os.system('pause')
if __name__=="__main__":
    mostrar_menu()