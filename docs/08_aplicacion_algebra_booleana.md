---
title: "Aplicando Álgebra Booleana"
create_index: true
---

![banner](./assets/banner_class_85.png)

# Aplicando Álgebra Booleana

## Reducción de ecuacion y generación de circuito y tabla de verdad

## Ejercicio 1
Simplifique la expresión, comprobar tabla de verdad y crear su circuito digital

|             Ecuación             |
| :------------------------------: |
| ![img](./assets/Clase1_S6_1.png) |

### Desarrollo

Simplificando la expresión, la ecuación es:

Factorizamos las variables comunes  $A\overline{B}$. Nos queda para reducir la $D$ con su complemento $\overline{D}$, y aplicamos la fórmula, nos da como resultado:

| Pasos | Operación                                                          |
| :---: | ------------------------------------------------------------------ |
|   1   | Se reduce $D + \overline{D} = 1$                                   |
|   2   | ![img](./assets/Clase1_S6_3.png)                                   |
|   3   | Se multiplica el resultadode la reducción con el factor resultante |
|   4   | ![img](./assets/Clase1_S6_4.png)                                   |
|   5   | Resolvemos la multiplicación y nos queda:                          |
|   6   | ![img](./assets/Clase1_S6_5.png)                                   |

### Resultado

Crear el circuito de la ecuación reducida:

|             Ecuación             |         Tabla de verdad          |
| :------------------------------: | :------------------------------: |
| ![img](./assets/Clase1_S6_5.png) | ![img](./assets/Clase1_S6_6.png) |

### Circuito

![img](./assets/Clase1_S6_8.png)

## Ejercicio 2

Simplifique la expresión, comprobar tabla de verdad y crear su circuito digital


|             Ecuación             |
| :------------------------------: |
| ![img](./assets/Clase1_S6_9.png) |

### Desarrollo

| Pasos | Operación                                                                        |
| :---: | -------------------------------------------------------------------------------- |
|   1   | ![img](./assets/Clase1_S6_9.png)                                                 |
|   2   | Realizamos la multiplicación:                                                    |
|   3   | ![img](./assets/Clase1_S6_11.png)                                                |
|   4   | Ahora podemos aplicar los teoremas siguientes: ![img](./assets/Clase1_S6_12.png) |
|   5   | Sustituimos en la ecuación: ![img](./assets/Clase1_S6_13.png)                    |
|   6   | ![img](./assets/Clase1_S6_14.png)                                                |
|       | Reducimos y nos queda:                                                           |
|       | ![img](./assets/Clase1_S6_15.png)                                                |
|       | Factorizamos a B                                                                 |
|       | ![img](./assets/Clase1_S6_16.png)                                                |
|       | Nos da como resultado:                                                           |
|       | ![img](./assets/Clase1_S6_17.png)                                                |

|             Ecuación              |          Tabla de verdad          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S6_17.png) | ![img](./assets/Clase1_S6_20.png) |

### Circuito

![img](./assets/Clase1_S6_19.png)

## Ejercicio 3

Simplifique la expresión, comprobar tabla de verdad y crear su circuito digital:

|             Ecuación              |
| :-------------------------------: |
| ![img](./assets/Clase1_S6_21.png) |

### Desarrollo

| Pasos | Operación                                                                     |
| :---: | ----------------------------------------------------------------------------- |
|   1   | Simplificando la expresión, la ecuación es:                                   |
|   2   | ![img](./assets/Clase1_S6_22.png)                                             |
|   3   | Si factorizamos las variables comunes $CD$, tenemos que                       |
|   4   | ![img](./assets/Clase1_S6_23.png)                                             |
|   5   | Utilizando el  _teorema_  podemos sustituir ![img](./assets/Clase1_S6_24.png) |
|   6   | Quedándonos:                                                                  |
|   7   | ![img](./assets/Clase1_S6_25.png)                                             |
|   8   | Volvemos a multiplicar todo, para el resultado final                          |
|   9   | ![img](./assets/Clase1_S6_26.png)                                             |


|             Ecuación              |          Tabla de verdad          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S6_26.png) | ![img](./assets/Clase1_S6_29.png) |

### Circuito

![img](./assets/Clase1_S6_31.png)

## A partir de circuito generar ecuación y reducción

## Ejercicio 4

Con base al circuito, generar la ecuación, reducirla y obtener tabla de verdad

|         Circuito inicial          |
| :-------------------------------: |
| ![img](./assets/Clase1_S6_33.png) |

### Desarrollo

Vamos asignando los valores por cada compuerta y su salida

| Pasos | Operación                                  |
| :---: | ------------------------------------------ |
|   1   | Inicio                                     |
|   2   | ![img](./assets/Clase1_S6_34.png)          |
|   3   | Nos da como resultado:                     |
|   4   | ![img](./assets/Clase1_S6_35.png)          |
|   5   | Nos da como resultado la ecuación booleana |
|   6   | ![img](./assets/Clase1_S6_36.png)          |

|             Ecuación              |          Tabla de verdad          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S6_36.png) | ![img](./assets/Clase1_S6_37.png) |

### Circuito 

![img](./assets/Clase1_S6_38.png)

## Ejercicio 5

Con base al circuito, generar la ecuación, reducirla y obtener tabla de verdad

|         Circuito inicial          |
| :-------------------------------: |
| ![img](./assets/Clase1_S6_39.png) |


### Desarrollo

| Pasos | Operación                                                                                             |
| :---: | ----------------------------------------------------------------------------------------------------- |
|   1   | Vamos asignando los valores por cada compuerta y su salida                                            |
|   2   | ![img](./assets/Clase1_S6_40.png)                                                                     |
|   3   | Nos da como resultado:                                                                                |
|   4   | ![img](./assets/Clase1_S6_41.png)                                                                     |
|   5   | La función obtenida fue:                                                                              |
|   6   | ![img](./assets/Clase1_S6_42.png)                                                                     |
|   7   | Para simplificar, aplicaremos **Teorema de Morgan** en las negaciones                                 |
|   8   | Con esto aplicamos para que la suma se convierta en multiplicación: ![img](./assets/Clase1_S6_43.png) |
|   9   | Nos queda de la siguiente manera al aplicar el teorema de Morgan                                      |
|  10   | ![img](./assets/Clase1_S6_44.png)                                                                     |
|  11   | Ahora, aplicamos el teorema para ![img](./assets/Clase1_S6_45.png)                                    |
|  12   | Con esto la ecuación nos queda:                                                                       |
|  13   | ![img](./assets/Clase1_S6_46.png)                                                                     |
|  14   | Volvemos a aplicar teorema de Morgan:                                                                 |
|  15   | ![img](./assets/Clase1_S6_47.png)                                                                     |
|  16   | Aplicamos el teorema                                                                                  |
|  17   | ![img](./assets/Clase1_S6_48.png)                                                                     |
|  18   | Con esto la ecuación se reduce                                                                        |
|  19   | ![img](./assets/Clase1_S6_49.png)                                                                     |
|  20   | Se reduce, quedando:                                                                                  |
|  21   | ![img](./assets/Clase1_S6_50.png)                                                                     |
|  22   | Aplicamos el teorema ![img](./assets/Clase1_S6_51.png)                                                |
|  23   | Multiplicamos los factores                                                                            |
|  24   | Para llegar al resultado final:                                                                       |
|  25   | ![img](./assets/Clase1_S6_52.png)                                                                     |

|         Ecuación Reducida         |          Tabla de verdad          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S6_52.png) | ![img](./assets/Clase1_S6_56.png) |

### Circuito

![img](./assets/Clase1_S6_58.png)

## Ejercicio 6

Con base al circuito, generar la ecuación, reducirla y obtener tabla de verdad

|         Circuito inicial          |
| :-------------------------------: |
| ![img](./assets/Clase1_S6_60.png) |

### Desarrollo

Vamos asignando los valores por cada compuerta y su salida

| Pasos | Operación                                                                       |
| :---: | ------------------------------------------------------------------------------- |
|   1   | Inicio                                                                          |
|   2   | ![img](./assets/Clase1_S6_61.png)                                               |
|   3   | Nos dá como resultado:                                                          |
|   4   | ![img](./assets/Clase1_S6_62.png)                                               |
|   5   | La función resultante fue:                                                      |
|   6   | ![img](./assets/Clase1_S6_63.png)                                               |
|   7   | Aplicamos el **teorema de Morgan**: $\overline{XY} = \overline{X}+\overline{Y}$ |
|   8   | ![img](./assets/Clase1_S6_64.png)                                               |
|   9   | Se reduce $\overline{\overline{A}}=A$. Cancelamos los inversos en $A$ y $C$     |
|  10   | ![img](./assets/Clase1_S6_65.png)                                               |
|  11   | Multiplicamos los factores:                                                     |
|  12   | ![img](./assets/Clase1_S6_66.png)                                               |
|  13   | Reduzimos $A \times A = A$. Nos queda:                                          |
|  14   | ![img](./assets/Clase1_S6_67.png)                                               |
|  15   | Fatorizamos $AC$.                                                               |
|  16   | ![img](./assets/Clase1_S6_68.png)                                               |
|  17   | Reduzimos las B complementarias:                                                |
|  18   | ![img](./assets/Clase1_S6_69.png)                                               |
|  19   | Nos queda:                                                                      |
|  20   | ![img](./assets/Clase1_S6_70.png)                                               |
|  21   | Aún podemos factorizar para que nos quede:                                      |
|  22   | ![img](./assets/Clase1_S6_71.png)                                               |

|         Ecuación Reducida         |          Tabla de verdad          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S6_71.png) | ![img](./assets/Clase1_S6_74.png) |

### Circuito

![img](./assets/Clase1_S6_77.png)

## A partir de Tabla de verdad generar ecuación y reducción

## Ejercicio 7

Con base a la tabla de verdad, obtener ecuación, reducir ecuación, y construir el circuito digital

|           Tabla inicial           |
| :-------------------------------: |
| ![img](./assets/Clase1_S6_79.png) |

### Desarrollo


| Pasos | Operación                                                                                                                                          |
| :---: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1   | Primero se debe obtener los valores de las salidas que sean 1                                                                                      |
|   2   | ![img](./assets/Clase1_S6_82.png)                                                                                                                  |
|   3   | Una vez tenemos las salidas en 1, se genera la ecuación sumando cada producto:                                                                     |
|   4   | ![img](./assets/Clase1_S6_81.png)                                                                                                                  |
|   5   | Ahora debemos reducir la ecuación, para esto vamos a aplicar el teorema  $x + x = x$ , con  $ABC$ ; duplicamos para reducir más fácil la ecuación: |
|   6   | ![img](./assets/Clase1_S6_87.png)                                                                                                                  |
|   7   | Factorizamos los términos:                                                                                                                         |
|   8   | ![img](./assets/Clase1_S6_88.png)                                                                                                                  |
|   9   | Hacemos las reducciones necesarias y llegamos a la resultante                                                                                      |
|  10   | ![img](./assets/Clase1_S6_89.png)                                                                                                                  |

|         Ecuación Reducida         |          Tabla de verdad          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S6_89.png) | ![img](./assets/Clase1_S6_96.png) |

### Circuito

![img](./assets/Clase1_S6_95.png)

## Ejercicio 8

Con base a la tabla de verdad, obtener ecuación, reducir ecuación, y construir el circuito digital

|           Tabla inicial           |
| :-------------------------------: |
| ![img](./assets/Clase1_S6_97.png) |

### Desarrollo

| Pasos | Operación                                                                       |
| :---: | ------------------------------------------------------------------------------- |
|   1   | Con base a la tabla de verdad, obtener ecuación, reducir ecuación, y construir el circuito digital|
|1|Primero se debe obtener los valores de las salidas que sean 1:|
||![img](./assets/Clase1_S6_98.png)|
||La ecuación generada es:|
||![img](./assets/Clase1_S6_99.png)<br>![img](./assets/Clase1_S6_100.png)|
||Creamos el circuito original con base la ecuación sin reducción|
||![img](./assets/Clase1_S6_102.png)|
||Retomando la ecuacion obtenida|
||![img](./assets/Clase1_S6_99.png)<br>![img](./assets/Clase1_S6_100.png)|
||Vamos a factorizar los complementos en $D$|
||![img](./assets/Clase1_S6_109.png)|
||La ecuación reducida nos queda:|
||![img](./assets/Clase1_S6_110.png)|
||Volvemos factorizar los complementos de $C$:|
||![img](./assets/Clase1_S6_111.png)|
||La ecuación reducida nos queda:|
||![img](./assets/Clase1_S6_112.png)|
||Factorizamos $A$|
||![img](./assets/Clase1_S6_113.png)|
||Aplicamos el complemento en $B$|
||![img](./assets/Clase1_S6_114.png)|
||Aún podemos reducir más, aplicando el Teorama  $x + \overline{x}y = x + y$.<br>En este caso  $x = A$  y  $y = BCD,$  nos queda:|
||![img](./assets/Clase1_S6_115.png)|

??? note "Ecuación raw"
    ( ~A B C D) + (A ~B ~C ~D ) + (A ~B ~C D ) + (A ~B C ~ D) + (A ~B C D) + (A B ~C ~D) + (A B ~C D ) + ( A B C ~D) + (A B C D)


|         Ecuación Reducida         |          Tabla de verdad          |
| :-------------------------------: | :-------------------------------: |
|![img](./assets/Clase1_S6_115.png)|![img](./assets/Clase1_S6_105.png)|


### Circuito

![img](./assets/Clase1_S6_118.png)

![img](./assets/Clase1_S6_122.png)



