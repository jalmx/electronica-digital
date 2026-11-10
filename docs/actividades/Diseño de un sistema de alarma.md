![banner](../assets/banner_class_85.png)

# 🚨 Actividad: Diseño de un sistema de alarma

## 🎯 Objetivo

Diseñar e implementar un sistema digital de seguridad para una vivienda, utilizando sensores de puertas, ventanas y humo. El sistema deberá controlar una alarma sonora, un extractor de humo y dos indicadores luminosos.

El desarrollo deberá incluir el análisis del problema, la elaboración de tablas de verdad, la simplificación de funciones booleanas y la construcción y simulación del circuito digital.

## 1. 🔌 Entradas del sistema

El sistema contará con las siguientes entradas:

| Entrada             | Descripción                                 |
|---------------------|---------------------------------------------|
| Sensor de puerta    | 1 = Puerta abierta; 0 = Puerta cerrada      |
| Sensor de ventana 1 | 1 = Ventana abierta; 0 = Ventana cerrada    |
| Sensor de ventana 2 | 1 = Ventana abierta; 0 = Ventana cerrada    |
| Sensor de humo      | 1 = Detecta humo; 0 = No detecta humo       |
| Alarma activa       | 1 = Alarma activada; 0 = Alarma desactivada |

## 2. 💡 Salidas del sistema

El circuito deberá controlar las siguientes salidas:

|           Salida          | Funcionamiento                                                       |
|---------------------------|----------------------------------------------------------------------|
| Buzzer (alarma sonora)    | Se activa cuando algún sensor detecta una condición de alerta y la alarma está activa. También deberá contemplar las condiciones anómalas que se establezcan en el análisis del sistema. |
| Extractor de humo         | Se enciende cuando el sensor detecta humo.                                                                                                                                               |
| LED de estado             | Indica si el sistema de alarma está activado: 1 = Encendido; 0 = Apagado.                                                                                                                |
| LED indicador de sensores | Se enciende cuando al menos uno de los sensores detecta una condición de alerta: 1 = Encendido; 0 = Apagado.                                                                             |

## 3. 📝 Desarrollo del proyecto

Deberán realizar el diseño completo del sistema, siguiendo las etapas que se describen a continuación:

A) Análisis e instrucciones de funcionamiento
- Explicar con sus propias palabras cómo debe funcionar el sistema.
- Identificar las entradas y salidas.
- Describir las condiciones que activan cada salida.
- Establecer qué situaciones se consideran anómalas y cómo debe responder el sistema.

B) Tablas de verdad
- Elaborar las tablas de verdad necesarias para representar el funcionamiento de cada salida.
- Considerar todas las combinaciones posibles de las entradas.
- Identificar claramente cuándo debe activarse o desactivarse cada salida.

C) Ecuaciones booleanas y simplificación
- Obtener la ecuación booleana correspondiente a cada salida.
- Simplificar las ecuaciones mediante álgebra booleana o mapas de Karnaugh.
- Mostrar el procedimiento realizado y las agrupaciones utilizadas, cuando corresponda.

D) Diseño del circuito digital en Logisim
- Construir el circuito digital correspondiente a las ecuaciones simplificadas.
- Utilizar las compuertas lógicas necesarias.
- Identificar todas las entradas y salidas.
- Organizar el circuito de manera clara y ordenada.

E) Simulación en SimulIDE o Proteus
- Implementar el circuito diseñado en Logisim en el simulador seleccionado.
- Comprobar su funcionamiento mediante diferentes combinaciones de entradas.
- Verificar que las salidas respondan de acuerdo con las tablas de verdad.
- Incluir evidencias de la simulación y explicar los resultados obtenidos.

## 4. 📄 Estructura del reporte en PDF

El reporte deberá contener obligatoriamente los siguientes apartados:

1. Portada
   - Nombre de la institución.
   - Nombre de la asignatura.
   - Título del proyecto.
   - Nombre completo del estudiante.
   - Grupo.
   - Fecha de entrega.

2. Índice
   - Apartados y número de página correspondiente.

3. Desarrollo
   - Instrucciones y lógica de funcionamiento del sistema.
   - Identificación de entradas y salidas.
   - Tablas de verdad.
   - Ecuaciones booleanas o mapas de Karnaugh.
   - Circuito digital elaborado en Logisim.
   - Simulación en SimulIDE o Proteus. (3 pantallazos del funcionamiento)
   - Evidencias y comprobación del funcionamiento.

4. Conclusión
   - Explicar qué aprendieron durante el desarrollo.
   - Describir las dificultades que encontraron y cómo las resolvieron.
   - Explicar por qué es importante simplificar las funciones antes de implementar un circuito digital.

## 5. 📌 Indicaciones de entrega

- El reporte debe entregarse en un solo archivo PDF.
- El documento debe estar organizado, completo y ser fácil de leer.
- Las tablas, ecuaciones, mapas de Karnaugh y diagramas deben ser legibles.
- Se deben incluir evidencias del circuito y de su simulación.
- No se aceptan fotografías o documentos separados: todo debe estar integrado en un único PDF.
- NO SE ACEPTAN ARCHIVOS FUENTE, SOLO EL DOCUMENTO PDF SOLICITADO.
- Los trabajos que incluyan contenido generado mediante inteligencia artificial (IA) no serán aceptados y se calificarán con 0.

✅ Importante: No basta con presentar el circuito terminado. Se debe demostrar todo el procedimiento: análisis del problema → tablas de verdad → ecuaciones booleanas → simplificación → circuito digital → simulación y verificación.

[.](./alarma_ejercicio.circ)
