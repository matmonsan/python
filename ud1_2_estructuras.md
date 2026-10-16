---
title: "UD1.2: Introducción a la programación en Python. Estructuras."
description: "<strong>Módulo:</strong> Programación y Automatización en Sistemas Informáticos y en Red <br> <strong>Profesor:</strong> Matías Montávez Sánchez"
---
[⌂ Volver al inicio](index.md)

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

Estas familias no son alternativas aisladas. Un programa real suele combinar las
tres: primero recibe y prepara unos datos, después toma decisiones sobre ellos y,
por último, repite una operación para cada elemento o hasta que se cumpla una
condición. La estructura elegida debe corresponder al problema que se quiere
resolver, no a una preferencia de escritura.

Un esquema general de un programa puede representarse así:

```text
ENTRADA DE DATOS
       ↓
SECUENCIA DE PASOS
       ↓
DECISIONES
       ↓
ACCIONES REPETIDAS, SI SON NECESARIAS
       ↓
RESULTADO
```

En Python, cada bloque debe quedar claramente separado del siguiente. La
indentación será la forma concreta de marcar esos bloques cuando se estudie la
sintaxis, pero en esta introducción basta con entender que las instrucciones
que pertenecen a una misma decisión o repetición forman un grupo.

### 1.1 Secuencia

La secuencia es el flujo más sencillo: cada paso se realiza una vez y en el
orden en que aparece. El resultado de un paso puede convertirse en la entrada
del siguiente. Por eso el orden sí importa; no es equivalente calcular un total
antes o después de aplicar un descuento.

Un esquema de secuencia sería:

```text
RECIBIR EL NOMBRE
       ↓
PREPARAR EL SALUDO
       ↓
MOSTRAR EL SALUDO
```

La secuencia es suficiente cuando no hay alternativas ni acciones que repetir.
Por ejemplo, un programa que pide un nombre, prepara un mensaje y lo muestra
solo necesita seguir esos pasos consecutivamente.

### 1.2 Condición como expresión booleana

Una condición es una pregunta cuya respuesta solo puede ser afirmativa o
negativa. El programa utiliza esa respuesta para decidir si continúa por un
camino o por otro. Las preguntas pueden comparar cantidades, comprobar si un
dato está disponible o verificar si una situación es válida.

Esquema de una decisión sencilla:

```text
COMPROBAR UNA CONDICIÓN
          ↓
   ¿SE CUMPLE?
     ↙     ↘
   SÍ       NO
   ↓        ↓
REALIZAR  CONTINUAR
ACCIÓN    SIN ESA ACCIÓN
```

Por ejemplo, antes de retirar dinero se puede comprobar si el saldo disponible
es suficiente. Si lo es, se realiza la retirada; si no, se informa de que la
operación no puede hacerse. La comprobación debe realizarse antes de la acción
que depende de ella.

### 1.3 Repetición controlada por colección

La repetición controlada por una colección se utiliza cuando una misma acción
debe realizarse para cada elemento de un conjunto de datos. El programa toma
un elemento, realiza la acción, pasa al siguiente y termina cuando ya no quedan
elementos.

```text
OBTENER LA COLECCIÓN
          ↓
TOMAR EL SIGUIENTE ELEMENTO
          ↓
REALIZAR LA ACCIÓN
          ↓
¿QUEDAN MÁS ELEMENTOS?
      ↙           ↘
    SÍ             NO
    ↑              ↓
VOLVER AL PASO   TERMINAR
ANTERIOR
```

Este modelo evita repetir manualmente las mismas instrucciones y sigue
funcionando aunque la colección tenga más o menos elementos.

### 1.4 Repetición controlada por condición

La repetición controlada por una condición se utiliza cuando no se conoce de
antemano cuántas veces debe repetirse una acción. Antes de cada vuelta se
comprueba si se mantiene la situación que permite continuar.

```text
COMPROBAR LA CONDICIÓN
          ↓
   ¿SE PUEDE CONTINUAR?
      ↙           ↘
    SÍ             NO
    ↓              ↓
REALIZAR        TERMINAR
LA ACCIÓN
    ↑
    └── ACTUALIZAR LOS DATOS
```

Es necesario que cada vuelta pueda cambiar el resultado de la comprobación.
Si la condición nunca cambia, se produce un bucle infinito. Este modelo es
apropiado para menús, reintentos y procesos que terminan cuando el usuario
introduce una respuesta concreta o cuando se alcanza un estado determinado.

### 1.5 Diseñar antes de codificar

Antes de escribir estructuras de control conviene responder:

1. ¿Qué datos entran?
2. ¿Qué resultado debe producirse?
3. ¿Qué decisiones existen?
4. ¿Qué acciones se repiten?
5. ¿Cuándo termina el programa?
6. ¿Qué pasa si la entrada no es válida?

Un esquema sencillo para clasificar una nota sería:

```text
LEER LA NOTA
      ↓
¿ESTÁ ENTRE 0 Y 10?
   ↙           ↘
 NO             SÍ
 ↓              ↓
AVISAR        ¿ALCANZA EL APROBADO?
DEL ERROR       ↙          ↘
              SÍ            NO
              ↓             ↓
          APROBADO       SUSPENSO
```

Este diseño separa los casos y hace visibles las reglas del problema. Después
se puede traducir a Python, comprobar cada camino y añadir validaciones sin
tener que improvisar la lógica mientras se escribe. También conviene preparar
casos de prueba para una nota inválida, una nota exactamente igual al límite
del aprobado, una nota intermedia y la nota máxima.

---

## 2. Selección y estructuras de selección

[⬆ Volver al índice](#índice)

Las estructuras de selección ejecutan uno u otro bloque según una condición.
Permiten representar decisiones del tipo «si ocurre esto, haz una cosa; en caso
contrario, haz otra». La condición debe expresar una pregunta clara sobre los
datos del programa y no mezclar cambios de estado innecesarios.

Python determina el bloque que se ejecuta siguiendo estas reglas:

1. Evalúa la condición del `if`.
2. Si es verdadera, ejecuta ese bloque y omite los bloques alternativos.
3. Si es falsa, prueba el siguiente `elif`, si existe.
4. Si ninguna condición es verdadera, ejecuta `else`, si se ha escrito.

En todos los casos se ejecuta como máximo una rama de una misma cadena
`if`/`elif`/`else`.

### 2.1 `if`

`if` sirve para ejecutar instrucciones solo cuando se cumple una condición. No
es necesario escribir un `else` si no hay ninguna acción que realizar cuando la
condición sea falsa.

```python
temperatura = 28

if temperatura > 25:
    print("Hace calor")
```

Si la temperatura fuese `25` o menor, no se mostraría ningún mensaje y el
programa continuaría después del bloque. Los dos puntos indican que comienza
un bloque y la indentación indica qué instrucciones forman parte de él.

Un `if` es adecuado cuando solo interesa actuar en el caso afirmativo. Por
ejemplo, se puede mostrar una advertencia si queda poco espacio en disco, pero
no hacer nada especial cuando el espacio disponible es suficiente. No conviene
añadir un `else` vacío: si no hay una respuesta para el caso contrario, es más
claro dejarlo sin escribir.

La condición se evalúa con el valor que tienen las variables en ese momento.
Si una variable cambia después, esa modificación no cambia una decisión que ya
se ha tomado. Por eso las comprobaciones deben colocarse justo antes de la
acción que protegen y deben utilizar datos que estén actualizados.

### 2.2 `if ... else`

`else` define el camino alternativo. Se utiliza cuando deben cubrirse
exactamente dos posibilidades, como par/impar, válido/no válido o
disponible/no disponible:

```python
numero = 7

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")
```

El operador `%` calcula el resto de la división. Si el resto de dividir entre
dos es cero, el número es par; si no, es impar. La condición no compara
directamente con las palabras «par» o «impar», sino que deduce la respuesta a
partir del dato.

`else` no lleva una condición propia: representa todos los casos en los que el
`if` no se ha cumplido. Por ese motivo es útil para garantizar una respuesta
completa. En este ejemplo, cualquier entero queda clasificado, porque todo
número es par o impar. Antes de utilizar `else`, conviene comprobar que el caso
alternativo realmente incluye todos los valores restantes y que no se están
ocultando entradas inválidas.

Si el programa acepta datos introducidos por una persona, la comprobación de
paridad debería hacerse después de validar que el dato es numérico. La
selección decide qué hacer con un dato válido; no sustituye por sí sola la
validación del formato de entrada.

### 2.3 `if ... elif ... else`

Cuando hay más de dos resultados posibles se encadenan varias condiciones con
`elif`. El orden es fundamental: las condiciones más específicas o exigentes
deben aparecer antes que las más generales.

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

Las condiciones se evalúan de arriba abajo y solo se ejecuta el primer bloque
verdadero. Con `nota = 8.4`, la primera comparación es falsa y la segunda es
verdadera, por lo que se asigna `notable` y no se revisan las condiciones
restantes. Si se colocara primero `nota >= 5`, todas las notas aprobadas
entrarían en esa rama y nunca se alcanzarían las categorías superiores.

Una cadena de `elif` funciona bien cuando las categorías son excluyentes y
están ordenadas. Los límites deben definirse con cuidado: en el ejemplo, una
nota exactamente igual a `7` obtiene `notable` y una exactamente igual a `5`
obtiene `aprobado`. Probar los valores situados justo en cada límite ayuda a
detectar errores como utilizar `>` cuando se necesitaba `>=`.

`else` puede omitirse si existe un caso que no se desea tratar o si la
validación se realiza en otra parte. Sin embargo, incluirlo suele ser
conveniente cuando el programa debe ofrecer una respuesta para cualquier dato
que llegue hasta esa decisión.

### 2.4 Condiciones compuestas

Los operadores lógicos permiten combinar comprobaciones:

- `and` exige que todas las condiciones sean verdaderas.
- `or` exige que al menos una sea verdadera.
- `not` invierte el resultado lógico.

```python
edad = 25
documento_valido = True

if edad >= 18 and documento_valido:
    print("Acceso permitido")
```

Aquí deben cumplirse simultáneamente la mayoría de edad y la validez del
documento. Los paréntesis ayudan a dejar clara la prioridad cuando se mezclan
`and` y `or`, por ejemplo:

```python
if (es_personal or es_administrador) and cuenta_activa:
    print("Acceso permitido")
```

En la segunda condición, basta con que la persona sea personal o
administradora, pero en ambos casos la cuenta debe estar activa. Sin los
paréntesis, una expresión con varios operadores puede resultar difícil de leer
e interpretar de forma incorrecta al modificarla más adelante.

Python además aplica evaluación en cortocircuito: con `and`, si la primera
parte ya es falsa no necesita evaluar la segunda; con `or`, si la primera ya es
verdadera tampoco necesita evaluar la segunda. Esta característica puede
evitar operaciones innecesarias, pero las condiciones no deberían depender de
efectos secundarios ocultos. Es preferible que cada comprobación sea clara y
predecible.

### 2.5 Guard clauses

Una *guard clause* comprueba al principio un caso inválido y termina pronto la
función. Así se evita envolver toda la lógica válida dentro de varios niveles
de `if` anidados:

```python
def procesar_edad(edad):
    if edad < 0:
        return "Edad no válida"
    if edad < 18:
        return "Menor"
    return "Adulto"
```

Cada `return` deja claro qué resultado corresponde a cada caso. Si la función
recibe `-1`, no continúa con las comprobaciones posteriores. Esta técnica es
especialmente útil para validar parámetros al comienzo de una función.

Las guard clauses no significan que toda función deba tener muchos `return`.
Su objetivo es separar pronto los casos excepcionales y dejar la ruta normal
sin anidamientos. Una función bien diseñada debe mantener un orden fácil de
seguir: primero rechaza los datos imposibles, después comprueba los casos
especiales y finalmente ejecuta el caso válido.

También es importante decidir qué ocurre ante un dato incorrecto. La función
puede devolver un mensaje, devolver un valor especial o lanzar una excepción,
según el contrato del programa. La guard clause organiza la decisión, pero no
elige por sí sola la estrategia de comunicación del error.

### 2.6 `match` y `case`

Desde Python 3.10 se puede hacer coincidencia estructural. `match` compara un
valor con varios patrones y ejecuta el primer `case` que coincide:

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

El patrón `_` actúa como caso por defecto y coincide con cualquier valor que no
haya coincidido antes. `match` es útil cuando hay muchos patrones posibles o
cuando se comparan estructuras de datos. Para una sola condición booleana,
`if` suele ser más claro.

Cada `case` representa una posibilidad concreta del valor que se está
analizando. En el ejemplo, el programa no pregunta si el comando es mayor,
menor o igual que otro valor, sino que compara su forma con varios patrones
conocidos. El caso `_` evita que una entrada desconocida quede sin respuesta.

`match` no debe utilizarse solo porque el código parezca más moderno. Si las
decisiones dependen de intervalos, de varias comprobaciones lógicas o de
condiciones que no son patrones concretos, una cadena de `if`/`elif` suele
expresar mejor la regla. La elección debe favorecer la lectura del criterio que
se está aplicando.

También es posible añadir una **guarda** a un `case` mediante `if`. La guarda
se evalúa después de que el patrón haya coincidido, por lo que permite expresar
comparaciones como intervalos o combinar varias condiciones:

En cada `case`, `valor` es una variable que captura el valor que se está
analizando: aquí, el valor de `numero`. Por tanto, como `numero` vale `12`,
la primera guarda comprueba si `12 > 10` y se ejecuta ese bloque. El nombre
`valor` podría sustituirse por otro nombre; no es una palabra especial de
`match`.

```python
numero = 12

match numero:
    case valor if valor > 10:
        print("Mayor que 10")
    case valor if 0 <= valor <= 10:
        print("Entre 0 y 10")
    case _:
        print("Negativo")
```

También se pueden combinar alternativas dentro de un patrón y utilizar una
guarda para una comprobación adicional:

```python
rol = "editor"
cuenta_activa = True

match rol:
    case "admin" | "editor" if cuenta_activa:
        print("Puede modificar contenido")
    case _:
        print("Acceso limitado")
```

Por tanto, `match` sí puede participar en comprobaciones complejas, pero no
conviene forzar toda la lógica dentro de un `case`. Si la decisión consiste
principalmente en varias expresiones booleanas independientes, `if`/`elif`
normalmente resulta más directo. `match` aporta más claridad cuando primero se
quiere identificar el tipo, la forma o el valor de los datos y después aplicar
una condición adicional.

### 2.7 Evitar comparaciones innecesarias

Los valores booleanos ya representan una condición, por lo que no hace falta
compararlos explícitamente con `True` o `False`:

```python
activo = True

if activo:
    print("Activo")

# Menos idiomático:
# if activo == True:
#     print("Activo")
```

También se puede comprobar directamente si una colección contiene elementos:

```python
usuarios = ["Ana"]
if usuarios:
    print("Hay usuarios para procesar")
```

Una lista vacía, una cadena vacía, `0` y `None` se consideran falsos en una
condición. Conviene usar esta característica cuando mejora la legibilidad, pero
comparar explícitamente con `None` sigue siendo recomendable:

```python
resultado = buscar_usuario()
if resultado is None:
    print("Usuario no encontrado")
```

Estos valores se conocen como valores *falsy*. Muchos valores distintos de
ellos se consideran *truthy*, como una lista con elementos, una cadena no vacía
o un número distinto de cero. No significa que sean literalmente `True` o
`False`, sino que Python puede utilizarlos como resultado práctico de una
condición.

Hay que diferenciar entre «no hay valor» y «el valor es falso». Por ejemplo,
`0` puede ser una cantidad válida y no debería confundirse automáticamente con
un resultado ausente. Cuando esa diferencia importa, conviene comparar de
forma explícita y documentar qué representa cada valor.

### Actividades 2

#### Actividad 1: simulación de operaciones bancarias

Simula una única operación de un banco. Parte de una cuenta existente con un
titular, un saldo inicial aleatorio entre `0 €` y `1.000 €` y el estado de la
cuenta. Solicita la operación que se quiere realizar: `ingresar`, `retirar`,
`abrir cuenta`, `cerrar cuenta` o `consultar`.

Cada operación debe producir el resultado adecuado:

- al ingresar, solicita una cantidad positiva y actualiza el saldo;
- al retirar, solicita una cantidad positiva e impide que el saldo quede
  negativo;
- al abrir cuenta, informa si ya existe una cuenta activa;
- al cerrar cuenta, solo permite el cierre si el saldo es exactamente `0`;
- al consultar, muestra el titular, el saldo y el estado de la cuenta;
- una operación desconocida debe mostrar un aviso claro.

Normaliza el texto de la operación para aceptar mayúsculas y espacios
sobrantes. Muestra el estado final de la cuenta tras la operación. Prueba, como
mínimo, un ingreso válido e inválido, una retirada con y sin saldo suficiente,
un intento de cierre con saldo y otro con saldo `0`. El programa debe resolver
una sola operación; no es necesario repetir el menú.

#### Actividad 2: calcular el precio de una entrada

Una sala de cine vende entradas con estas reglas:

- la entrada general cuesta `8 €`;
- las personas menores de `12` años pagan `5 €`;
- las personas de `65` años o más pagan `6 €`;
- los miércoles se aplica un descuento adicional de `1 €`;
- una sesión en formato 3D añade `2 €`.

Pide la edad, el día de la semana y si la sesión es 3D. Calcula el precio final
y muestra el desglose de los importes aplicados. Rechaza edades negativas y
decide qué debe ocurrir con una edad que no pueda convertirse a número.
Normaliza el día introducido para aceptar mayúsculas y espacios sobrantes.
Prueba edades por debajo, justo en y por encima de `12` y `65`, tanto en una
sesión normal como en una sesión 3D.

#### Actividad 3: calculadora con módulos

Crea una calculadora formada por dos archivos:

- `operaciones.py`, que contiene una función independiente para cada operación:
  sumar, restar, multiplicar y dividir;
- `calculadora.py`, que solicita dos números y la operación deseada, importa las
  funciones necesarias desde `operaciones.py` y muestra el resultado.

Cada función debe recibir dos valores y devolver el resultado, sin pedir datos
ni mostrar mensajes. La división debe controlar el caso de divisor igual a `0`
y comunicarlo de forma clara al programa principal. La calculadora debe aceptar
las operaciones `+`, `-`, `*` y `/`, además de informar de una operación no
reconocida.

El programa principal de `calculadora.py` solo debe ejecutarse cuando ese
archivo sea el módulo principal. Prueba cada operación con números enteros y
decimales, una división entre cero y un símbolo de operación inválido.

#### Actividad 4: calcular un envío

Una tienda calcula el coste de envío según el peso del paquete y el tipo de
entrega:

- hasta `1 kg`: `3 €`;
- más de `1 kg` y hasta `5 kg`: `6 €`;
- más de `5 kg`: `10 €`;
- la entrega urgente añade `4 €`;
- los pedidos superiores a `50 €` no pagan el envío estándar.

Pide el importe del pedido, el peso y si se desea entrega urgente. Valida que
el importe y el peso sean valores no negativos. Muestra el coste de transporte
y el total de la compra. Si el pedido supera `50 €`, explica si la entrega
urgente se mantiene como coste adicional. Prueba valores en los límites del
peso y del importe, con entrega normal y urgente.

#### Actividad 5: recomendar un plan de almacenamiento

Una aplicación ofrece tres planes de almacenamiento: `básico`, `profesional`
y `empresa`. Pide el plan elegido, el espacio que necesita la persona en
gigabytes y si necesita copias de seguridad.

Los planes disponibles ofrecen, respectivamente, `50`, `200` y `1000 GB`.
Determina si el plan elegido cubre el espacio solicitado. Las copias de
seguridad solo están incluidas en los planes `profesional` y `empresa`; si se
solicitan en el plan básico, informa de que es necesario cambiar de plan.

Acepta el nombre del plan con mayúsculas y espacios sobrantes, rechaza planes
desconocidos y valida que el espacio solicitado sea un número positivo.
Presenta una recomendación final explicando si el plan sirve, si falta espacio
o si hay que contratar un plan superior. El programa debe resolver una sola
consulta y no necesita repetir el menú ni procesar una colección de consultas.

---

## 3. Repetición y estructuras de repetición

[⬆ Volver al índice](#índice)

Un bucle ejecuta varias veces un bloque de instrucciones. Cada ejecución se
llama **iteración**. En Python hay dos estructuras principales:

- `for`, para recorrer los elementos de una secuencia o repetir una acción un
  número determinado de veces;
- `while`, para repetir una acción mientras se cumpla una condición.

El bloque que se repite se escribe indentado debajo de la línea del bucle.

### 3.1 El bucle `for`

El bucle `for` repite un bloque de instrucciones **una vez por cada elemento**
de una colección o secuencia. En Python, esta es la forma habitual de recorrer
una cadena o una lista. No se indica un contador ni se avanza manualmente: el
propio `for` toma el siguiente elemento en cada vuelta.

La forma general es:

```python
for variable in secuencia:
	# instrucciones que se repiten
	pass
```

`variable` es un nombre que se elige para representar el elemento actual.
`secuencia` es aquello que se quiere recorrer. Las instrucciones indentadas se
ejecutan en cada vuelta. Cuando ya no quedan elementos, el bucle termina.

Por ejemplo:

```python
for letra in "Sol":
	print(letra)
```

Primero `letra` vale `"S"` y se ejecuta `print(letra)`. Después vale `"o"` y
se vuelve a ejecutar la instrucción; por último vale `"l"`. El resultado son
tres líneas: `S`, `o` y `l`.

```python
frutas = ["pera", "uva", "manzana"]

for fruta in frutas:
	print(fruta)
```

En este caso, `fruta` toma primero el valor `"pera"`, luego `"uva"` y después
`"manzana"`. Como la lista tiene tres elementos, el bloque se ejecuta tres
veces. Este uso de `for` es parecido al `foreach` de otros lenguajes: se
recorren directamente los elementos, sin trabajar con sus posiciones.

#### Repetir con `range()`

Si no se necesita recorrer una lista concreta y solo se quiere repetir una
acción cierta cantidad de veces, se usa `range()`:

```python
for numero in range(5):
	print(numero)
```

`range(5)` proporciona los números `0`, `1`, `2`, `3` y `4`; por eso el bloque
se ejecuta cinco veces. En cada vuelta, `numero` recibe uno de esos valores.
El número final (`5`) no se incluye.

También se pueden indicar el inicio y el final:

```python
for numero in range(1, 4):
	print(numero)  # 1, 2, 3
```

Y, si hace falta, cuánto avanzar entre un número y el siguiente:

```python
for numero in range(2, 10, 2):
	print(numero)  # 2, 4, 6, 8
```

En `range(inicio, fin, paso)`, el recorrido empieza en `inicio`, avanza según
`paso` y se detiene antes de `fin`. Si solo se da el final, se empieza en `0`
y se avanza de uno en uno. El paso también puede ser negativo para contar hacia
atrás:

```python
for numero in range(3, 0, -1):
	print(numero)  # 3, 2, 1
```

Por tanto, `for` y `foreach` no son dos tipos de bucle de Python: Python tiene
la instrucción `for`, que recorre los valores que se le proporcionan. Para
recorrer los elementos se escribe `for elemento in coleccion`; para repetir un
número de veces, se combina con `range()`. La forma `for...of` pertenece a
JavaScript, no a Python.

#### Usar `for` para procesar elementos

Un bucle puede ir procesando los valores y guardar un resultado en una
variable. Por ejemplo, para sumar los precios de una lista:

```python
precios = [10.5, 8.0, 12.25]
total = 0

for precio in precios:
	total = total + precio

print(total)  # 30.75
```

`total` empieza en `0`; en cada iteración se le añade el precio actual.
También se puede escribir `total += precio`.

### 3.2 El bucle `while`

`while` repite un bloque **mientras** su condición sea verdadera. La condición
se comprueba antes de cada iteración:

```python
contador = 3

while contador > 0:
	print(contador)
	contador = contador - 1

print("Fin")
```

Se muestran `3`, `2` y `1`. En cada vuelta se resta uno a `contador`; cuando
llega a `0`, la condición `contador > 0` es falsa y el bucle termina. Si la
condición es falsa desde el principio, el bloque no se ejecuta.

Usa `while` cuando no sepas de antemano cuántas repeticiones harán falta, por
ejemplo, si quieres seguir pidiendo una respuesta hasta que sea válida. Es
importante que algo dentro del bucle permita que la condición cambie. Si nunca
cambia y no hay otra forma de terminar, el programa se queda en un **bucle
infinito**.

### 3.3 Repetir una pregunta o mostrar un menú

Un valor especial puede servir para indicar que se quiere terminar. Se suele
llamar **valor de salida** o **centinela**:

```python
respuesta = input("Escribe algo (o 'fin' para terminar): ")

while respuesta != "fin":
	print(f"Has escrito: {respuesta}")
	respuesta = input("Escribe algo (o 'fin' para terminar): ")
```

La pregunta aparece antes del bucle y al final de cada iteración. Así se
comprueba la respuesta nueva y se puede salir cuando se escribe `"fin"`.

Un menú también puede repetirse usando una condición en el `while`. En este
ejemplo, la variable `opcion` se actualiza después de cada respuesta y el
menú termina cuando se escribe `"3"`:

```python
opcion = ""

while opcion != "3":
	print("1) Saludar")
	print("2) Mostrar ayuda")
	print("3) Salir")
	opcion = input("Elige una opción: ")

	if opcion == "1":
		print("Hola")
	elif opcion == "2":
		print("Selecciona una opción del menú.")
	elif opcion != "3":
		print("Opción no válida")
```

### 3.4 Resumen: ¿qué bucle elegir?

- Elige `for` para recorrer los elementos de una secuencia o repetir una acción
  una cantidad conocida de veces con `range()`.
- Elige `while` para repetir mientras se cumpla una condición, cuando todavía
  no sabes cuántas vueltas serán necesarias.

En cualquier bucle, comprueba qué hace que avance y qué condición hace que
termine. Esto evita repetir trabajo innecesariamente o crear un bucle que no
acaba.

### Actividades 3

Resuelve los siguientes problemas diseñando el orden de las instrucciones, las
condiciones y la repetición necesarias. No uses clases ni excepciones. Cuando
un enunciado indique que los datos introducidos son válidos, no hace falta
programar su validación.

#### Actividad 1: control de acceso

Un sistema permite hasta tres intentos para introducir un código. El código
correcto es `"4826"`.

Pide el código y comunica si el acceso está autorizado. Si no es correcto,
permite intentarlo de nuevo y avisa de cuántos intentos quedan. Después del
tercer error, muestra que el acceso se ha bloqueado. Cuando el código sea
correcto, no vuelvas a pedirlo.

Prueba el caso en que se acierta en el primer intento, en el último intento y
en ninguno. Resuelve el ejercicio usando un bucle y condicionales.

#### Actividad 2: comprobar si un número es primo

Pide un número entero mayor que `1` y determina si es primo. Un número primo
solo se puede dividir exactamente entre `1` y entre sí mismo.

Prueba, si algún número entre `2` y el número anterior al
introducido lo divide exactamente. Si encuentras un divisor, el número no es
primo, si terminas las comprobaciones sin encontrar ninguno, sí lo es.
Muestra el resultado. Comprueba el programa con un número primo, uno compuesto
y el `2`, que es el menor número primo.

#### Actividad 3: máquina expendedora

Una máquina vende un producto que cuesta `170` céntimos. Solicita el valor de
cada moneda en céntimos, de una en una; acepta `10`, `20`, `50` y `100`. La
persona puede introducir monedas hasta completar el precio.

Si se introduce una moneda no aceptada, informa del problema y vuelve a
solicitar una moneda sin aumentar el importe pagado. Cuando se haya alcanzado
o superado el precio, indica que entrega el producto y cuánto cambio debe
devolver. El programa debe terminar en cuanto la compra se pueda completar.

No hace falta validar que la entrada se pueda convertir a número. Al final,
muestra el cambio tanto en céntimos como en euros.

#### Actividad 4: control de aforo de una sala

Una sala admite como máximo `8` personas. El programa debe llevar la cuenta de
cuántas hay dentro. En cada turno, pide una acción: `entra`, `sale` o `fin`.

- Si la acción es `entra` y aún hay plazas, aumenta el aforo ocupado en uno.
- Si la sala está llena, no admitas a nadie más e informa de ello.
- Si la acción es `sale` y hay personas dentro, reduce el aforo ocupado en
  uno.
- Si la sala está vacía, no permitas que salga una persona y avisa de que no
  hay nadie dentro.
- Si se escribe `fin`, termina el control e informa de cuántas personas quedan
  en la sala.

Después de cada acción distinta de `fin`, muestra el aforo actual. Supón que
las acciones introducidas son válidas. Prueba entradas y salidas en los
límites, como intentar entrar con la sala llena y salir cuando está vacía.

#### Actividad 5: simulación de operaciones bancarias

Simula el uso de una cuenta bancaria mediante un menú que se repite hasta que
se elija `salir`. La cuenta empieza activa, tiene un titular y un saldo inicial
aleatorio entre `0 €` y `1.000 €`. Puedes usar el módulo `random` para generar
el saldo. En cada vuelta, pide una operación: `ingresar`, `retirar`, `consultar`,
`cerrar cuenta`, `abrir cuenta` o `salir`.

Aplica estas reglas:

- **Ingresar**: solicita una cantidad positiva y súmala al saldo. Solo se
  puede operar con una cuenta activa.
- **Retirar**: solicita una cantidad positiva. Solo permite la retirada si la
  cuenta está activa y hay saldo suficiente.
- **Consultar**: muestra el titular, el saldo y si la cuenta está activa o
  cerrada.
- **Cerrar cuenta**: solo se puede cerrar si está activa y el saldo es `0`.
- **Abrir cuenta**: solo se puede abrir si está cerrada. Al abrirla, el saldo
  empieza en `0 €`.
- **Salir**: termina el menú y muestra el estado final de la cuenta.

Si una operación no se puede realizar, explica el motivo y vuelve a mostrar
el menú. Normaliza el texto de la operación para aceptar mayúsculas y espacios
sobrantes. Supón que las cantidades introducidas son números positivos; no
hace falta gestionar errores de conversión. Prueba una secuencia que incluya
un ingreso, una retirada superior al saldo disponible, una consulta, un intento
de cierre con saldo, una retirada que deje el saldo en cero, el cierre, una
nueva apertura y la salida.

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