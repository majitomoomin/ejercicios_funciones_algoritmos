#confeccionar una funcion que le enviemos como parametro un string y nos retorne
#la cantidad de caracteres que tiene. en el bloque principal solicitar la carga de dos nombres por teclado
#y llamar a la funcion dos veces. imprimir en el bloque principal cual de las dos palabras tiene mas
#caracteres

def largo(cadena):
    return len(cadena)

#bloque principal

nombre1=input("ingrese primer nombre: ")
nombre2=input("ingrese segundo nombre: ")
la1=largo(nombre1)
la2=largo(nombre2)
if la1==la2:
    print("los nombres: ", nombre1, nombre2, "tienen la misma cantidad de caracteres")
else:
    if la1>la2:
        print(nombre1, " es el nombre más largo")
    else:
        print(nombre2, " es el maás largo")
