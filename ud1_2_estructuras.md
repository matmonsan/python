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
   - [Actividades extra](#actividades-extra)
4. [Estructuras de salto](#4-estructuras-de-salto)
5. [Documentación de programas](#5-documentación-de-programas)
   - [Actividades 5](#actividades-5)
6. [Control de excepciones](#6-control-de-excepciones)
   - [Actividades 6](#actividades-6)
7. [Depuración y uso del depurador](#7-depuración)
   - [Actividades 7](#actividad-7-el-total-que-no-suma)
8. [Programación orientada a objetos](#8-programación-orientada-a-objetos)
   - [Actividades 8](#actividades-8)
9. [Proyecto práctico integrador: gestor de tareas en consola](#9-proyecto-práctico-integrador-gestor-de-tareas-en-consola)

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

### Actividades extra

#### Actividad 6: promedio de notas por alumno

Dispones de una lista bidimensional con el nombre de cada alumno y sus tres
notas. Cada fila contiene primero el nombre y, a continuación, las notas; por
ejemplo:

```python
alumnos = [
	["Ana", 8, 7.5, 9],
	["Luis", 6, 8, 7],
	["Marta", 9.5, 10, 8.5],
]
```

Recorre la lista y calcula el promedio de las tres notas de cada alumno.
Muestra el nombre y el promedio de cada uno en una tabla clara, con encabezados
para las columnas. Presenta los promedios con dos decimales.

Ejemplo de datos y salida:

```text
Datos:
Ana: 8, 7.5, 9
Luis: 6, 8, 7
Marta: 9.5, 10, 8.5

Alumno  | Promedio
--------|---------
Ana     | 8.17
Luis    | 7.00
Marta   | 9.33
```

#### Actividad 7: contar las letras de una palabra

Pide al usuario una palabra y cuenta cuántas veces aparece cada letra. El
conteo no debe distinguir entre mayúsculas y minúsculas: por ejemplo, en
`"Casa"` la `a` aparece dos veces. Usa un diccionario para guardar cada letra
y su cantidad.

Muestra los resultados en una tabla con una columna para la letra y otra para
su frecuencia. Cada letra debe aparecer una sola vez en la tabla.

Ejemplo de ejecución:

```text
Dígame una palabra: Casa

Letra | Frecuencia
------+-----------
c     | 1
a     | 2
s     | 1
```

#### Actividad 8: sucesión de valores enteros

Pide un valor inicial, un valor final mayor que el inicial y cuántos valores
intermedios se desean. Genera y muestra la lista de valores enteros que empieza
en el valor inicial y termina en el final, repartiendo los valores de forma
equidistante. Elige valores que permitan obtener saltos enteros. No cuentes
los extremos como valores intermedios. Por ejemplo, con los valores `10`,
`25` y `2`, la lista debe ser `[10, 15, 20, 25]`.

Ejemplo de ejecución:

```text
Dígame el valor inicial: 10
Dígame el valor final: 25
Dígame el número de valores intermedios: 2
La lista correspondiente es [10, 15, 20, 25]
```

#### Actividad 9: detectar números pares

Pregunta cuántos números se van a introducir y pide esa cantidad de números.
Al terminar, indica si se ha escrito al menos un número par. Prueba tanto una
serie que incluya un número par como otra en la que todos sean impares.

Ejemplo de ejecución:

```text
Dígame cuántos números va a escribir: 5
Dígame el número 1: 17
Dígame el número 2: 5
Dígame el número 3: 7
Dígame el número 4: 22
Dígame el número 5: 19
Ha escrito algún número par
```

#### Actividad 10: crear una lista de letras

Pide una palabra o frase y crea una lista con sus caracteres, manteniendo el
orden original e incluyendo los espacios. Muestra la lista resultante.

Ejemplo de ejecución:

```text
Dígame algo: Una prueba
La lista creada es ['U', 'n', 'a', ' ', 'p', 'r', 'u', 'e', 'b', 'a']
```

#### Actividad 11: sustituir las vocales de una frase

Pide una frase y una vocal. Crea una nueva frase sustituyendo todas las
vocales de la frase original por la vocal indicada. Conserva los espacios y
las consonantes, y muestra el resultado. Por ejemplo, con la frase
`"tengo una hormiguita"` y la vocal `a`, el resultado empieza por
`"tanga ana..."`.

Ejemplo de ejecución:

```text
Dígame algo: tengo una hormiguita en la panchita
Dígame una vocal: a
La frase es ahora: tanga ana harmagaata an la panchata
```

#### Actividad 12: calcular la letra del DNI

Pide el número de un DNI sin letra y calcula la letra correspondiente. Para
obtenerla, divide el número entre `23` y usa el resto como índice en esta
cadena: `TRWAGMYFPDXBNJZSQVHLCKE`. Muestra el número seguido de su letra.

Ejemplo de ejecución:

```text
Dígame su DNI (sin letra): 31415926
Su DNI (con letra) es: 31415926L
```

#### Actividad 13: convertir un número a números romanos

Pide un número entero positivo inferior a `5000` y muestra su representación
en números romanos. Usa los valores `I=1`, `V=5`, `X=10`, `L=50`, `C=100`,
`D=500` y `M=1000`. Para simplificar, se permite la notación romana antigua:
pueden aparecer hasta cuatro símbolos iguales seguidos. Por ejemplo, `3799`
se escribe `MMMDCCLXXXXVIIII`.

Ejemplo de ejecución:

```text
Dígame un número: 3799
En números romanos, 3799 se escribe MMMDCCLXXXXVIIII
```

#### Actividad 14: contar años bisiestos entre dos años

Pide dos años y recorre todos los años del intervalo, incluyendo ambos
extremos. Cuenta cuántos son bisiestos y suma el número de días de cada año
del intervalo. Un año es bisiesto si es divisible por `400`, o si es divisible
por `4` pero no por `100`. Muestra la cantidad de años bisiestos y el total
de días. Si el primer año es posterior al segundo, intercambia los valores
para recorrer el intervalo en orden.

Ejemplo de ejecución:

```text
Dígame un año: 1999
Dígame otro año: 2001
Entre 1999 y 2001 (ambos incluidos) hubo 1 año bisiesto
y en total 1096 días.
```

#### Actividad 15: jugar a adivinar una clave

Crea una versión sencilla de Master Mind. Pide una longitud entre `2` y `9`
y genera una clave secreta de esa longitud formada por cifras distintas. A
continuación, pide intentos hasta que se adivine la clave. Después de cada
intento, indica cuántas cifras coinciden con la clave tanto en valor como en
posición. Cuando se acierten todas, muestra un mensaje de felicitación y
termina el juego. Puedes utilizar el módulo `random` para generar la clave.

Ejemplo de ejecución (la clave generada en esta partida es `2431`):

```text
Dígame la longitud de la cadena: 4
Intente adivinar la cadena: 1234
Con 1234 ha adivinado 1 valores. Intente adivinar la cadena: 2435
Con 2435 ha adivinado 3 valores. Intente adivinar la cadena: 2431
Con 2431 ha adivinado 4 valores. Felicidades
```

---

## 4. Estructuras de salto

[⬆ Volver al índice](#índice)

En esta sección veremos dos instrucciones que cambian el recorrido de un bucle:
`break` y `continue`. Ambas afectan al bucle más cercano en el que aparecen,
pero de forma distinta.

### 4.1 `break`

`break` termina inmediatamente el bucle más cercano. El programa continúa con
la primera instrucción que haya después de ese bucle. No termina el programa
completo ni, si hay bucles anidados, los bucles exteriores.

```python
for numero in range(100):
	if numero == 10:
		break
	print(numero)
```

En este ejemplo se muestran los números del `0` al `9`. Cuando `numero` vale
`10`, se ejecuta `break`, por lo que no se muestra ese número y el bucle acaba.

### 4.2 `continue`

`continue` no termina el bucle: interrumpe solo la iteración actual. Se omiten
las instrucciones que quedan en esa vuelta y el bucle pasa a la siguiente
iteración.

```python
for numero in range(1, 11):
	if numero % 2 == 0:
		continue
	print(numero)  # solo impares
```

El ejemplo muestra los números impares del `1` al `9`: para cada número par,
`continue` salta `print(numero)`, pero el bucle sigue con el siguiente número.

### Criterio de diseño

Usa estas instrucciones cuando hagan más claro el recorrido del bucle. La
condición que provoca el salto debe ser fácil de identificar: `break` sirve
para salir del bucle y `continue` para descartar solo la vuelta actual. Si
aparecen muchos saltos, puede resultar más difícil entender qué instrucciones
se ejecutan y en qué orden.

---

## 5. Documentación de programas

[⬆ Volver al índice](#índice)

Documentar un programa consiste en dejar por escrito la información que otras
personas —incluida quien lo creó meses después— necesitan para utilizarlo,
entenderlo y mantenerlo. La documentación complementa al código: explica su
propósito y sus contratos, mientras que el código muestra exactamente cómo se
ejecuta.

No toda la documentación debe estar en el mismo lugar. El `README.md` orienta
sobre el proyecto completo; los docstrings describen módulos, clases y
funciones desde el propio código; las anotaciones de tipo muestran qué datos
se esperan; y los comentarios aclaran decisiones que no resultan evidentes al
leer las instrucciones. Elegir el lugar adecuado evita repetir información y
facilita encontrarla.

Una regla útil es documentar lo que una persona necesita saber y no puede
deducir fácilmente del código. Hay que explicar el propósito, los pasos de
uso, las restricciones, los resultados y los errores relevantes. No conviene
describir línea por línea una operación sencilla: si el código cambia, ese
comentario puede quedar desactualizado y confundir.

### 5.1 README

El archivo `README.md` es la puerta de entrada al proyecto. Debe permitir que
alguien que no conoce el código sepa qué resuelve y pueda ponerlo en marcha.
Según el tamaño del proyecto, puede incluir:

- **Propósito:** qué problema resuelve y para quién.
- **Requisitos:** versión de Python y dependencias necesarias.
- **Instalación:** cómo preparar el entorno y las dependencias.
- **Ejecución:** comando para iniciar el programa.
- **Uso:** ejemplo de entrada y salida o una descripción de las opciones.
- **Pruebas:** cómo ejecutarlas, si el proyecto las incluye.
- **Configuración:** opciones necesarias, sin publicar contraseñas ni claves.
- **Estructura y mantenimiento:** dónde están las partes principales y cómo
  contribuir, cuando sea pertinente.

Por ejemplo, no basta con indicar «ejecuta `main.py`» si antes hay que crear
un entorno virtual o instalar paquetes. Es preferible escribir los pasos en
el orden en que se deben realizar y comprobarlos en una instalación limpia.

Ejemplo de estructura habitual de un proyecto:

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

### 5.2 Docstrings de funciones

Un docstring es una cadena de texto situada al principio de un módulo, una
clase o una función. Describe su propósito y forma parte de la información que
las herramientas de Python pueden mostrar, por ejemplo mediante `help()`.
Para una función, conviene explicar los parámetros, el valor que devuelve y
las excepciones que puede producir en condiciones relevantes.

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

El docstring describe el contrato de la función: qué espera, qué garantiza y
qué error comunica cuando no se cumple una condición. Debe coincidir con el
código; por ejemplo, no se debe prometer aceptar valores negativos si la
función los rechaza.

### 5.3 Docstrings de clases

El docstring de una clase debe describir qué representa y, cuando no sea
obvio, cómo se crea o qué invariantes mantiene. Los métodos públicos también
pueden documentarse si tienen reglas de uso propias.

```python
class Cuenta:
	"""Representa una cuenta con saldo y operaciones básicas."""

	def __init__(self, titular, saldo=0):
		self.titular = titular
		self.saldo = saldo
```

### 5.4 Documentar decisiones

Los comentarios son adecuados para explicar el motivo de una decisión, una
restricción externa o un comportamiento que no se deduce del código. Si el
motivo es relevante para el mantenimiento, debe actualizarse junto con el
código al cambiar esa decisión.

```python
# Se conserva el orden de llegada porque el informe se revisa cronológicamente.
eventos = list(eventos_recibidos)
```

### 5.5 Calidad de la documentación

Una documentación útil permite completar una tarea concreta —por ejemplo,
instalar el programa o llamar a una función— sin tener que adivinar pasos.
Para conseguirlo, debe ser:

- Exacta y actualizada.
- Clara y organizada según quién la consulta: usuario, desarrollador o
  persona que mantiene el proyecto.
- Concisa cuando el comportamiento es obvio y detallada cuando hay reglas,
  límites, efectos secundarios o errores importantes.
- Accionable: permite instalar y ejecutar.
- Verificable: los ejemplos funcionan.
- Coherente con los nombres del código.

Antes de publicar un cambio, revisa si también han cambiado las instrucciones
de instalación, los ejemplos, los parámetros o los resultados descritos.
Eliminar o corregir información obsoleta es tan importante como añadir
información nueva.

### 5.6 Generación automática

Las herramientas de generación reúnen docstrings y páginas escritas en
Markdown para producir documentación fácil de consultar. Cada una se adapta
a necesidades distintas: `pydoc` permite empezar rápidamente, Sphinx ofrece
más opciones para proyectos Python y MkDocs facilita crear un sitio a partir
de páginas Markdown.

##### 1. `pydoc`

Es la opción más sencilla y viene incluida con Python. Puede mostrar la
documentación de módulos en el navegador o generar un archivo HTML. Para
probarlo, desde la terminal ejecuta:

```console
python -m pydoc -b
```

Se iniciará un servidor local y se abrirá el navegador con la documentación
de los módulos disponibles. Para generar un archivo HTML con la información
de un módulo propio, sitúate en la carpeta desde la que se puede importar y
ejecuta:

```console
python -m pydoc -w mi_programa
```

El comando crea `mi_programa.html` a partir de los docstrings del módulo.

La generación automática no sustituye la escritura cuidadosa: publica lo que
se ha expresado en los docstrings y las páginas, pero no comprueba por sí
misma que sus explicaciones sigan siendo ciertas. Revisa los ejemplos y
actualiza la documentación cuando cambie el programa.

### Actividades 5

#### Actividad 1: organiza tu día libre

Desarrolla un programa que ayude al usuario a organizar un día libre
según su presupuesto, el tiempo disponible y sus preferencias.

El programa deberá mostrar las posibles actividades, como ir al
cine, salir a comer, visitar un museo, hacer deporte o quedarse en casa. El
usuario podrá elegir varias actividades y el programa comprobará si puede
realizarlas teniendo en cuenta el dinero y el tiempo disponibles. Para ello el usuario debe indicar de cuánto tiempo dispone y cuál es su presupuesto.

Cada actividad tendrá un precio y una duración. Si el usuario no dispone de
suficiente dinero o tiempo, el programa deberá avisarle y ofrecerle la
posibilidad de elegir otra actividad.

Al finalizar, se mostrará un resumen del día con las actividades
seleccionadas, el dinero gastado, el tiempo utilizado y el presupuesto
restante.

El programa deberá cumplir los siguientes requisitos:

- Utilizar condicionales para comprobar si se puede   realizar cada actividad.
- Utilizar bucles para permitir que el usuario seleccione varias actividades.
- Crear funciones para mostrar el menú, comprobar el presupuesto, calcular
  el tiempo disponible y mostrar el resumen final.
- Validar los datos introducidos para evitar errores.
- Documentar las funciones mediante docstrings y añadir comentarios cuando
  sean necesarios.

El programa deberá ejecutarse por consola, ser fácil de utilizar y estar
organizado en funciones independientes.

---

## 6. Control de excepciones

[⬆ Volver al índice](#índice)

Una excepción es un evento que interrumpe el flujo normal del programa porque se ha producido una situación excepcional: entrada inválida, archivo inexistente, división por cero o fallo de red. Python representa cada una de estas situaciones como un objeto de excepción que "sube" por la pila de llamadas hasta que alguien lo captura. Si nadie lo hace, el programa se detiene y el intérprete muestra el *traceback*.

Gestionar excepciones permite que un programa falle de forma controlada: informar al usuario, reintentar, liberar recursos o registrar el problema en lugar de terminar abruptamente.

### 6.1 Excepción básica

La conversión con `int()` solo funciona si el texto representa un número entero válido. Como `"no es un número"` no cumple ese formato, Python no puede realizar la conversión y genera una excepción `ValueError`. Si no se gestiona, el programa se detiene y muestra el traceback.

```python
numero = int("no es un número")  # ValueError
```

Salida:

```text
Traceback (most recent call last):
  File "ejemplo.py", line 1, in <module>
    numero = int("no es un número")
ValueError: invalid literal for int() with base 10: 'no es un número'
```

El traceback se lee de arriba abajo: primero la ruta de llamadas (de la más antigua a la más reciente) y, en la última línea, el **tipo de excepción** y su **mensaje**. La línea señalada suele ser donde el error se manifiesta; conviene leer también las llamadas anteriores para entender cómo se llegó hasta ella.

### 6.2 `try` y `except`

El bloque `try` contiene las instrucciones que podrían fallar. Si la conversión de la entrada no es posible, Python interrumpe ese bloque (las líneas restantes de `try` no se ejecutan) y ejecuta el `except` asociado a `ValueError`, en lugar de finalizar el programa. Si la conversión tiene éxito, el bloque `except` se omite.

```python
try:
    edad = int(input("Edad: "))
except ValueError:
    print("Debes introducir un entero")
```

Se debe capturar la excepción concreta que se sabe manejar. Capturar `Exception` sin una razón clara puede ocultar errores de programación, porque también atraparía fallos que este código no sabe resolver. Evita además el `except:` sin tipo, que captura incluso `KeyboardInterrupt` y `SystemExit` y hace imposible interrumpir el programa con `Ctrl+C`.

Un patrón habitual es repetir la petición hasta que la entrada sea válida:

```python
while True:
    try:
        edad = int(input("Edad: "))
        break
    except ValueError:
        print("Debes introducir un entero")
```

### 6.3 `else`

El bloque `else` se ejecuta solo si el bloque `try` termina sin excepciones. En este ejemplo, el cálculo se realiza únicamente cuando la entrada se ha convertido correctamente; si no, se muestra el mensaje del bloque `except`.

```python
try:
    numero = int(input("Número: "))
except ValueError:
    print("Entrada inválida")
else:
    print(f"El doble es {numero * 2}")
```

Poner el código dependiente en `else` y no dentro de `try` tiene una ventaja: las excepciones que se produzcan en `else` **no** son capturadas por los `except` anteriores, de modo que `try` queda limitado a las instrucciones que realmente se quieren vigilar.

### 6.4 `finally`

`finally` se ejecuta tanto si el bloque `try` termina correctamente como si se produce una excepción (e incluso si dentro de `try` hay un `return`, `break` o `continue`). Por eso se utiliza para liberar recursos, como cerrar un archivo que se haya abierto. La comprobación de `archivo is not None` evita intentar cerrar una variable que nunca llegó a recibir un archivo, por ejemplo si `open()` falló.

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

En este caso, si el archivo no existe, se captura `FileNotFoundError` y la variable `contenido` queda sin definir, de modo que usarla después provocaría un `NameError`. Conviene asignarle siempre un valor en el camino de error.

Cuando se usa `with`, Python cierra el archivo automáticamente al salir del bloque, incluso si ocurre un error durante la lectura; por eso suele ser la opción preferible a `finally` para recursos que lo admiten.

```python
try:
    with open("datos.txt", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    contenido = ""
```

El valor vacío asignado en `except` permite que el programa continúe, pero se debe elegir una respuesta adecuada para cada aplicación: también podría ser mejor informar del error o volver a solicitar el archivo.

> **Cuidado:** un `return` dentro de `finally` descarta cualquier excepción pendiente y la silencia. Evítalo.

### 6.5 Varias excepciones

Una operación puede fallar por motivos distintos. Aquí se gestionan por separado una entrada que no puede convertirse a entero (`ValueError`) y un divisor igual a cero (`ZeroDivisionError`), de modo que cada caso recibe un mensaje específico. Si ambas conversiones y la división terminan correctamente, se ejecuta `else` y se muestra el resultado.

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

Si varios errores distintos se resuelven de la misma manera, se pueden agrupar en una **tupla**:

```python
try:
    resultado = int(texto) / int(divisor)
except (ValueError, ZeroDivisionError):
    print("Datos no válidos")
```

Python revisa los `except` **de arriba abajo** y ejecuta el primero que coincide. Por eso las excepciones más específicas deben ir antes que las más generales: si `except OSError` aparece antes que `except FileNotFoundError`, este último nunca se ejecutará, porque `FileNotFoundError` es una subclase de `OSError`.

### 6.6 Capturar como variable

Al escribir `as error`, el programa guarda el objeto de excepción en una variable. Su mensaje puede aportar información adicional para diagnosticar el problema o elaborar una respuesta más precisa. En una aplicación dirigida a usuarios, conviene no mostrar detalles internos si no son apropiados.

```python
try:
    numero = int("abc")
except ValueError as error:
    print(f"Detalle: {error}")
```

La variable `error` solo existe dentro del bloque `except`; Python la elimina al salir de él. Si necesitas conservar la excepción, guárdala en otra variable.

### 6.7 Lanzar excepciones propias

`raise` permite señalar que una función ha recibido un valor que incumple su contrato. Esta función solo acepta porcentajes entre 0 y 100, incluidos ambos extremos; ante cualquier otro valor, genera `ValueError`. Quien llame a la función puede capturar esa excepción y decidir cómo informar o recuperarse.

```python
def establecer_porcentaje(porcentaje):
    if not 0 <= porcentaje <= 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return porcentaje
```

Es habitual elegir el tipo de excepción según la causa: `ValueError` si el tipo es correcto pero el valor no, y `TypeError` si el tipo es incorrecto.

Dentro de un `except`, un `raise` sin argumentos **vuelve a lanzar** la excepción actual. Es útil cuando se quiere hacer algo (por ejemplo, registrar el error) pero sin resolverlo:

```python
try:
    procesar_pedido(pedido)
except ValueError:
    print("Pedido inválido, se registra el error")
    raise  # la excepción sigue subiendo al código que llamó
```

### 6.8 Encadenamiento de excepciones

Al convertir un valor de texto, `int()` puede generar `ValueError`. El ejemplo captura ese error y genera otro con un mensaje más adecuado para la función. La parte `from error` conserva explícitamente la excepción original como causa, por lo que el traceback permite consultar tanto el nuevo contexto como el fallo inicial.

```python
def leer_entero_desde_texto(texto):
    try:
        return int(texto)
    except ValueError as error:
        raise ValueError("El texto no contiene un entero") from error
```

Si se lanza una excepción dentro de un `except` **sin** usar `from`, Python también las enlaza de forma implícita y muestra el mensaje *"During handling of the above exception, another exception occurred"*. Con `from None` se suprime esa cadena cuando el error original no aporta información útil al usuario:

```python
raise ValueError("El texto no contiene un entero") from None
```

### 6.10 Jerarquía de excepciones integradas

Las excepciones forman una jerarquía de clases. Capturar una clase captura también todas sus subclases. Un fragmento de la jerarquía de uso más común:

```text
BaseException
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── OSError
      │    ├── FileNotFoundError
      │    └── PermissionError
      ├── ValueError
      ├── TypeError
      ├── AttributeError
      └── NameError
```

Excepciones frecuentes y cuándo aparecen:

| Excepción | Causa típica | Ejemplo |
|---|---|---|
| `ValueError` | Tipo correcto, valor inadecuado | `int("abc")` |
| `TypeError` | Operación con un tipo incorrecto | `"a" + 1` |
| `ZeroDivisionError` | División o módulo entre cero | `10 / 0` |
| `IndexError` | Índice fuera de rango | `[1, 2][5]` |
| `KeyError` | Clave inexistente en un diccionario | `{"a": 1}["b"]` |
| `AttributeError` | El objeto no tiene ese atributo | `None.append(1)` |
| `FileNotFoundError` | El archivo no existe | `open("no_existe.txt")` |
| `PermissionError` | Sin permisos sobre el archivo | Escribir en una ruta protegida |

`Exception` es la raíz de las excepciones de programa habituales; `KeyboardInterrupt` y `SystemExit` heredan directamente de `BaseException` precisamente para que `except Exception` no las atrape.

### Actividades 6

### Actividad 6: la caja del supermercado

Programa una caja de supermercado con un carrito. El programa **no debe terminar por errores del usuario**: cada fallo se gestiona con un mensaje claro.

```python
productos = ["pan", "leche", "huevos"]
precios = [0.85, 1.20, 2.50]   # el precio de productos[0] es precios[0], etc.
carrito = []                   # aquí se guardan los precios de lo que se compra
```

El usuario elige los productos por su **número** (0 = pan, 1 = leche, 2 = huevos) y quita del carrito por su **posición** (la primera es la 0).

#### Parte A: funciones (sin `input()` ni `print()`)

1. `convertir_numero(texto)`: devuelve el entero. Si `int()` falla, captura el `ValueError` y lanza otro con un mensaje claro usando `raise ... from error`. Si el número es negativo, lanza `ValueError` (en las listas, `-1` sería válido y no queremos que lo sea).
2. `anadir(carrito, numero)`: añade `precios[numero]` al carrito. Deja que salte el `IndexError` si el producto no existe.
3. `quitar(carrito, posicion)`: elimina esa posición del carrito con `carrito.pop(posicion)`. Deja que salte el `IndexError` si no existe.
4. `calcular_total(carrito)`: devuelve la suma de los precios del carrito.
5. `repartir(total, personas)`: devuelve `total / personas`. No compruebes el cero: deja que salte `ZeroDivisionError`.

#### Parte B: programa principal

Un menú en bucle: **1. Añadir, 2. Quitar, 3. Repartir la cuenta, 4. Salir**. Cada operación va en su `try` y debe cumplir:

- `IndexError` y `ValueError` se gestionan en `except` **separados** (en `ValueError`, muestra el mensaje con `as error`).
- En el reparto, agrupa `(ValueError, ZeroDivisionError)` en un solo `except`.
- `else`: muestra `"Operación realizada"`.
- `finally`: muestra siempre el carrito y el total actual.
- **Relanzar:** cuenta los `ValueError` seguidos (una operación correcta reinicia el contador). Al tercero, usa `raise` dentro del `except`. Un `try/except ValueError` exterior que rodea el bucle muestra `"Demasiados errores. Se cierra la caja"` y termina. En ese mismo `try` exterior captura `KeyboardInterrupt` con un mensaje de despedida.

#### Casos de prueba

| Acción | Resultado esperado |
|---|---|
| Añadir producto `0` | Carrito `[0.85]` |
| Añadir producto `7` | "Ese producto no existe" |
| Añadir producto `dos` o `-1` | Error de número no válido |
| Quitar posición `5` con 1 producto | "Esa posición no existe" |
| Quitar posición `0` con el carrito vacío | "Esa posición no existe" |
| Repartir entre `0` o `hola` | Mismo mensaje agrupado |
| Tres `ValueError` seguidos | La caja se cierra |

---

## 7. Depuración

[⬆ Volver al índice](#índice)

Depurar es **encontrar y corregir errores** en un programa. No consiste en mirar el código esperando ver el fallo, sino en observar qué hace realmente el programa y compararlo con lo que debería hacer.

### 7.1 Tipos de error

| Tipo | Qué ocurre | Ejemplo |
|---|---|---|
| **Sintaxis** | El programa ni siquiera arranca. Python indica `SyntaxError`. | Olvidar los dos puntos en un `if` |
| **Ejecución** | El programa se detiene con una excepción y un traceback. | `int("hola")` |
| **Lógico** | No hay ningún mensaje, pero el resultado es incorrecto. | Sumar `total = precio` en lugar de acumular |

Los errores lógicos son los más difíciles de encontrar, porque Python no avisa. Para ellos es especialmente útil el depurador.

### 7.2 Método para depurar

1. **Reproduce el error** con unos datos concretos.
2. **Lee el mensaje** completo, si lo hay. Indica el tipo de error y la línea.
3. **Compara** el resultado esperado con el obtenido.
4. **Observa los valores** de las variables mientras se ejecuta el programa.
5. **Corrige una sola cosa** y vuelve a probar.

> **Importante:** no cambies varias cosas a la vez. Si lo haces, no sabrás cuál ha arreglado (o estropeado) el programa.

### 7.3 Observar con `print()`

La forma más sencilla de ver qué ocurre es imprimir valores:

```python
precio = 10
unidades = 3
subtotal = precio * unidades
print("DEBUG subtotal:", subtotal)
```

Es útil, pero tiene inconvenientes: hay que escribir y borrar líneas, y solo ves lo que has decidido imprimir. **Recuerda eliminar los `print` de depuración al terminar.**

### 7.4 El depurador de Visual Studio Code

El depurador permite **ejecutar el programa línea a línea** y ver el valor de todas las variables en cada momento, sin modificar el código.

**Requisito:** tener instalada la extensión **Python** de VS Code.

#### Conceptos básicos

- **Breakpoint (punto de interrupción):** marca una línea donde el programa se detendrá.
- **Paso a paso:** ejecutar el programa avanzando de una línea en una línea.
- **Variables:** panel donde se ve el valor actual de cada variable.

#### Cómo depurar, paso a paso

1. Abre el archivo `.py`.
2. **Coloca un breakpoint:** haz clic a la izquierda del número de la línea. Aparece un punto rojo.
3. **Inicia la depuración:** pulsa `F5` (o *Run and Debug* en el menú lateral). Si te lo pide, elige **Python Debugger** y **Python File**.
4. El programa se detiene en el breakpoint. La línea queda marcada en **amarillo**.

> **Ojo:** la línea amarilla es la que **todavía no se ha ejecutado**. Los valores que ves son los de *antes* de ejecutarla.

5. Avanza con `F10` y observa cómo cambian las variables.
6. Para terminar, pulsa `F5` (continuar hasta el final) o `Shift + F5` (detener).

#### Paneles que debes mirar

| Panel | Para qué sirve |
|---|---|
| **Variables** | Muestra las variables y su valor actual. Los valores que cambian se resaltan. |
| **Watch** | Permite vigilar una variable o una expresión. Pulsa `+` y escribe, por ejemplo, `total`. |
| **Call Stack** | Muestra en qué función estás y desde dónde se la llamó. |
| **Breakpoints** | Lista de todos los puntos de interrupción. |

#### Botones y atajos

| Acción | Atajo | Qué hace |
|---|---|---|
| **Continue** | `F5` | Sigue hasta el siguiente breakpoint o hasta el final. |
| **Step Over** | `F10` | Ejecuta la línea actual **sin entrar** en las funciones que llame. |
| **Step Into** | `F11` | Si la línea llama a una función, **entra** en ella. |
| **Step Out** | `Shift + F11` | Termina la función actual y vuelve a quien la llamó. |
| **Stop** | `Shift + F5` | Detiene la depuración. |

#### Ejemplo guiado

```python
def aplicar_descuento(precio, porcentaje):
    descuento = precio * porcentaje / 100
    total = precio - descuento
    return total


precios = [10.0, 25.0, 40.0]
totales = []

for precio in precios:
    totales.append(aplicar_descuento(precio, 10))

print(totales)
```

Resultado esperado: `[9.0, 22.5, 36.0]`.

1. Pon un breakpoint en la línea `totales.append(...)` y pulsa `F5`.
2. En **Variables** verás `precio = 10.0` y `totales = []`.
3. Pulsa `F11` para **entrar** en la función. En **Call Stack** aparece `aplicar_descuento`.
4. Pulsa `F10` dos veces y observa cómo se calculan `descuento` (`1.0`) y `total` (`9.0`).
5. Pulsa `Shift + F11` para salir de la función y comprueba cómo se añade `9.0` a `totales`.
6. Pulsa `F5` para pasar a la siguiente vuelta del bucle y repite la observación.

### 7.5 Qué observar al depurar

- ¿Cada variable tiene el **valor** que esperabas en cada vuelta?
- ¿Tiene el **tipo** adecuado? Recuerda que `input()` siempre devuelve texto (`str`).
- ¿El bucle da el **número de vueltas** correcto?
- ¿Qué pasa con los **casos límite**: cero, lista vacía, un solo elemento?

### Actividad 7: el total que no suma

Este programa debería mostrar `60`, pero no lo hace:

```python
precios = [10, 20, 30]
total = 0

for precio in precios:
    total = precio

print(total)
```

**Sigue estos pasos:**

1. **Reproduce el error.** Copia el código en un archivo, ejecútalo y anota lo que muestra. ¿Coincide con lo esperado (`60`)?
2. **Coloca un breakpoint** en la línea `total = precio`.
3. **Inicia la depuración** con `F5`.
4. **Vigila `total`.** En el panel *Watch*, añade `total`.
5. **Rellena la tabla.** Cada vez que el programa se detenga, anota los valores *antes* de ejecutar la línea. Después pulsa `F10` y anota el valor de `total` *después*. Usa `F5` para pasar a la siguiente vuelta.

| Vuelta | `precio` | `total` antes | `total` después |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

6. **Responde:** ¿qué le ocurre al valor anterior de `total` en cada vuelta? ¿Se suma o se sustituye?
7. **Corrige** la instrucción para que acumule la suma. *Pista: el nuevo valor de `total` debe calcularse a partir del valor anterior de `total`.*
8. **Comprueba** con el depurador que ahora `total` vale `10`, `30` y `60` en cada vuelta.
9. **Prueba otros casos** cambiando la lista:

| Lista | Resultado esperado |
|---|---|
| `[]` | `0` |
| `[5]` | `5` |
| `[1, 2, 3, 4]` | `10` |

**Cuando termines**, escribe en un comentario al final del programa una frase que explique cuál era el error y cómo lo encontraste.

---

## 8. Programación orientada a objetos

[⬆ Volver al índice](#índice)

La programación orientada a objetos (POO) organiza un programa mediante objetos que combinan estado (datos) y comportamiento (operaciones). Una clase define cómo serán sus objetos; cada objeto concreto creado a partir de ella se denomina instancia.

### 8.1 Clases, instancias, atributos y métodos

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

### 8.2 Encapsulación y propiedades

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

### 8.3 Atributos de clase y de instancia

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

### 8.4 Herencia y polimorfismo

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

### 8.5 Composición

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

### 8.6 Métodos especiales y representaciones

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

### 8.7 Clases de datos

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

### Actividades 8

#### Actividad 1: clase Rectangulo

Implementa una clase `Rectangulo` que reciba ancho y alto, calcule el área y el perímetro, y rechace dimensiones no positivas. Crea dos instancias con dimensiones diferentes y muestra ambos resultados. No uses listas ni tuplas.

---

## 9. Proyecto práctico integrador: gestor de tareas en consola

[⬆ Volver al índice](#índice)

El siguiente proyecto combina variables, tipos, funciones, listas, diccionarios, selección, repetición, excepciones, documentación y depuración. Permite añadir, listar, completar y eliminar tareas.

### 9.1 Diseño

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

### 9.2 Implementación completa

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

### 9.3 Mejoras propuestas

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
