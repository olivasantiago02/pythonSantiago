# For: Iterar lista de elementos


buscar = 10
for numero in range (5):
    print(numero)
    if numero == buscar:
        print("Lo encontramos al", buscar)
        break
else:
    print("No enconte el numero buscado")

for char in "Ultimate Python":
    print(char)