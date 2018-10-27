"<?php
echo "Author : Bang Naga";
echo "Informasi Lebih Lanjut : https://github.com/bangnaga1";
echo "List Tools :\n[1]TOKOPEDIA\n[2]TELKOMSEL\n[3]MATAHARI MALL\n[4]PHD\n[5]JD.ID\n[6]WHATSAPP\n[7]HOOQ\n[8]KFC\n[9]WHISKAS\n[10]ZIPAY\n[11]LAZADA\n[12]KELUAR\nMasukan Pilihanmu (1-11) : ";
$pilih = trim(fgets(STDIN));
if($pilih>11 OR $pilih<1){
    echo "Pilihan Tidak ada, silahkan pilih yang ada!\nMasukan Pilihanmu : ";
    $pilih = trim(fgets(STDIN));
    if($pilih>11 OR $pilih<1) $type = "carina";
}
if($pilih==1){
    $type = "1";
    $n = "WHISKAS";
}elseif($pilih==2){
    $type = "2";
    $n = "TELKOMSEL";
}elseif($pilih==3){
    $type = "3";
    $n = "MATAHRI MALL";
}elseif($pilih==4){
    $type = "4";
    $n = "PHD";
}elseif ($pilih==5){
    $type = "5";
    $n = "JD.ID";
}elseif ($pilih==6){
    $type = "wa";
    $n = "WHATSAPP";
}elseif ($pilih==7){
    $type = "hooq";
    $n = "HOOQ";
}elseif ($pilih==8){
    $type = "kfc";
    $n = "KFC";
}elseif ($pilih==9){
    $type = "whiskas1";
    $n = "WHISKAS";
}elseif ($pilih==10){
    $type = "zipay2";
    $n = "ZIPAY";
}elseif ($pilih==11){
    $type = "lazada";
    $n = "LAZADA";
}elseif ($pilih==12){
    $type = "exit";
    $n = "KELUAR";
}
if($type=="carina"){
    echo "Kamu Tidak Memilih Tools Manapun.\n";
}else{
    echo "Kamu Telah Memilih Tools $n , Silahkan Tekan Enter untuk Melanjutkan..";
    $lanjut = trim(fgets(STDIN));
    require_once($type.".php");
}