<?php
// Obtener tasas de cambio desde JAG-Media API
$API_KEY = 'jmg_tu_api_key'; // obténla en jagmedia.com.ve/cuenta.php
$BASE = 'https://api.jagmedia.com.ve';

function api_get(string $path): array {
    global $API_KEY, $BASE;
    $ch = curl_init($BASE . $path);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 10,
        CURLOPT_HTTPHEADER => ["X-API-Key: {$API_KEY}"],
    ]);
    $body = curl_exec($ch);
    if (curl_errno($ch) || curl_getinfo($ch, CURLINFO_HTTP_CODE) !== 200) {
        throw new RuntimeException('API error: ' . curl_getinfo($ch, CURLINFO_HTTP_CODE));
    }
    curl_close($ch);
    return json_decode($body, true);
}

$d = api_get('/v1/tasas');
echo "BCV USD: {$d['bcv']['USD']['promedio']}\n";
echo "P2P: " . json_encode($d['p2p'] ?? null) . "\n";

$conv = api_get('/v1/convertir?monto=10&moneda=USD&destino=VES');
echo "10 USD en VES: {$conv['resultado']}\n";
