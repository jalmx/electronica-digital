# Aplicación: Mapa de Karnaugh

Transformar la siguiente suma de productos estándar en un mapa de Karnaugh:

![img](./assets/Clase1_S7_36.png)

![img](./assets/Clase1_S7_37.png)

Vamos a agrupar:

![img](./assets/Clase1_S7_38.png)

![img](./assets/Clase1_S7_39.png)

![img](./assets/Clase1_S7_40.png)

![img](./assets/Clase1_S7_41.png)

![img](./assets/Clase1_S7_42.png)

![img](./assets/Clase1_S7_43.png)

![img](./assets/Clase1_S7_44.png)

![img](./assets/Clase1_S7_45.png)

![img](./assets/Clase1_S7_46.png)

Transformar la siguiente suma de productos estándar en un mapa de Karnaugh:

![img](./assets/Clase1_S7_47.png)

![img](./assets/Clase1_S7_48.png)

![img](./assets/Clase1_S7_49.png)

Vamos a agrupar:

![img](./assets/Clase1_S7_50.png)

![img](./assets/Clase1_S7_51.png)

![img](./assets/Clase1_S7_52.png)

![img](./assets/Clase1_S7_53.png)

![img](./assets/Clase1_S7_54.png)

![img](./assets/Clase1_S7_55.png)

![img](./assets/Clase1_S7_56.png)

![img](./assets/Clase1_S7_57.png)

![img](./assets/Clase1_S7_58.png)

![img](./assets/Clase1_S7_59.png)


De la tabla de verdad genera tu mapa de Karnaugh, y el circuito digital:

![img](./assets/Clase1_S7_60.png)

Sacar los 1s

![img](./assets/Clase1_S7_61.png)

![img](./assets/Clase1_S7_62.png)

![img](./assets/Clase1_S7_63.png)

![img](./assets/Clase1_S7_64.png)

![img](./assets/Clase1_S7_65.png)

![img](./assets/Clase1_S7_66.png)

![img](./assets/Clase1_S7_67.png)

![img](./assets/Clase1_S7_68.png)

![img](./assets/Clase1_S7_69.png)

![img](./assets/Clase1_S7_70.png)

![img](./assets/Clase1_S7_71.png)

## Control de lámpara

Se desea gobernar una lámpara desde dos interruptores A y B, de forma que cada vez que varíe el estado de uno de ellos, la lámpara cambie de estado. Es decir, que si en un estado de los interruptores la lámpara está encendida, al cambiar A ó B, la lámpara se apague y si estaba apagada se encienda.

![img](./assets/Clase1_S7_72.png)

En un principio, si están abiertos los dos interruptores A y B, la lámpara está apagada.

![img](./assets/Clase1_S7_73.png)

1a fase: Se establece la tabla de verdad, teniendo en cuenta que hay dos variables binarias de entrada, A y B, una salida, que es la lámpara L, y un estado definido por el enunciado, en el que si A = 0 y B = 0, L = 0. A partir de aquí, el cambio de una variable provoca la variación del estado de la lámpara.

![img](./assets/Clase1_S7_74.png)

Según la tabla de verdad, la lámpara se ilumina solo en dos casos:

![img](./assets/Clase1_S7_75.png)

Debemos obtener la ecuación a partir de la tabla

![img](./assets/Clase1_S7_76.png)

![img](./assets/Clase1_S7_77.png)

No tiene reducción la ecuación, por lo tanto, así queda.

![img](./assets/Clase1_S7_78.png)

![img](./assets/Clase1_S7_79.png)

![img](./assets/Clase1_S7_80.png)

![img](./assets/Clase1_S7_81.png)

![img](./assets/Clase1_S7_82.png)

## Control de 2 motores

Se desea controlar dos motores M1 y M2 por medio de los contactos de tres interruptores  _A, B y C_ , de forma que se cumplan las siguientes condiciones:

Si  _A_  está pulsado y los otros dos no, se activa M1

Si  _C_  está pulsado y los otros dos nó, se activa M2

Si los  _tres interruptores_  están cerrados se activan M1 y M2

En las demás condiciones no mencionadas, los dos motores están parados.

![img](./assets/Clase1_S7_83.png)

Obteniendo la tabla de verdad para M1 y M2

![img](./assets/Clase1_S7_84.png)

Obtenido la ecuación para M1

![img](./assets/Clase1_S7_85.png)

![img](./assets/Clase1_S7_86.png)

Obtenido la ecuación para M2

![img](./assets/Clase1_S7_87.png)

![img](./assets/Clase1_S7_88.png)

Generamos la reducción y el circuito

![img](./assets/Clase1_S7_89.png)

![img](./assets/Clase1_S7_90.png)

![img](./assets/Clase1_S7_91.png)

![img](./assets/Clase1_S7_92.png)

![img](./assets/Clase1_S7_93.png)

![img](./assets/Clase1_S7_94.png)
