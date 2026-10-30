// Obtener tasas de cambio desde JAG-Media API (Node 18+ o browser)
const API_KEY = "jmg_tu_api_key"; // obténla en jagmedia.com.ve/cuenta.php
const BASE = "https://api.jagmedia.com.ve";

async function tasas() {
  const r = await fetch(`${BASE}/v1/tasas`, {
    headers: { "X-API-Key": API_KEY }
  });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json();
}

async function convertir(monto, origen = "USD", destino = "VES") {
  const r = await fetch(
    `${BASE}/v1/convertir?monto=${monto}&moneda=${origen}&destino=${destino}`,
    { headers: { "X-API-Key": API_KEY } }
  );
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json();
}

const d = await tasas();
console.log(`BCV USD: ${d.bcv.USD.promedio}`);
console.log(`P2P:`, d.p2p);
console.log(`10 USD en VES: ${(await convertir(10)).resultado}`);
