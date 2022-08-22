import conversiones


def solicitar_datos():
    bases_soportadas = ["2", "8", "10", "16", ]
    input("Bienvenido al conversor numérico :D. Oprime cualquier ENTER para continuar")
    base_origen = input("""
Por favor elige la base desde donde quieres convertir: [2, 8, 10, 16]:
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal""")
    if base_origen not in bases_soportadas:
        print("La base que ingresaste no es la correcta")
        return
    numero = input(
       f"Vas a convertir desde la base {base_origen} Ingresa el número a convertir: ")
    base_destino = input("""
Elige la base a la que conviertes: [2, 8, 10, 16]:
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal""")
    if base_destino not in bases_soportadas:
        print("La base que ingresaste no es correcta")
        return
    return (base_origen, numero, base_destino)
def obtener_numero_decimal(base_origen, numero):
    if base_origen == "2":
        return conversiones.binario_a_decimal(numero)
    elif base_origen == "8":
        return conversiones.octal_a_decimal(numero)
    elif base_origen == "10":
        return int(numero)
    elif base_origen == "16":
        return conversiones.hexadecimal_a_decimal(numero)
def convertir(numero, base_destino):
    if base_destino == "2":
        return conversiones.decimal_a_binario(numero)
    elif base_destino == "8":
        return conversiones.decimal_a_octal(numero)
    elif base_destino == "10":
        return int(numero)
    elif base_destino == "16":
        return conversiones.decimal_a_hexadecimal(numero)
    
if __name__ == '__main__':
    datos = solicitar_datos()
    
    if datos:
        base_origen, numero, base_destino = datos
        numero_decimal = obtener_numero_decimal(base_origen, numero)
        resultado = convertir(numero_decimal, base_destino)
        #for varible in resultado:
        #print ('%s: %i' % (variable, chr(variable)))
        input(f" El número es el {resultado} en base {base_destino} ")
        #chr(resultado)
        
        print(f" El número en lenguaje ASCII es {chr(resultado)} ")
        
        