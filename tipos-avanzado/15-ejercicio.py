from pprint import pprint
# 1- Eliminar los espacios en blanco de un "string"
string = "Hola mundo este es mi string"


def quita_espacios(texto):
    return [char for char in texto if char != " "]

# 2-


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

# 3-


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )

#4-


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
        return respuesta


def crea_mensajes(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"-{key} con {valor} repeticiones \n"
    return mensaje

sin_espacios = quita_espacios(string)
cuenta_caracteres(sin_espacios)
contados = cuenta_caracteres(sin_espacios)
ordenados = ordena(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensajes(mayores)
print(mensaje)
print(mayores)
print(sin_espacios)
pprint(contados, width=1)
print(ordenados)

# 2- Contar en un diccionario cuando se repiten los caracteres de un string

# 3- Ordenar las llaves de un diccionario por el valor que tienen 
# y devolver una lista que contenga tuplas

# 4- De un listado de tuplas devolver las tuplas que tengan el mayor valor

# 5- crea un mensaje que diga:
#los caracteres que mas se repiten con 4 repeticiones son:
# - C
# - D
