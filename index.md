---
title: "UD1.2: Introducción a la programación en Python"
description: "<strong>Módulo:</strong> Programación y Automatización en Sistemas Informáticos y en Red <br> <strong>Profesor:</strong> Matías Montávez Sánchez"
---

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
18. [El depurador como herramienta de control de errores](#18-el-depurador-como-herramienta-de-control-de-errores)
19. [Documentación y documentación de programas](#19-documentación-y-documentación-de-programas)
20. [Programación orientada a objetos](#20-programación-orientada-a-objetos)
21. [Proyecto práctico integrador](#21-proyecto-práctico-integrador-gestor-de-tareas-en-consola)
22. [Ejercicios y actividades](#22-ejercicios-y-actividades)
23. [Soluciones orientativas](#23-soluciones-orientativas)
24. [Resumen y lista de comprobación](#24-resumen-y-lista-de-comprobación)

---

## 1. Introducción y objetivos

[⬆ Volver al índice](#índice)

![Logo de Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

Python es un lenguaje de programación de propósito general, interpretado, de alto nivel y con una sintaxis diseñada para favorecer la legibilidad. Se utiliza en automatización, desarrollo web, análisis de datos, inteligencia artificial, ciencia, educación, administración de sistemas y creación de herramientas de escritorio.

Este documento presenta los fundamentos necesarios para leer, escribir, ejecutar, probar, depurar y documentar programas en Python 3. Los ejemplos se han pensado para poder copiarse en un archivo `.py` y ejecutarse con una instalación estándar de Python, sin depender de librerías externas.

Contenidos clave:

- Variables
- Tipos de datos
- Literales
- Constantes
- Operadores y expresiones
- Conversiones de tipo
- Comentarios
- Entornos integrados de desarrollo
- Estructuras de control
- Selección
- Repetición
- Salto
- Control de excepciones
- Depuración
- Depurador
- Documentación

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

[⬆ Volver al índice](#índice)

Un programa es un conjunto ordenado de instrucciones que procesa datos para producir resultados. Aunque Python permite escribir programas muy pequeños, incluso un ejemplo de pocas líneas contiene varios elementos conceptuales.

<div class="mermaid">
graph TD
    A[Programa]
    A --> B[Código fuente]
    B --> C[Instrucciones]
    C --> D[Identificadores]
    D --> E[Variables]
    E --> F[Tipos de datos]
    F --> G[Literales y constantes]
    G --> H[Operadores y expresiones]
    H --> I[Comentarios]
    I --> J[Estructuras de control]
</div>

<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>mermaid.initialize({ startOnLoad: true });</script>

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

Las tabulaciones (o su equivalente en espacios) no separan instrucciones, sino que definen la indentación: el nivel de sangrado que delimita los bloques de código (por ejemplo, el cuerpo de un `if`, un `for` o una función). A diferencia de otros lenguajes que usan llaves `{}`, en Python la indentación es obligatoria y forma parte de la sintaxis. Se recomienda usar siempre 4 espacios y no mezclar tabulaciones con espacios, ya que Python puede rechazar el código con un error de indentación (`IndentationError` o `TabError`).

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

El listado completo y actualizado de palabras reservadas de Python 3 puede consultarse en la [documentación oficial de Python](https://docs.python.org/3/reference/lexical_analysis.html#keywords).

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

La **sintaxis** son las reglas que definen si el texto de un programa está bien formado, es decir, si el intérprete es capaz de leerlo. Determina cosas como el orden de las palabras clave, el uso de paréntesis, comillas o dos puntos, y la indentación. Un fallo de sintaxis impide que el programa llegue a ejecutarse: el intérprete se detiene y muestra un `SyntaxError` antes de procesar ninguna instrucción.

La **semántica** es el significado de lo que está escrito, es decir, qué hace realmente cada instrucción cuando se ejecuta. Un programa puede tener una sintaxis perfectamente correcta y aun así hacer algo distinto de lo que se pretendía, porque el significado de las instrucciones no coincide con la intención de quien programa.

La diferencia se puede resumir así:

- La sintaxis responde a la pregunta "¿está bien escrito?".
- La semántica responde a la pregunta "¿hace lo que se quiere?".
- Un error de sintaxis se detecta antes de ejecutar el programa.
- Un error de semántica (o error lógico) solo se detecta observando el comportamiento o el resultado durante o después de la ejecución.

```python
print("Hola")       # sintaxis y significado correctos
```

El siguiente ejemplo tiene un error sintáctico porque falta cerrar el paréntesis; el intérprete no consigue leer la instrucción:

```python
# print("Hola"
```

Este ejemplo es sintácticamente correcto (el intérprete lo ejecuta sin protestar), pero tiene un error semántico si la intención era sumar dos cantidades y multiplicar el número 10 tres veces produce un resultado distinto del esperado:

```python
resultado = "10" * 3
print(resultado)    # produce "101010", no 30
```

### 2.7 Errores de un programa

Los errores más habituales son:

1. **Errores de sintaxis:** el código no respeta las reglas del lenguaje.
2. **Errores de ejecución:** el programa empieza, pero falla durante la ejecución, por ejemplo al dividir entre cero.
3. **Errores lógicos:** el programa se ejecuta, pero produce un resultado incorrecto.

![Errores mostrados en el editor y en el panel Problems de Visual Studio Code](https://code.visualstudio.com/assets/docs/python/linting/lint-messages.png)

En Visual Studio Code, los errores y avisos se subrayan directamente en el código (normalmente en rojo los errores y en amarillo los avisos) y también aparecen listados en el panel **Problems**, donde se puede ver el mensaje completo, el archivo y la línea exacta en la que se producen.

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

### Actividad 2.2: identificadores válidos

Indica cuáles de los siguientes nombres son identificadores válidos en Python y, para los que no lo sean, explica por qué: `total_1`, `1total`, `Total`, `for`, `_precio`, `precio-unitario`, `precio_unitario_€`, `class`, `Class`, `__init__`, `2do_intento`, `nombre completo`, `número_de_cuenta`, `total__final`, `def_valores`, `True`, `variable-2`, `_`, `mi.variable`, `while1`.

### Actividad 2.3: entrada, procesamiento y salida

Observa el siguiente código y clasifica cada línea como entrada, procesamiento o salida escribiéndolo en un comentario al lado. Algunas líneas combinan más de una categoría y una de ellas no encaja en ninguna de las tres:

```python
import math

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Qué edad tienes? "))
radio = float(input("Radio del círculo: "))

mayor_edad = edad >= 18
recargo = 0.05 if not mayor_edad else 0.0
superficie = math.pi * radio ** 2
superficie_con_recargo = superficie * (1 + recargo)

mensaje = f"{nombre}, ¿eres mayor de edad? {mayor_edad}"

print(mensaje)
print(f"Superficie: {superficie:.2f}")
print(f"Superficie con recargo: {superficie_con_recargo:.2f}")
```

### Actividad 2.4: depurar tipos de error

El siguiente código mezcla varios problemas: errores de sintaxis, de indentación/tabulación, de ejecución y errores lógicos. Localízalos todos, indica de qué tipo es cada uno y corrígelos:

```python
def calcular_media(numeros):
    suma = 0
  for numero in numeros:
        suma = suma + numero
	media = suma / len(numeros)
    return media


def calcular_area_triangulo(base, altura)
    area = base * altura / 2
    return area


notas = [4, 6, 8, 10]
print("Media: " media)
print("Área:", calcular_area_triangulo(4, 3))

lista_vacia = []
print("Media lista vacía:", calcular_media(lista_vacia))
```

Pistas:

- Hay una línea que mezcla espacios y tabulaciones en el mismo bloque.
- Hay un bloque indentado con menos sangrado del que le corresponde.
- Falta un símbolo indispensable en la definición de una función.
- Una llamada a `print` referencia una variable que no existe con ese nombre.
- Una de las funciones falla con una entrada concreta aunque el código sea sintácticamente correcto.

### Actividad 2.5: esquema propio

A partir del esquema de la sección 2, elabora tu propio diagrama (en papel o en Mermaid) que represente los elementos de un programa distinto, por ejemplo uno que calcule el precio final de una compra con IVA. Incluye al menos: identificadores, tipos de datos, literales, operadores y estructuras de control.

---

## 3. Estructura y bloques fundamentales

[⬆ Volver al índice](#índice)

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

> **Idea clave:** un archivo Python puede ser un programa que se ejecuta o un
> módulo que otro archivo importa. `main()` organiza la ejecución y evita que la
> interacción se dispare accidentalmente al importar.

#### Programa frente a módulo

| Uso | Qué ocurre | Ejemplo |
| --- | --- | --- |
| **Programa** | Se ejecuta directamente y realiza una tarea completa. | `python saludos.py` |
| **Módulo** | Otro archivo lo importa para reutilizar sus funciones. | `from saludos import saludar` |

La ventaja es escribir la lógica una sola vez y reutilizarla desde una aplicación,
una prueba automática o el intérprete interactivo.

#### El problema de ejecutar código al importar

Este archivo `saludos.py` parece correcto si se ejecuta directamente:

```python
def saludar(nombre):
	return f"Hola, {nombre}"


nombre = input("Nombre: ")
print(saludar(nombre))
```

Pero si `programa.py` solo quiere reutilizar la función:

```python
from saludos import saludar

print(saludar("Ana"))
```

Python también ejecutará el `input()` de `saludos.py` durante la importación.
Aparecerá una pregunta por teclado antes de `Hola, Ana`, aunque no la hemos
solicitado.

#### La solución: separar definición y ejecución

Colocamos la interacción dentro de `main()` y protegemos su llamada:

```python
def saludar(nombre):
	return f"Hola, {nombre}"


def main():
	nombre = input("Nombre: ")
	print(saludar(nombre))


if __name__ == "__main__":
	main()
```

> **Lectura de la condición:** ejecuta `main()` únicamente si este archivo es
> el programa principal que se ha ejecutado directamente.

| Situación | Valor de `__name__` | ¿Se llama a `main()`? |
| --- | --- | --- |
| `python saludos.py` | `"__main__"` | Sí |
| `programa.py` importa `saludos` | `"saludos"` | No |

#### Flujo completo entre dos archivos

**`saludos.py`** contiene las funciones y su punto de entrada:

```python
def saludar(nombre, tratamiento="Hola"):
	return f"{tratamiento}, {nombre}"


def main():
	nombre = input("Nombre: ")
	print(saludar(nombre))


if __name__ == "__main__":
	main()
```

**`programa.py`** reutiliza la función:

```python
from saludos import saludar


def main():
	print(saludar("Ana"))
	print(saludar("Luis", tratamiento="Buenos días"))


if __name__ == "__main__":
	main()
```

Al ejecutar `python programa.py`:

1. Se cargan las funciones de `saludos.py`.
2. No se ejecuta su `main()`, porque `__name__` vale `"saludos"`.
3. Se ejecuta el `main()` de `programa.py`, que sí es el archivo principal.

#### Reparto de responsabilidades

- **Funciones:** tareas concretas y reutilizables.
- **`main()`:** coordinación de entrada, llamadas y salida.
- **Condición `if`:** único punto que inicia automáticamente el programa.
- **Nivel superior del módulo:** definiciones y constantes, no acciones inesperadas.

> **Error frecuente:** escribir `main()` directamente al final, sin la
> condición. Así la interacción se inicia cada vez que otro archivo importa el
> módulo.

### 3.4 Funciones como bloques reutilizables

Una función agrupa instrucciones con un nombre, recibe parámetros y puede
devolver un resultado. Es una forma de convertir una tarea compleja o repetida
en un bloque que podemos llamar desde varios lugares.

```python
def calcular_iva(precio, porcentaje=21):
	"""Devuelve el importe del IVA para un precio dado."""
	return precio * porcentaje / 100


iva = calcular_iva(100)
print(iva)
```

Las funciones reducen la duplicación, facilitan las pruebas y permiten dividir
un problema grande en tareas pequeñas.

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

### 3.6 Nombres de archivos de programas

Los archivos de Python deben guardarse con la extensión `.py`. Para que sean
fáciles de localizar y entender, se recomienda:

- escribir los nombres en minúsculas;
- separar las palabras con guiones bajos (`snake_case`);
- incluir, cuando sea útil, una referencia al ejercicio o a la tarea que
	resuelve el programa.

Por ejemplo:

```text
operaciones_1.py
operaciones_media_numeros.py
gestor_tareas.py
```

Es preferible evitar espacios, acentos y caracteres especiales en los nombres
de archivo, ya que pueden causar dificultades al ejecutar programas desde la
terminal o al compartirlos entre sistemas.

La plantilla con `main()` mostrada en la sección anterior y esta convención de
nombres siguen las recomendaciones de [Programa básico de Python de
mclibre.org](https://www.mclibre.org/consultar/python/lecciones/python-plantilla.html).

### 3.7 Cómo se ejecuta un programa Python

Un programa Python se procesa de arriba abajo. Esta idea explica muchos errores
de principiante: una función debe estar definida antes de llamarse, una variable
debe recibir un valor antes de utilizarse y una condición se comprueba en el
punto exacto en el que aparece. El intérprete no reordena las instrucciones.

En un programa pequeño podemos imaginar el flujo así:

1. Python lee una instrucción.
2. Evalúa las expresiones que necesita.
3. Ejecuta la acción resultante.
4. Continúa con la siguiente instrucción, salvo que encuentre una decisión, un
   bucle, una llamada a función o una excepción.

```python
print("1. Inicio")

def duplicar(numero):
	return numero * 2


valor = duplicar(4)
print("2. Resultado:", valor)
print("3. Fin")
```

La definición de `duplicar` no ejecuta todavía su cuerpo: crea la función. El
cuerpo se ejecuta cuando aparece `duplicar(4)`. Distinguir entre definir y
llamar es fundamental para organizar programas en funciones.

### 3.8 La indentación como parte de la sintaxis

En muchos lenguajes las llaves indican dónde empieza y termina un bloque. En
Python esa información la aporta la indentación. No es solo formato visual:
cambiar el sangrado puede cambiar el significado del programa. Todas las
instrucciones del mismo bloque deben comenzar en la misma columna.

```python
numero = 7

if numero > 0:
	print("El número es positivo")
	if numero % 2 == 0:
		print("Además es par")
	else:
		print("Además es impar")
```

En el ejemplo hay dos niveles: el primer `if` contiene al segundo, y este
último contiene dos posibles bloques. Un `else` se relaciona con el `if` que
está al mismo nivel de indentación. Para evitar errores:

- configura el editor para insertar cuatro espacios al pulsar Tab;
- no mezcles tabuladores y espacios;
- mantén el mismo nivel para instrucciones hermanas;
- reduce la profundidad extrayendo una función cuando un bloque sea difícil de
  leer.

### 3.9 Diseñar un bloque antes de escribirlo

Antes de codificar conviene expresar cada bloque como una responsabilidad. Un
programa que calcula una compra puede dividirse en `leer_precio()`,
`calcular_total()`, `mostrar_resumen()` y `main()`. Así no se mezclan entrada,
cálculos y salida, y se puede probar el cálculo sin responder preguntas por
teclado. La regla práctica es que una función debería poder describirse con un
verbo: calcular, validar, convertir, buscar o mostrar.

```python
def calcular_total(precio, unidades, iva=21):
	subtotal = precio * unidades
	importe_iva = subtotal * iva / 100
	return subtotal + importe_iva


def main():
	precio = 12.5
	unidades = 3
	print(f"Total: {calcular_total(precio, unidades):.2f} euros")


if __name__ == "__main__":
	main()
```

`main()` coordina el programa, pero no debe convertirse en un lugar donde se
acumule toda la lógica. Si aparece una nueva tarea, normalmente puede extraerse
como otra función pequeña y comprobable.

### 3.10 Parámetros, argumentos y valores devueltos

El parámetro es el nombre de la definición; el argumento es el valor concreto de
la llamada. En `calcular_total(precio, unidades)`, los parámetros son `precio` y
`unidades`; en `calcular_total(12.5, 3)`, los argumentos son `12.5` y `3`.

`return` termina la función y entrega un valor. `print()` solo muestra algo en
pantalla y no sustituye a `return`:

```python
def sumar_y_devolver(a, b):
	return a + b


def sumar_y_mostrar(a, b):
	print(a + b)


resultado = sumar_y_devolver(2, 3)  # vale 5
otro_resultado = sumar_y_mostrar(2, 3)  # muestra 5, pero vale None
```

Una función que calcula debería devolver el resultado; quien la llama decidirá
si lo muestra, lo guarda o lo utiliza en otra operación. Esta separación permite
reutilizar el código en una consola, una prueba automática o una interfaz.

### 3.11 Alcance, flujo y errores habituales

El alcance indica dónde se puede utilizar un nombre. Los nombres locales nacen
dentro de una función y dejan de estar disponibles al terminar su ejecución.
Una variable global puede ser visible en más lugares, pero depender demasiado de
ella hace que las funciones sean difíciles de entender y probar.

```python
def crear_usuario():
	nombre = "Lucía"
	return nombre


usuario = crear_usuario()
# print(nombre)  # NameError: solo existe dentro de crear_usuario
```

Los errores más frecuentes al construir bloques son olvidar los dos puntos,
indentar una línea en el nivel incorrecto, llamar a una función con argumentos
incorrectos, confundir `print()` con `return` y ejecutar código de prueba al
importar un módulo por no usar `main()`. Para localizar el problema, prueba
primero cada función con datos sencillos, comprueba qué recibe y qué devuelve, y
añade complejidad solo después de validar el bloque pequeño.

### 3.12 Videotutoriales recomendados

Aquí algunos videotutoriales en español:

- [Indentación y bloques en Python](https://youtu.be/Bs_Eq7Vo5XU?si=ufuzahIgwe49QEsU).
- [Funciones, parámetros y `return` en Python](https://youtu.be/g78juF9pB_w?si=rMB2W1JHnyIIJ5SJ).
- [Módulos y `if __name__ == "__main__"`](https://youtu.be/wZKTUcTqekw?si=bhU2BagxSaOyjx9W).
- [Alcance de variables y funciones en Python](https://youtu.be/Xn5-W5gXdak?si=0C_-3Wy2_h6DUW9I).

> **Nivel inicial:** estas actividades no piden crear un programa desde cero.
> Primero se observa, se ordena, se completa y se explica.

### Actividad 3.1: reconocer los bloques

Observa este ejemplo y colorea o marca cada parte con una letra:

```python
def mostrar_mensaje():       # A
	mensaje = "Bienvenido"    # B
	print(mensaje)             # C


mostrar_mensaje()            # D
```

Relaciona cada letra con una descripción:

- definición de una función;
- instrucción que guarda un texto;
- instrucción que muestra un resultado;
- llamada que hace que la función se ejecute.

Después responde: ¿qué líneas se agrupan por la indentación? ¿Qué ocurriría si
la línea `print(mensaje)` se escribiera sin sangrado?

### Actividad 3.2: ordenar un programa

Las siguientes tarjetas forman un programa, pero están desordenadas. Numéralas
del 1 al 6 para indicar el orden correcto. No es necesario escribir código.

```text
[ ] Mostrar el saludo en pantalla.
[ ] Definir una función llamada saludar.
[ ] Pedir el nombre de la persona.
[ ] Devolver el texto "Hola, " seguido del nombre.
[ ] Llamar a la función saludar.
[ ] Terminar el programa.
```

Explica por qué no tendría sentido llamar a `saludar` antes de definirla. Como
ampliación, dibuja flechas entre las tarjetas que dependen unas de otras.

### Actividad 3.3: leer la indentación

En ambos fragmentos, `hay_entradas` vale `True`. Los dos fragmentos son válidos,
pero la última instrucción no pertenece al mismo bloque en ambos casos. Para
cada fragmento, indica qué mensajes se muestran y explica por qué usando las
palabras **bloque**, **nivel** e **indentación**.

```python
# Fragmento A
if hay_entradas:
	print("Comenzamos")
	print("Hay trabajo")
```

```python
# Fragmento B
if hay_entradas:
	print("Comenzamos")
print("Hay trabajo")
```

Después marca las instrucciones que pertenecen al `if` en cada fragmento.
Recuerda: una instrucción indentada bajo el `if` pertenece a su bloque; una
instrucción que vuelve al margen izquierdo está fuera de él.

### Actividad 3.4: extraer funciones de un enunciado

Un taller de asistencia informática quiere un programa que prepare el
presupuesto de una reparación. El programa debe pedir el nombre del cliente,
las horas de trabajo, el precio por hora, el coste de las piezas y el porcentaje
de IVA. A continuación, debe calcular el coste de la mano de obra, el subtotal,
el importe del IVA y el total. Por último, debe mostrar el nombre del cliente y
el presupuesto desglosado.

Sin escribir todavía el código, analiza el enunciado y divídelo en funciones.
Completa una fila por cada función que consideres necesaria:

| Nombre propuesto para la función | Qué tarea realiza | Qué datos necesita | Qué resultado devuelve o muestra |
| --- | --- | --- | --- |
| `__________` | `__________` | `__________` | `__________` |
| `__________` | `__________` | `__________` | `__________` |
| `__________` | `__________` | `__________` | `__________` |
| `__________` | `__________` | `__________` | `__________` |

Después, indica qué función coordinaría el proceso completo y escribe el orden
en que llamaría a las demás. Puede haber distintas soluciones: cada función
debe encargarse de una tarea concreta y el conjunto debe resolver todo el
enunciado.

### Actividad 3.5: completar una plantilla con pistas

Completa los seis huecos, identificados con letras, usando estas palabras:
`def`, `main`, `return`, `if` y `print`. Algunas palabras se necesitan más de
una vez.

```python
_____ saludar(nombre):  # A
	_____ f"Hola, {nombre}"  # B


_____ _____():  # C, D
	_____ (saludar("Ana"))  # E


_____ __name__ == "__main__":  # F
	main()
```

Después de completar la plantilla:

1. Señala la definición de cada función y el valor que devuelve `saludar()`.
2. Si ejecutas el archivo directamente, indica qué función se llama desde el
   bloque `if`.
3. Sigue la llamada a `saludar("Ana")` y escribe el texto que termina mostrando
   `print()`.

---

## 4. Variables

[⬆ Volver al índice](#índice)

Una variable es un nombre que permite guardar y utilizar un valor durante la ejecución de un programa. En Python, una variable se crea al asignarle un valor por primera vez.

### Variables en Matemáticas y en programación

En Matemáticas, una variable representa una cantidad, conocida o desconocida, dentro de una expresión. Por ejemplo, en `x + 3 = 5`, se puede averiguar que `x` vale 2. En una fórmula como `y = x + 1`, en cambio, se pueden probar distintos valores de `x` y calcular el valor correspondiente de `y`.

En programación, una variable es un nombre al que se asigna un valor para poder utilizarlo más adelante. El signo `=` indica una **asignación**, no una igualdad matemática: Python calcula lo que aparece a la derecha y asigna el resultado al nombre de la izquierda. Por eso `total = precio * unidades` se lee como «calcula el producto y guarda el resultado en `total`», no como una ecuación que haya que resolver.

### 4.1 Asignación

Para crear una variable, escribe su nombre, el signo `=` y el valor que quieres asignarle:

```python
nombre = "Ana"
edad = 28
```

La asignación puede guardar un valor escrito directamente o el resultado de un cálculo. Python evalúa primero lo que aparece a la derecha y luego guarda ese resultado con el nombre de la izquierda:
En el intérprete interactivo, escribir el nombre muestra su valor. En un archivo `.py`, una línea que solo contiene un nombre no lo muestra en pantalla; para ello se utiliza `print()`. Esta diferencia importa al probar instrucciones en la consola y al ejecutar un programa guardado en un archivo.

```python
horas = 2
minutos = horas * 60
print(minutos)  # 120
```

En el intérprete interactivo, escribir el nombre muestra su valor. En un archivo `.py`, para mostrarlo en pantalla se utiliza `print()`.

```pycon
>>> edad = 28
>>> edad
28
```

El texto se escribe entre comillas simples o dobles. Sin comillas, Python interpreta la palabra como el nombre de otra variable:

```pycon
>>> nombre = "Pepito Conejo"
>>> nombre
'Pepito Conejo'
>>> nombre = Pepe
Traceback (most recent call last):
	...
NameError: name 'Pepe' is not defined
```

Las comillas marcan dónde empieza y termina el texto. En cambio, sin comillas, `Pepe` no es texto: Python intenta encontrar una variable llamada `Pepe`.

### 4.2 Reasignación

Se puede asignar un valor nuevo a una variable. La asignación nueva reemplaza el valor anterior:

```python
edad = 28
edad = 29
print(edad)  # 29
```

También se puede usar el valor actual para calcular el siguiente:

```python
puntuacion = 10
puntuacion = puntuacion + 5
print(puntuacion)  # 15
```

La expresión de la derecha se calcula primero. Por eso `puntuacion = puntuacion + 5` significa «toma el valor actual, súmale 5 y asigna el resultado otra vez a `puntuacion`».
Esta forma se utiliza para llevar una cuenta acumulada, actualizar una puntuación o aumentar un importe. El nombre debe tener un valor antes de poder aparecer en la expresión de la derecha.

### 4.3 Intercambiar valores

Para intercambiar los valores de dos variables, se puede utilizar una tercera variable temporal:

```python
primero = 5
segundo = 10

temporal = primero
primero = segundo
segundo = temporal

print(primero)  # 10
print(segundo)  # 5
```

La variable `temporal` evita perder uno de los valores. Si se escribiera primero `primero = segundo`, el valor inicial de `primero` se reemplazaría; al hacer después `segundo = primero`, ambas variables acabarían valiendo lo mismo. La variable temporal conserva el primer valor mientras se realizan las otras asignaciones.
Para separar palabras, se recomienda usar guiones bajos, por ejemplo `fecha_de_nacimiento`. Esta forma se llama `snake_case` y facilita la lectura. También se pueden usar mayúsculas dentro del nombre, pero Python distingue entre ellas: `precio` y `Precio` no son el mismo nombre.

### 4.4 Nombres de variables

Elige nombres que describan el valor, como `precio` o `numero_de_intentos`. Las reglas básicas son:

- El nombre puede contener letras, números y guiones bajos (`_`).
- Debe empezar por una letra o un guion bajo, no por un número.
- No puede contener espacios.
- Python distingue mayúsculas de minúsculas: `nombre` y `Nombre` son nombres distintos.
- No se pueden usar palabras reservadas como `for` o `if`.

Para separar palabras, se recomienda usar guiones bajos, por ejemplo `fecha_de_nacimiento`. Esta forma se llama `snake_case`.

```python
nombre_completo = "Lucía García"
numero_de_intentos = 3
```

Conviene evitar nombres demasiado cortos o que no expliquen el dato. Por ejemplo, `p` puede ser difícil de entender, mientras que `precio` indica claramente qué representa. El nombre no cambia el valor ni el resultado del cálculo: solo ayuda a quien lee el programa.

### 4.5 Asignaciones aumentadas

Las asignaciones aumentadas actualizan una variable a partir de su valor actual. Se escriben con un operador aritmético seguido de `=`:

```python
contador = 0
contador += 1  # equivale a contador = contador + 1
contador *= 2  # equivale a contador = contador * 2
```

En la primera línea, `contador += 1` suma uno al valor actual. En la segunda, `contador *= 2` multiplica ese nuevo valor por dos. También existen `-=`, `/=`, `//=`, `%=`, y `**=` para restar, dividir, calcular una división entera, obtener el resto y elevar a una potencia.

Python no tiene operadores `++` ni `--`; para aumentar o reducir una unidad se usa `+= 1` o `-= 1`. La variable debe haberse definido antes de aplicar una asignación aumentada.

### 4.6 Constantes

Python no tiene una instrucción que impida modificar una variable. Para indicar que un valor no debería cambiar, se escribe su nombre en mayúsculas y se evita reasignarlo:

```python
MAXIMO_INTENTOS = 3
```

Las mayúsculas son una convención, no una protección: Python permite cambiar el valor con otra asignación. No existe una forma incorporada de declarar una constante que el propio lenguaje impida modificar.

Se suelen usar constantes para valores que tienen un significado fijo dentro del programa, como un límite o un porcentaje. Darles un nombre evita repetir un número sin explicar qué representa:

```python
IVA = 0.21
precio_final = 100 * (1 + IVA)
```

Por convención, el nombre de una constante se escribe en mayúsculas y con guiones bajos entre palabras. La persona que programa debe respetar esa convención y no reasignarle otro valor.

### 4.7 Borrar una variable

La instrucción `del` elimina un nombre. Si se intenta utilizar después, Python produce un `NameError`:

```python
nombre = "Ana"
del nombre
# print(nombre)  # NameError: el nombre ya no existe
```

`del` no es necesario para cambiar el valor: para eso basta con hacer otra asignación. Se puede usar cuando se quiere dejar de utilizar un nombre. Después de borrarlo, hay que asignarle un valor de nuevo antes de volver a consultarlo.

### 4.8 Error frecuente: usar un nombre antes de asignarlo

Una variable debe recibir un valor antes de utilizarse:

```python
# print(ciudad)  # NameError: ciudad aún no está definida
ciudad = "Sevilla"
print(ciudad)
```

Un `NameError` también puede deberse a un error al escribir el nombre. Python distingue mayúsculas y minúsculas, así que `ciudad`, `Ciudad` y `CIUDAD` se interpretan como nombres diferentes. Para localizar el problema, compara el nombre de la asignación con el de la instrucción que lo utiliza.

### Actividad 4.1: ficha de variables

Crea un programa que asigne un nombre y una edad a dos variables. Muestra ambos
valores. Después cambia la edad y vuelve a mostrarla.

### Actividad 4.2: reasignar variables

Asigna `10` a `a` y luego asigna el valor de `a` a `b`. Muestra ambas variables.
Cambia `a` a `20` y vuelve a mostrar las dos. Explica por qué `b` sigue valiendo
`10`.

### Actividad 4.3: calcular y actualizar un valor

Asigna un precio y una cantidad a dos variables. Calcula el importe en una
tercera variable y muéstralo. Aumenta la cantidad con `+=` y calcula de nuevo el
importe.

### Actividad 4.4: elegir nombres válidos

Indica cuáles de estos nombres se pueden usar como variables y explica por qué:
`2precio`, `precio total`, `for`, `precio_total` y `precioUnitario`. Después
elige nombres descriptivos para guardar el precio y la cantidad de un producto.

### Actividad 4.5: conversor de distancia

Asigna una distancia en kilómetros a una variable y calcula su equivalencia en
metros en otra variable. Muestra ambos valores con `print()`. Después modifica la
distancia en kilómetros y vuelve a calcular la equivalencia en metros.

### Actividad 4.6: constante por convención

Define `MAXIMO_INTENTOS` con el valor `3`. Explica por qué se escribe en
mayúsculas y qué ocurriría si después le asignas el valor `5`. ¿Python impide el
cambio o depende de la persona que escribe el programa respetar la convención?

### Actividad 4.7: seguir las asignaciones

Sin ejecutar el código, completa el valor de `total` después de cada instrucción.
Después comprueba tus respuestas ejecutándolo:

```python
total = 12
total = total + 5
descuento = 3
total = total - descuento
```

| Instrucción ejecutada | Valor de `total` |
| --- | --- |
| `total = 12` | `__________` |
| `total = total + 5` | `__________` |
| `total = total - descuento` | `__________` |

Explica por qué la última instrucción utiliza el valor actual de `total`.

### Actividad 4.8: corregir nombres

En cada línea hay un problema con el nombre utilizado. Explica el error y
reescribe la instrucción correctamente:

```python
2precio = 4.5
nombre completo = "Ana"
for = 3
ciudad = "Cádiz"
print(Ciudad)
```

En la última línea, utiliza el nombre que se definió en la instrucción anterior.

### Actividad 4.9: actualizar cantidades

Empieza con `saldo = 50`. Aplica, en orden, estas operaciones usando
asignaciones aumentadas: ingresa 20, gasta 15 y duplica el saldo restante.
Escribe el saldo después de cada operación y comprueba el resultado con
`print()`.

### Actividad 4.10: preparar un recibo

Define variables para el nombre de un producto, su precio y la cantidad
comprada. Calcula el subtotal y el total con IVA, usando una constante llamada
`IVA`. Muestra el nombre del producto y ambos importes. Después cambia la
cantidad y vuelve a calcular los importes.

---

## 5. Tipos de datos

[⬆ Volver al índice](#índice)

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
Una pequeña empresa de asistencia informática quiere un programa de consola
para preparar el presupuesto de una reparación. El programa debe pedir el
nombre del cliente, las horas de trabajo, el precio por hora, el coste de las
piezas y el porcentaje de IVA. Después debe calcular el coste de mano de obra,
el subtotal, el IVA y el total, y mostrar un presupuesto desglosado.
Python permite literales en distintas bases:
Divide el problema en módulos `.py`. Propón al menos tres módulos e indica la
responsabilidad de cada uno. Puedes considerar, por ejemplo, un módulo para
coordinar el programa, otro para los cálculos y otro para solicitar o mostrar
información. No existe una única división correcta: lo importante es que cada
módulo tenga una responsabilidad clara y que el programa principal coordine el
trabajo.
octal = 0o52
Completa una tabla como esta:

| Módulo propuesto | Responsabilidad | Funciones que podría contener |
| --- | --- | --- |
| `main.py` | `__________` | `__________` |
| `__________` | `__________` | `__________` |
| `__________` | `__________` | `__________` |
Representan números con parte decimal usando punto:
Al terminar, explica por qué no conviene escribir todo el programa en un solo
archivo. Los módulos de esta actividad son archivos Python que contienen código;
no se pide guardar datos en ficheros ni usar bases de datos.
saldo = -15.75
### Actividad 3.5: diseñar las llamadas entre módulos

Usa la propuesta de módulos de la actividad 3.4 para diseñar cómo colaboran.
Escribe el nombre de una función que podría realizar cada tarea y qué
información recibe o devuelve:
print(0.1 + 0.2)  # puede mostrar 0.30000000000000004
| Tarea | Función propuesta | Información que recibe o devuelve |
| --- | --- | --- |
| Pedir los datos del presupuesto | `__________` | `__________` |
| Calcular el coste de mano de obra | `__________` | `__________` |
| Calcular el IVA y el total | `__________` | `__________` |
| Mostrar el presupuesto | `__________` | `__________` |

Después dibuja un esquema con flechas que muestre qué módulos llaman a las
funciones de otros. El flujo debe comenzar en `main.py`; indica qué función
coordina las llamadas y en qué orden se prepara y se muestra el presupuesto.
No hace falta escribir el programa completo.
```python

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

```python
saludo = "hola"
saludo_mayusculas = saludo.upper()
print(saludo)             # hola
print(saludo_mayusculas)  # HOLA
```

El método `upper()` no modifica la cadena original: devuelve una nueva cadena.
Por eso `saludo` conserva el valor `"hola"`.

En cambio, algunos métodos de las listas modifican el objeto existente. Por
ejemplo, `sort()` ordena la lista y devuelve `None`:

```python
numeros = [3, 1, 2]
resultado = numeros.sort()
print(numeros)   # [1, 2, 3]
print(resultado) # None
```

Si se necesita obtener una lista ordenada sin modificar la original, se puede
usar `sorted()`:

```python
numeros = [3, 1, 2]
ordenados = sorted(numeros)
print(numeros)   # [3, 1, 2]
print(ordenados) # [1, 2, 3]
```

Antes de usar un método, conviene comprobar si modifica el objeto o si devuelve
uno nuevo.

if not nombre:
	print("El nombre está vacío")
```

### Actividad 5.1: elección de tipos

Asigna un tipo apropiado a cada dato: nombre de una persona, número de matrícula, precio, lista de asignaturas, coordenadas GPS, permisos de usuario y ausencia de fecha de cierre. Justifica cada elección.

---

## 6. Literales

[⬆ Volver al índice](#índice)

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

[⬆ Volver al índice](#índice)

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

[⬆ Volver al índice](#índice)

Una expresión combina valores, variables, operadores y llamadas para producir un resultado.

### 8.1 Tipos numéricos y operadores aritméticos

Python trabaja principalmente con enteros (`int`), números decimales
(`float`) y números complejos (`complex`). En los literales decimales se usa
un punto, no una coma: `3.5` es un número decimal, mientras que `3,5` crea una
pareja de valores.

Los guiones bajos permiten mejorar la lectura de números largos sin cambiar su
valor:

```python
poblacion = 48_000_000
micras = 0.000_001
```

También se pueden escribir números en binario (`0b`), octal (`0o`) y
hexadecimal (`0x`):

```python
binario = 0b1010       # 10
octal = 0o12           # 10
hexadecimal = 0xA      # 10
```

#### Operaciones básicas

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

La división entera `//` devuelve el cociente redondeado hacia abajo, no el
cociente truncado hacia cero. El resto `%` y el cociente están relacionados
por la expresión `a == (a // b) * b + (a % b)`.

```python
print(11 // 3)       # 3
print(11 % 3)        # 2
print(divmod(11, 3)) # (3, 2)
```

`divmod()` devuelve en una tupla el cociente y el resto. Tanto `/` como `//`,
`%` y `divmod()` producen un error `ZeroDivisionError` si el divisor es cero.

#### Potencias y raíces

El operador `**` calcula potencias. Los exponentes negativos producen el
inverso y los exponentes fraccionarios permiten calcular raíces:

```python
print(2 ** 3)       # 8
print(10 ** -2)     # 0.01
print(9 ** 0.5)     # 3.0
print(pow(2, 3, 5)) # 3: (2 ** 3) % 5
```

Hay que usar paréntesis cuando el signo negativo forma parte de la base:

```python
print(-2 ** 2)      # -4
print((-2) ** 2)    # 4
```

#### Redondeo y precisión

`round()` redondea un número. Su segundo argumento indica cuántas cifras
decimales conservar y también puede ser negativo para redondear decenas,
centenas, etc. En los casos exactamente intermedios, Python utiliza el
redondeo al par más cercano.

```python
print(round(4.3527))      # 4
print(round(4.3527, 2))   # 4.35
print(round(4352, -2))    # 4400
print(round(2.5))         # 2
print(round(3.5))         # 4
```

Los `float` se almacenan normalmente en formato binario y algunos decimales
no se pueden representar exactamente. Por eso un cálculo sencillo puede
mostrar una pequeña diferencia:

```python
print(0.1 + 0.1 + 0.1)    # 0.30000000000000004
```

Para mostrar resultados al usuario se puede usar un formato como `:.2f`, pero
no conviene redondear resultados intermedios que se reutilizarán en cálculos
posteriores. Cuando se necesita exactitud decimal, se puede utilizar
`decimal.Decimal`.

#### Funciones matemáticas habituales

Algunas operaciones frecuentes están disponibles como funciones integradas:

```python
print(abs(-7))                    # 7
print(max(4, 8, 2))               # 8
print(min(4, 8, 2))               # 2
print(sum([1, 2, 3, 4]))           # 10
```

Para redondear hacia abajo o hacia arriba se puede importar el módulo `math`:

```python
import math

print(math.floor(2.9))             # 2
print(math.ceil(2.1))              # 3
print(math.sqrt(25))               # 5.0
```

La información de esta ampliación se basa en [Números y operaciones
aritméticas elementales](https://www.mclibre.org/consultar/python/lecciones/python-operaciones-matematicas.html),
de mclibre.org.

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

[⬆ Volver al índice](#índice)

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

[⬆ Volver al índice](#índice)

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

[⬆ Volver al índice](#índice)

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

[⬆ Volver al índice](#índice)

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

[⬆ Volver al índice](#índice)

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

[⬆ Volver al índice](#índice)

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

[⬆ Volver al índice](#índice)

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

[⬆ Volver al índice](#índice)

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

[⬆ Volver al índice](#índice)

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

[⬆ Volver al índice](#índice)

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

## 19. Documentación y documentación de programas

[⬆ Volver al índice](#índice)

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

## 20. Programación orientada a objetos

[⬆ Volver al índice](#índice)

La programación orientada a objetos (POO) organiza un programa mediante objetos que combinan estado (datos) y comportamiento (operaciones). Una clase define cómo serán sus objetos; cada objeto concreto creado a partir de ella se denomina instancia.

### 20.1 Clases, instancias, atributos y métodos

Los atributos describen el estado de una instancia y los métodos definen operaciones que puede realizar. El método especial `__init__` inicializa el objeto cuando se crea. El parámetro `self` representa la instancia actual y aparece como primer parámetro de los métodos de instancia; Python lo proporciona al llamar al método.

```python
class Rectangulo:
	def __init__(self, ancho, alto):
		if ancho <= 0 or alto <= 0:
			raise ValueError("Las dimensiones deben ser positivas")
		self.ancho = ancho
		self.alto = alto

	def calcular_area(self):
		return self.ancho * self.alto


rectangulo = Rectangulo(5, 3)
print(rectangulo.calcular_area())  # 15
```

`Rectangulo` es la clase; `rectangulo` es una instancia. `ancho` y `alto` son atributos de instancia, y `calcular_area()` es un método. Cada instancia mantiene sus propios valores.

### 20.2 Encapsulación y propiedades

La encapsulación consiste en mantener juntos el estado y las operaciones que lo modifican, ofreciendo una interfaz clara. En Python, un atributo sin prefijo especial se considera público. Un guion bajo inicial, como `_saldo`, indica por convención que se trata de un detalle interno; no lo hace inaccesible.

Una propiedad permite consultar un valor mediante una sintaxis de atributo y, a la vez, controlar cómo se obtiene:

```python
class Cuenta:
	def __init__(self, titular, saldo_inicial=0):
		if saldo_inicial < 0:
			raise ValueError("El saldo inicial no puede ser negativo")
		self.titular = titular
		self._saldo = saldo_inicial

	@property
	def saldo(self):
		return self._saldo

	def ingresar(self, cantidad):
		if cantidad <= 0:
			raise ValueError("La cantidad debe ser positiva")
		self._saldo += cantidad


cuenta = Cuenta("Ana", 100)
cuenta.ingresar(25)
print(cuenta.saldo)  # 125
```

Se consulta `cuenta.saldo` sin paréntesis porque es una propiedad. La modificación del saldo se realiza mediante un método que puede comprobar la cantidad recibida.

### 20.3 Atributos de clase y de instancia

Un atributo de instancia pertenece a un objeto concreto. Un atributo de clase se define en la clase y se comparte como valor común entre sus instancias mientras no se sobrescriba:

```python
class Alumno:
	centro = "IES Central"

	def __init__(self, nombre):
		self.nombre = nombre


ana = Alumno("Ana")
luis = Alumno("Luis")
print(ana.nombre, luis.nombre)
print(ana.centro, luis.centro)
```

Conviene usar atributos de clase para datos realmente comunes. El estado que cambia de una instancia a otra debe guardarse en atributos de instancia.

### 20.4 Herencia y polimorfismo

La herencia permite definir una clase especializada a partir de otra. La clase hija puede reutilizar métodos de la clase base, añadir comportamiento y redefinir métodos. `super()` permite llamar a la implementación de la clase base.

```python
class Vehiculo:
	def __init__(self, marca):
		self.marca = marca

	def descripcion(self):
		return f"Vehículo de marca {self.marca}"


class Coche(Vehiculo):
	def __init__(self, marca, numero_puertas):
		super().__init__(marca)
		self.numero_puertas = numero_puertas

	def descripcion(self):
		return f"Coche {self.marca} de {self.numero_puertas} puertas"


vehiculo = Vehiculo("Genérica")
coche = Coche("Ejemplo", 5)
print(vehiculo.descripcion())
print(coche.descripcion())
```

El polimorfismo permite utilizar objetos de distintas clases a través de una operación común, como `descripcion()`. La herencia resulta útil cuando existe una relación «es un tipo de»; no conviene crear jerarquías solo para compartir unas pocas líneas.

### 20.5 Composición

La composición representa una relación «tiene un»: un objeto utiliza otro objeto como parte de su funcionamiento. A menudo es una alternativa más sencilla y flexible que la herencia.

```python
class Motor:
	def arrancar(self):
		return "Motor en marcha"


class CocheConMotor:
	def __init__(self, marca):
		self.marca = marca
		self.motor = Motor()

	def arrancar(self):
		return f"{self.marca}: {self.motor.arrancar()}"


coche = CocheConMotor("Ejemplo")
print(coche.arrancar())
```

### 20.6 Métodos especiales y representaciones

Los métodos especiales permiten definir cómo interactúan los objetos con operaciones y funciones de Python. Por ejemplo, `__str__` proporciona una representación legible para las personas cuando se usa `print()`:

```python
class Producto:
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio = precio

	def __str__(self):
		return f"{self.nombre}: {self.precio:.2f} euros"


producto = Producto("Cuaderno", 2.5)
print(producto)
```

Otros métodos especiales habituales son `__repr__`, para una representación útil durante el desarrollo, y `__eq__`, para definir cómo se comparan dos instancias con `==`. No se deben confundir con métodos normales llamados directamente: Python los invoca al realizar determinadas operaciones.

### 20.7 Clases de datos

Cuando una clase sirve principalmente para agrupar datos, `dataclasses` puede generar automáticamente métodos habituales como `__init__`, `__repr__` y `__eq__`:

```python
from dataclasses import dataclass


@dataclass
class Coordenada:
	x: float
	y: float


punto = Coordenada(3, 4)
print(punto)  # Coordenada(x=3, y=4)
```

`@dataclass` reduce código repetitivo, pero no sustituye el diseño de la clase ni añade validaciones automáticamente. Se pueden añadir métodos propios cuando el objeto necesita comportamiento.

### Actividad 20.1: clase Rectangulo

Implementa una clase `Rectangulo` que reciba ancho y alto, calcule el área y el perímetro, y rechace dimensiones no positivas. Crea dos instancias con dimensiones diferentes y muestra ambos resultados. No uses listas ni tuplas.

---

## 21. Proyecto práctico integrador: gestor de tareas en consola

[⬆ Volver al índice](#índice)

El siguiente proyecto combina variables, tipos, funciones, listas, diccionarios, selección, repetición, excepciones, documentación y depuración. Permite añadir, listar, completar y eliminar tareas.

### 21.1 Diseño

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

### 21.2 Implementación completa

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

### 21.3 Mejoras propuestas

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

## 22. Ejercicios y actividades

[⬆ Volver al índice](#índice)

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

## 23. Soluciones orientativas

[⬆ Volver al índice](#índice)

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

## 24. Resumen y lista de comprobación

[⬆ Volver al índice](#índice)

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
