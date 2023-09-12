#programa que muestra una presentacion, solicite cargar dos valores y muestre la suma, y la despedida del programa
#implementar estas 3 actividades en tres funciones

def presentacion():
    print("Programa que permite cargar dos valores por teclado. ")
    print("efectua la suma de los valores")
    print("Muestra el resultado de la suma")
    print("********************************")

def carga_suma():
    valor1=int(input("ingrese el primer valor: "))
    valor2=int(input("ingrese el segundo valor: "))
    suma= valor1+valor2
    print("la suma de los dos valores es ", suma)


def finalizacion():
   print("********************************")
   print("Gracias por utilizar este programa")


#programa principal

presentacion()
carga_suma()
finalizacion()
