# Patrones de Diseño - Repositorio Académico

Este repositorio está pensado como un laboratorio práctico para estudiar y aplicar los patrones de diseño más importantes del desarrollo de software. Aquí se irán desarrollando ejemplos, implementaciones y ejercicios a medida que avancemos en las clases de la universidad, con el objetivo de comprender no solo la teoría, sino también cómo se aplican en proyectos reales.

## Objetivo del proyecto

El propósito principal es crear una colección organizada de implementaciones de patrones de diseño en Python, con ejemplos claros, modularizados y fáciles de entender. Cada patrón se desarrollará de forma progresiva para reforzar conceptos como:

- reutilización de código
- mantenibilidad del sistema
- escalabilidad y extensibilidad
- separación de responsabilidades
- diseño orientado a objetos

## ¿Qué se encontrará aquí?

Este repositorio servirá como portafolio y material de estudio para todos los patrones de diseño que se vayan viendo en la carrera. Algunos de ellos que se irán incorporando en el tiempo son:

- Factory Method
- Abstract Factory
- Singleton
- Builder
- Prototype
- Adapter
- Facade
- Decorator
- Strategy
- Observer
- Composite
- State
- Template Method
- Proxy
- Command
- etc.

La idea es que cada patrón se implemente en un módulo o carpeta independiente, con ejemplos concretos y documentación breve para explicar su uso, ventajas y estructura.

## Estructura del repositorio

```text
patrones_software/
│
├── README.md
├── factory/
│   ├── base.py
│   └── roomies_con_factory/
│       ├── main.py
│       ├── models/
│       │   ├── apartamento.py
│       │   ├── casa.py
│       │   ├── habitacion.py
│       │   ├── inmueble.py
│       │   └── factory/
│       │       ├── apartamento_factory.py
│       │       ├── casa_factory.py
│       │       ├── habitacion_factory.py
│       │       └── inmueble_factory.py
│       └── service/
│           └── servicio_arriendo.py
│
├── roomies_sin_factory/
│   ├── main.py
│   ├── models/
│   └── service/
│
└── uml/
```

## Estado actual

Actualmente el repositorio ya incluye ejemplos iniciales relacionados con el patrón Factory Method y comparaciones entre una implementación con fábrica y otra sin fábrica. Este tipo de ejercicios permite observar la diferencia entre:

- un diseño más rígido y acoplado
- un diseño más modular y extensible
- una solución que facilita futuras ampliaciones del sistema

## Filosofía del proyecto

Este repositorio no busca ser solo una colección de archivos aleatorios, sino una guía de aprendizaje progresiva. Cada patrón se agregará a medida que avance la universidad y el curso, de tal forma que se convierta en:

- un espacio de práctica
- una referencia para estudiar
- un proyecto de crecimiento continuo
- un ejemplo real de aplicación de principios de diseño

## Cómo usar este repositorio

1. Revisar cada carpeta según el patrón o ejercicio que se esté estudiando.
2. Leer la lógica de las clases y la relación entre ellas.
3. Comparar diferentes implementaciones para entender ventajas y desventajas.
4. Probar ejecutar los ejemplos para observar el comportamiento real.
5. Extender o refactorizar los modelos cuando se quiera practicar más.

## Objetivo académico

La finalidad es que, al final del curso, este repositorio contenga una biblioteca de ejemplos de patrones de diseño y sirva como evidencia del aprendizaje adquirido en clase, lo que lo convierte en un proyecto técnico y didáctico al mismo tiempo.

## Nota

Este proyecto va en crecimiento constante. Cada nueva clase, ejercicio o patrón agregado se reflejará en el repositorio para mantenerlo actualizado con el proceso académico.

---

Desarrollado como proyecto de estudio de patrones de diseño en Python, con enfoque académico y evolución continua.