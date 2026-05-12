
#!/bin/bash

IMAGEN_NOMBRE="football-stats"
CONTENEDOR_APY_NOMBRE="samplerunning"

echo "================================================"
echo "  Football Stats CLI - Automatizacion Docker"
echo "================================================"

echo ">> [1/3] Generando Dockerfile..."
cat > Dockerfile <<EOF
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
ENV SPORTSDB_API_KEY=123
ENV SPORTSDB_LEAGUE="English Premier League"
CMD ["python", "app.py"]
EOF

echo "   Dockerfile generado."

echo ">> [2/3] Construyendo imagen Docker..."
docker build -t $IMAGEN_NOMBRE .
echo "   Imagen construida."

echo ">> [3/3] Ejecutando contenedor..."
docker run --name $CONTENEDOR_APY_NOMBRE \
  -e SPORTSDB_API_KEY=123 \
  -e SPORTSDB_LEAGUE="English Premier League" \
  $IMAGEN_NOMBRE

echo "================================================"
echo "  Proceso completado."
echo "================================================"
