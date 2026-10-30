# JAG-Media API — Ejemplos de Consumo

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![API](https://img.shields.io/badge/API-v1-0085B2)](https://api.jagmedia.com.ve/v1/estado)
[![Docs](https://img.shields.io/badge/Docs-jagmedia.com.ve-292D3D)](https://jagmedia.com.ve/api-docs.php)


Ejemplos oficiales de integración con la API de tasas de cambio venezolanas.

**Base URL:** `https://api.jagmedia.com.ve`
**Documentación:** https://jagmedia.com.ve/api-docs.php
**Crear cuenta:** https://jagmedia.com.ve/registro.php

## Autenticación

| Método | Header | Para |
|--------|--------|------|
| API Key | `X-API-Key: jmg_tu_api_key` | scripts, backend |
| JWT | `Authorization: Bearer <token>` | apps con sesión |

## Endpoints principales

| Endpoint | Auth | Descripción |
|----------|------|-------------|
| `GET /v1/tasas` | sí | Tasas consolidadas BCV + P2P + paralelo |
| `GET /v1/convertir` | sí | Conversión entre monedas |
| `GET /v1/spread` | sí | Brecha BCV vs mercado |
| `GET /v1/historico/{moneda}` | sí* | Histórico (Starter 7d · Dev/Ent 365d) |
| `GET /v1/estado` | no | Estado de fuentes |

## Ejemplos por lenguaje

- [Python](python/tasas.py) — `requests`
- [JavaScript](javascript/tasas.js) — `fetch` (Node 18+)
- [PHP](php/tasas.php) — `cURL`
- [cURL](curl/ejemplos.sh) — terminal

## Respuesta típica `GET /v1/tasas`

```json
{
  "pais": "VE",
  "base": "USD",
  "bcv": {
    "USD": { "venta": 889.2553, "compra": 889.2553, "promedio": 889.2553, "fuente": "BCV" },
    "EUR": { "venta": 982.7589, "promedio": 982.7589 }
  },
  "p2p": { "binance_ves": 998.5 },
  "paralelo": 1008.49
}
```
