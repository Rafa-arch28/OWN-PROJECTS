## Funcion range
range(inicio, fin, paso)

## WHILE TRUE
Para terminarlo usa "break"

## LIMPIAR VARIABLES 
Para strings: variable = ""
Para otras: variable = 0
Se limpian solas en un bucle

## LISTAS
Las listas son con corchetes: []
Para agregar elementos de un usario usas el input y el .append() con la variable en el ()
Para desempaquetar valores de una lista usa * antes de la variable de la lista, ejemplo: *lista1

## DIFERENCIAS ENTRE SORTED() Y .SORT()
sorted() solo ordena para el print(), no modifica la lista original, hace una "copia"
.sort() va despues del nombre de la lista y ordena la lista original, la modifica: dario.sort()

## .SORT()
En el .sort() puedes usar dentro de los parentesis (reverse = True), oredenara los valores en orden inverso

## PARA LITAS
¿Quieres borrar buscando el nombre/valor? ➔ .remove(valor)
¿Quieres borrar por posición y guardar lo que borraste? ➔ .pop(indice)
¿Quieres borrar por posición o rangos sin guardar nada? ➔ del lista[indice]

## .COUNT
.count() para hacer conteos en variables

## list()
para hacer una variable normal una lista, puedes usar list(variable) para hacerlo

## PRIMER Y ULTIMO ELEMENTO DE LISTAS
el indice 0 siempre es el primer elemeto
el indice -1 siempre es el ultimo elemento

## DICCIONARIOS SIEMPRE [] para ir al valor
Son como listas pero que una tipo variable guarda un dato, la primera parte siempre va a ser 
un string, la segunda si va a ser cualquier tipo de dato

NO hay indices en un diccionario, no se puede usar 0, 1 y eso para acceder a los datos,
tiene que ser un string

Para verificar si hay una llave con valor en el diccionario usa un if con la funcion in seguida del diccionario

Puedes usar .get() despues de la variable diccionario para obtener un valor directamente
con el .get("Aqui pones la variable", Despues de la coma pones un valor por defecto que arroje si no encuentra lo que buscaba)

puedes usar del variable["Llave"] para borrar alguna llave con su valor

Puedes iterar las llaven con un for: for valor in dicionario, asi se hace. Si pones un print va a imprimir las llaves, para sacar los valores tienes que poner la variable valor, ya que son las llaves 

Puedes usar for valor in diccionario.items():, eso te va a devolver una tupla y la desempaquetas con poniendo dos variables separadas con coma en el for, ejemplo: for llave,valor in diccionario.items(): print(llave, valor)

Puedes poner diccionarios dentro de listas

tambien puedes usar la funcion in en if's

## .SPLIT()
Puedes usar .split("char") para partir el texto donde incie cada uno de esos caracteres, hara una lista con el texto dividido (te sirve mucho si quieres pasar formatos a listas o diccionarios)