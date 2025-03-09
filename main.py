import modulos.menus as mn
import modulos.utils.agregar as ag
import os
import modulos.utils.corefiles as cf
import modulos.utils.listar as li
import modulos.utils.editar as ed
import modulos.utils.buscar as bu
import modulos.utils.eliminar as el
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
                os.system('cls')
                ed.editar_elemento(productos)
                os.system('pause')
                return mostrar_menu()
            case 4:
                os.system('cls')
                bu.buscar_elemento(productos)
                os.system('pause')
                return mostrar_menu()
            case 5:
                os.system('cls')
                el.eliminar_elemento(productos)
                os.system('pause')
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