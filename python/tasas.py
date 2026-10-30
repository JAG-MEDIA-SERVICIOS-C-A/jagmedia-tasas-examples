"""Obtener tasas de cambio desde JAG-Media API."""
import requests

API_KEY = "jmg_tu_api_key"  # obténla en jagmedia.com.ve/cuenta.php
BASE = "https://api.jagmedia.com.ve"


def tasas() -> dict:
    """GET /v1/tasas — consolidado BCV + P2P + paralelo."""
    r = requests.get(f"{BASE}/v1/tasas",
                     headers={"X-API-Key": API_KEY}, timeout=10)
    r.raise_for_status()
    return r.json()


def convertir(monto: float, origen: str = "USD", destino: str = "VES") -> dict:
    """GET /v1/convertir — convertir monto entre monedas."""
    r = requests.get(f"{BASE}/v1/convertir",
                     params={"monto": monto, "moneda": origen, "destino": destino},
                     headers={"X-API-Key": API_KEY}, timeout=10)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    d = tasas()
    print(f"BCV USD: {d['bcv']['USD']['promedio']}")
    print(f"P2P:     {d.get('p2p', {})}")
    print(f"10 USD en VES: {convertir(10)['resultado']}")
