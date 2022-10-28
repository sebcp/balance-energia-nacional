# Análisis del balance de energía nacional
Este repositorio se creó con la finalidad de analizar el consumo de energía en Chile utilizando Python y librerías afines. Para eso se tomaron los [datos abiertos dispuestos por la Comisión Nacional de Energía relacionados al balance energético](http://energiaabierta.cl/categorias-estadistica/electricidad).
Originalmente se pensó trabajar con los distintos archivos en formato Excel que contienen información relacionada a la generación, consumo y distribución de energía en Chile desde el año 1991 hasta el año 2020. Debido a que los formatos no están estandarizados y que existen distintos tipos de energías que fueron siendo incluidas en las estadísticas medidas a medida que avanzó el tiempo, se optó por trabajar con el archivo CSV dispuesto con información estandarizada sobre el consumo energético entre los años 2008 y 2020.

## Preprocesamiento
Preliminarmente se consideran cuatro categorías importantes a nivel nacional en términos de consumo energético:
* Minería (Que engloba todo lo relacionado a la extracción y procesamiento del cobre, salitre, hierro y otros minerales no especificados)
* Industria (Que engloba las industrias de papel y celulosa, siderurgia, petroquímica, cemento, azúcar, pesca y otros tipos no especificados)
* Transporte (Que engloba el transporte terrestre común, el transporte ferroviario, el transporte marítimo y el transporte aéreo)
* Consumo no industrial (Que engloba el consumo energético de las áreas comercial, pública, residencial y sanitaria)

Para preprocesar los datos se utilizó la librería Pandas, con la cual se segmentaron los datos en distintos CSVs, creando nuevos archivos separados que contienen el año, el tipo de energético del que proviene la energía y la cantidad de energía consumida en teracalorías para cada categoría. También se generó un CSV con el consumo total por categoría a través de los años.

## Visualización
Antes de generar un análisis utilizando (TBD), se realizaron visualizaciones para poder ganar una intuición de cómo ha evolucionado el consumo energético nacional por categoría de forma más detallada y cómo ha variado el consumo total por categoría de forma general a través del tiempo.

## Análisis
(TBD)