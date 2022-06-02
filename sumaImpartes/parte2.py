print("Cuando se le indique ingrese 2 numeros, luego se sumaran los digitos impares que hay entre ellos.")
a = int(input("ingrese un numero: "))
b= int(input("ingrese otro numero: "))

lista_impares = []

for variable in range(a, b):
    verificador = variable % 2
    if verificador > 0:
        lista_impares.append(variable)

suma_impares = sum(lista_impares)
print(suma_impares)