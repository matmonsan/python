# Programación en Python: fundamentos, control, errores y documentación

## Índice

1. [Introducción y objetivos](#1-introducción-y-objetivos)
2. [Identificación de los elementos de un programa](#2-identificación-de-los-elementos-de-un-programa-informático)
3. [Estructura y bloques fundamentales](#3-estructura-y-bloques-fundamentales)
4. [Variables](#4-variables)
5. [Tipos de datos](#5-tipos-de-datos)
6. [Literales](#6-literales)
7. [Constantes](#7-constantes)
8. [Operadores y expresiones](#8-operadores-y-expresiones)
9. [Conversiones de tipo](#9-conversiones-de-tipo)
10. [Comentarios](#10-comentarios)
11. [Entornos integrados de desarrollo](#11-entornos-integrados-de-desarrollo)
12. [Estructuras de control](#12-uso-de-estructuras-de-control)
13. [Selección y estructuras de selección](#13-selección-y-estructuras-de-selección)
14. [Repetición y estructuras de repetición](#14-repetición-y-estructuras-de-repetición)
15. [Estructuras de salto](#15-estructuras-de-salto)
16. [Control de excepciones](#16-control-de-excepciones)
17. [Depuración y depurador](#17-depuración-y-depurador)
18. [Documentación y documentación de programas](#18-documentación-y-documentación-de-programas)
19. [Proyecto práctico integrador](#19-proyecto-práctico-integrador)
20. [Ejercicios y actividades](#20-ejercicios-y-actividades)
21. [Soluciones orientativas](#21-soluciones-orientativas)
22. [Resumen y lista de comprobación](#22-resumen-y-lista-de-comprobación)

---

## 1. Introducción y objetivos

Python es un lenguaje de programación de propósito general, interpretado, de alto nivel y con una sintaxis diseñada para favorecer la legibilidad. Se utiliza en automatización, desarrollo web, análisis de datos, inteligencia artificial, ciencia, educación, administración de sistemas y creación de herramientas de escritorio.

Este documento presenta los fundamentos necesarios para leer, escribir, ejecutar, probar, depurar y documentar programas en Python 3. Los ejemplos se han pensado para poder copiarse en un archivo `.py` y ejecutarse con una instalación estándar de Python, sin depender de librerías externas.

Contenidos clave: variables, tipos de datos, literales, constantes, operadores y expresiones, conversiones de tipo, comentarios, entornos integrados de desarrollo, estructuras de control, selección, repetición, salto, control de excepciones, depuración, depurador y documentación.

### Objetivos de aprendizaje

Al terminar el tema, se debería poder:

- Reconocer las partes de un programa y explicar la función de cada una.
- Crear variables y seleccionar tipos de datos adecuados.
- Distinguir entre literales, variables y constantes convencionales.
- Construir expresiones usando operadores aritméticos, relacionales y lógicos.
- Convertir datos de un tipo a otro y validar entradas.
- Escribir comentarios y documentación útil.
- Utilizar un IDE para editar, ejecutar y depurar programas.
- Tomar decisiones con `if`, `elif` y `else`.
- Repetir acciones con `for` y `while`.
- Alterar el flujo con `break`, `continue`, `pass` y `return`.
- Controlar errores mediante excepciones.
- Investigar errores con mensajes, pruebas y puntos de interrupción.
- Organizar un pequeño proyecto mantenible.

### Requisito: Python 3

Los ejemplos están escritos para Python 3. En una terminal se puede comprobar la versión con:

```bash
python --version
```

En algunos sistemas el comando es:

```bash
python3 --version
```

El primer programa habitual es:

```python
print("Hola, Python")
```

`print()` es una función que escribe información en la salida estándar. La cadena está delimitada por comillas y la llamada se ejecuta al escribir los paréntesis.

---

## 2. Identificación de los elementos de un programa informático

Un programa es un conjunto ordenado de instrucciones que procesa datos para producir resultados. Aunque Python permite escribir programas muy pequeños, incluso un ejemplo de pocas líneas contiene varios elementos conceptuales.

### 2.1 Código fuente

El código fuente es el texto que escribe la persona programadora. En Python suele guardarse en archivos con extensión `.py`:

```python
nombre = input("¿Cómo te llamas? ")
mensaje = f"Hola, {nombre}"
print(mensaje)
```

El intérprete de Python lee ese código, comprueba su sintaxis y ejecuta las instrucciones. El código fuente debe ser comprensible para las personas y válido para el intérprete.

### 2.2 Instrucciones

Una instrucción es una orden que puede producir un efecto. Algunos ejemplos son una asignación, una llamada a función o una sentencia condicional:

```python
total = 25 + 10       # asignación
print(total)          # llamada a función

if total > 30:        # selección
	print("Supera 30")
```

Python utiliza el salto de línea para separar normalmente las instrucciones. También se puede usar un punto y coma, pero no es recomendable porque reduce la legibilidad.

### 2.3 Identificadores

Los identificadores son nombres que designan variables, funciones, clases, módulos u otros elementos. Sus reglas principales son:

- Pueden contener letras, dígitos y guiones bajos.
- No pueden comenzar por un dígito.
- Distinguen mayúsculas de minúsculas: `total`, `Total` y `TOTAL` son nombres distintos.
- No deben coincidir con palabras reservadas como `if`, `for`, `class` o `return`.
- Se recomienda `snake_case` para variables y funciones.

```python
precio_unitario = 12.50
cantidad = 4
importe = precio_unitario * cantidad
```

Conviene elegir nombres que expresen el significado: `edad_usuario` es preferible a `x` cuando la variable representa una edad.

### 2.4 Palabras reservadas

Python reserva determinadas palabras para su propia sintaxis. Se pueden consultar con:

```python
import keyword

print(keyword.kwlist)
```

Entre ellas están `and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `elif`, `else`, `except`, `False`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `None`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `True`, `try`, `while`, `with` y `yield`.

### 2.5 Entrada, procesamiento y salida

Un esquema muy común es **entrada -> procesamiento -> salida**:

```python
# Entrada
base = float(input("Base del rectángulo: "))
altura = float(input("Altura del rectángulo: "))

# Procesamiento
area = base * altura

# Salida
print(f"El área es {area:.2f}")
```

- **Entrada:** datos recibidos desde teclado, archivos, red, sensores o parámetros.
- **Procesamiento:** cálculos, comparaciones, transformaciones y decisiones.
- **Salida:** información mostrada, guardada o enviada a otro sistema.

### 2.6 Sintaxis y semántica

La **sintaxis** son las reglas de escritura. La **semántica** es el significado de lo escrito.

```python
print("Hola")       # sintaxis y significado correctos
```

El siguiente ejemplo tiene un error sintáctico porque falta cerrar el paréntesis:

```python
# print("Hola"
```

Este ejemplo es sintácticamente correcto, pero puede tener un error de significado si se esperaba calcular un área y se multiplican datos inadecuados:

```python
resultado = "10" * 3
print(resultado)    # produce "101010", no 30
```

### 2.7 Errores de un programa

Los errores más habituales son:

1. **Errores de sintaxis:** el código no respeta las reglas del lenguaje.
2. **Errores de ejecución:** el programa empieza, pero falla durante la ejecución, por ejemplo al dividir entre cero.
3. **Errores lógicos:** el programa se ejecuta, pero produce un resultado incorrecto.

```python
# Sintaxis: falta el signo de cierre.
# print("Hola"

# Ejecución: ZeroDivisionError.
# resultado = 10 / 0

# Lógica: la fórmula no corresponde al perímetro de un cuadrado.
lado = 5
perimetro_incorrecto = lado * lado
```

### Actividad 2.1: reconocer elementos

Analiza el siguiente código e identifica variables, literales, operadores, funciones, entrada, procesamiento y salida:

```python
precio = float(input("Precio: "))
unidades = int(input("Unidades: "))
descuento = 0.10
total = precio * unidades * (1 - descuento)
print(f"Total: {total:.2f}")
```

---

## 3. Estructura y bloques fundamentales

Python utiliza la indentación para delimitar bloques de código. Esto diferencia a Python de lenguajes que emplean llaves, y hace que la presentación visual del programa forme parte de su sintaxis.

### 3.1 Indentación

Después de una línea que termina en dos puntos, las instrucciones del bloque se escriben indentadas:

```python
edad = 20

if edad >= 18:
	print("Es mayor de edad")
	print("Puede continuar")
```

La recomendación habitual es usar cuatro espacios por nivel. No se deben mezclar tabuladores y espacios en el mismo bloque.

```python
if True:
	mensaje = "Este bloque tiene cuatro espacios"
	print(mensaje)
```

### 3.2 Bloques anidados

Un bloque puede contener otro bloque. Cada nivel añade una indentación:

```python
temperatura = 26
llueve = False

if temperatura > 20:
	if llueve:
		print("Temperatura agradable y lluvia")
	else:
		print("Temperatura agradable y tiempo seco")
```

Cuando hay muchos niveles anidados, suele ser mejor reorganizar la lógica con condiciones compuestas o funciones.

### 3.3 Módulos y función `main`

Un archivo `.py` puede usarse como programa ejecutable y como módulo importable. El patrón siguiente separa la definición de la ejecución:

```python
def saludar(nombre):
	return f"Hola, {nombre}"


def main():
	nombre = input("Nombre: ")
	print(saludar(nombre))


if __name__ == "__main__":
	main()
```

`__name__` vale `"__main__"` cuando el archivo se ejecuta directamente. Si se importa desde otro archivo, la llamada a `main()` no se produce automáticamente.

### 3.4 Funciones como bloques reutilizables

Una función agrupa instrucciones con un nombre y puede recibir parámetros y devolver un resultado:

```python
def calcular_iva(precio, porcentaje=21):
	"""Devuelve el importe del IVA para un precio dado."""
	return precio * porcentaje / 100


iva = calcular_iva(100)
print(iva)
```

Las funciones reducen la duplicación, facilitan las pruebas y permiten dividir un problema grande en tareas pequeñas.

### 3.5 Alcance de los nombres

Una variable creada dentro de una función suele ser local a esa función:

```python
def crear_mensaje():
	mensaje = "Solo existe dentro de la función"
	return mensaje


resultado = crear_mensaje()
print(resultado)
```

Es preferible pasar datos como argumentos y devolver resultados, en lugar de depender de variables globales.

### Actividad 3.1: modularizar

Transforma un programa que calcule el área y el perímetro de un círculo en tres funciones: una para el área, otra para el perímetro y otra función `main()` para interactuar con la persona usuaria.

---

## 4. Variables

Una variable es un nombre asociado a un objeto almacenado en memoria. En Python no se declara previamente el tipo de la variable: el tipo pertenece al objeto y el nombre puede volver a asociarse a otro objeto.

### 4.1 Asignación

El operador `=` asigna una referencia:

```python
nombre = "Ana"
edad = 28
activo = True
```

La asignación se evalúa de derecha a izquierda. Primero se calcula el valor y después se vincula al nombre.

```python
total = 10 + 5 * 2
print(total)  # 20
```

### 4.2 Reasignación

Una variable puede cambiar de valor y, técnicamente, incluso de tipo:

```python
valor = 10
valor = 20
valor = "veinte"
```

Aunque es posible, cambiar de tipo sin una razón clara puede dificultar la lectura. Es mejor mantener un significado estable para cada variable.

### 4.3 Asignación múltiple y desempaquetado

```python
ancho, alto = 800, 600
print(ancho, alto)

primero, segundo = segundo, primero
```

El desempaquetado también funciona con listas y tuplas si el número de elementos coincide:

```python
coordenada = (10, 25)
x, y = coordenada
```

### 4.4 Variables mutables e inmutables

Los enteros, flotantes, cadenas, booleanos y tuplas son inmutables: una operación produce otro objeto en lugar de modificar el original. Las listas, diccionarios y conjuntos son mutables.

```python
texto = "hola"
texto = texto.upper()  # se crea otra cadena

numeros = [1, 2]
numeros.append(3)       # se modifica la lista
```

### 4.5 Convenciones de nombres

```python
nombre_completo = "Lucía García"
numero_de_intentos = 3
MAXIMO_REINTENTOS = 5
```

Se recomienda:

- Variables y funciones: `snake_case`.
- Clases: `PascalCase`.
- Constantes convencionales: `MAYUSCULAS_CON_GUIONES_BAJOS`.
- Evitar nombres de una sola letra salvo índices sencillos como `i` en bucles cortos.
- Evitar nombres demasiado genéricos como `dato`, `cosa` o `resultado` si existe una descripción mejor.

### 4.6 Comprobar el tipo y la identidad

```python
numero = 42
print(type(numero))
print(isinstance(numero, int))
```

`type()` muestra el tipo exacto. `isinstance()` comprueba si un objeto pertenece a un tipo o a una familia de tipos y suele ser más flexible.

El operador `is` comprueba identidad, no igualdad:

```python
valor = None
if valor is None:
	print("No hay valor")
```

Para comparar contenidos se usa `==`.

### Error frecuente: usar una variable antes de asignarla

```python
# print(nombre)  # NameError
nombre = "Mario"
```

El orden de las instrucciones importa. Una variable debe existir antes de utilizarse.

---

## 5. Tipos de datos

Un tipo describe qué clase de valor representa un objeto y qué operaciones son válidas sobre él. Python ofrece tipos integrados y permite crear tipos propios mediante clases.

### 5.1 Booleanos: `bool`

Solo existen dos valores booleanos: `True` y `False`.

```python
es_mayor = 18 >= 18
print(es_mayor)       # True
print(type(es_mayor)) # <class 'bool'>
```

Los booleanos aparecen en condiciones y expresiones lógicas.

### 5.2 Enteros: `int`

Representan números sin parte decimal y pueden ser positivos, negativos o cero.

```python
usuarios = 150
temperatura = -3
```

Python permite literales en distintas bases:

```python
decimal = 42
binario = 0b101010
octal = 0o52
hexadecimal = 0x2A
```

Todos representan el mismo valor decimal: 42.

### 5.3 Reales: `float`

Representan números con parte decimal usando punto:

```python
pi_aproximado = 3.14159
saldo = -15.75
```

Los `float` usan representación de punto flotante. Por eso algunas operaciones no son exactas en binario:

```python
print(0.1 + 0.2)  # puede mostrar 0.30000000000000004
```

Para dinero se recomienda considerar `decimal.Decimal`:

```python
from decimal import Decimal

precio = Decimal("0.10")
cantidad = Decimal("0.20")
print(precio + cantidad)
```

### 5.4 Complejos: `complex`

Un número complejo tiene una parte real y otra imaginaria:

```python
z = 3 + 4j
print(z.real)
print(z.imag)
```

Se usa principalmente en contextos científicos y matemáticos.

### 5.5 Cadenas: `str`

Una cadena es una secuencia inmutable de caracteres Unicode:

```python
nombre = "Ada Lovelace"
saludo = 'Hola'
texto_largo = """Primera línea
Segunda línea"""
```

Operaciones comunes:

```python
texto = "Python"
print(len(texto))
print(texto[0])
print(texto[-1])
print(texto[0:3])
print(texto.lower())
print(texto.upper())
print("th" in texto)
```

La indexación empieza en cero. El corte `texto[inicio:fin]` incluye `inicio` y excluye `fin`.

### 5.6 Listas: `list`

Una lista es una colección ordenada y mutable:

```python
frutas = ["manzana", "pera", "uva"]
frutas.append("kiwi")
frutas[0] = "plátano"
print(frutas)
```

Operaciones habituales:

```python
numeros = [4, 1, 8, 2]
numeros.sort()
print(numeros)
print(len(numeros))
print(sum(numeros))
```

Una lista puede mezclar tipos, aunque en código mantenible suele ser preferible que represente elementos homogéneos.

### 5.7 Tuplas: `tuple`

Una tupla es una secuencia ordenada e inmutable:

```python
punto = (10, 20)
x, y = punto
```

La tupla de un solo elemento necesita una coma:

```python
un_elemento = (7,)
```

### 5.8 Conjuntos: `set`

Un conjunto no mantiene duplicados y resulta útil para pertenencia y operaciones de conjuntos:

```python
colores = {"rojo", "verde", "rojo"}
print(colores)  # solo contiene un "rojo"

permitidos = {"admin", "editor"}
solicitados = {"editor", "invitado"}
print(permitidos & solicitados)
print(permitidos | solicitados)
```

Un conjunto vacío se crea con `set()`, no con `{}`, porque `{}` representa un diccionario vacío.

### 5.9 Diccionarios: `dict`

Un diccionario almacena asociaciones clave-valor:

```python
persona = {
	"nombre": "Elena",
	"edad": 31,
	"activo": True,
}

print(persona["nombre"])
persona["ciudad"] = "Valencia"
```

Para evitar un error cuando la clave no existe:

```python
telefono = persona.get("telefono", "No disponible")
```

### 5.10 `None`

`None` representa la ausencia intencionada de valor:

```python
resultado = None
if resultado is None:
	print("Todavía no hay resultado")
```

No debe confundirse con `0`, `False` o una cadena vacía, aunque todos pueden considerarse falsos en un contexto booleano.

### 5.11 Valores verdaderos y falsos

En una condición se consideran falsos `False`, `None`, `0`, `0.0`, `""`, `[]`, `()`, `{}` y `set()`. La mayoría de los demás objetos son verdaderos.

```python
nombre = ""
if not nombre:
	print("El nombre está vacío")
```

### Actividad 5.1: elección de tipos

Asigna un tipo apropiado a cada dato: nombre de una persona, número de matrícula, precio, lista de asignaturas, coordenadas GPS, permisos de usuario y ausencia de fecha de cierre. Justifica cada elección.

---

## 6. Literales

Un literal es una notación escrita directamente en el código para representar un valor. No es lo mismo un literal que una variable: `25` es un literal entero, mientras que `edad` es un nombre que puede referirse a un objeto entero.

### 6.1 Literales numéricos

```python
entero = 100
negativo = -25
real = 2.5
notacion_cientifica = 1.2e3
binario = 0b1101
```

Se pueden utilizar guiones bajos para mejorar la lectura:

```python
presupuesto = 1_000_000
```

### 6.2 Literales booleanos y nulo

```python
disponible = True
eliminado = False
sin_resultado = None
```

### 6.3 Literales de cadena

```python
uno = "cadena"
dos = 'cadena'
multilinea = """texto
con varias líneas"""
```

Caracteres especiales:

```python
mensaje = "Primera línea\nSegunda línea"
ruta = r"C:\\Users\\Ana\\archivo.txt"
```

La `r` crea una cadena cruda, útil para rutas y expresiones regulares. Las f-strings permiten insertar expresiones:

```python
producto = "libro"
precio = 19.9
print(f"{producto}: {precio:.2f} €")
```

### 6.4 Literales de colecciones

```python
lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
diccionario = {"uno": 1, "dos": 2}
```

### 6.5 Literales con comprensión

Las comprensiones crean colecciones de forma declarativa:

```python
cuadrados = [numero ** 2 for numero in range(1, 6)]
pares = {numero for numero in range(10) if numero % 2 == 0}
longitudes = {palabra: len(palabra) for palabra in ["sol", "luna"]}
```

No deben utilizarse para ocultar una lógica compleja; si la expresión deja de ser clara, un bucle normal es mejor.

---

## 7. Constantes

Python no impone constantes inmutables mediante una palabra reservada. La convención consiste en escribir en mayúsculas los nombres cuyo valor no debería cambiar durante la ejecución:

```python
PI = 3.141592653589793
MAX_INTENTOS = 3
NOMBRE_APLICACION = "Gestor de tareas"
```

La convención comunica una intención, pero no impide la reasignación:

```python
MAX_INTENTOS = 3
MAX_INTENTOS = 10  # Python lo permite, aunque puede ser un error de diseño
```

### 7.1 Constantes agrupadas en un módulo

Archivo `configuracion.py`:

```python
TASA_IVA = 0.21
MONEDA = "EUR"
```

Otro archivo puede importarlas:

```python
from configuracion import TASA_IVA

precio_final = 100 * (1 + TASA_IVA)
```

### 7.2 `Final` para expresar intención estática

El módulo `typing` permite indicar que un nombre no debería reasignarse. Es una ayuda para herramientas de análisis, no una barrera durante la ejecución:

```python
from typing import Final

PI: Final = 3.141592653589793
```

### 7.3 Cuándo usar constantes

Una constante es apropiada para valores que:

- Se repiten en varios lugares.
- Tienen un significado de negocio o configuración.
- Podrían cambiar en el futuro en un único punto.
- No dependen de los datos de una ejecución concreta.

Es mejor escribir `SEGUNDOS_POR_MINUTO = 60` que repetir el número `60` sin explicar su significado.

---

## 8. Operadores y expresiones

Una expresión combina valores, variables, operadores y llamadas para producir un resultado.

### 8.1 Operadores aritméticos

```python
a = 17
b = 5

print(a + b)   # suma: 22
print(a - b)   # resta: 12
print(a * b)   # multiplicación: 85
print(a / b)   # división real: 3.4
print(a // b)  # división entera: 3
print(a % b)   # resto: 2
print(a ** b)  # potencia: 1419857
```

`/` siempre produce una división real. `//` redondea hacia abajo, lo que conviene tener en cuenta con números negativos:

```python
print(-7 // 3)  # -3
```

### 8.2 Operadores de comparación

Devuelven `True` o `False`:

```python
edad = 20
print(edad == 20)
print(edad != 18)
print(edad > 18)
print(edad >= 20)
print(edad < 30)
print(edad <= 20)
```

### 8.3 Operadores lógicos

```python
es_mayor = edad >= 18
tiene_entrada = True

print(es_mayor and tiene_entrada)
print(es_mayor or tiene_entrada)
print(not tiene_entrada)
```

`and` devuelve el primer operando falso o el último si todos son verdaderos. `or` devuelve el primer operando verdadero o el último si todos son falsos. Esta evaluación perezosa permite patrones como:

```python
nombre = entrada.strip() if entrada else "Anónimo"
```

### 8.4 Operadores de pertenencia

```python
frutas = ["pera", "uva"]
print("uva" in frutas)
print("manzana" not in frutas)
```

En un diccionario, `in` comprueba claves:

```python
persona = {"nombre": "Ana"}
print("nombre" in persona)
```

### 8.5 Operadores de identidad

```python
valor = None
print(valor is None)
print(valor is not None)
```

Para valores ordinarios se debe usar `==`, no `is`:

```python
primero = [1, 2]
segundo = [1, 2]
print(primero == segundo)  # mismo contenido
print(primero is segundo)  # objetos distintos
```

### 8.6 Operadores de asignación aumentada

```python
contador = 0
contador += 1
contador *= 2
contador -= 1
```

También existen `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=` y `>>=`.

### 8.7 Operadores bit a bit

Se aplican a enteros representados en binario:

```python
a = 0b1100
b = 0b1010
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)
```

Se usan en máscaras, permisos y programación de bajo nivel. No deben confundirse con `and` y `or`.

### 8.8 Precedencia y paréntesis

Python sigue una precedencia parecida a la matemática:

1. Paréntesis.
2. Potencias.
3. Signos unarios.
4. Multiplicación, división, división entera y resto.
5. Suma y resta.
6. Comparaciones.
7. `not`.
8. `and`.
9. `or`.

```python
resultado = 2 + 3 * 4       # 14
resultado_claro = (2 + 3) * 4  # 20
```

Los paréntesis son recomendables cuando mejoran la intención, incluso si no son estrictamente necesarios.

### 8.9 Expresiones condicionales

```python
edad = 17
tipo = "adulto" if edad >= 18 else "menor"
```

Conviene reservarlas para condiciones simples. Una expresión condicional anidada suele ser menos legible que un `if` normal.

### Actividad 8.1: calcular una factura

Crea un programa que lea precio, unidades y porcentaje de descuento, calcule subtotal, descuento, IVA y total, y muestre cada importe con dos decimales. Añade una condición que indique si el pedido supera un umbral de envío gratuito.

---

## 9. Conversiones de tipo

La conversión transforma un valor en otro tipo cuando la operación es válida. La entrada de `input()` siempre devuelve una cadena, incluso si la persona escribe un número.

```python
edad_texto = input("Edad: ")
edad = int(edad_texto)
```

### 9.1 Conversiones habituales

```python
print(int("42"))
print(float("3.14"))
print(str(2025))
print(bool(1))
print(list("abc"))
print(tuple([1, 2]))
print(set([1, 1, 2]))
```

### 9.2 Conversión explícita frente a implícita

Python realiza alguna promoción numérica automáticamente:

```python
resultado = 5 + 2.5  # 7.5, un float
```

Pero no concatena automáticamente una cadena y un entero:

```python
edad = 25
print("Edad: " + str(edad))
print(f"Edad: {edad}")
```

### 9.3 Validar antes de convertir

Comprobar un texto antes de convertirlo puede evitar errores simples:

```python
texto = input("Introduce un entero: ").strip()
if texto.lstrip("+-").isdigit():
	numero = int(texto)
	print(numero * 2)
else:
	print("El valor no es un entero válido")
```

Para casos reales, `try` y `except` son más generales porque aceptan formatos que una comprobación textual podría no cubrir bien.

### 9.4 Conversiones con pérdida

```python
print(int(3.99))  # 3, trunca la parte decimal
```

Si se necesita redondear se puede usar `round()`:

```python
print(round(3.99))
print(round(3.14159, 2))
```

### 9.5 Conversiones de estructuras

```python
texto = "rojo,verde,azul"
colores = [elemento.strip() for elemento in texto.split(",")]
print(colores)

pares = [("a", 1), ("b", 2)]
diccionario = dict(pares)
print(diccionario)
```

### Actividad 9.1: entrada robusta

Escribe una función `leer_entero(mensaje, minimo, maximo)` que repita la petición hasta recibir un entero dentro del intervalo. Debe controlar tanto entradas no numéricas como valores fuera del rango.

---

## 10. Comentarios

Los comentarios son texto para las personas que leen el código. El intérprete los ignora. Sirven para explicar intención, decisiones o advertencias, no para repetir literalmente lo que hace cada línea.

### 10.1 Comentarios de una línea

```python
# El descuento se aplica antes del IVA.
subtotal = precio * unidades
descuento = subtotal * porcentaje_descuento
```

Un comentario al final de línea debe ser corto:

```python
limite = 100  # Máximo permitido por el negocio
```

### 10.2 Cadenas multilínea y docstrings

Las cadenas triples pueden utilizarse como docstrings cuando aparecen al principio de un módulo, clase o función:

```python
def cuadrado(numero):
	"""Devuelve el cuadrado de numero."""
	return numero ** 2
```

Una cadena triple colocada en cualquier lugar sin asignarla no es una buena forma de comentar. Para documentar elementos públicos se deben usar docstrings.

### 10.3 Qué comentar

Es útil comentar:

- Por qué se toma una decisión no evidente.
- Una limitación externa o regla de negocio.
- La razón de una solución aparentemente poco habitual.
- Un algoritmo complejo o una fórmula especializada.

No es útil escribir comentarios que contradigan el código o repitan nombres obvios:

```python
# Incrementa contador en uno
contador += 1
```

### 10.4 Comentarios temporales

Los comentarios `TODO` pueden señalar trabajo pendiente:

```python
# TODO: sustituir este almacenamiento temporal por una base de datos.
```

Deben revisarse antes de entregar el proyecto; un `TODO` olvidado puede indicar una funcionalidad incompleta.

---

## 11. Entornos integrados de desarrollo

Un IDE (Integrated Development Environment, entorno integrado de desarrollo) reúne herramientas para escribir, ejecutar y mantener programas. Para Python, opciones habituales son Visual Studio Code, PyCharm, IDLE y JupyterLab.

### 11.1 Componentes de un IDE

Un IDE suele incluir:

- Editor con resaltado de sintaxis.
- Autocompletado y navegación de símbolos.
- Terminal integrada.
- Ejecución y configuración de programas.
- Depurador con puntos de interrupción.
- Integración con Git.
- Diagnósticos de sintaxis y tipos.
- Herramientas de formato y análisis estático.
- Explorador de archivos y gestión de entornos.

### 11.2 Flujo de trabajo en Visual Studio Code

Un flujo básico es:

1. Abrir la carpeta del proyecto.
2. Instalar la extensión de Python de Microsoft.
3. Seleccionar un intérprete con `Python: Select Interpreter`.
4. Crear un archivo como `main.py`.
5. Escribir el programa y guardarlo.
6. Ejecutarlo desde el botón de ejecución o la terminal.
7. Revisar diagnósticos y corregirlos.
8. Ejecutar pruebas y depurar con puntos de interrupción.

### 11.3 Entornos virtuales

Un entorno virtual aísla dependencias de un proyecto:

```bash
python -m venv .venv
```

Activación en Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Activación en macOS o Linux:

```bash
source .venv/bin/activate
```

Después se pueden instalar paquetes sin afectar a otras aplicaciones:

```bash
python -m pip install nombre-paquete
```

Es buena práctica guardar dependencias:

```bash
python -m pip freeze > requirements.txt
```

### 11.4 Formateo y análisis

Herramientas populares son `black` para formato y `ruff` para análisis y estilo. Si se utilizan en un proyecto, deben configurarse y ejecutarse de forma consistente. El objetivo no es obedecer mecánicamente a una herramienta, sino reducir errores y discusiones de estilo.

### 11.5 Ejecutar desde la terminal

```bash
python main.py
```

Ejecutar mediante `python -m` es útil para módulos y paquetes:

```bash
python -m mi_paquete
```

### Actividad 11.1: preparar un entorno

Crea una carpeta de proyecto, genera `.venv`, selecciona el intérprete en el IDE, crea `main.py`, ejecuta un saludo y documenta en un `README.md` los pasos de instalación y ejecución.

---

## 12. Uso de estructuras de control

Las estructuras de control determinan el orden en que se ejecutan las instrucciones. Sin ellas, un programa solo avanzaría de arriba abajo una vez.

Las tres familias principales son:

- **Secuencia:** instrucciones en orden.
- **Selección:** elegir entre caminos.
- **Repetición:** ejecutar un bloque varias veces.

### 12.1 Secuencia

```python
nombre = input("Nombre: ")
saludo = f"Hola, {nombre}"
print(saludo)
```

### 12.2 Condición como expresión booleana

```python
saldo = 100
retirada = 40

if retirada <= saldo:
	saldo -= retirada
```

### 12.3 Repetición controlada por colección

```python
for numero in [1, 2, 3]:
	print(numero)
```

### 12.4 Repetición controlada por condición

```python
respuesta = ""
while respuesta.lower() != "salir":
	respuesta = input("Escribe salir para terminar: ")
```

### 12.5 Diseñar antes de codificar

Antes de escribir estructuras de control conviene responder:

1. ¿Qué datos entran?
2. ¿Qué resultado debe producirse?
3. ¿Qué decisiones existen?
4. ¿Qué acciones se repiten?
5. ¿Cuándo termina el programa?
6. ¿Qué pasa si la entrada no es válida?

Un pseudocódigo sencillo para clasificar una nota sería:

```text
leer nota
si nota no está entre 0 y 10:
	mostrar error
si nota es al menos 5:
	mostrar aprobado
si no:
	mostrar suspenso
```

---

## 13. Selección y estructuras de selección

Las estructuras de selección ejecutan uno u otro bloque según una condición.

### 13.1 `if`

```python
temperatura = 28

if temperatura > 25:
	print("Hace calor")
```

Si la condición es falsa, el bloque no se ejecuta.

### 13.2 `if ... else`

```python
numero = 7

if numero % 2 == 0:
	print("Es par")
else:
	print("Es impar")
```

### 13.3 `if ... elif ... else`

```python
nota = 8.4

if nota >= 9:
	calificacion = "sobresaliente"
elif nota >= 7:
	calificacion = "notable"
elif nota >= 5:
	calificacion = "aprobado"
else:
	calificacion = "suspenso"

print(calificacion)
```

Las condiciones se evalúan de arriba abajo y solo se ejecuta el primer bloque verdadero.

### 13.4 Condiciones compuestas

```python
edad = 25
documento_valido = True

if edad >= 18 and documento_valido:
	print("Acceso permitido")
```

### 13.5 Guard clauses

Una guard clause termina pronto un caso inválido y evita anidamientos:

```python
def procesar_edad(edad):
	if edad < 0:
		return "Edad no válida"
	if edad < 18:
		return "Menor"
	return "Adulto"
```

### 13.6 `match` y `case`

Desde Python 3.10 se puede hacer coincidencia estructural:

```python
comando = "listar"

match comando:
	case "crear":
		print("Creando")
	case "listar":
		print("Listando")
	case "salir":
		print("Saliendo")
	case _:
		print("Comando desconocido")
```

`match` es útil cuando hay muchos patrones posibles. Para una sola condición booleana, `if` suele ser más claro.

### 13.7 Evitar comparaciones innecesarias

```python
activo = True

if activo:
	print("Activo")

# Menos idiomático:
# if activo == True:
#     print("Activo")
```

### Actividad 13.1: menú

Crea un menú con las opciones `1. Añadir`, `2. Consultar`, `3. Eliminar` y `4. Salir`. Usa una estructura de selección y muestra un mensaje específico para cada opción. La opción desconocida debe producir un aviso.

---

## 14. Repetición y estructuras de repetición

Los bucles permiten repetir acciones sin duplicar código.

### 14.1 Bucle `for`

`for` recorre elementos de un iterable:

```python
for letra in "Python":
	print(letra)
```

Con `range()`:

```python
for numero in range(5):
	print(numero)  # 0, 1, 2, 3, 4

for numero in range(2, 10, 2):
	print(numero)  # 2, 4, 6, 8
```

El límite final de `range()` no se incluye.

### 14.2 Recorrer listas y diccionarios

```python
precios = [10.5, 8.0, 12.25]
total = 0

for precio in precios:
	total += precio

for clave, valor in {"a": 1, "b": 2}.items():
	print(clave, valor)
```

`enumerate()` aporta índice y valor:

```python
for indice, fruta in enumerate(["pera", "uva"], start=1):
	print(indice, fruta)
```

`zip()` recorre varias secuencias a la vez:

```python
nombres = ["Ana", "Luis"]
edades = [22, 30]

for nombre, edad in zip(nombres, edades):
	print(f"{nombre}: {edad}")
```

### 14.3 Bucle `while`

Se repite mientras una condición sea verdadera:

```python
contador = 3
while contador > 0:
	print(contador)
	contador -= 1
print("Fin")
```

Hay que modificar alguna variable de control o usar una salida para evitar bucles infinitos.

### 14.4 Menús repetitivos

```python
while True:
	opcion = input("1) Saludar  2) Salir: ").strip()
	if opcion == "1":
		print("Hola")
	elif opcion == "2":
		break
	else:
		print("Opción no válida")
```

### 14.5 Comprensiones

```python
pares = [numero for numero in range(20) if numero % 2 == 0]
```

Una comprensión equivale conceptualmente a un bucle que construye una colección, pero debe mantenerse sencilla.

### 14.6 `else` en bucles

El `else` de un bucle se ejecuta si el bucle termina normalmente, no si se interrumpe con `break`:

```python
for numero in range(2, 10):
	if numero == 7:
		print("Encontrado")
		break
else:
	print("No encontrado")
```

### 14.7 Evitar modificar una colección mientras se recorre

Puede provocar resultados inesperados. Es más seguro construir otra colección:

```python
numeros = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
```

### Actividad 14.1: estadísticas

Pide números hasta que se escriba `fin`. Guarda los válidos y muestra cantidad, suma, media, mínimo y máximo. Decide qué debe ocurrir si no se introduce ningún número.

---

## 15. Estructuras de salto

Las estructuras de salto modifican el flujo habitual de un bucle o una función.

### 15.1 `break`

Termina el bucle más cercano:

```python
for numero in range(100):
	if numero == 10:
		break
	print(numero)
```

### 15.2 `continue`

Salta el resto de la iteración actual y continúa con la siguiente:

```python
for numero in range(1, 11):
	if numero % 2 == 0:
		continue
	print(numero)  # solo impares
```

### 15.3 `pass`

No hace nada; sirve como marcador sintáctico temporal:

```python
def funcionalidad_pendiente():
	pass
```

No debe utilizarse para ocultar errores ni como sustituto permanente de una implementación requerida.

### 15.4 `return`

Termina una función y puede entregar un valor:

```python
def es_par(numero):
	return numero % 2 == 0
```

Un `return` sin valor devuelve `None`.

### 15.5 `raise`

Lanza una excepción de manera explícita:

```python
def dividir(a, b):
	if b == 0:
		raise ValueError("El divisor no puede ser cero")
	return a / b
```

### 15.6 `yield`

`yield` convierte una función en generador y produce valores de uno en uno:

```python
def contar_hasta(limite):
	for numero in range(1, limite + 1):
		yield numero


for numero in contar_hasta(3):
	print(numero)
```

Los generadores pueden ahorrar memoria cuando la secuencia es grande.

### Criterio de diseño

Los saltos son herramientas útiles, pero demasiados `break`, `continue` y retornos dispersos pueden dificultar la lectura. Cada salto debería hacer evidente qué condición lo provoca y por qué mejora el algoritmo.

---

## 16. Control de excepciones

Una excepción es un evento que interrumpe el flujo normal porque se ha producido una situación excepcional: entrada inválida, archivo inexistente, división por cero o fallo de red.

### 16.1 Excepción básica

```python
numero = int("no es un número")  # ValueError
```

El intérprete muestra el tipo de excepción, el mensaje y el traceback, que indica la ruta de llamadas hasta el error.

### 16.2 `try` y `except`

```python
try:
	edad = int(input("Edad: "))
except ValueError:
	print("Debes introducir un entero")
```

Se debe capturar la excepción concreta que se sabe manejar. Capturar `Exception` sin una razón clara puede ocultar errores de programación.

### 16.3 `else`

El bloque `else` se ejecuta solo si no ocurrió una excepción:

```python
try:
	numero = int(input("Número: "))
except ValueError:
	print("Entrada inválida")
else:
	print(f"El doble es {numero * 2}")
```

### 16.4 `finally`

`finally` se ejecuta ocurra o no una excepción. Es útil para limpieza:

```python
archivo = None
try:
	archivo = open("datos.txt", encoding="utf-8")
	contenido = archivo.read()
except FileNotFoundError:
	print("No existe el archivo")
finally:
	if archivo is not None:
		archivo.close()
```

Para archivos se recomienda `with`, que gestiona el cierre automáticamente:

```python
try:
	with open("datos.txt", encoding="utf-8") as archivo:
		contenido = archivo.read()
except FileNotFoundError:
	contenido = ""
```

### 16.5 Varias excepciones

```python
try:
	valor = int(input("Dividendo: "))
	divisor = int(input("Divisor: "))
	resultado = valor / divisor
except ValueError:
	print("Los dos valores deben ser enteros")
except ZeroDivisionError:
	print("No se puede dividir entre cero")
else:
	print(resultado)
```

### 16.6 Capturar como variable

```python
try:
	numero = int("abc")
except ValueError as error:
	print(f"Detalle: {error}")
```

### 16.7 Lanzar excepciones propias

```python
def establecer_porcentaje(porcentaje):
	if not 0 <= porcentaje <= 100:
		raise ValueError("El porcentaje debe estar entre 0 y 100")
	return porcentaje
```

### 16.8 Excepciones personalizadas

```python
class SaldoInsuficienteError(Exception):
	"""Indica que una operación supera el saldo disponible."""


def retirar(saldo, cantidad):
	if cantidad > saldo:
		raise SaldoInsuficienteError("Saldo insuficiente")
	return saldo - cantidad
```

### 16.9 Encadenamiento de excepciones

```python
def leer_entero_desde_texto(texto):
	try:
		return int(texto)
	except ValueError as error:
		raise ValueError("El texto no contiene un entero") from error
```

`from error` conserva la causa original y facilita el diagnóstico.

### 16.10 Buenas prácticas

- Capturar la excepción más específica posible.
- Mantener el bloque `try` pequeño.
- No usar `except: pass` salvo casos muy justificados.
- Mostrar mensajes útiles para la persona usuaria.
- Registrar detalles técnicos cuando el programa sea una aplicación real.
- No utilizar excepciones para sustituir todas las condiciones normales.
- Liberar recursos con `with` o `finally`.

### Actividad 16.1: validador resistente

Implementa un conversor de temperatura que acepte Celsius y Fahrenheit, rechace unidades desconocidas y controle entradas no numéricas sin finalizar abruptamente.

---

## 17. Depuración y depurador

Depurar es localizar y corregir defectos. No consiste simplemente en leer el código al azar: requiere formular hipótesis, observar el comportamiento y comprobarlas con evidencia.

### 17.1 Proceso sistemático

1. Reproducir el error con una entrada concreta.
2. Leer todo el mensaje y el traceback.
3. Identificar la línea donde se manifiesta el problema.
4. Distinguir síntoma de causa.
5. Formular una hipótesis.
6. Inspeccionar valores y flujo.
7. Aplicar el cambio mínimo que corrija la causa.
8. Repetir la prueba y ejecutar regresiones.

### 17.2 `print()` como observación rápida

```python
def calcular_total(precio, unidades):
	subtotal = precio * unidades
	print(f"DEBUG subtotal={subtotal!r}")
	return subtotal
```

`repr()` muestra una representación útil para detectar espacios, saltos de línea o tipos inesperados:

```python
entrada = input("Texto: ")
print(repr(entrada))
```

Los mensajes temporales deben retirarse o sustituirse por logging al terminar.

### 17.3 Afirmaciones

`assert` comprueba una condición que se considera cierta durante el desarrollo:

```python
def calcular_media(total, cantidad):
	assert cantidad > 0, "La cantidad debe ser positiva"
	return total / cantidad
```

No se debe usar `assert` para validar entradas externas en producción, porque las aserciones pueden desactivarse.

### 17.4 Pruebas pequeñas

```python
def es_par(numero):
	return numero % 2 == 0


assert es_par(2) is True
assert es_par(3) is False
```

Las pruebas deben incluir casos normales, límites y entradas inválidas.

### 17.5 Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Aplicación iniciada")
logger.warning("El archivo de configuración no existe")
```

Los niveles habituales son `DEBUG`, `INFO`, `WARNING`, `ERROR` y `CRITICAL`.

### 17.6 Errores lógicos

Un programa puede no producir excepciones y aun así estar mal:

```python
def calcular_media(numeros):
	return sum(numeros) / len(numeros)
```

Hay que decidir qué ocurre con una lista vacía. El problema no se resuelve solo capturando excepciones; se debe definir el contrato de la función.

---

## 18. El depurador como herramienta de control de errores

El depurador permite ejecutar un programa paso a paso e inspeccionar su estado interno.

### 18.1 Conceptos principales

- **Breakpoint o punto de interrupción:** línea donde se pausa la ejecución.
- **Step over:** ejecuta la línea actual sin entrar en una función llamada.
- **Step into:** entra en la función llamada.
- **Step out:** termina la función actual y vuelve al llamador.
- **Continue:** continúa hasta el siguiente punto de interrupción.
- **Call stack:** cadena de funciones activas.
- **Variables locales:** nombres disponibles en el contexto actual.
- **Watch o expresión vigilada:** valor que se observa mientras se avanza.

### 18.2 Depurar en Visual Studio Code

1. Abre el archivo Python.
2. Haz clic a la izquierda de un número de línea para colocar un punto rojo.
3. Inicia `Run and Debug`.
4. Elige el depurador de Python si se solicita.
5. Cuando se detenga, observa `Variables`, `Watch` y `Call Stack`.
6. Avanza con `Step Over` y observa cuándo cambia cada valor.
7. Usa `Continue` para comprobar otros puntos.

Ejemplo preparado para depuración:

```python
def aplicar_descuento(precio, porcentaje):
	descuento = precio * porcentaje / 100
	total = precio - descuento
	return total


def main():
	precios = [10.0, 25.0, 40.0]
	porcentaje = 10
	totales = []
	for precio in precios:
		totales.append(aplicar_descuento(precio, porcentaje))
	print(totales)


if __name__ == "__main__":
	main()
```

Colocar un breakpoint en `descuento` permite observar los parámetros y verificar cada iteración.

### 18.3 Depurar desde la biblioteca estándar

Python incluye `pdb`:

```python
def calcular(numero):
	resultado = numero * 2
	breakpoint()
	return resultado + 1


print(calcular(5))
```

En la consola de `pdb` se pueden usar comandos como `n` (next), `s` (step), `p` para imprimir una expresión, `l` para listar código y `c` para continuar.

### 18.4 Depuración remota y configuración

Para proyectos complejos se puede crear `.vscode/launch.json` con configuraciones de ejecución, argumentos, variables de entorno y directorio de trabajo. La configuración debe adaptarse al proyecto y no debe contener secretos.

### 18.5 Estrategias para localizar un error

- Reducir el caso a la entrada mínima que falla.
- Dividir el flujo y comprobar invariantes.
- Comparar un resultado esperado con el real.
- Revisar tipos con `type()` o `isinstance()`.
- Inspeccionar espacios con `repr()`.
- Revisar índices y límites de rangos.
- Probar los valores frontera: cero, vacío, uno, máximo y mínimo.

### Actividad 18.1: depuración guiada

Depura este programa y explica qué ocurre con `total`:

```python
precios = [10, 20, 30]
total = 0

for precio in precios:
	total = precio

print(total)
```

El resultado esperado es 60. Coloca un breakpoint dentro del bucle, observa el valor en cada vuelta y corrige la instrucción.

---

## 18. Documentación y documentación de programas

Documentar es explicar cómo usar, mantener y comprender un programa. Una buena documentación reduce el tiempo de incorporación y evita que las decisiones importantes dependan de conversaciones informales.

### 19.1 README

Un `README.md` debería incluir, según el proyecto:

- Propósito.
- Requisitos.
- Instalación.
- Activación del entorno virtual.
- Ejecución.
- Uso con ejemplos.
- Ejecución de pruebas.
- Estructura de carpetas.
- Configuración.
- Limitaciones conocidas.
- Contribución y licencia si corresponde.

Ejemplo de estructura:

```text
mi_proyecto/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── mi_app/
│       ├── __init__.py
│       └── main.py
└── tests/
	└── test_main.py
```

### 19.2 Docstrings de funciones

```python
def convertir_kilometros_a_millas(kilometros):
	"""Convierte una distancia de kilómetros a millas.

	Args:
		kilometros: Distancia no negativa en kilómetros.

	Returns:
		La distancia equivalente en millas.

	Raises:
		ValueError: Si la distancia es negativa.
	"""
	if kilometros < 0:
		raise ValueError("La distancia no puede ser negativa")
	return kilometros * 0.621371
```

La documentación debe describir el contrato: entradas, salida, efectos secundarios, errores y supuestos.

### 19.3 Docstrings de clases

```python
class Cuenta:
	"""Representa una cuenta con saldo y operaciones básicas."""

	def __init__(self, titular, saldo=0):
		self.titular = titular
		self.saldo = saldo
```

### 19.4 Type hints

Las anotaciones de tipo documentan la intención y ayudan a herramientas:

```python
def sumar(a: int, b: int) -> int:
	return a + b
```

En Python no obligan por sí solas a que se reciban esos tipos durante la ejecución.

Para colecciones:

```python
def promedio(valores: list[float]) -> float:
	return sum(valores) / len(valores)
```

### 19.5 Documentar decisiones

La documentación debe explicar el porqué cuando el código no lo hace evidente:

```python
# Se conserva el orden de llegada porque el informe se revisa cronológicamente.
eventos = list(eventos_recibidos)
```

### 19.6 Calidad de la documentación

Una documentación útil es:

- Exacta y actualizada.
- Concisa cuando el comportamiento es obvio.
- Detallada cuando hay reglas o efectos importantes.
- Accionable: permite instalar y ejecutar.
- Verificable: los ejemplos funcionan.
- Coherente con los nombres del código.

### 19.7 Generación automática

Herramientas como Sphinx, pydoc y MkDocs pueden construir documentación a partir de docstrings y archivos Markdown. La generación automática no sustituye la escritura cuidadosa: solo publica lo que se ha expresado en el código.

### Actividad 19.1: documentar una API

Escribe tres funciones relacionadas con una agenda. Añade anotaciones de tipo, docstrings con parámetros, valor de retorno y excepciones. Después redacta un ejemplo de uso para el `README.md`.

---

## 20. Proyecto práctico integrador: gestor de tareas en consola

El siguiente proyecto combina variables, tipos, funciones, listas, diccionarios, selección, repetición, excepciones, documentación y depuración. Permite añadir, listar, completar y eliminar tareas.

### 20.1 Diseño

Cada tarea será un diccionario:

```python
{
	"titulo": "Estudiar Python",
	"completada": False,
}
```

El programa tendrá estas operaciones:

- Añadir una tarea.
- Listar tareas.
- Marcar una tarea como completada.
- Eliminar una tarea.
- Salir.

### 20.2 Implementación completa

```python
"""Gestor de tareas sencillo para la terminal."""


def mostrar_menu():
	"""Muestra las opciones disponibles."""
	print("\nGESTOR DE TAREAS")
	print("1. Añadir tarea")
	print("2. Listar tareas")
	print("3. Completar tarea")
	print("4. Eliminar tarea")
	print("5. Salir")


def pedir_indice(tareas, mensaje):
	"""Solicita un índice válido y lo devuelve como índice de lista."""
	if not tareas:
		raise ValueError("No hay tareas disponibles")

	texto = input(mensaje).strip()
	try:
		indice = int(texto) - 1
	except ValueError as error:
		raise ValueError("El índice debe ser un entero") from error

	if not 0 <= indice < len(tareas):
		raise ValueError("El índice está fuera de rango")
	return indice


def anadir_tarea(tareas):
	"""Añade una tarea no vacía a la lista."""
	titulo = input("Título de la tarea: ").strip()
	if not titulo:
		raise ValueError("El título no puede estar vacío")
	tareas.append({"titulo": titulo, "completada": False})
	print("Tarea añadida")


def listar_tareas(tareas):
	"""Muestra las tareas numeradas."""
	if not tareas:
		print("No hay tareas")
		return

	for indice, tarea in enumerate(tareas, start=1):
		estado = "x" if tarea["completada"] else " "
		print(f"{indice}. [{estado}] {tarea['titulo']}")


def completar_tarea(tareas):
	"""Marca una tarea como completada."""
	indice = pedir_indice(tareas, "Número de tarea: ")
	tareas[indice]["completada"] = True
	print("Tarea completada")


def eliminar_tarea(tareas):
	"""Elimina una tarea seleccionada."""
	indice = pedir_indice(tareas, "Número de tarea: ")
	eliminada = tareas.pop(indice)
	print(f"Eliminada: {eliminada['titulo']}")


def ejecutar():
	"""Ejecuta el bucle principal de la aplicación."""
	tareas = []

	while True:
		mostrar_menu()
		opcion = input("Elige una opción: ").strip()

		try:
			if opcion == "1":
				anadir_tarea(tareas)
			elif opcion == "2":
				listar_tareas(tareas)
			elif opcion == "3":
				completar_tarea(tareas)
			elif opcion == "4":
				eliminar_tarea(tareas)
			elif opcion == "5":
				print("Hasta pronto")
				break
			else:
				print("Opción no válida")
		except ValueError as error:
			print(f"Error: {error}")


if __name__ == "__main__":
	ejecutar()
```

### 20.3 Mejoras propuestas

Amplía el proyecto con:

1. Persistencia en un archivo JSON.
2. Fecha de creación y fecha límite.
3. Prioridad alta, media o baja.
4. Filtrado de tareas pendientes.
5. Búsqueda por palabras.
6. Pruebas automatizadas.
7. Separación en módulos.
8. Registro de eventos con `logging`.
9. Argumentos de línea de comandos.
10. Importación y exportación a CSV.

---

## 21. Ejercicios y actividades

### Nivel inicial

1. Escribe un programa que muestre tu nombre, ciudad y lenguaje favorito.
2. Lee dos números y muestra suma, resta, producto y división. Controla divisor cero.
3. Calcula el área de un triángulo.
4. Convierte minutos a horas y minutos.
5. Indica si un número es positivo, negativo o cero.
6. Comprueba si una palabra está vacía después de quitar espacios.
7. Convierte grados Celsius a Fahrenheit y Kelvin.
8. Pide una edad y clasifica: infancia, adolescencia, adultez o vejez.
9. Calcula el precio final aplicando IVA.
10. Intercambia el valor de dos variables sin crear una tercera variable.

### Nivel intermedio

11. Muestra la tabla de multiplicar de un número.
12. Calcula factorial con un bucle `for`.
13. Cuenta vocales de una frase.
14. Invierte una cadena sin usar `reversed()`.
15. Determina si una palabra es palíndroma.
16. Calcula el máximo y mínimo de una lista sin usar `max()` ni `min()`.
17. Elimina duplicados de una lista conservando el orden.
18. Cuenta la frecuencia de palabras de una frase con un diccionario.
19. Simula tres intentos de inicio de sesión.
20. Pide números hasta `fin` y calcula estadísticas.
21. Crea un menú de conversión de unidades.
22. Valida una contraseña con longitud mínima, mayúscula, minúscula y dígito.
23. Implementa una búsqueda lineal y devuelve la posición encontrada.
24. Ordena una lista con el algoritmo de selección.
25. Lee un archivo de texto y cuenta líneas, palabras y caracteres.

### Nivel avanzado

26. Crea una agenda de contactos con altas, consultas, modificaciones y bajas.
27. Guarda y carga la agenda en JSON controlando archivos inexistentes.
28. Implementa una clase `Producto` con validación de precio y stock.
29. Construye una clase `Carrito` y calcula subtotal, descuento e impuestos.
30. Escribe pruebas para un módulo de conversiones.
31. Añade logging a una aplicación de consola.
32. Crea un generador que lea un archivo línea a línea sin cargarlo completo.
33. Construye un analizador de notas con media, mediana y distribución por tramos.
34. Diseña un pequeño sistema de reservas y controla solapamientos.
35. Documenta un proyecto con README, docstrings, type hints y ejemplos.

### Actividades de reflexión

36. Explica por qué `input()` requiere conversión para operar con números.
37. Compara una lista, una tupla, un conjunto y un diccionario con un caso de uso para cada uno.
38. Describe la diferencia entre error de sintaxis, ejecución y lógica con ejemplos.
39. Explica cuándo usarías `for` y cuándo `while`.
40. Razona por qué capturar todas las excepciones con `except Exception` puede ser peligroso.
41. Describe un caso donde `None` sea mejor que una cadena vacía.
42. Explica la diferencia entre igualdad e identidad.
43. Propón tres pruebas de frontera para una función que acepta edades de 0 a 120.
44. Lee un traceback inventado y señala la excepción, el archivo y la línea causante.
45. Analiza un programa con demasiadas condiciones anidadas y propón funciones más pequeñas.

### Reto final

Desarrolla una aplicación de consola para gestionar calificaciones. Debe permitir:

- Registrar estudiantes y notas.
- Validar notas entre 0 y 10.
- Calcular media individual y del grupo.
- Mostrar aprobados y suspensos.
- Buscar por nombre.
- Guardar los datos en JSON.
- Cargar datos al iniciar.
- Controlar errores de entrada y archivos.
- Incluir docstrings, anotaciones de tipo y un README.
- Tener al menos diez pruebas para funciones esenciales.

---

## 22. Soluciones orientativas

Las soluciones siguientes muestran una posible estrategia. No son las únicas respuestas correctas.

### Solución 1: positivo, negativo o cero

```python
def clasificar(numero):
	if numero > 0:
		return "positivo"
	if numero < 0:
		return "negativo"
	return "cero"
```

### Solución 2: minutos a horas

```python
def convertir_minutos(minutos):
	if minutos < 0:
		raise ValueError("Los minutos no pueden ser negativos")
	horas = minutos // 60
	restantes = minutos % 60
	return horas, restantes
```

### Solución 3: contador de vocales

```python
def contar_vocales(texto):
	vocales = "aeiouáéíóúü"
	return sum(1 for caracter in texto.lower() if caracter in vocales)
```

### Solución 4: eliminar duplicados conservando orden

```python
def sin_duplicados(elementos):
	vistos = set()
	resultado = []

	for elemento in elementos:
		if elemento not in vistos:
			vistos.add(elemento)
			resultado.append(elemento)

	return resultado
```

### Solución 5: lectura robusta de un entero

```python
def leer_entero(mensaje, minimo=None, maximo=None):
	while True:
		try:
			valor = int(input(mensaje))
		except ValueError:
			print("Introduce un número entero")
			continue

		if minimo is not None and valor < minimo:
			print(f"Debe ser como mínimo {minimo}")
			continue
		if maximo is not None and valor > maximo:
			print(f"Debe ser como máximo {maximo}")
			continue
		return valor
```

### Solución 6: frecuencia de palabras

```python
def frecuencia_palabras(frase):
	frecuencias = {}
	for palabra in frase.lower().split():
		frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
	return frecuencias
```

### Solución 7: búsqueda lineal

```python
def buscar(elementos, objetivo):
	for indice, elemento in enumerate(elementos):
		if elemento == objetivo:
			return indice
	return -1
```

### Solución 8: media segura

```python
def media(valores):
	if not valores:
		raise ValueError("Se necesita al menos un valor")
	return sum(valores) / len(valores)
```

---

## 23. Resumen y lista de comprobación

Antes de considerar terminado un programa Python, comprueba:

- [ ] El programa tiene un propósito claro.
- [ ] Los nombres describen los datos.
- [ ] La indentación es consistente.
- [ ] Las entradas se validan.
- [ ] Los tipos son adecuados.
- [ ] Las conversiones se hacen explícitamente.
- [ ] Las condiciones cubren casos normales y límites.
- [ ] Los bucles tienen una terminación garantizada.
- [ ] `break`, `continue` y `return` se usan con intención.
- [ ] Las excepciones se capturan de forma específica.
- [ ] Los archivos y recursos se gestionan con `with` cuando corresponde.
- [ ] No quedan mensajes de depuración temporales.
- [ ] Se han probado casos válidos, inválidos y extremos.
- [ ] El programa puede depurarse con breakpoints.
- [ ] Las funciones tienen docstrings cuando su contrato no es obvio.
- [ ] El README explica instalación, ejecución y ejemplos.
- [ ] Las dependencias están aisladas en un entorno virtual.
- [ ] El código está formateado y revisado.

La programación se aprende escribiendo, ejecutando, observando y corrigiendo. La teoría aporta vocabulario y modelos mentales; los ejercicios convierten esos modelos en habilidades. Un programa pequeño, bien probado y bien documentado ofrece una base más sólida que un programa grande copiado sin comprenderlo.
