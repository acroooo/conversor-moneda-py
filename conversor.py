def conversor(tipo_moneda, valor_dolar, valor_pesos):
    if tipo_moneda == '1':
        valor_dolar = float(valor_dolar)
        valor_pesos = float(valor_pesos)
        valor_dolar = valor_pesos / valor_dolar
        round_result = round(valor_dolar, 2)
        print("El valor en dolares es: U$S ", round_result)
    elif tipo_moneda == '2':
        valor_dolar = float(valor_dolar)
        valor_pesos = float(valor_pesos)
        valor_dolar = valor_pesos / valor_dolar
        round_result = round(valor_dolar, 2)
        print("El valor en dolares es: U$S ", round_result)


menu = """
Bienvenido al conversor de monedas 🪙

1 - Pesos argentinos
2 - Pesos mexicanos

Elige una opción: """
opcion = input(menu)
dolar = input("Ingresa el valor del dolar actual en tu moneda: ")
pesos = input("Ingresa el valor de tus pesos: ")

conversor(opcion, dolar, pesos)
