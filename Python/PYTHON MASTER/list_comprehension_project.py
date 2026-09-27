tweets = [
    "Me encanta Python #python #code",
    "Que frío hace hoy #invierno",
    "Practicando list comprehensions 🎉 #python",
    "Odio los lunes #lunes",
]

palabras = [t.split() for t in tweets]
print(palabras)

hashtags = [w for t in tweets for w in t.split() if w[0] == "#"]
print(hashtags)

cortos = [t for t in tweets if len(t) <= 31]
print(cortos)

mayus = [t.upper() for t in tweets if len(t) <= 31]
print(mayus)

letra_l = [w for t in tweets for w in t.split() if w[0].upper() == "L"]
print(letra_l)

unicos = list(set(hashtags))
c_hashtags = [(h, hashtags.count(h)) for h in unicos]
print(c_hashtags)

# ANIDADOS

matriz =[[1,2,3], [4,5], [6,7,8,9,10]]
juntos = [i for i in matriz for j in matriz]
print(juntos)