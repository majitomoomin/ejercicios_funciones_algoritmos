#confeccionar una funcion que reciba tres enteros y nos muestre el mayor de ellos. la carga de
#Los valores hacerlo por teclado.

def mostrar_mayor(v1, v2, v3):
    print("el valor mayor de los tres numeros es: ")
    if v1>v2 and v1>v3:
        print(v1)

    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)


def cargar():
    valor1=int(input("ingrese el primer valor: "))
    valor2=int(input("ingrese el segundo valor: "))
    valor3=int(input("ingrese el tercer valor: "))
    mostrar_mayor(valor1, valor2, valor3)

#programa principal
cargar()
