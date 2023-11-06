# and - or - not

# and: cuando tengamos dos condiciones, cuando ambos sean True evalua en True, al menos que uno sea False

# or: Dos condiciones, en el caso que uno sea True para que el resultado sea True

# not: negara el resultado final no importa los valores

gas = True
encendido = True
edad = 18

if not gas and encendido and edad > 17:
    print("puedes avanzar")

# Primero se evaluan los parentesis siempre ().
# Siempre las operaciones se ejecutan de izq. a der. al menos que tengamos parentesis
