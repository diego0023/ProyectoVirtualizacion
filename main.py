from faker import Faker
import random
import string
import time
import mysql.connector

# Configuración de la conexión a la base de datos
config = {
    'user': 'root',
    'password': 'root',
    'host': '3.144.105.214',
    'database': 'mydb',
    'raise_on_warnings': True
}

fake = Faker()


# Función para generar un ID aleatorio
def generar_id(maximo):
    return random.randint(1, maximo)


# Función para insertar un artículo en la base de datos
def insertar_articulo():
    # Establecer conexión a la base de datos
    conexion = mysql.connector.connect(**config)
    cursor = conexion.cursor()

    fecha = time.strftime('%Y-%m-%d %H:%M:%S')
    contenido = fake.text()
    titulo = fake.name()

    cursor.execute("SELECT COUNT(*) FROM user")
    num_usuarios = cursor.fetchone()[0]

    # Generar un ID aleatorio basado en el número de usuarios
    id_usuario = generar_id(num_usuarios)

    query = "INSERT INTO post (`created_at`, `content`, `title`, `user_id`) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (fecha, contenido, titulo, id_usuario))
    print('Artículo insertado correctamente.')
    conexion.commit()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conexion.close()


# Función para mostrar el último artículo insertado
def mostrar_ultimo_articulo():
    # Establecer conexión a la base de datos
    conexion = mysql.connector.connect(**config)
    cursor = conexion.cursor()

    query = "SELECT * FROM post ORDER BY created_at DESC LIMIT 1"
    cursor.execute(query)
    resultado = cursor.fetchone()

    if resultado:
        print('\nÚltimo artículo:')
        print(f'ID: {resultado[0]}')
        print(f'Fecha Creacion: {resultado[1]}')
        print(f'Titulo: {resultado[2]}')
        print(f'Contenido: {resultado[3]}')
        print(f'ID Usuario: {resultado[4]}')
    else:
        print('No hay artículos en la base de datos.')

    # Cerrar la conexión a la base de datos
    cursor.close()
    conexion.close()


# Menú principal
def menu_principal():

    while True:
        print('\n--- Menú Principal ---')
        print('1. Insertar artículo')
        print('2. Mostrar último artículo')
        print('d. Salir')

        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            # Insertar el artículo en la base de datos
            while True:
                insertar_articulo()

        elif opcion == '2':
            # Mostrar el último artículo cada 5 segundos
            while True:
                mostrar_ultimo_articulo()
                time.sleep(5)


# Ejecutar el programa
menu_principal()
