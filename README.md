# Scrapy Web Crawler.

Utilizando el framework Scrapy, se implemento un "spider" que recorre las paginas web de forma autonoma.

Dicho recorrido se encuentra determinado por las reglas que se le definan al comportamiento del "spider".

## Concepto de Spider

Un rastreador web, indexador web, indizador web o araña web es un programa informático que inspecciona las páginas del World Wide Web de forma metódica y automatizada. Uno de los usos más frecuentes que se les da consiste en crear una copia de todas las páginas web visitadas para su procesado posterior por un motor de búsqueda que indexa las páginas proporcionando un sistema de búsquedas rápido. Las arañas web suelen ser bots.

Las arañas web comienzan visitando una lista de URL, identifica los hiperenlaces en dichas páginas y los añade a la lista de URL a visitar de manera recurrente de acuerdo a determinado conjunto de reglas. La operación normal es que se le da al programa un grupo de direcciones iniciales, la araña descarga estas direcciones, analiza las páginas y busca enlaces a páginas nuevas. Luego descarga estas páginas nuevas, analiza sus enlaces, y así sucesivamente.

## Preparación (única vez)

Requisitos previos:

Instalar Node.js:
* `sudo apt-get install -g npm`
* `sudo apt-get install node`

Instalar Grunt (opcional):
* `sudo npm install -g grunt-cli`

Tener instalado `python 3.x` y en lo posible el `virtualenv 15.x`.

## Despliegue

1. Clonar el repositorio: `https://github.com/emanuelbalcazar/scrapy-web-crawler`.
2. Cambiar de directorio: `cd scrapy-web-crawler`.
3. Activar el virtualenv: `source ./bin/activate` (opcional).
4. Cambiar al directorio: `cd scrapy-web-crawler/classifier`
5. Ejecutar: `npm run grunt install` para instalar dependencias de python3. 
6. Ejecutar: `npm run grunt crawl` para iniciar la ejecución del spider.
