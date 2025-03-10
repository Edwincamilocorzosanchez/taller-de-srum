import json
import hashlib

ARCHIVO_USUARIOS = "usuarios.json"

def cargar_usuarios():
    """Carga la lista de usuarios desde el archivo JSON."""
    try:
        with open(ARCHIVO_USUARIOS, "r",encoding="utf-8" ) as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_usuarios(usuarios):
    """Guarda la lista de usuarios en el archivo JSON."""
    with open(ARCHIVO_USUARIOS, "w", encoding="utf-8" ) as archivo:
        json.dump(usuarios, archivo, indent=4)

def hash_contraseña(contraseña):
    """Cifra la contraseña con SHA-256."""
    return hashlib.sha256(contraseña.encode()).hexdigest()

def registrar_usuario():
    """Registra un nuevo usuario en el sistema."""
    print("\n=== Registro de Usuario ===")
    usuarios = cargar_usuarios()
    
    nombre = input("Ingrese un nombre de usuario: ").strip()
    
    # Verificar si el usuario ya existe
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print("Error: El nombre de usuario ya existe. Intente con otro.")
            return

    contraseña = input("Ingrese una contraseña: ").strip()
    contraseña_hash = hash_contraseña(contraseña)  # Cifrar contraseña

    nuevo_usuario = {"nombre": nombre, "contraseña": contraseña_hash}
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    
    print("✅ Usuario registrado con éxito.")

def iniciar_sesion():
    """Permite al usuario iniciar sesión."""
    print("\n=== Inicio de Sesión ===")
    usuarios = cargar_usuarios()

    nombre = input("Ingrese su nombre de usuario: ").strip()
    contraseña = input("Ingrese su contraseña: ").strip()
    contraseña_hash = hash_contraseña(contraseña)  # Cifrar la ingresada para comparar

    for usuario in usuarios:
        if usuario["nombre"] == nombre and usuario["contraseña"] == contraseña_hash:
            print(f"✅ Bienvenido, {nombre}!")
            return True  # Inicio de sesión exitoso

    print("❌ Usuario o contraseña incorrectos.")
    return False  # Fallo en el inicio de sesión

