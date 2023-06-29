##### Recuperativa

num_parte = []
nombres = []
precios =[]

def validar_parte(parte):
    if isinstance(parte, str):
        return True
    else:
        return False
    
def grabar():

    for _ in range(10):
        parte = int(input('Ingrese los numeros del parte:\n'))
        while not validar_parte(parte):
            print('Numero de parte incorrecto.')
            parte = int(input('Ingrese el numero del parte:\n'))
        num_parte.append(parte)

        nombre = int(input('Ingrese el nombre del producto(minimo 6 caracteres.):\n'))
        while len(nombre) < 6:
            print('Nombre incorrecto.')
            nombre = int(input('Ingrese el nombre del producto(minimo 6 caracteres.):\n'))
        nombres.append(nombre)

        precio = int(input('Ingrese el precio del producto:\n'))
        while precio <= 0:
            print('El precio del producto tiene que ser mayor que 0.')
            precio = int(input('Ingrese el precio del producto:\n'))
        precios.append(precio)

    return num_parte, nombres, precios

def buscar(num_parte, nombres, precios):
    numero = int(input('Ingrese el numero de parte(producto):\n'))
    if numero in num_parte:
        indice = num_parte.index(numero)
        if precios[indice] >= 500:
            print('Numero de parte: ', num_parte[indice])
            print('Nombre: ', nombres[indice])
            print('Precio: ', precios[indice])
        else:
            print('No hay stock.')
    else:
        print('El numero ingresado del parte, no a sido encontrado.')

def reporte(num_parte, nombres, precios):
    print('-------------------------------------------')
    print('                 Reporte                   ')
    for i in range(len(num_parte)):
        print('Numero de parte:', num_parte[i])
        print('Nombre del producto: ', nombres[i])
        print('Precio del producto: \n', precios[i])

despedida = 'Este es un progama de gestion de productos\nVersion 1.0\nDesarrollado por:\n      Matias Nuñez        \n'
menu = '            ¡Bienvenido!            \n1) Grabar producto - Registrar nuevo producto:\n2) Buscar producto:\n3) Imprimir reporte del producto(descripcion y valor):\n4) Salir.'
opcion = 0

while True:
    print(menu)

    try:
        opcion = int(input('Ingrese un opcion:'))
    except ValueError:
        print("Solo tiene que se tiene que ocupar los numeros del menú.")
        continue

    if opcion == 1:
        grabar()
    elif opcion == 2:
        buscar()
    elif opcion == 3:
        reporte()
    elif opcion == 4:
        print(despedida)
        break
    else:
        print('Opcion no válida')

