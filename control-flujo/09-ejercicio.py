"""
Crear calculadora para usuario utilizando la terminal.
1) Ingrese un numero
2) Seleccione una operacion
3) ingrese segundo numero
4) mostrar resultado

"""


print("Bienvenidos a la calculadora de Python de : Santiago Oliva")
print("Para salir escribe Salir")
print("Ingrese operacion que quiere seleccionar (suma, resta, division o multiplicacion) :")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresar Operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese siguientes numeros: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "sumar":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("operacion no valida")
        break


    print(f"El resultado es {resultado}")
