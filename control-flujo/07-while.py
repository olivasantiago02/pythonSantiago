# numero= 1
# while numero < 100:
#     print(numero)
#     numero *= 2


# comando = ""

# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)

# Loop infinito: suceden cuando nop tenemos una condicion de salida, por lo que se ejecuta para siempre

comando = ""

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break

