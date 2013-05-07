<?php

$address = $_GET['address'];

$url  = 'https://maps.googleapis.com/maps/api/geocode/json?address='.urlencode($address).'&sensor=true';
 
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_FAILONERROR, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $data = curl_exec($ch);
    curl_close($ch);
$output = json_decode($data);

if($output->status == 'OK')
{
 $gps = $output->results[0]->geometry->location;
}
else
{
	echo $data;
}

echo json_encode($gps);
?>
