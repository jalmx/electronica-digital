![banner](../assets/banner_class_85.png)

# Ejercicios de Aplicación

Para cada ejercicio:

1. La tabla de verdad generada de cada ejercicio.
2. Ecuacion booleana o Mapa de Karnaugh (cualquiera de los 2 o los 2)
3. El diagrama del circuito digital. (Usando logicsim)
4. De 2 a 3 pantallazos de la simulacion (si lo haces a mano no aplica)

> *Nota: En caso de no contar con Logisim, puedes buscar alguna aplicación que te pueda ayudar para resolverlo, pero la tienes que investigar y aprender a usarla.*

## Ejercicio 1 Sistema automático de llenado de un tanque de agua 💧

### 1. Descripción del problema

Se requiere diseñar un sistema digital para controlar el llenado de un tanque de agua. El sistema utiliza sensores para detectar el nivel del agua y verificar si existe suministro disponible.

El objetivo es activar una bomba de agua únicamente cuando sea necesario llenar el tanque y se cumplan las condiciones de funcionamiento.

### 2. Variables de entrada y salida

| Variable | Descripción          | Estado 0                                 | Estado 1                        |
|----------|----------------------|------------------------------------------|---------------------------------|
| A        | Sensor de nivel bajo | El agua está por encima del nivel mínimo | El agua alcanzó el nivel mínimo |
| B        | Sensor de nivel alto | El tanque no está lleno                  | El tanque está lleno            |
| C        | Sensor de suministro | No hay suministro de agua                | Hay suministro de agua          |
| M        | Bomba de agua        | Bomba apagada                            | Bomba encendida                 |

### 3. Reglas de funcionamiento

1. La bomba debe encenderse cuando el nivel del agua sea bajo y exista suministro de agua.
2. Si el tanque está lleno, la bomba debe permanecer apagada.
3. Si no hay suministro de agua, la bomba debe permanecer apagada.
4. Si el nivel del agua es adecuado y no se requiere llenado, la bomba debe permanecer apagada.

Para este ejercicio, se considera que el sensor A se activa cuando el agua alcanza el nivel mínimo de llenado, mientras que B indica que se alcanzó el nivel máximo. La combinación A = 1 y B = 1 representa una condición anómala que debe mantener la bomba apagada.

<!-- ### 4. Tabla de verdad

| A | B | C | M | Descripción                       |
|:-:|:-:|:-:|:-:|-----------------------------------|
| 0 | 0 | 0 | 0 | Nivel adecuado, sin suministro    |
| 0 | 0 | 1 | 0 | Nivel adecuado, con suministro    |
| 0 | 1 | 0 | 0 | Tanque lleno, sin suministro      |
| 0 | 1 | 1 | 0 | Tanque lleno, con suministro      |
| 1 | 0 | 0 | 0 | Nivel bajo, sin suministro        |
| 1 | 0 | 1 | 1 | Nivel bajo, con suministro        |
| 1 | 1 | 0 | 0 | Condición anómala, sin suministro |
| 1 | 1 | 1 | 0 | Condición anómala, con suministro | -->


## Ejercicio 2 Puerta automática para un acceso peatonal 🚪

### 1. Descripción del problema

Se desea diseñar un sistema digital para controlar la apertura de una puerta automática en la entrada de un edificio.
El sistema dispone de un sensor de presencia, un lector de autorización y un sensor de seguridad que detecta si existe algún obstáculo en el recorrido de la puerta.
La puerta solamente debe abrirse cuando se detecte una persona autorizada y no exista un obstáculo.

### 2. Variables de entrada y salida

| Variable | Descripción          | Estado 0               | Estado 1            |
|----------|----------------------|------------------------|---------------------|
| P        | Sensor de presencia  | No detecta una persona | Detecta una persona |
| A        | Lector de acceso     | Acceso no autorizado   | Acceso autorizado   |
| O        | Sensor de obstáculos | No hay obstáculo       | Hay un obstáculo    |
| M        | Motor de apertura    | Motor apagado          | Motor encendido     |

### 3. Reglas de funcionamiento

1. El motor debe activarse cuando haya una persona, su acceso esté autorizado y no exista ningún obstáculo.
2. Si no hay una persona, el motor debe permanecer apagado.
3. Si el acceso no está autorizado, el motor debe permanecer apagado.
4. Si se detecta un obstáculo, el motor de apertura debe permanecer apagado, independientemente de las otras entradas.

<!-- ### 4. Tabla de verdad

| P | A | O | M | Descripción                              |
|:-:|:-:|:-:|:-:|------------------------------------------|
| 0 | 0 | 0 | 0 | Sin persona y sin autorización           |
| 0 | 0 | 1 | 0 | Sin persona, con obstáculo               |
| 0 | 1 | 0 | 0 | Autorización sin presencia               |
| 0 | 1 | 1 | 0 | Sin presencia, con obstáculo             |
| 1 | 0 | 0 | 0 | Persona sin autorización                 |
| 1 | 0 | 1 | 0 | Persona sin autorización y con obstáculo |
| 1 | 1 | 0 | 1 | Persona autorizada, sin obstáculo        |
| 1 | 1 | 1 | 0 | Persona autorizada, con obstáculo        | -->

## Ejercicio 3 Sistema de clasificación de productos en una banda transportadora 📦

### 1. Descripción del problema

Una empresa utiliza una banda transportadora para clasificar productos según su peso y tamaño.
El sistema cuenta con tres sensores digitales. Dependiendo de las características detectadas, se activará un actuador que desvía el producto hacia una línea de clasificación.
Para este ejercicio, se considera que el producto debe desviarse cuando se cumplan determinadas combinaciones de peso y tamaño.

### 2. Variables de entrada y salida

| Variable | Descripción           | Estado 0                        | Estado 1                       |
|----------|-----------------------|---------------------------------|--------------------------------|
| P        | Sensor de peso        | Peso dentro del rango permitido | Peso fuera del rango permitido |
| T        | Sensor de tamaño      | Tamaño pequeño                  | Tamaño grande                  |
| D        | Sensor de detección   | No detecta producto             | Detecta producto               |
| S        | Cilindro de simple efecto (*Actuador*) | No desvía el producto           | Desvía el producto             |

### 3. Reglas de funcionamiento

1. El actuador debe activarse cuando se detecte un producto con peso fuera del rango permitido y tamaño grande.
2. También debe activarse cuando se detecte un producto con peso fuera del rango permitido, independientemente de su tamaño.
3. Si no se detecta un producto, el actuador debe permanecer apagado.
4. Si el producto tiene un peso dentro del rango permitido, el actuador debe permanecer apagado.

Las reglas 1 y 2 implican que cualquier producto detectado cuyo peso esté fuera del rango permitido debe desviarse, sin importar su tamaño.

<!-- ### 4. Tabla de verdad

| P | T | D | S | Descripción                           |
|:-:|:-:|:-:|:-:|---------------------------------------|
| 0 | 0 | 0 | 0 | Sin producto                          |
| 0 | 0 | 1 | 0 | Producto pequeño, peso permitido      |
| 0 | 1 | 0 | 0 | Sin producto                          |
| 0 | 1 | 1 | 0 | Producto grande, peso permitido       |
| 1 | 0 | 0 | 0 | Sin producto                          |
| 1 | 0 | 1 | 1 | Producto pequeño, peso fuera de rango |
| 1 | 1 | 0 | 0 | Sin producto                          |
| 1 | 1 | 1 | 1 | Producto grande, peso fuera de rango  | -->

## Ejercicio 4 Sistema automático de ventilación para un invernadero 🌱

### 1. Descripción del problema

Un invernadero cuenta con un sistema automático de ventilación para mantener condiciones adecuadas para el crecimiento de las plantas.
El sistema utiliza sensores digitales para medir la temperatura, la humedad ambiental y la intensidad de la luz.
Se desea activar un ventilador cuando las condiciones ambientales lo requieran, siguiendo las reglas establecidas para este ejercicio.

### 2. Variables de entrada y salida

| Variable | Descripción           | Estado 0           | Estado 1            |
|----------|-----------------------|--------------------|---------------------|
| T        | Sensor de temperatura | Temperatura normal | Temperatura elevada |
| H        | Sensor de humedad     | Humedad normal     | Humedad elevada     |
| L        | Sensor de luminosidad | Luminosidad baja   | Luminosidad elevada |
| V        | Ventilador            | Apagado            | Encendido           |

### 3. Reglas de funcionamiento

1. El ventilador debe encenderse cuando la temperatura sea elevada.
2. También debe encenderse cuando la humedad sea elevada y la luminosidad sea elevada.
3. Si la temperatura es normal y no se cumplen simultáneamente las condiciones de humedad y luminosidad elevadas, el ventilador debe permanecer apagado.

<!-- ### 4. Tabla de verdad

| T | H | L | V | Descripción                               |
|:-:|:-:|:-:|:-:|-------------------------------------------|
| 0 | 0 | 0 | 0 | Condiciones normales                      |
| 0 | 0 | 1 | 0 | Solo luminosidad elevada                  |
| 0 | 1 | 0 | 0 | Solo humedad elevada                      |
| 0 | 1 | 1 | 1 | Humedad y luminosidad elevadas            |
| 1 | 0 | 0 | 1 | Temperatura elevada                       |
| 1 | 0 | 1 | 1 | Temperatura elevada y luminosidad elevada |
| 1 | 1 | 0 | 1 | Temperatura y humedad elevadas            |
| 1 | 1 | 1 | 1 | Todas las condiciones elevadas            | -->


## Ejercicio 5 Sistema de seguridad para una máquina industrial ⚙️

### 1. Descripción del problema

Una máquina industrial cuenta con un sistema de seguridad que impide su funcionamiento cuando se detectan condiciones peligrosas.
El sistema utiliza cuatro entradas digitales para supervisar el estado de la máquina y las condiciones de seguridad. Como salida, controla la activación del motor principal.
La máquina solamente podrá funcionar cuando el sistema esté habilitado, la protección esté cerrada y no exista una condición de emergencia.

### 2. Variables de entrada y salida

| Variable | Descripción              | Estado 0              | Estado 1           |
|----------|--------------------------|-----------------------|--------------------|
| H        | Habilitación del sistema | Sistema deshabilitado | Sistema habilitado |
| P        | Sensor de protección     | Protección abierta    | Protección cerrada |
| E        | Paro de emergencia       | Paro activado         | Paro no activado   |
| S        | Sensor de seguridad      | Condición insegura    | Condición segura   |
| M        | Motor principal          | Motor apagado         | Motor encendido    |

**Nota:** En la variable E, el estado 0 indica que el paro de emergencia está activado. Por seguridad, el motor debe permanecer apagado en ese estado.

### 3. Reglas de funcionamiento

1. El motor debe encenderse cuando el sistema esté habilitado, la protección esté cerrada, el paro de emergencia no esté activado y el sensor de seguridad indique una condición segura.
2. Si el sistema está deshabilitado, el motor debe permanecer apagado.
3. Si la protección está abierta, el motor debe permanecer apagado.
4. Si el paro de emergencia está activado, el motor debe permanecer apagado.
5. Si el sensor de seguridad indica una condición insegura, el motor debe permanecer apagado.

<!-- ### 4. Tabla de verdad

| H | P | E | S | M | Descripción                       |
|:-:|:-:|:-:|:-:|:-:|-----------------------------------|
| 0 | 0 | 0 | 0 | 0 | Sistema deshabilitado             |
| 0 | 0 | 0 | 1 | 0 | Sistema deshabilitado             |
| 0 | 0 | 1 | 0 | 0 | Sistema deshabilitado             |
| 0 | 0 | 1 | 1 | 0 | Sistema deshabilitado             |
| 0 | 1 | 0 | 0 | 0 | Sistema deshabilitado             |
| 0 | 1 | 0 | 1 | 0 | Sistema deshabilitado             |
| 0 | 1 | 1 | 0 | 0 | Sistema deshabilitado             |
| 0 | 1 | 1 | 1 | 0 | Sistema deshabilitado             |
| 1 | 0 | 0 | 0 | 0 | Protección abierta                |
| 1 | 0 | 0 | 1 | 0 | Protección abierta                |
| 1 | 0 | 1 | 0 | 0 | Protección abierta                |
| 1 | 0 | 1 | 1 | 0 | Protección abierta                |
| 1 | 1 | 0 | 0 | 0 | Paro de emergencia activado       |
| 1 | 1 | 0 | 1 | 0 | Paro de emergencia activado       |
| 1 | 1 | 1 | 0 | 0 | Condición insegura                |
| 1 | 1 | 1 | 1 | 1 | Todas las condiciones son seguras | -->


## Ejercicio 6 Control de Nivel y Ventilación en Invernadero
**Contexto:** Un invernadero automatizado cuenta con un sensor de alta temperatura ($T$), un sensor de humedad de suelo baja ($H$) y un interruptor manual de mantenimiento ($M$). Se controla una bomba de riego ($R$) y un extractor de aire ($E$).

* **Entradas:**
  * $T$: 1 = Temperatura alta, 0 = Normal
  * $H$: 1 = Suelo seco (requiere agua), 0 = Suelo húmedo
  * $M$: 1 = Mantenimiento activo (inhibe todo), 0 = Funcionamiento normal
* **Salidas:**
  * $R$ (Bomba de riego): Se activa si el suelo está seco y no está en mantenimiento.
  * $E$ (Extractor): Se activa si la temperatura es alta y no está en mantenimiento.
<!--
#### Tabla de verdad
| M | T | H |   R   |   E   | Descripción / Observaciones                                   |
|:-:|:-:|:-:|:-----:|:-----:|---------------------------------------------------------------|
| 0 | 0 | 0 | **0** | **0** | Condición ideal, todo apagado                                 |
| 0 | 0 | 1 | **1** | **0** | Suelo seco $\rightarrow$ Activa Riego                         |
| 0 | 1 | 0 | **0** | **1** | Temperatura alta $\rightarrow$ Activa Extractor               |
| 0 | 1 | 1 | **1** | **1** | Alta temp y suelo seco $\rightarrow$ Activa Riego y Extractor |
| 1 | 0 | 0 | **0** | **0** | Mantenimiento activo                                          |
| 1 | 0 | 1 | **0** | **0** | Mantenimiento activo (bloqueo)                                |
| 1 | 1 | 0 | **0** | **0** | Mantenimiento activo (bloqueo)                                |
| 1 | 1 | 1 | **0** | **0** | Mantenimiento activo (bloqueo)                                | -->


## Ejercicio 7 Dosificador Químico Industrial de Seguridad
**Contexto:** Una mezcla química requiere la adición de reactivo mediante una válvula ($V$). Se requiere que al menos 2 de 3 operadores presionen su botón de confirmación ($A, B, C$) y que la temperatura del tanque ($T$) sea segura.

* **Entradas:**
  * $A, B, C$ (Operadores 1, 2 y 3): 1 = Presionado, 0 = Liberado
  * $T$ (Térmico): 0 = Temperatura segura, 1 = Sobrecalentamiento
* **Salidas:**
  * $V$ (Válvula de llenado): Activa solo si $T = 0$ y por lo menos 2 botones ($A, B, C$) están presionados.

<!-- #### Tabla de verdad
| T | A | B | C |   V   | Descripción / Observaciones                                            |
|:-:|:-:|:-:|:-:|:-----:|------------------------------------------------------------------------|
| 0 | 0 | 0 | 0 | **0** | Nadie presiona                                                         |
| 0 | 0 | 0 | 1 | **0** | Solo 1 presiona                                                        |
| 0 | 0 | 1 | 0 | **0** | Solo 1 presiona                                                        |
| 0 | 0 | 1 | 1 | **1** | B y C presionan $\rightarrow$ Permiso concedido                        |
| 0 | 1 | 0 | 0 | **0** | Solo 1 presiona                                                        |
| 0 | 1 | 0 | 1 | **1** | A y C presionan $\rightarrow$ Permiso concedido                        |
| 0 | 1 | 1 | 0 | **1** | A y B presionan $\rightarrow$ Permiso concedido                        |
| 0 | 1 | 1 | 1 | **1** | Todos presionan $\rightarrow$ Permiso concedido                        |
| 1 | X | X | X | **0** | Temp Alta (filas 8 a 15) $\rightarrow$ Válvula bloqueada por seguridad |

*(Nota: En las 8 filas donde $T=1$, la salida $V$ es igual a 0).* -->

## Ejercicio 8 Mezcladora de Lote Automatizada
**Contexto:** Un tanque industrial cuenta con 2 reactivos. Hay dos sensores de nivel ($N_1$ bajo, $N_2$ alto) y un sensor de viscosidad ($V$). Controla un Motor Mezclador ($M$) y una Alarma de Desbordamiento ($A$).

* **Entradas:**
  * $N_1$: 1 = Nivel bajo alcanzado
  * $N_2$: 1 = Nivel alto alcanzado
  * $V$: 1 = Viscosidad óptima
* **Salidas:**
  * $M$ (Motor): Se activa para mezclar si el nivel es al menos $N_1$ y aún no alcanza la viscosidad $V$ requerida.
  * $A$ (Alarma): Se enciende si ocurre la falla $N_1=0$ y $N_2=1$.

<!-- #### Tabla de verdad
| $N_1$ | $N_2$ | V |   M   |   A   | Descripción / Observaciones                        |
|:-----:|:-----:|:-:|:-----:|:-----:|----------------------------------------------------|
|   0   |   0   | 0 | **0** | **0** | Tanque vacío                                       |
|   0   |   0   | 1 | **0** | **0** | Tanque vacío                                       |
|   0   |   1   | 0 | **0** | **1** | Error: $N_2$ activo sin $N_1$                      |
|   0   |   1   | 1 | **0** | **1** | Error: $N_2$ activo sin $N_1$                      |
|   1   |   0   | 0 | **1** | **0** | Tanque a nivel medio $\rightarrow$ Mezclar ($M=1$) |
|   1   |   0   | 1 | **0** | **0** | Mezcla lista, detiene motor                        |
|   1   |   1   | 0 | **1** | **0** | Tanque lleno $\rightarrow$ Mezclar ($M=1$)         |
|   1   |   1   | 1 | **0** | **0** | Mezcla lista a nivel alto                          | -->

## Ejercicio 9 Sistema de Extinción contra Incendios
**Contexto:** Un edificio tiene dos detectores de humo ($H_1, H_2$) y un sensor de temperatura extrema ($T$). Para evitar falsas alarmas, el rociador ($R$) y la sirena ($S$) se activan mediante reglas específicas.

* **Entradas:**
  * $H_1, H_2$: Detectores de humo (1 = Humo detectado)
  * $T$: Sensor de temperatura (1 = Temperatura alta)
* **Salidas:**
  * $S$ (Sirena): Se activa si se detecta cualquier condición de riesgo (humo o temperatura).
  * $R$ (Rociadores de agua): Se activan si **ambos** sensores de humo detectan humo, O bien si hay al menos un sensor de humo Y la temperatura es alta.

<!-- #### Tabla de verdad
| $H_1$ | $H_2$ | T |   S   |   R   | Descripción / Observaciones                              |
|:-----:|:-----:|:-:|:-----:|:-----:|----------------------------------------------------------|
|   0   |   0   | 0 | **0** | **0** | Seguro                                                   |
|   0   |   0   | 1 | **1** | **0** | Solo alta temp $\rightarrow$ Sirena de advertencia       |
|   0   |   1   | 0 | **1** | **0** | Humo aislado $\rightarrow$ Sirena                        |
|   0   |   1   | 1 | **1** | **1** | Humo + Temp alta $\rightarrow$ Activa Rociador           |
|   1   |   0   | 0 | **1** | **0** | Humo aislado $\rightarrow$ Sirena                        |
|   1   |   0   | 1 | **1** | **1** | Humo + Temp alta $\rightarrow$ Activa Rociador           |
|   1   |   1   | 0 | **1** | **1** | Confirmación doble de humo $\rightarrow$ Activa Rociador |
|   1   |   1   | 1 | **1** | **1** | Emergencia total $\rightarrow$ Activa todo               | -->

## Ejercicio 10 Control Digital de Faros Automotrices
**Contexto:** Un vehículo controla sus luces altas ($L_A$) y luces bajas ($L_B$) según la iluminación ambiental ($S_{LUZ}$), sensor de lluvia ($S_{LL}$) y el interruptor manual de luces ($I$).

* **Entradas:**
  * $S_{LUZ}$: 1 = Noche / Oscuro, 0 = Día
  * $S_{LL}$: 1 = Lluvia detectada, 0 = Seco
  * $I$: 1 = Encendido manual, 0 = Apagado
* **Salidas:**
  * $L_B$ (Luces Bajas): Se encienden si es de noche, si está lloviendo o si el mando manual está activo.
  * $L_A$ (Luces Altas): Se encienden si es de noche, el mando manual está activo y **no** está lloviendo (para evitar deslumbrar por reflejo).

<!-- #### Tabla de verdad
| I | $S_{LUZ}$ | $S_{LL}$ | $L_B$ | $L_A$ | Descripción / Observaciones                                       |
|:-:|:---------:|:--------:|:-----:|:-----:|-------------------------------------------------------------------|
| 0 |     0     |    0     | **0** | **0** | Todo apagado en día                                               |
| 0 |     0     |    1     | **1** | **0** | Lluvia de día $\rightarrow$ Enciende Bajas                        |
| 0 |     1     |    0     | **1** | **0** | Noche en auto $\rightarrow$ Enciende Bajas                        |
| 0 |     1     |    1     | **1** | **0** | Noche + Lluvia $\rightarrow$ Enciende Bajas                       |
| 1 |     0     |    0     | **1** | **0** | Manual en día $\rightarrow$ Enciende Bajas                        |
| 1 |     0     |    1     | **1** | **0** | Manual en lluvia $\rightarrow$ Enciende Bajas                     |
| 1 |     1     |    0     | **1** | **1** | Manual + Noche sin lluvia $\rightarrow$ Activa Altas y Bajas      |
| 1 |     1     |    1     | **1** | **0** | Manual + Noche con lluvia $\rightarrow$ Cancela Altas por reflejo | -->

## Ejercicio 11 Sistema de Estación de Bombeo Doble (Redundancia)
**Contexto:** Un pozo cuenta con dos bombas ($B_1$ y $B_2$) y tres sensores de nivel ($N_B$ bajo, $N_M$ medio, $N_A$ alto).

* **Entradas:**
  * $N_{Bajo}, N_{Medio}, N_{Alto}$: 1 = Agentes sumergidos en agua.
* **Salidas:**
  * $B_1$: Se activa cuando el nivel llega a Medio ($N_M$).
  * $B_2$: Se activa adicionalmente como refuerzo solo cuando el nivel llega a Alto ($N_A$).

<!-- #### Tabla de verdad
| $N_B$ | $N_M$ | $N_A$ | $B_1$ | $B_2$ | Descripción / Observaciones                    |
|:-----:|:-----:|:-----:|:-----:|:-----:|------------------------------------------------|
|   0   |   0   |   0   | **0** | **0** | Pozo seco                                      |
|   0   |   0   |   1   | **0** | **0** | Error de lectura                               |
|   0   |   1   |   0   | **0** | **0** | Error de lectura                               |
|   0   |   1   |   1   | **0** | **0** | Error de lectura                               |
|   1   |   0   |   0   | **0** | **0** | Agua en nivel bajo (reposo)                    |
|   1   |   0   |   1   | **0** | **0** | Error de lectura                               |
|   1   |   1   |   0   | **1** | **0** | Nivel medio $\rightarrow$ Arranca Bomba 1      |
|   1   |   1   |   1   | **1** | **1** | Nivel alto $\rightarrow$ Arrancan Bombas 1 y 2 | -->
