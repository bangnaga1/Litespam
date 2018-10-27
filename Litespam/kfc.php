<?php
include 'funcKFC.php';

/*
    https://github.com/nee48/BomSmsKFC
    Made by Handika Pratama
*/

$init = new Bom();

//Eksekusi Sms Boomber
$init->no = ""; //Nomer Hp tujuan Pakai awalan 62. contoh 6281xxxxxxx
$loop = ""; //Jumlah eksekusi
for ($i=0; $i < $loop; $i++) { 
    $init->Verif($init->no);
}