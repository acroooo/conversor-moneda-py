# No puedo utilizar funciones, imports o clases por el momento
# conversor de monedas
valor_dolar = input("Ingresa el valor del dolar actual: ")  # valor ---- 1 dls
valor_dolar = float(valor_dolar)
# valor ---- x dls
valor_pesos = input("Ingresa el valor en pesos que queres convertir: ")
valor_pesos = float(valor_pesos)
resultado = int(valor_pesos / valor_dolar)
res = round(resultado, 2)
print("El resultado es: U$S", res)
