"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones 
múltiplos de 3, y muestre por pantalla la lista resultante.
"""
# 25 indices
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w", "x", "y","z"]
eliminados = []

for i in range(0, 26):
    hp = i + 1
    if hp % 3 != 0:
        eliminados.append(abc[i])

for letra in eliminados:
    print(letra)