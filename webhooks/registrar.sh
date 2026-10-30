#!/bin/bash
# Registrar y probar webhook
API_KEY="jmg_tu_api_key"
BASE="https://api.jagmedia.com.ve"

# Crear (Developer/Enterprise) → guarda el 'secret' de la respuesta
curl -s "$BASE/v1/webhooks" -X POST \
  -H "X-API-Key: $API_KEY" -H "Content-Type: application/json" \
  -d '{"url":"https://tu-dominio.com/hook","events":["*"]}' | jq .

# Listar
curl -s "$BASE/v1/webhooks" -H "X-API-Key: $API_KEY" | jq .

# Disparar un evento de prueba
curl -s "$BASE/v1/webhooks/ID/deliver/test" -X POST -H "X-API-Key: $API_KEY" | jq .
