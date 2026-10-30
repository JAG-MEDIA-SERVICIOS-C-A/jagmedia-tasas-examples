#!/bin/bash
# JAG-Media API — ejemplos cURL
API_KEY="jmg_tu_api_key"   # obténla en jagmedia.com.ve/cuenta.php
BASE="https://api.jagmedia.com.ve"

# 1. Tasas consolidadas (BCV + P2P + paralelo)
curl -s "$BASE/v1/tasas" -H "X-API-Key: $API_KEY" | jq .

# 2. Convertir 10 USD a VES
curl -s "$BASE/v1/convertir?monto=10&moneda=USD&destino=VES" -H "X-API-Key: $API_KEY" | jq .

# 3. Spread BCV vs mercado
curl -s "$BASE/v1/spread" -H "X-API-Key: $API_KEY" | jq .

# 4. Estado de las fuentes (sin auth)
curl -s "$BASE/v1/estado" | jq .

# 5. Histórico USD (plan Starter+)
curl -s "$BASE/v1/historico/USD" -H "X-API-Key: $API_KEY" | jq .

# 6. Login por JWT (alternativa a API key)
TOKEN=$(curl -s "$BASE/auth/token" -X POST -H "Content-Type: application/json" \
  -d '{"email":"tu@email.com","password":"tu_password"}' | jq -r .access_token)
curl -s "$BASE/v1/tasas" -H "Authorization: Bearer $TOKEN" | jq .
