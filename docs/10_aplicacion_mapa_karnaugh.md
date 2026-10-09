---
title: "Aplicación: Mapa de Karnaugh"
create_index: true
---

![banner](./assets/banner_class_85.png)

# Aplicación: Mapa de Karnaugh

## Ejemplo básico 1

Transformar la siguiente suma de productos estándar en un mapa de Karnaugh:

|             Ecuación              |
| :-------------------------------: |
| ![img](./assets/Clase1_S7_36.png) |
| ![img](./assets/Clase1_S7_37.png) |

### Agrupamineto

![ejercicio](./assets/ejercicio_1_k.png)

### Circuito

| Tabla de verdad                   | Mapa de Karnaugh                  |
| --------------------------------- | --------------------------------- |
| ![img](./assets/Clase1_S7_46.png) | ![img](./assets/Clase1_S7_43.png) |

![img](./assets/Clase1_S7_44.png)

![img](./assets/Clase1_S7_45.png)

## Ejercicio básico 2

Transformar la siguiente suma de productos estándar en un mapa de Karnaugh:

|                              Ecuación                               |
| :-----------------------------------------------------------------: |
| ![img](./assets/Clase1_S7_47.png) ![img](./assets/Clase1_S7_48.png) |
|                  ![img](./assets/Clase1_S7_49.png)                  |

### Agrupamiento

![ejercicio](./assets/ejercicio_2_k.png)

### Circuito

|          Tabla de verdad          |         Mapa de Karnaugh          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S7_59.png) | ![img](./assets/Clase1_S7_56.png) |

![img](./assets/Clase1_S7_57.png)

![img](./assets/Clase1_S7_58.png)

## Ejercicio básico 3

De la tabla de verdad genera tu mapa de Karnaugh, y el circuito digital:

|               Tabla               |             Sacar los 1s             |
| :-------------------------------: | :----------------------------------: |
| ![img](./assets/Clase1_S7_60.png) | ![table](./assets/tabla_ejerc_3.png) |

### Circuito

|          Tabla de verdad          |         Mapa de Karnaugh          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S7_71.png) | ![img](./assets/Clase1_S7_68.png) |

![img](./assets/Clase1_S7_67.png)

![img](./assets/Clase1_S7_70.png)

## Control de lámpara

Se desea gobernar una lámpara desde dos interruptores $A$ y $B$, de forma que cada vez que varíe el estado de uno de ellos, la lámpara cambie de estado. Es decir, que si en un estado de los interruptores la lámpara está encendida, al cambiar $A$ ó $B$, la lámpara se apague y si estaba apagada se encienda.

![img](./assets/Clase1_S7_72.png)

En un principio, si están abiertos los dos interruptores $A$ y $B$, la lámpara está apagada.

![img](./assets/Clase1_S7_73.png)

### 1a fase

Se establece la tabla de verdad, teniendo en cuenta que hay dos variables binarias de entrada, $A$ y $B$, una salida, que es la lámpara L, y un estado definido por el enunciado, en el que si $A = 0$ y $B = 0$, $L = 0$. A partir de aquí, el cambio de una variable provoca la variación del estado de la lámpara.

![img](./assets/Clase1_S7_74.png)

Según la tabla de verdad, la lámpara se ilumina solo en dos casos:

![img](./assets/Clase1_S7_75.png)

Debemos obtener la ecuación a partir de la tabla

![img](./assets/Clase1_S7_76.png)

No tiene reducción la ecuación, por lo tanto, así queda.

### Circuito

|          Tabla de verdad          |         Mapa de Karnaugh          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S7_80.png) | ![img](./assets/Clase1_S7_79.png) |

![img](./assets/Clase1_S7_78.png)

![img](./assets/Clase1_S7_82.png)

## Control de 2 motores

Se desea controlar dos motores $M1$ y $M2$ por medio de los contactos de tres interruptores  $A$, $B$ y $C$ , de forma que se cumplan las siguientes condiciones:

- Si  $A$  está pulsado y los otros dos no, se activa $M1$
- Si  $C$  está pulsado y los otros dos nó, se activa $M2$
- Si los  _tres interruptores_  están cerrados se activan $M1$ y $M2$
- En las demás condiciones no mencionadas, los dos motores están parados.

![img](./assets/Clase1_S7_83.png)

Obteniendo la tabla de verdad para $M1$ y $M2$

![img](./assets/Clase1_S7_84.png)

Obtenido la ecuación para $M1$

![img](./assets/tabla_m1.png)

Obtenido la ecuación para $M2$

![img](./assets/tabla_m2.png)

### Circuito

Generamos la reducción y el circuito

|          Tabla de verdad          |         Mapa de Karnaugh          |
| :-------------------------------: | :-------------------------------: |
| ![img](./assets/Clase1_S7_89.png) | ![img](./assets/Clase1_S7_92.png) |
| ![img](./assets/Clase1_S7_89.png) | ![img](./assets/Clase1_S7_91.png) |

---

![img](./assets/Clase1_S7_90.png)
![img](./assets/Clase1_S7_93.png)

![img](./assets/Clase1_S7_94.png)

## Contador Hexadecimal

### Display de 7 segmentos

Un display de 7 segmentos es un componente electrónico que se utiliza para representar números del 0 al 9 (y algunas letras de la A a la F en formato hexadecimal) mediante el encendido o apagado de siete diodos LED individuales dispuestos en forma de "8".

#### Tipos

Se tienen 2 tipos de display de segmentos:

- Ánodo Común
- Cátodo Común

![display](./assets/Display-de-7-segmentos-anodo-comun.jpg)

#### Pines

Existen diversos modelos de display de 7 segmentos, pero la comun es la siguiente:

![Display](./assets/displays_7seg.png)

#### Desarrollo

Se realizara el diseño de un contador hexadecimal, que vaya del **0 a la F**. Para esto se tomara de base un display de catodo común, es decir, el negativo es el comun en el display, con la siguiente disposicion de pines:

![pines](./assets/7seg_pinout.png)


Se debe hacer el control de un display de 7 segmentos. Para mostrar los digitos desde el 0 hasta la F

| Digito |   A   |   B   |   C   |   D   |   a   |   b   |   c   |   d   |   e   |   f   |   g   |
| :----: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0**  | **0** | **0** | **0** | **0** |   1   |   1   |   1   |   1   |   1   |   1   |   0   |
| **1**  | **0** | **0** | **0** | **1** |   0   |   1   |   1   |   0   |   0   |   0   |   0   |
| **2**  | **0** | **0** | **1** | **0** |   1   |   1   |   0   |   1   |   1   |   0   |   1   |
| **3**  | **0** | **0** | **1** | **1** |   1   |   1   |   1   |   1   |   0   |   0   |   1   |
| **4**  | **0** | **1** | **0** | **0** |   0   |   1   |   1   |   0   |   0   |   1   |   1   |
| **5**  | **0** | **1** | **0** | **1** |   1   |   0   |   1   |   1   |   0   |   1   |   1   |
| **6**  | **0** | **1** | **1** | **0** |   0   |   0   |   1   |   1   |   1   |   1   |   1   |
| **7**  | **0** | **1** | **1** | **1** |   1   |   1   |   1   |   0   |   0   |   0   |   0   |
| **8**  | **1** | **0** | **0** | **0** |   1   |   1   |   1   |   1   |   1   |   1   |   1   |
| **9**  | **1** | **0** | **0** | **1** |   1   |   1   |   1   |   0   |   0   |   1   |   1   |
| **A**  | **1** | **0** | **1** | **0** |   1   |   1   |   1   |   0   |   1   |   1   |   1   |
| **B**  | **1** | **0** | **1** | **1** |   0   |   0   |   1   |   1   |   1   |   1   |   1   |
| **C**  | **1** | **1** | **0** | **0** |   1   |   0   |   0   |   1   |   1   |   1   |   0   |
| **D**  | **1** | **1** | **0** | **1** |   0   |   1   |   1   |   1   |   1   |   0   |   1   |
| **E**  | **1** | **1** | **1** | **0** |   1   |   0   |   0   |   1   |   1   |   1   |   1   |
| **F**  | **1** | **1** | **1** | **1** |   1   |   0   |   0   |   0   |   1   |   1   |   1   |

![](./assets/7_seg_sim.png)

??? Note "Ecuacion RAW"
    - a = ~B ~D + ~A ~B C + ~A B D + A ~B ~C + A ~D + A B C
    - b = ~A ~B + ~A ~C ~D + ~B ~D + ~A C D + A ~C D
    - c = ~A ~C + ~A D + ~C D + ~A B + A ~B
    - d = ~A ~B ~D + ~B C D + B ~C D + B C ~D + A ~C ~D
    - e = ~B ~D + C ~D + A C + A B
    - f = ~C ~D + ~A B ~C + B ~D + A ~B + A C
    - g = ~B C + C ~D + ~A B ~C + A ~B + A D


![tabla de verdad](./assets/tabla_7segmentos.png)

### Circuito

![circuito digital](./assets/7_segmetos_circuito.jpg)

| Eucación                                                                                                                                   |         Mapa de Karnaugh          |
| :----------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------: |
| $a = \overline{B} \overline{D} + \overline{A} \overline{B} C + \overline{A} B D + A \overline{B} \overline{C} + A \overline{D} + A B C$    | ![mapa](./assets/7_seg_map_a.png) |
| $b = \overline{A} \overline{B} + \overline{A} \overline{C} \overline{D} + \overline{B} \overline{D} + \overline{A} C D + A \overline{C} D$ | ![mapa](./assets/7_seg_map_b.png) |
| $c = \overline{A} \overline{C} + \overline{A} D + \overline{C} D + \overline{A} B + A \overline{B}$                                        | ![mapa](./assets/7_seg_map_c.png) |
| $d = \overline{A} \overline{B} \overline{D} + \overline{B} C D + B \overline{C} D + B C \overline{D} + A \overline{C} \overline{D}$        | ![mapa](./assets/7_seg_map_d.png) |
| $e = \overline{B} \overline{D} + C \overline{D} + A C + A B$                                                                               | ![mapa](./assets/7_seg_map_e.png) |
| $f = \overline{C} \overline{D} + \overline{A} B \overline{C} + B \overline{D} + A \overline{B} + A C$                                      | ![mapa](./assets/7_seg_map_f.png) |
| $g = \overline{B} C + C \overline{D} + \overline{A} B \overline{C} + A \overline{B} + A D$                                                 | ![mapa](./assets/7_seg_map_g.png) |

[Descargar simulación de Logisim](./assets/circuitos/display_7seg.circ)
