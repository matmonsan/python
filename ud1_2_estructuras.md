---
title: "UD1.2: Introducción a la programación en Python. Estructuras."
description: "<strong>Módulo:</strong> Programación y Automatización en Sistemas Informáticos y en Red <br> <strong>Profesor:</strong> Matías Montávez Sánchez"
---

## Índice

1. [Uso de estructuras de control](#1-uso-de-estructuras-de-control)
2. [Selección y estructuras de selección](#2-selección-y-estructuras-de-selección)
   - [Actividades 2](#actividades-2)
3. [Repetición y estructuras de repetición](#3-repetición-y-estructuras-de-repetición)
   - [Actividades 3](#actividades-3)
4. [Estructuras de salto](#4-estructuras-de-salto)
5. [Control de excepciones](#5-control-de-excepciones)
   - [Actividades 5](#actividades-5)
6. [Depuración y depurador](#6-depuración-y-depurador)
7. [El depurador como herramienta de control de errores](#7-el-depurador-como-herramienta-de-control-de-errores)
   - [Actividades 7](#actividades-7)
8. [Documentación y documentación de programas](#8-documentación-y-documentación-de-programas)
   - [Actividades 8](#actividades-8)
9. [Programación orientada a objetos](#9-programación-orientada-a-objetos)
   - [Actividades 9](#actividades-9)
10. [Proyecto práctico integrador: gestor de tareas en consola](#10-proyecto-práctico-integrador-gestor-de-tareas-en-consola)
11. [Ejercicios y actividades](#11-ejercicios-y-actividades)
12. [Soluciones orientativas](#12-soluciones-orientativas)

---

## 1. Uso de estructuras de control

[⬆ Volver al índice](#índice)

Las estructuras de control determinan el orden en que se ejecutan las instrucciones. Sin ellas, un programa solo avanzaría de arriba abajo una vez.

Las tres familias principales son:

- **Secuencia:** instrucciones en orden.
- **Selección:** elegir entre caminos.
- **Repetición:** ejecutar un bloque varias veces.

### 1.1 Secuencia

```python
nombre = input("Nombre: ")
saludo = f"Hola, {nombre}"
print(saludo)
```

### 1.2 Condición como expresión booleana

```python
saldo = 100
retirada = 40

if retirada <= saldo:
	saldo -= retirada
```

### 1.3 Repetición controlada por colección

```python
for numero in [1, 2, 3]:
	print(numero)
```

### 1.4 Repetición controlada por condición

```python
respuesta = ""
while respuesta.lower() != "salir":
	respuesta = input("Escribe salir para terminar: ")
```

### 1.5 Diseñar antes de codificar

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

## 2. Selección y estructuras de selección

[⬆ Volver al índice](#índice)

Las estructuras de selección ejecutan uno u otro bloque según una condición.

### 2.1 `if`

```python
temperatura = 28

if temperatura > 25:
	print("Hace calor")
```

Si la condición es falsa, el bloque no se ejecuta.

### 2.2 `if ... else`

```python
numero = 7

if numero % 2 == 0:
	print("Es par")
else:
	print("Es impar")
```

### 2.3 `if ... elif ... else`

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

### 2.4 Condiciones compuestas

```python
edad = 25
documento_valido = True

if edad >= 18 and documento_valido:
	print("Acceso permitido")
```

### 2.5 Guard clauses

Una guard clause termina pronto un caso inválido y evita anidamientos:

```python
def procesar_edad(edad):
	if edad < 0:
		return "Edad no válida"
	if edad < 18:
		return "Menor"
	return "Adulto"
```

### 2.6 `match` y `case`

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

### 2.7 Evitar comparaciones innecesarias

```python
activo = True

if activo:
	print("Activo")

# Menos idiomático:
# if activo == True:
#     print("Activo")
```

### Actividades 2

#### Actividad 1: menú

Crea un menú con las opciones `1. Añadir`, `2. Consultar`, `3. Eliminar` y `4. Salir`. Usa una estructura de selección y muestra un mensaje específico para cada opción. La opción desconocida debe producir un aviso.

---

## 3. Repetición y estructuras de repetición

[⬆ Volver al índice](#índice)

Los bucles permiten repetir acciones sin duplicar código.

### 3.1 Bucle `for`

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

### 3.2 Recorrer listas y diccionarios

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

### 3.3 Bucle `while`

Se repite mientras una condición sea verdadera:

```python
contador = 3
while contador > 0:
	print(contador)
	contador -= 1
print("Fin")
```

Hay que modificar alguna variable de control o usar una salida para evitar bucles infinitos.

### 3.4 Menús repetitivos

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

### 3.5 Comprensiones

```python
pares = [numero for numero in range(20) if numero % 2 == 0]
```

Una comprensión equivale conceptualmente a un bucle que construye una colección, pero debe mantenerse sencilla.

### 3.6 `else` en bucles

El `else` de un bucle se ejecuta si el bucle termina normalmente, no si se interrumpe con `break`:

```python
for numero in range(2, 10):
	if numero == 7:
		print("Encontrado")
		break
else:
	print("No encontrado")
```

### 3.7 Evitar modificar una colección mientras se recorre

Puede provocar resultados inesperados. Es más seguro construir otra colección:

```python
numeros = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
```

### Actividades 3

#### Actividad 1: estadísticas

Pide números hasta que se escriba `fin`. Guarda los válidos y muestra cantidad, suma, media, mínimo y máximo. Decide qué debe ocurrir si no se introduce ningún número.

---

## 4. Estructuras de salto

[⬆ Volver al índice](#índice)

Las estructuras de salto modifican el flujo habitual de un bucle o una función.

### 4.1 `break`

Termina el bucle más cercano:

```python
for numero in range(100):
	if numero == 10:
		break
	print(numero)
```

### 4.2 `continue`

Salta el resto de la iteración actual y continúa con la siguiente:

```python
for numero in range(1, 11):
	if numero % 2 == 0:
		continue
	print(numero)  # solo impares
```

### 4.3 `pass`

No hace nada; sirve como marcador sintáctico temporal:

```python
def funcionalidad_pendiente():
	pass
```

No debe utilizarse para ocultar errores ni como sustituto permanente de una implementación requerida.

### 4.4 `return`

Termina una función y puede entregar un valor:

```python
def es_par(numero):
	return numero % 2 == 0
```

Un `return` sin valor devuelve `None`.

### 4.5 `raise`

Lanza una excepción de manera explícita:

```python
def dividir(a, b):
	if b == 0:
		raise ValueError("El divisor no puede ser cero")
	return a / b
```

### 4.6 `yield`

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

## 5. Control de excepciones

[⬆ Volver al índice](#índice)

Una excepción es un evento que interrumpe el flujo normal porque se ha producido una situación excepcional: entrada inválida, archivo inexistente, división por cero o fallo de red.

### 5.1 Excepción básica

```python
numero = int("no es un número")  # ValueError
```

El intérprete muestra el tipo de excepción, el mensaje y el traceback, que indica la ruta de llamadas hasta el error.

### 5.2 `try` y `except`

```python
try:
	edad = int(input("Edad: "))
except ValueError:
	print("Debes introducir un entero")
```

Se debe capturar la excepción concreta que se sabe manejar. Capturar `Exception` sin una razón clara puede ocultar errores de programación.

### 5.3 `else`

El bloque `else` se ejecuta solo si no ocurrió una excepción:

```python
try:
	numero = int(input("Número: "))
except ValueError:
	print("Entrada inválida")
else:
	print(f"El doble es {numero * 2}")
```

### 5.4 `finally`

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

### 5.5 Varias excepciones

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

### 5.6 Capturar como variable

```python
try:
	numero = int("abc")
except ValueError as error:
	print(f"Detalle: {error}")
```

### 5.7 Lanzar excepciones propias

```python
def establecer_porcentaje(porcentaje):
	if not 0 <= porcentaje <= 100:
		raise ValueError("El porcentaje debe estar entre 0 y 100")
	return porcentaje
```

### 5.8 Excepciones personalizadas

```python
class SaldoInsuficienteError(Exception):
	"""Indica que una operación supera el saldo disponible."""


def retirar(saldo, cantidad):
	if cantidad > saldo:
		raise SaldoInsuficienteError("Saldo insuficiente")
	return saldo - cantidad
```

### 5.9 Encadenamiento de excepciones

```python
def leer_entero_desde_texto(texto):
	try:
		return int(texto)
	except ValueError as error:
		raise ValueError("El texto no contiene un entero") from error
```

`from error` conserva la causa original y facilita el diagnóstico.

### 5.10 Buenas prácticas

- Capturar la excepción más específica posible.
- Mantener el bloque `try` pequeño.
- No usar `except: pass` salvo casos muy justificados.
- Mostrar mensajes útiles para la persona usuaria.
- Registrar detalles técnicos cuando el programa sea una aplicación real.
- No utilizar excepciones para sustituir todas las condiciones normales.
- Liberar recursos con `with` o `finally`.

### Actividades 5

#### Actividad 1: validador resistente

Implementa un conversor de temperatura que acepte Celsius y Fahrenheit, rechace unidades desconocidas y controle entradas no numéricas sin finalizar abruptamente.

---

## 6. Depuración y depurador

[⬆ Volver al índice](#índice)

Depurar es localizar y corregir defectos. No consiste simplemente en leer el código al azar: requiere formular hipótesis, observar el comportamiento y comprobarlas con evidencia.

### 6.1 Proceso sistemático

1. Reproducir el error con una entrada concreta.
2. Leer todo el mensaje y el traceback.
3. Identificar la línea donde se manifiesta el problema.
4. Distinguir síntoma de causa.
5. Formular una hipótesis.
6. Inspeccionar valores y flujo.
7. Aplicar el cambio mínimo que corrija la causa.
8. Repetir la prueba y ejecutar regresiones.

### 6.2 `print()` como observación rápida

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

### 6.3 Afirmaciones

`assert` comprueba una condición que se considera cierta durante el desarrollo:

```python
def calcular_media(total, cantidad):
	assert cantidad > 0, "La cantidad debe ser positiva"
	return total / cantidad
```

No se debe usar `assert` para validar entradas externas en producción, porque las aserciones pueden desactivarse.

### 6.4 Pruebas pequeñas

```python
def es_par(numero):
	return numero % 2 == 0


assert es_par(2) is True
assert es_par(3) is False
```

Las pruebas deben incluir casos normales, límites y entradas inválidas.

### 6.5 Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Aplicación iniciada")
logger.warning("El archivo de configuración no existe")
```

Los niveles habituales son `DEBUG`, `INFO`, `WARNING`, `ERROR` y `CRITICAL`.

### 6.6 Errores lógicos

Un programa puede no producir excepciones y aun así estar mal:

```python
def calcular_media(numeros):
	return sum(numeros) / len(numeros)
```

Hay que decidir qué ocurre con una lista vacía. El problema no se resuelve solo capturando excepciones; se debe definir el contrato de la función.

---

## 7. El depurador como herramienta de control de errores

[⬆ Volver al índice](#índice)

El depurador permite ejecutar un programa paso a paso e inspeccionar su estado interno.

### 7.1 Conceptos principales

- **Breakpoint o punto de interrupción:** línea donde se pausa la ejecución.
- **Step over:** ejecuta la línea actual sin entrar en una función llamada.
- **Step into:** entra en la función llamada.
- **Step out:** termina la función actual y vuelve al llamador.
- **Continue:** continúa hasta el siguiente punto de interrupción.
- **Call stack:** cadena de funciones activas.
- **Variables locales:** nombres disponibles en el contexto actual.
- **Watch o expresión vigilada:** valor que se observa mientras se avanza.

### 7.2 Depurar en Visual Studio Code

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

### 7.3 Depurar desde la biblioteca estándar

Python incluye `pdb`:

```python
def calcular(numero):
	resultado = numero * 2
	breakpoint()
	return resultado + 1


print(calcular(5))
```

En la consola de `pdb` se pueden usar comandos como `n` (next), `s` (step), `p` para imprimir una expresión, `l` para listar código y `c` para continuar.

### 7.4 Depuración remota y configuración

Para proyectos complejos se puede crear `.vscode/launch.json` con configuraciones de ejecución, argumentos, variables de entorno y directorio de trabajo. La configuración debe adaptarse al proyecto y no debe contener secretos.

### 7.5 Estrategias para localizar un error

- Reducir el caso a la entrada mínima que falla.
- Dividir el flujo y comprobar invariantes.
- Comparar un resultado esperado con el real.
- Revisar tipos con `type()` o `isinstance()`.
- Inspeccionar espacios con `repr()`.
- Revisar índices y límites de rangos.
- Probar los valores frontera: cero, vacío, uno, máximo y mínimo.

### Actividades 7

#### Actividad 1: depuración guiada

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

## 8. Documentación y documentación de programas

[⬆ Volver al índice](#índice)

Documentar es explicar cómo usar, mantener y comprender un programa. Una buena documentación reduce el tiempo de incorporación y evita que las decisiones importantes dependan de conversaciones informales.

### 8.1 README

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

### 8.2 Docstrings de funciones

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

### 8.3 Docstrings de clases

```python
class Cuenta:
	"""Representa una cuenta con saldo y operaciones básicas."""

	def __init__(self, titular, saldo=0):
		self.titular = titular
		self.saldo = saldo
```

### 8.4 Type hints

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

### 8.5 Documentar decisiones

La documentación debe explicar el porqué cuando el código no lo hace evidente:

```python
# Se conserva el orden de llegada porque el informe se revisa cronológicamente.
eventos = list(eventos_recibidos)
```

### 8.6 Calidad de la documentación

Una documentación útil es:

- Exacta y actualizada.
- Concisa cuando el comportamiento es obvio.
- Detallada cuando hay reglas o efectos importantes.
- Accionable: permite instalar y ejecutar.
- Verificable: los ejemplos funcionan.
- Coherente con los nombres del código.

### 8.7 Generación automática

Herramientas como Sphinx, pydoc y MkDocs pueden construir documentación a partir de docstrings y archivos Markdown. La generación automática no sustituye la escritura cuidadosa: solo publica lo que se ha expresado en el código.

### Actividades 8

#### Actividad 1: documentar una API

Escribe tres funciones relacionadas con una agenda. Añade anotaciones de tipo, docstrings con parámetros, valor de retorno y excepciones. Después redacta un ejemplo de uso para el `README.md`.

---

## 9. Programación orientada a objetos

[⬆ Volver al índice](#índice)

La programación orientada a objetos (POO) organiza un programa mediante objetos que combinan estado (datos) y comportamiento (operaciones). Una clase define cómo serán sus objetos; cada objeto concreto creado a partir de ella se denomina instancia.

### 9.1 Clases, instancias, atributos y métodos

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

### 9.2 Encapsulación y propiedades

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

### 9.3 Atributos de clase y de instancia

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

### 9.4 Herencia y polimorfismo

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

### 9.5 Composición

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

### 9.6 Métodos especiales y representaciones

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

### 9.7 Clases de datos

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

### Actividades 9

#### Actividad 1: clase Rectangulo

Implementa una clase `Rectangulo` que reciba ancho y alto, calcule el área y el perímetro, y rechace dimensiones no positivas. Crea dos instancias con dimensiones diferentes y muestra ambos resultados. No uses listas ni tuplas.

---

## 10. Proyecto práctico integrador: gestor de tareas en consola

[⬆ Volver al índice](#índice)

El siguiente proyecto combina variables, tipos, funciones, listas, diccionarios, selección, repetición, excepciones, documentación y depuración. Permite añadir, listar, completar y eliminar tareas.

### 10.1 Diseño

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

### 10.2 Implementación completa

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

### 10.3 Mejoras propuestas

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

## 11. Ejercicios y actividades

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

## 12. Soluciones orientativas

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