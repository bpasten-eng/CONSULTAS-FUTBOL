
=============
USO DE LA API
=============

=============================
CONSULTAS-FUTBOL
=============================

Stakeholder
Analista deportivo que necesita consultar datos de equipos
de fútbol de forma rápida sin depender de sitios web.

Problema / Solución
Un analista pierde tiempo buscando información básica de equipos
en distintos sitios. Esta herramienta consulta la API de TheSportsDB
y muestra los datos directamente en consola con un solo comando.


¿Qué necesito para usarlo?
Docker instalado
Git instalado
Conexión a internet

¿Cómo lo uso?

1. Descargar el proyecto
    git clone https://github.com/bpasten-eng/CONSULTAS-FUTBOL.git
cd CONSULTAS-FUTBOL

2. Dar permisos al script
    chmod +x build.sh

3. Definir la clave de la API
    export SPORTSDB_API_KEY="123"

Esta variable le entrega la clave de TheSportsDB al sistema.
El script la lee desde aquí, nunca está escrita dentro del código.

4. Ejecutar
    ./build.sh

Esto construye la imagen Docker, ejecuta el contenedor y
consulta la API automáticamente.

5. Resultado esperado
FOOTBALL STATS CLI
Liga consultada : English Premier League
1  Arsenal       1892  Emirates Stadium
2  Aston Villa   1874  Villa Park
Consulta completada exitosamente.
----------------------------------

Variables de Entorno
Variable	Descripción	Valor
SPORTSDB_API_KEY	Clave de la API	123
SPORTSDB_LEAGUE	Liga a consultar	English Premier League


API Utilizada
Nombre: TheSportsDB
URL: https://www.thesportsdb.com
Autenticación: API Key por variable de entorno
