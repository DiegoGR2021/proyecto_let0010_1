# Datos
Datos para el proyecto del ramo LET0010-1

Esta carpeta contiene las bases de datos a utilizar en el proyecto:

* 1 - Tenemos las rentabilidades reales de los fondos de pensiones, las cuales fueron extraídas mediante web-scraping desde 
el sitio web de la superintendencia de pensiones (https://www.spensiones.cl/apps/rentabilidad/getRentabilidad.php?tiprent=FP), el proceso
de procesamiento de los datos, se realizó en conjunto con la extracción, usando Python y diversos paquetes (Pandas, Requests, Selenium), y
debido a su método, el código podría dejar de funcionar a medida que se actualice la página.

* 2 - También disponemos del valor del dólar en clp, del período 2014-2022, estos datos fueron descargados desde la base de datos estadísticos
del banco central de chile, pueden ser encontrados en (https://si3.bcentral.cl/siete). Estos archivos fueron procesados en Python, para ajustar
la cantidad de datos, y convertirlos a un formato de series de tiempo adecuados, se utilizó principalmente Pandas para procesar.

* 3 - La carpeta datos_sin_procesar, contiene versiones previas de los datos del dólar, ya que para su obtención, no podía descargarlos todos
directamente, por lo que fueron agrupados en una sola tabla mediante código.