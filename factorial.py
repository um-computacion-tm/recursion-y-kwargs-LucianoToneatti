def factorial(valor):
    if valor > 0:
        return valor * factorial(valor - 1)
    return 1
result = factorial(5)
print(result)

def factorial2(value):
    resultado = value
    while value > 2:
        resultado = resultado * (value - 1)
        value -= 1
    return resultado
resultado = factorial2(4)
print(resultado)