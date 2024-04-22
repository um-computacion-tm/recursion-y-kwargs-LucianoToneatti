
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
####### ACA USAMOS Las dos juntas para probar si funciona y como nos daria el resultado
def escribir_nombres1(*args,**kwargs):
    print ("    Inicio")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("key",key,"valor", value)
    
escribir_nombres1("Ludmila", 
                primer_nombre = "Luciano",
                primer_apellido ="Toneatti",
                segundo_nombre ="Cristian",
                segundo_apellido ="Gandolfo")
escribir_nombres1("Liz", 
                primer_nombre="Ian", 
                primer_apellido="Olmedo")
