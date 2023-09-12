#aplicacion que solicite la carga de dos valores enteros y muestre su suma.
#repetir la carga e impresion de la suma 5 veces.
#mostrar una linea separadora despues de cada vez que cargamos dos valores y su suma.

def carga_suma():
    valor1=int(input("ingrese el primer valor: "))
    valor2=int(input("ingrese el segundo valor: "))
    suma=valor1+valor2
    print("La suma de los dos valores es: ", suma)

def barra_separadora():
    print("***************************************")


#bloque principal

for x in range(5):
    carga_suma()
    barra_separadora()
