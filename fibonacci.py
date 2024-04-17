   
##SERIE DE FIBONACCI##
#NO RECURSIVA CON LISTA
def fibonacci1(value):
    if value < 2:
        return value
    values = [0, 1]
    for _ in range(value -1):
        values.append(values [-1] + values [-2])
    print(values)
    return values[value]

resultado = fibonacci1(8)
print (resultado)
# TOMAMOS DOS VARIABLES TAMBIEN NO RECURSIVAS

def fibonacci2(value):
    anterior, resultado = 1,0
    for _ in range(value):
        resultado, anterior = anterior + resultado, resultado
    return resultado
resutado = fibonacci2(7)
print (resutado)


##RECURSIVA##
def fibonacci3(value1):
    if value1 == 0 or value1 == 1:
        return value1
    return fibonacci3(value1 - 1) + fibonacci3(value1 - 2)
resultado = fibonacci3(13)
print (resultado)