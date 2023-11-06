# Set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

print(primer | segundo) #|: Union los va a unir
print(primer & segundo) #&: Devuelve los elementos en comun
print(primer - segundo) #-: Deja los elementos de la izquierda en dif. con los de la derecha
print(primer ^ segundo) #^: Los que se encuentren duplicados los va a eliminar 1,2,3 / 2,3,4 = 1 y 4

# primer.add(5)
# primer.remove(1)
