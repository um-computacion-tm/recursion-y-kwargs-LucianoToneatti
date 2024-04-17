def sumatoria1(value):
    resultado = 0
    while value > 0:
        resultado = resultado + value 
        value -= 1
    return resultado
result = sumatoria1(7)
print(result)

def sumatoria(value):
    if value == 1:
        return 1
    return value + sumatoria(value - 1)
resultado = sumatoria(6)
print(resultado)


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
   
##SERIE DE FIBONACCI##

def fibonacci2(value):
    if value < 2:
        return value
    values = [0, 1]
    for _ in range(value -1):
        values.append(values [-1] + values [-2])
    print(values)
    return values[value]

resultado = fibonacci2(10)
print (resultado)



#####
#*args: Es una lista para cuando no sabes cuantos parametros tienen las variables 
def escribir_nombres(*args): 
    print ("    Inicio")
    for i in range(len(args)):
        print(args[i])
escribir_nombres("Luciano",
                 "Toneatti",
                 "Cristian",
                "Gandolfo")
escribir_nombres("Ian", 
                 "Olmedo")

#**kwargs: keyword arguments: Puede llamarce de cualquier manera. Sirve para cuando no sabes cuantos argumentos tiene la función con nombre de parametros

def escribir_nombres(**kwargs): 
    print ("    Inicio")
    print(kwargs)
escribir_nombres(primer_nombre = "Luciano",
                 primer_apellido ="Toneatti",
                 segundo_nombre ="Cristian",
                segundo_apellido ="Gandolfo")
escribir_nombres(primer_nombre="Ian", 
                 primer_apellido="Olmedo")

#####items. ES una forma de crear una lista de key y su valor asociado con un diccionario que le damos en este caso es kwargs
def escribir_nombres1(**kwargs):
    print ("    Inicio")
    print (kwargs.items())
escribir_nombres(primer_nombre = "Luciano",
                 primer_apellido ="Toneatti",
                 segundo_nombre ="Cristian",
                segundo_apellido ="Gandolfo")
escribir_nombres(primer_nombre="Ian", 
                 primer_apellido="Olmedo")
#######
def escribir_nombres1(*args,**kwargs):
    print ("    Inicio")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("key",key,"valor", value)
    
escribir_nombres1("Ludmila", primer_nombre = "Luciano",
                 primer_apellido ="Toneatti",
                 segundo_nombre ="Cristian",
                segundo_apellido ="Gandolfo")
escribir_nombres1("Liz", primer_nombre="Ian", 
                 primer_apellido="Olmedo")
