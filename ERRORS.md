# Respuestas de error reales

La API responde errores estándar JSON con `detail`. Capturados en vivo.

| Código | Cuándo | Ejemplo |
|--------|--------|---------|
| `401` | Sin `X-API-Key`/`Bearer` | [`samples/error_401.json`](samples/error_401.json) |
| `403` | Plan insuficiente (ej. histórico en Free) | `{"detail": "Requiere plan Starter o superior"}` |
| `422` | Parámetro inválido | [`samples/error_422.json`](samples/error_422.json) |
| `429` | Rate limit excedido | `{"detail": "Rate limit excedido. Retry-After: N"}` |
| `503` | Método de pago deshabilitado (PayPal) | `{"detail": "Pago con PayPal no está disponible"}` |
