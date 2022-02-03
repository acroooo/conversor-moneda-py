menu = """
Bienvenido al conversor de monedas 🪙

1 - Pesos argentinos
2 - Pesos mexicanos

Elige una opción: """
opcion = input(menu)

if opcion == '1':
    # valor ---- 1 dls
    valor_dolar = input("Ingresa el valor del dolar actual en tu moneda: ")
    valor_dolar = float(valor_dolar)
    # valor ---- x dls
    valor_pesos = input(
        "Ingresa el valor en pesos argentinos que queres convertir: ")
    valor_pesos = float(valor_pesos)
    resultado = int(valor_pesos / valor_dolar)
    res = round(resultado, 2)
    print("El resultado es: U$S", res)
elif opcion == '2':
    # valor ---- 1 dls
    valor_dolar = input("Ingresa el valor del dolar actual en tu moneda: ")
    valor_dolar = float(valor_dolar)
    # valor ---- x dls
    valor_pesos = input(
        "Ingresa el valor en pesos mexicanos que queres convertir: ")
    valor_pesos = float(valor_pesos)
    resultado = int(valor_pesos / valor_dolar)
    res = round(resultado, 2)
    print("El resultado es: U$S", res)
else:
    print("Opción no válida, por favor vuelva a ejecutar el programa")
# No puedo utilizar funciones, imports o clases por el momento
# conversor de monedas
