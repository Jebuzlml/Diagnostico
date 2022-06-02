print("Cuando se le indique ingrese un numero, se sumaran los digitos impares entre 0 y el valor que escogió.")
n = int(input("ingrese un numero: "))

lista_impares = []

for variable in range(n):
    verificador = variable % 2
    if verificador > 0:
        lista_impares.append(variable)

suma_impares = sum(lista_impares)
print(suma_impares)