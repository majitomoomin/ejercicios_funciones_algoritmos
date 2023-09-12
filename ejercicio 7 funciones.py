#confeccionar una funcion que le enviamos como parametros dos enteros y nos retorne el mayor
def retornar_mayor(v1, v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor

#bloque principal

valor1=int(input("ingrese el primer valor: "))
valor2=int(input("ingrese el segundo valor:"))

print(retornar_mayor(valor1, valor2))
