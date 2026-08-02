# ROADMAP PYTHON MASTER

Ruta para pasar de intermedio-bajo a Python solido, despues avanzado. Cada tema = tutorial rapido (10-15 min) + mini-proyecto sin ayuda + debuggear solo cuando falle.

---

## Nivel 1: Fundamentos (ya lo tienes ✅)

- Variables, tipos de datos
- Strings y sus metodos
- Condicionales (if/elif/else)
- Loops (for, while)
- Listas, tuplas, diccionarios
- Funciones
- Clases, metodos, `__init__`, `__str__`
- JSON, archivos, try/except
- Modularizacion (import)

**Proyecto que lo demuestra:** PIA2 en Python (hecho ✅)

---

## Nivel 2: Python intermedio (2-3 semanas)

### Tema 1: List comprehensions
- Sintaxis: `[expresion for elemento in iterable if condicion]`
- Mini-proyecto: convertir loops de tu PIA2 a comprehensions (ej: buscar pacientes por nombre)

### Tema 2: Lambda, map, filter
- Lambda = funcion anonima de una linea
- Mini-proyecto: ordenar doctores por nombre con `sorted(doctores, key=lambda d: d.nombre)`

### Tema 3: *args y **kwargs
- Funciones que reciben numero variable de argumentos
- Mini-proyecto: funcion que registre resultados con datos extra opcionales

### Tema 4: Herencia y polimorfismo
- Clase base `Persona`, hijas `Paciente` y `Doctor`
- Mini-proyecto: REFACTORIZAR tu PIA2 para que Paciente y Doctor hereden de Persona

### Tema 5: Decoradores
- Funcion que modifica otra funcion
- Mini-proyecto: decorador que valide la contrasena ADMIN123 en vez del if

### Tema 6: Generadores (yield)
- Memoria eficiente vs listas
- Mini-proyecto: generar ids de pacientes infinitos sin guardarlos todos

### Tema 7: Type hints
- `def suma(a: int, b: int) -> int:`
- Mini-proyecto: agregar type hints a todo tu PIA2

### Tema 8: Context managers (with)
- Mas alla de archivos: crear tus propios context managers
- Mini-proyecto: `with` que conecte y cierre conexiones a la "BD"

### Tema 9: Virtual env y pip
- `python -m venv venv`
- `pip install`, requirements.txt
- Mini-proyecto: crear venv para tu PIA2 e instalar una libreria

---

## Nivel 3: Python avanzado (1-2 meses)

### Modulos y paquetes
- Crear paquetes con `__init__.py`
- Estructura de proyecto profesional

### Testing
- pytest, unittest
- Escribir tests para tu PIA2
- `assert`, fixtures

### Errores custom
- `class MiError(Exception)`
- Manejo de errores profesional

### Buenas practicas
- PEP 8 (nombres, espacios, longitud de lineas)
- Docstrings
- Codigo limpio (funciones chicas, nombres claros)

### Bases de datos
- SQLite + sqlite3
- Migrar tu PIA2 de JSON a SQLite

### API
- FastAPI o Flask basico
- Exponer tus datos de la clinica como API

---

## Regla de oro

1. Tutorial de 10-15 min para ver el patron
2. Mini-proyecto SIN copiar la solucion
3. Si falla: lee el error, googlealo, debuggea solo
4. Si llevas 30+ min atorado: pregunta/pide ayuda
5. Escribe lo aprendido en tu NOTAS.md

## Orden semanal sugerido

```
Semana 1: comprehensions, lambda/map/filter, *args/**kwargs
Semana 2: herencia, decoradores, generadores
Semana 3: type hints, context managers, venv/pip
Semana 4+: testing, errores custom, SQLite, API
```

## Que marca "soy avanzado"

- Resuelvo problemas que no he visto antes
- Refactorizo mi propio codigo sin miedo
- Escribo tests
- Manejo errores como profesional
- Documento mi codigo
- Contribuyo a proyectos open source (opcional)
