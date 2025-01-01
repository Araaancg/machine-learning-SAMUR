# Análisis de Incidencias de Emergencia en la Comunidad de Madrid

Este repositorio corresponde a un proyecto final para MSMK University Unidad 25 - Machine Learning en el Grado Profesional de Applied Computing y IA. La nota final fue 'Distinction'.

## Overview

Este proyecto tiene como objetivo aplicar técnicas de machine learning para analizar las operaciones de SAMUR y Protección Civil en la Comunidad de Madrid, utilizando datos de emergencias en los distritos de la ciudad. El análisis se enfoca en identificar patrones en las activaciones de recursos mediante un enfoque de **Análisis de Componentes Principales (PCA)** y **Análisis de Clusters** con el algoritmo **K-means**. 

Los datos provienen de archivos CSV que incluyen registros de activaciones de emergencias y datos de los distritos de Madrid. El análisis busca descubrir patrones y tendencias en las operaciones, agrupando la información por distrito y tipo de incidencia.


## Tecnologías y Lenguajes

- **Lenguajes**: Python
- **Bibliotecas**: 
  - lubridate
  - tibble
  - dplyr
  - factoextra
  - ggplot2
  - cluster
- **IDE**: RStudio
- 

## Key Features

- Análisis no supervisado utilizando **cluster**.
- Análisis de los datos de emergencias agrupados por **distritos** y **códigos de incidencia**.
- Preprocesamiento de datos, incluyendo limpieza, transformación y reducción de dimensionalidad mediante **PCA**.
- Visualización de resultados utilizando **ggplot2** y **cluster**.
- Resultados y conclusiones detalladas en un archivo PDF adjunto.


## Instalación y Ejecución

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   ```
2. Para poder ver el código fuente, abrir los archivos .Rmd con RStudio.
3. Para poder visualizar el proyecto de una forma más formal, abrir con el navegador los archivos nb.html.


## Detectar Codificación de Archivos
Al ser archivos externos, cuando los importamos en R tenemos que tener en cuenta la codificación que pueden tener. En este caso, hay un archivo adicional en el repositorio que se llama `detectEncoding.py` que contiene un pequeño programa que retorna las codificaciones de los archivos utilizados.
