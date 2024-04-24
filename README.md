# MACHINE LEARNING SAMUR
Este proyecto tiene como objetivo realizar una predicción utilizando los datos de las activaciones sdel SAMUR que proporicona el ayuntameinto de Madrid y redes neuronales.

## Guía de instalación
Para poder utilizar este código, lo primero que hay que hacer es clonar el repositorio.
```bash
git clone https://github.com/Araaancg/machine-learning-SAMUR
```

Este proyecto está desarrollado en Python y utiliza librerías externas, por lo que para una buena práctica será necesario crear un entorno virtual.

```bash
python -m venv venv
```

Para activarlo ejecutamos el siguiente comando
```bash
source venv/Scripts/activate
```

Una vez activado seguramaente aparezca un "(venv)" en la terminal. Ahora está el entorno listo para poder instalar los requerimientos de la aplicación. En total son:

1. **chardet==5.2.0**: Chardet es una biblioteca que detecta la codificación de caracteres de un texto. Es útil cuando se trabaja con datos de texto de múltiples fuentes y se necesita determinar la codificación para su correcto procesamiento.

2. **numpy==1.26.4**: NumPy es una biblioteca fundamental para la computación científica en Python. Proporciona soporte para matrices y operaciones matemáticas de alto nivel, lo que la hace ideal para el procesamiento de datos numéricos, incluyendo manipulaciones de matrices, álgebra lineal, generación de números aleatorios, y más.

3. **pandas==2.2.2**: Pandas es una biblioteca de Python que proporciona estructuras de datos y herramientas de análisis de datos de alto rendimiento. Es especialmente útil para trabajar con datos tabulares y de series temporales, permitiendo la manipulación, limpieza, agregación y análisis de datos de manera eficiente.

4. **python-dateutil==2.9.0.post0**: Python-dateutil es una extensión de la biblioteca estándar de Python para manejar fechas y horas de una manera más conveniente. Proporciona funcionalidades para analizar y manipular fechas y horas en diversos formatos, así como la conversión entre zonas horarias.

5. **pytz==2024.1**: pytz es una biblioteca de Python que proporciona funcionalidades para trabajar con zonas horarias. Permite la conversión entre diferentes zonas horarias, el manejo de horarios de verano y horarios estándar, y otras operaciones relacionadas con la gestión del tiempo.

6. **six==1.16.0**: Six es una biblioteca que proporciona herramientas para escribir código Python compatible con versiones tanto de Python 2 como de Python 3. Facilita la transición entre las dos versiones del lenguaje y ayuda a mantener la compatibilidad entre ellas.

7. **tzdata==2024.1**: tzdata es una biblioteca que contiene datos de zonas horarias utilizados por varios sistemas y aplicaciones para manejar la información sobre la hora local y las zonas horarias en todo el mundo.

Para poder instalarlos, se puede ejectuar el siguiente comando.
```bash
pip install -r requirements.txt
```

Para poder desactivar el entorno virtual cuando se termine con el código, se puede ejecutar el siguiente comando.
```bash
deactivate
```