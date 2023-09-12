#aplicacion que muestra una presentación del programa, solicite carga de dos valores y nos muestre la suma
#Mostrar finalmente un mensaje de despedida del programa

def mostrar_mensaje(mensaje):
    print("*************************")
    print(mensaje)
    print("*************************")

def carga_suma():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el el segundo valor: "))
    suma=valor1+valor2
    print("la suma de los dos valores es: ", suma)


#programa principal

mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado")
carga_suma()
mostrar_mensaje("Gracias por utilizar este programa")
