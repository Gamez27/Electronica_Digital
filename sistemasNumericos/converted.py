

def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario #obtenemos el residuo de la division entre 2 y lo concatenamos al resultado binario
        decimal //= 2 #dividimos el numero entre 2 y lo asignamos a decimal para continuar el proceso hasta que decimal sea 0
    return binario

def decimal_a_octal(decimal):
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder - 10 + ord('A')) + hexadecimal
        decimal //= 16
    return hexadecimal

def numerosnegativos(decimal):
    if decimal < 0:
        return "El numero es negativo"

while True:

    print ("Seleccione la conversion que desea realizar:")
    print ("1. Decimal a Binario")
    print ("2. Decimal a Octal")        
    print ("3. Decimal a Hexadecimal")
    print ("4. Salir")

    opcion = (input("Ingrese una opcion : "))

    match opcion:
        case "1":
            print("El numero en binario es: ", decimal_a_binario(int(input("Ingrese un numero decimal: "))))
        case "2":
            print("El numero en octal es: ", decimal_a_octal(int(input("Ingrese un numero decimal: "))))
        case "3":
            print("El numero en hexadecimal es: ", decimal_a_hexadecimal(int(input("Ingrese un numero decimal: "))))
        case "4":
            print ("Saliste del programa")
            break
        case _:
            print("Opcion no valida")