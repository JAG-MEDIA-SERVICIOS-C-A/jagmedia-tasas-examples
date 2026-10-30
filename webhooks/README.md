# Webhooks

Recibe `rate.*.updated` o `*` cuando las tasas cambian (plan Developer/Enterprise).

1. `receptor.py` — servidor que **verifica la firma HMAC** `X-Signature-256`
2. `registrar.sh` — crear/listar/probar el webhook por API

El `secret` se muestra una sola vez al crear. Sin firma válida → 401.
