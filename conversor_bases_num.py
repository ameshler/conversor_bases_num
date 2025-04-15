def decimal_a_binario():
    print("Pasando de decimal a binario...")
    # Pedir al usuario un número entero decimal y guardarlo como int
    decimal = int(input("Ingrese el número decimal: "))
    # Asignar el decimal a una variable aux para operarla sin afectar el número ingresado.
    aux = decimal
    # Inicializar la variable binario como un string vacío.
    binario = ''
    # Recorrer cada cifra decimal y obtener parte entera y resto de la division por 2.
    while aux > 0: # El bucle se ejecuta mientras aux sea mayor a 0.
        # Ir concatenando los restos de dividir por 2 en cada iteración.
        binario = binario + str(aux % 2)
        # Actualizar aux con la parte entera de la división por 2 para operarla en la próxima iteración.
        aux = aux//2
    # Invertir el string generardo para obtener el orden correcto de las cifras binarias.
    binario = binario[::-1]
    # Informar el resultado
    print(f"{decimal} decimal en binario es igual a {binario}")

def binario_a_decimal():
    print("Pasando de binario a decimal...")
    # Pedir al usuario un número binario y guardarlo como string
    binario = input("Ingrese el número binario: ")
    # Obtener la cantidad de cifras del binario.
    cant_cifras = len(str(binario))
    # Obtener la maxima potencia. Como la de la primer cifra es 0, la maxima es la cant de cifras menos uno.
    potencia = cant_cifras - 1
    # Inicializar variable decimal en 0.
    decimal = 0
    # Recorrer cada cifra del binario
    for cifra in binario:
        # Ir acumulando cada cifra * 2 elevado a la potencia de cada posicion
        decimal = decimal + int(cifra) * 2 ** potencia
        # Decrementar en uno la potencia
        potencia = potencia - 1
    # Informar el resultado
    print(f"{binario} binario en decimal es igual a {decimal}")

def decimal_a_octal():
    print("Pasando de decimal a octal...")
    # Pedir al usuario un número entero decimal y guardarlo como int
    decimal = int(input("Ingrese el número decimal: "))
    # Asignar el decimal a una variable aux para operarla sin afectar el número ingresado.
    aux = decimal
    # Inicializar la variable octal como un string vacío.
    octal = ''
    # Recorrer cada cifra decimal y obtener parte entera y resto de la division por 8.
    while aux > 0: # El bucle se ejecuta mientras aux sea mayor a 0.
        # Ir concatenando los restos de dividir por 8 en cada iteración.
        octal = octal + str(aux % 8)
        # Actualizar aux con la parte entera de la división por 8 para operarla en la próxima iteración.
        aux = aux//8
    # Invertir el string generardo para obtener el orden correcto de las cifras octales.
    octal = octal[::-1]
    # Informar el resultado
    print(f"{decimal} decimal en octal es igual a {octal}")

def octal_a_decimal():
    print("Pasando de octal a decimal...")
    # Pedir al usuario un número octal y guardarlo como string
    octal = input("Ingrese el número octal: ")
    # Obtener la cantidad de cifras del binario.
    cant_cifras = len(str(octal))
    # Obtener la maxima potencia. Como la de la primer cifra es 0, la maxima es la cant de cifras menos uno.
    potencia = cant_cifras - 1
    # Inicializar variable decimal en 0.
    decimal = 0
    # Recorrer cada cifra del binario
    for digito in octal:
        # Ir acumulando cada cifra * 8 elevado a la potencia de cada posición
        decimal = decimal + int(digito) * 8 ** potencia
        # Decrementar en uno la potencia
        potencia = potencia - 1
     # Informar el resultado
    print(f"{octal} octal en decimal es igual a {decimal}")

def hexadecimal_a_decimal():
    print("Pasando de hexadecimal a decimal...")
    # Pedir al usuario un número hexadecimal y guardarlo como string
    hexadecimal = input("Ingrese el número hexadecimal: ")
    # Obtener la cantidad de cifras del hexadecimal.
    cant_cifras = len(str(hexadecimal))
    # Obtener la maxima potencia. Como la de la primer cifra es 0, la maxima es la cant de cifras menos uno.
    potencia = cant_cifras - 1
    # Inicializar variable decimal en 0.
    decimal = 0
    # Crear diccionario con valores numéricos de los dígitos hexadecimales
    valores_hexadecimal = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    # Recorrer cada cifra del hexadecimal
    for digito in hexadecimal:
        # Ir acumulando cada cifra * 16 elevado a la potencia de cada posición
        decimal = decimal + valores_hexadecimal[digito] * 16 ** potencia
        # Decrementar en uno la potencia
        potencia = potencia - 1
    # Informar el resultado
    print(f"{hexadecimal} hexadecimal en decimal es igual a {decimal}")

def decimal_a_hexadecimal():
    print("Pasando de decimal a hexadecimal...")
    # Pedir al usuario un número entero decimal y guardarlo como int
    decimal = int(input("Ingrese el número decimal: "))
    # Asignar el decimal a una variable aux para operarla sin afectar el número ingresado.
    aux = decimal
    # Inicializar la variable octal como un string vacío.
    hexadecimal = ''
    # Crear diccionario con valores numéricos de los dígitos hexadecimales
    valores_hexadecimal = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    # Recorrer cada cifra decimal y obtener parte entera y resto de la division por 16.
    while aux > 0: # El bucle se ejecuta mientras aux sea mayor a 0.
        # Ir concatenando los restos de dividir por 16 en cada iteración
        hexadecimal = hexadecimal + valores_hexadecimal[aux % 16]
        # Actualizar aux con la parte entera de la división por 16 para operarla en la próxima iteración.
        aux = aux//16
    # Invertir el string generardo para obtener el orden correcto de las cifras octales.
    hexadecimal = hexadecimal[::-1]
    # Informar el resultado
    print(f"{decimal} decimal en hexadecimal es igual a {hexadecimal}")

# Flujo principal
# Crear diccionario de funciones
opciones = {
    '1': decimal_a_binario,
    '2': binario_a_decimal,
    '3': decimal_a_octal,
    '4': octal_a_decimal,
    '5': hexadecimal_a_decimal,
    '6': decimal_a_hexadecimal
}
# Crear bucle que imprima en pantalla las opciones.
while True:
    print("--- MENU DE CONVERSIONES ---")
    print("1 - De decimal a binario")
    print("2 - De binario a decimal")
    print("3 - De decimal a octal")
    print("4 - De octal a decimal")
    print("5 - De hexadecimal a decimal")
    print("6 - De decimal a hexadecimal")
    print("0 - Salir")
    # Pedir al usuario que ingrese una opción y guardarla como string
    opcion = input("Ingese una opción: ")
    # Controlar si la opcion ingresada es 0 para detener la ejecución
    if opcion == '0':
        print("Saliendo...")
        break
    # Validar la opción ingresada, si la opcion existe llamo a la función
    if opcion in opciones:
        opciones[opcion]()
    # Sino informar al usuario y pedir que vuelva a intentar
    else:
        print("Opcion inválida, vuelva a intentar...")

