# JAG-Media API — Consumption Examples

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![API](https://img.shields.io/badge/API-v1-0085B2)](https://api.jagmedia.com.ve/v1/estado)
[![Docs](https://img.shields.io/badge/Docs-jagmedia.com.ve-292D3D)](https://jagmedia.com.ve/api-docs.php)
[![🇻🇪 Español](https://img.shields.io/badge/Idioma-Español-yellow)](README.es.md)

Official integration examples for the Venezuelan exchange rates API.

**Base URL:** `https://api.jagmedia.com.ve`
**Docs:** https://jagmedia.com.ve/api-docs.php
**Sign up:** https://jagmedia.com.ve/registro.php

## Authentication

| Method | Header | Best for |
|--------|--------|----------|
| API Key | `X-API-Key: jmg_your_api_key` | scripts, backends |
| JWT | `Authorization: Bearer <token>` | session-based apps |

## Main endpoints

| Endpoint | Auth | Description |
|----------|------|-------------|
| `GET /v1/tasas` | yes | Consolidated rates: BCV + P2P + parallel |
| `GET /v1/convertir` | yes | Convert amounts between currencies |
| `GET /v1/spread` | yes | BCV vs market spread |
| `GET /v1/historico/{currency}` | yes* | History (Starter 7d · Dev/Ent 365d) |
| `GET /v1/estado` | no | Data-source health |
| `GET /bancos` | yes | Venezuelan bank rates |

## Examples by language

- [Python](python/tasas.py) — `requests`
- [JavaScript](javascript/tasas.js) — `fetch` (Node 18+)
- [PHP](php/tasas.php) — `cURL`
- [cURL](curl/ejemplos.sh) — terminal
- [Postman](postman/JAG-Media-Tasas.postman_collection.json) — importable collection

## Typical response `GET /v1/tasas`

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

---

*Documentación en español:* [README.es.md](README.es.md)
