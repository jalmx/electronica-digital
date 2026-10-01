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

Factorizamos las variables comunes  $A\overline{B}$. Nos queda para reducir la $D$ con su complemento $D’$, y aplicamos la fórmula, nos da como resultado:

| Pasos | Operación                                 |
| :---: | ----------------------------------------- |
|   1   | ![img](./assets/Clase1_S6_3.png)          |
|   2   | Se reduce $D + \overline{D} = 1$          |
|   3   | ![img](./assets/Clase1_S6_4.png)          |
|   4   | Resolvemos la multiplicación y nos queda: |
|   5   | ![img](./assets/Clase1_S6_5.png)          |

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
|   1   | ![img](./assets/Clase1_S6_61.png)                                               |
|       | Nos dá como resultado:                                                          |
|       | ![img](./assets/Clase1_S6_62.png)                                               |
|       | La función resultante fue:                                                      |
|       | ![img](./assets/Clase1_S6_63.png)                                               |
|       | Aplicamos el **teorema de Morgan**: $\overline{XY} = \overline{X}+\overline{Y}$ |
|       | ![img](./assets/Clase1_S6_64.png)                                               |
|       | Se reduce $\overline{\overline{A}}=A$. Cancelamos los inversos en $A$ y $C$     |
|       | ![img](./assets/Clase1_S6_65.png)                                               |
|       | Multiplicamos los factores:                                                     |
|       | ![img](./assets/Clase1_S6_66.png)                                               |
|       | Reduzimos $A \times A = A$. Nos queda:                                          |
|       | ![img](./assets/Clase1_S6_67.png)                                               |
|       | Fatorizamos $AC$.                                                               |
|       | ![img](./assets/Clase1_S6_68.png)                                               |
|       | Reduzimos las B complementarias:                                                |
|       | ![img](./assets/Clase1_S6_69.png)                                               |
|       | Nos queda:                                                                      |
|       | ![img](./assets/Clase1_S6_70.png)                                               |
|       | Aún podemos factorizar para que nos quede:                                      |
|       | ![img](./assets/Clase1_S6_71.png)                                               |

|         Ecuación Reducida         |          Tabla de verdad          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S6_71.png) | ![img](./assets/Clase1_S6_74.png) |

### Circuito

![img](./assets/Clase1_S6_77.png)

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
|       | Una vez tenemos las salidas en 1, se genera la ecuación sumando cada producto:                                                                     |
|       | ![img](./assets/Clase1_S6_81.png)                                                                                                                  |
|       | Ahora debemos reducir la ecuación, para esto vamos a aplicar el teorema  $x + x = x$ , con  $ABC$ ; duplicamos para reducir más fácil la ecuación: |
|       | ![img](./assets/Clase1_S6_87.png)                                                                                                                  |
|       | Factorizamos los términos:                                                                                                                         |
|       | ![img](./assets/Clase1_S6_88.png)                                                                                                                  |
|       | Hacemos las reducciones necesarias y llegamos a la resultante                                                                                      |
|       | ![img](./assets/Clase1_S6_89.png)                                                                                                                  |

|         Ecuación Reducida         |          Tabla de verdad          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S6_89.png) | ![img](./assets/Clase1_S6_96.png) |

### Circuito

![img](./assets/Clase1_S6_95.png)

### Ejercicio 8

Con base a la tabla de verdad, obtener ecuación, reducir ecuación, y construir el circuito digital

|           Tabla inicial           |
| :-------------------------------: |
| ![img](./assets/Clase1_S6_97.png) |

Con base a la tabla de verdad, obtener ecuación, reducir ecuación, y construir el circuito digital

![img](./assets/Clase1_S6_98.png)

Primero se debe obtener los valores de las salidas que sean 1:

La ecuación generada es:

( ~A B C D) + (A ~B ~C ~D ) + (A ~B ~C D ) +

(A ~B C ~ D) + (A ~B C D) + (A B ~C ~D) + (A B ~C D )

( A B C ~D) + (A B C D)

![img](./assets/Clase1_S6_99.png)

![img](./assets/Clase1_S6_100.png)

![img](./assets/Clase1_S6_101.png)

![img](./assets/Clase1_S6_102.png)

![img](./assets/Clase1_S6_103.png)

![img](./assets/Clase1_S6_104.png)

![img](./assets/Clase1_S6_105.png)

![img](./assets/Clase1_S6_106.png)

La función obtenida es:

Vamos a factorizar los complementos en D:

La ecuación reducida nos queda:

![img](./assets/Clase1_S6_107.png)

![img](./assets/Clase1_S6_108.png)

![img](./assets/Clase1_S6_109.png)

![img](./assets/Clase1_S6_110.png)

Volvemos factorizar los complementos de C:

La ecuación reducida nos queda:

Factorizamos A:

![img](./assets/Clase1_S6_111.png)

![img](./assets/Clase1_S6_112.png)

![img](./assets/Clase1_S6_113.png)

Aplicamos el complemento en B:

Aún podemos reducir más, aplicando el Teorama  $x + \overline{x}y = x + y$ . En este caso  $x = A$  y  $y = BCD,$  nos queda:

![img](./assets/Clase1_S6_114.png)

![img](./assets/Clase1_S6_115.png)

![img](./assets/Clase1_S6_116.png)

![img](./assets/Clase1_S6_117.png)

![img](./assets/Clase1_S6_118.png)

La tabla de verdad resultante:

![img](./assets/Clase1_S6_121.png)

![img](./assets/Clase1_S6_122.png)
