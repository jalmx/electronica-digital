---
create_index: true
title: "Práctica 9 - Sistema de alarma"

---

# Práctica 8 - Sistema de alarma [Equipo]

## Objetivo

Aplicar los conocimientos de sistemas digitales de control a un sistema de seguridad básico


## Material

| Cantidad | Nombre                  | Descripción   |
| -------- | ----------------------- | ------------- |
| 1        | Multímetro              | Voltímetro    |
| x        | IC 7404                 | Compuerta     |
| x        | IC 7408                 | Compuerta     |
| x        | IC7432                  | Compuerta     |
| x        | Led                     |               |
| 1        | Resistencias 330        |               |
| 2        | Resistencias 1k         |               |
| 1        | Sensor de presencia     | Sensor PIR    |
| 1        | Buzzer                  | Buzzer activo |
| 1        | Dipswitch o push button |               |

## Desarrollo

### Filosofía de operación

Tenemos la siguiente arquitectura, y se debe desarrollar el circuito de control para lograrlo:

![arq](../../assets/arquitectura_alarma.png)

Las condiciones para que se activen los actuadores con base a los sensores son:

1. Si existe presencia, hay un obstáculo y no hay luz, se debe activar el buzzer, el cual indica que hay una presencia en el lugar. Y apagara el led de OK, encender la lámpara.
2. Si no hay luz, ni obstáculo y si hay presencia, se debe encender la lámpara, y estar el led OK encendido, el buzzer apagado
3. Si hay obstáculo, no hay luz y ni presencia, se activa el buzzer, se apaga el led OK, y la lámpara se enciende.
4. Hay luz, la lámpara se debe estar apagada. El resto de sensores no importan.
5. Si no hay presencia, ni obstáculo, el led de OK debe estar encendido
6. Si no hay presencia, ni obstáculo, el buzzer debe estar apagado.
7. Si hay obstáculo, se debe activar el buzzer
8.  Si no hay obstáculo, se debe encender el led de OK

## Diseño

Con base a la información anterior, desarrollar el circuito, haciendo uso de la técnica de Algebra o Mapa de Karnaugh. Obtén la tabla de verdad y realiza los pasos necesarios para generar tu circuito de control digital e implementalo.

|  PIR  | Obstáculo |  Luz  | Buzzer/LED | Lámpara | LED |
| :---: | :-------: | :---: | ---------- | ------- | --- |
|   0   |     0     |   0   |            |         |     |
|   0   |     0     |   1   |            |         |     |
|   0   |     1     |   0   |            |         |     |
|   0   |     1     |   1   |            |         |     |
|   1   |     0     |   0   |            |         |     |
|   1   |     0     |   1   |            |         |     |
|   1   |     1     |   0   |            |         |     |
|   1   |     1     |   1   |            |         |     |
