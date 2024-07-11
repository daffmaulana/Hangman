import random as rd
import string
import os as os
import time

setKata = [
['Anggur', 'Apel', 'Alpukat', 'Arbei', 'Tin', 'Asam', 'kolangkaling', 'Aprikot', 'Belimbing', 'Kelapa', 'Kiwi', 'Stroberi', 'Pisang', 'Semangka', 'ceri', 'lemon', 'Nanas', 'Jeruk', 'delima', 'Blackberry', 'Blueberry', 'Coklat', 'sukun', 'blewah', 'Jambu', 'Durian', 'Duku', 'nipis', 'Kedondong', 'Kesemek', 'Kismis', 'Labu', 'Leci', 'Lengkeng', 'Mangga', 'Melon', 'Mengkudu', 'Mentimun', 'Nangka', 'Pepaya', 'pir', 'Salak', 'Sawo', 'Sirsak', 'Tomat', 'Srikaya', 'Buah Naga', 'Lobak', 'Bengkoang', 'persik', 'Singkong', 'Cempedak', 'Kurma', 'Terong', 'Matoa', 'Rambutan', 'Manggis', 'Markisa', 'Jamblang'],
['Kera', 'Babon', 'Luwak', 'Kelelawar', 'Beruang', 'Lebah', 'Kumbang', 'Burung', 'Bison', 'Babi', 'Kucing', 'Banteng', 'Bulldog', 'Kupukupu', 'Rajawali', 'Unta', 'Kenari', 'Kasuari', 'Kucing', 'Ulat', 'Lele', 'Kelabang', 'Bunglon', 'Cheetah', 'Ayam', 'Simpanse', 'Tupai', 'Kerang', 'Tongkol', 'kobra', 'Kakatua', 'Kecoa', 'Keong', 'Sapi', 'Kepiting', 'Bangau', 'Jangkrik', 'Buaya', 'Gagak', 'Rusa', 'Anjing', 'LumbaLumba', 'Keledai', 'Dara', 'Capung', 'Bebek', 'Elang', 'Belut', 'Gajah', 'Rusa', 'Burung', 'Elang', 'kunangkunang', 'Ikan', 'Flamingo', 'Kutu', 'Lalat', 'Laron', 'Rubah', 'Katak', 'Cicak', 'Jerapah', 'Kambing', 'Angsa', 'Belalang', 'Penyu', 'Kerapu', 'Belibis', 'Marmot', 'Camar', 'Hamster', 'Landak', 'Bangau', 'Cupang', 'Kuda', 'Kuda', 'Kolibri', 'Elang', 'Hiena', 'Iguana', 'Jaguar', 'Monyet', 'Uburubur', 'Kanguru', 'Koala', 'Komodo', 'Kepik', 'Lutung', 'Lintah', 'Kera', 'Macan', 'Kutu', 'Singa', 'Kadal', 'Llama', 'Lobster', 'Makaw', 'Belatung', 'Murai', 'Maleo', 'Mamut', 'Belalang', 'Bandeng', 'Luwak', 'Biawak', 'Monyet', 'Uburubur', 'Nyamuk', 'Kancil', 'Tikus', 'Kadal', 'Hiu', 'Ocelot', 'Gurita', 'OrangUtan', 'unta', 'Berangberang', 'Kerbau', 'Kumbang', 'Panda', 'Harimau', 'Beo', 'Merak', 'Pelikan', 'Babi', 'Merpati', 'Platipus', 'Beruang', 'Landak', 'piton', 'Puyuh', 'Kelinci', 'Tikus', 'Badak', 'Salamander', 'Sarden', 'Kalajengking', 'camar', 'Hiu', 'Domba', 'Udang', 'Kukang', 'Siput', 'Ular', 'Kakap', 'Labalaba', 'Cumicumi', 'Tupai', 'pari', 'Angsa', 'Kecebong', 'Tarantula', 'Mujair', 'Rayap', 'Harimau', 'Kodok', 'Kurakura', 'tuna', 'Kalkun', 'Penyu', 'Perkutut', 'Tawon', 'Musang', 'Paus', 'Serigala', 'pelatuk', 'Cacing', 'Zebra'], 
['terong', 'paprika', 'tomat', 'kentang', 'jagung', 'wortel', 'jamur', 'bawang', 'lobak', 'pete', 'kol', 'brokoli', 'Seledri', 'Cabai', 'peterseli', 'asparagus', 'timun', 'bayam', 'kacang', 'kubis', 'Lada', 'selada', 'polong', 'labu', 'mint', 'bit', 'jahe', 'sawi', 'singkong', 'pare', 'tauge', 'mete', 'buncis', 'kedelai', 'rebung', 'kemangi', 'kecambah', 'kangkung', 'kucai', 'ketela'],
['Amerika', 'Tiongkok', 'Jepang', 'Jerman', 'India', 'Prancis', 'Italia', 'Kanada', 'Korea', 'Rusia', 'Brasil', 'Australia', 'Spanyol', 'Meksiko', 'Indonesia', 'Belanda', 'Swiss', 'Turki', 'Arab', 'Taiwan', 'Polandia', 'Swedia', 'Belgia', 'Thailand', 'Venezuela', 'Austria', 'Nigeria', 'Irlandia', 'Argentina', 'Mesir', 'Norwegia', 'Filipina', 'Arab', 'Denmark', 'HongKong', 'Singapura', 'Malaysia', 'Bangladesh', 'Kolombia', 'Vietnam', 'Finlandia', 'Pakistan', 'Chili', 'Rumania', 'Ceko', 'Portugal', 'Iran', 'Peru', 'Yunani', 'Kazakhstan', 'Irak', 'Hongaria', 'Ukraina', 'Qatar', 'Maroko', 'Kuba', 'Kuwait', 'PuertoRiko', 'Kenya', 'Ekuador', 'SriLanka', 'Myanmar', 'Dominika', 'Oman', 'Bulgaria', 'Ghana', 'KostaRika', 'Belarus', 'Uzbekistan', 'Kroasia', 'Panama', 'Uruguay', 'Serbia', 'Kongo', 'Turkmenistan', 'Yordania', 'Azerbaijan', 'Tunisia', 'Kamerun', 'Suriah', 'Uganda', 'Bolivia', 'Paraguay', 'Nepal', 'Lebanon', 'Kamboja', 'Libya', 'Senegal', 'ElSalvador', 'Islandia', 'Yaman', 'Sudan', 'Afganistan', 'Bosnia', 'Laos', 'Zimbabwe', 'Guinea', 'Mozambik', 'Jamaika', 'Niger', 'Mongolia', 'Madagaskar', 'Armenia', 'Brunei', 'Moldova', 'Kongo', 'Tajikistan', 'Kirgizstan', 'Somalia', 'Monako', 'Liberia', 'Greenland', 'Suriname']
]

stickman = {
0: """
    ┏━━━━━━━━━━┓
    ┃ ╱        │
    ┃╱        (-)
    ┃         /│\\
    ┃          │
    ┃         / \\
    ┃
""",
1: """
    ┏━━━━━━━━━━┓
    │ ╱        │
    │╱        (@)
    │         \│/
    │          │
    │
    │
""",
2: """
    ┏━━━━━━━━━━┓
    │ ╱        │ 
    │╱        (@)
    │         \│/
    │          
    │
    │
""",
3: """
    ┏━━━━━━━━━━┓
    │ ╱        │ 
    │╱        (@)
    │         \│/
    │          
    │
    │
""",
4: """
    ┏━━━━━━━━━━┓
    │ ╱        │ 
    │╱        (@)
    │          
    │          
    │
    │
""",
5: """
    ┏━━━━━━━━━━┓
    │ ╱        │
    │╱        
    │          
    │          
    │
    │
""",
6: """
    ┏━━━━━━━━━━┓
    │ ╱        
    │╱        
    │          
    │          
    │
    │
""",
7: """
    ┏━━━━━━━━━━┓
    │         
    │        
    │          
    │          
    │
    │
""",
99: """
    ┏━━━━━━━━━━┓
    │          
    │
    │         (@) 
    │         \│_  Terima kasih sudah menyelamatkanku!
    │          │
    │         / \\
"""
}

countdownNumber = {
0: '''
 333333333333333   
3:::::::::::::::33 
3::::::33333::::::3
3333333     3:::::3
            3:::::3
            3:::::3
    33333333:::::3 
    3:::::::::::3  
    33333333:::::3 
            3:::::3
            3:::::3
            3:::::3
3333333     3:::::3
3::::::33333::::::3
3:::::::::::::::33 
 333333333333333   
''',
1:'''
 222222222222222    
2:::::::::::::::22  
2::::::222222:::::2 
2222222     2:::::2 
            2:::::2 
            2:::::2 
         2222::::2  
    22222::::::22   
  22::::::::222     
 2:::::22222        
2:::::2             
2:::::2             
2:::::2       222222
2::::::2222222:::::2
2::::::::::::::::::2
22222222222222222222
''',
2:'''
   1111111111   
  1:::::::::1   
 1::::::::::1   
 111111:::::1   
       1::::1   
       1::::1   
       1::::1   
       1::::l   
       1::::l   
       1::::l   
       1::::l   
       1::::l   
11111111::::11111111
1::::::::::::::::::1
1::::::::::::::::::1
11111111111111111111
'''
}

def hangman_guest():
    cari_kategori()
    kata = cari_kata(listKategori)
    hurufPenyusunKata = set(kata)
    alfabet = set(string.ascii_uppercase)
    hurufTerpakai = set()
    nyawa = 7

    countdown()
    while len(hurufPenyusunKata) > 0 and nyawa > 0:
        print("Nyawa: ", "\u2764\uFE0F  "*nyawa, "(", nyawa, ")")
        print("Huruf yang sudah kamu gunakan: ", " ".join(hurufTerpakai))

        list_huruf = [huruf if huruf in hurufTerpakai else "-" for huruf in kata]
        print(stickman[nyawa])
        print("Kategori kata: ", kategori)
        print("\nKata: ", " ".join(list_huruf))

        userInput = input("Masukkan huruf: ").upper()
        if userInput in alfabet - hurufTerpakai:
            hurufTerpakai.add(userInput)
            if userInput in hurufPenyusunKata:
                hurufPenyusunKata.remove(userInput)
                os.system('cls')
                print("YAY! Huruf \"" + userInput + "\" yang kamu masukkan betul\n")
            else:
                nyawa -= 1
                os.system('cls')
                print("YAH! Huruf \"" + userInput + "\" yang kamu masukkan salah\n")

        elif userInput in hurufTerpakai:
            os.system('cls')
            print("Huruf \"" + userInput + "\" telah dimasukkan. Masukkan huruf yang lain!\n")
        else:
            os.system('cls')
            print("Masukan tidak valid! Masukkan huruf abjad [A-Z]\n")

    if nyawa == 0:
        print(stickman[nyawa])
        print("Kamu kalah. Kata yang dimaksud adalah \""+kata+"\".\n")
        
    else:
        print(stickman[99])
        print("Kamu berhasil menebak kata\033[1;3m", kata, "\033[0m!!!\n")
    print("\nKamu ingin bermain lagi?")
    print("Iya\t[1]\nTidak\t[any]")
    play = input("> Pilih menu\t: ").upper()
    os.system('cls')
    if play == "1": 
        hangman_guest()
    else:
        print("\nTerima kasih telah bermain\nSampai jumpa di lain waktu!")

def cari_kategori():
    global listKategori
    global indexKategori
    global kategori
    listKategori = rd.choice(setKata)
    indexKategori = setKata.index(listKategori)
    if indexKategori == 3:
        kategori = "Negara"
    elif indexKategori == 2:
        kategori = "Sayur"
    elif indexKategori == 1:
        kategori = "Hewan"
    else:
        kategori = "Buah"

def cari_kata(listKategori):
    kata = rd.choice(listKategori)
    while '-' in kata or " " in kata:
        kata = rd.choice(listKategori)
        
    return kata.upper()

def hangman():
    cari_kategori()
    indexPemain = nama.index(Username)
    kata = cari_kata(listKategori)
    hurufPenyusunKata = set(kata)
    alfabet = set(string.ascii_uppercase)
    hurufTerpakai = set()
    nyawa = 7
   
    while len(hurufPenyusunKata) > 0 and nyawa > 0:
        print("Nyawa: ", "\u2764\uFE0F  "*nyawa, "(", nyawa, ")") 
        print("Huruf yang sudah kamu gunakan: ", " ".join(hurufTerpakai))

        list_huruf = [huruf if huruf in hurufTerpakai else "-" for huruf in kata]
        print(stickman[nyawa])
        print("Kategori kata: ", kategori)
        print("\nKata: ", " ".join(list_huruf))
        userInput = input("Masukkan huruf: ").upper()
        if userInput in alfabet - hurufTerpakai:
            hurufTerpakai.add(userInput)
            if userInput in hurufPenyusunKata:
                hurufPenyusunKata.remove(userInput)
                os.system('cls')
                print("YAY! Huruf \"" + userInput + "\" yang kamu masukkan betul\n")
            else:
                nyawa -= 1
                os.system('cls')
                print("YAH! Huruf \"" + userInput + "\" yang kamu masukkan salah\n")

        elif userInput in hurufTerpakai:
            os.system('cls')
            print("Huruf \"" + userInput + "\" telah dimasukkan. Masukkan huruf yang lain!\n")
        else:
            os.system('cls')
            print("Masukan tidak valid! Masukkan huruf abjad [A-Z]\n")

    if nyawa == 0:
        print(stickman[nyawa])
        print("Kamu kalah. Kata yang dimaksud adalah \""+kata+"\".\n")
        poin[indexPemain] -= 1
        if poin[indexPemain] <= 0:
            poin[indexPemain] = 0
        
    else:
        print(stickman[99])
        print("Kamu berhasil menebak kata \""+kata+"\"!\n")
        poin[indexPemain] += 1
    sort()
    restart()

def restart():
    print("\n"+ Username +  " ingin bermain lagi?")
    print("Iya\t[1]\nTidak\t[2]")
    play = input("> Pilih Menu\t: ").upper()
    os.system('cls')
    if play == "1": 
        mulai_permainan()
    elif play=="2":
        print("\nTerima kasih telah bermain\nSampai jumpa di lain waktu "+ Username + "!")
    else:
        restart()

def sort():
    global a
    global b
    data = []
    for i in range(len(poin)):
        z = [poin[i],nama[i]]
        data.append(z)
    data.sort(reverse=True)
    a = []
    b = []
    for i in range(len(data)):
        a.append(data[i][1])
        b.append(data[i][0])
    leaderboard()

def leaderboard():
    print("="*54)
    print("|{:^6}|{:^24}|{:^20}|".format("No","Username","Score"))
    print("="*54)
    for i in range(len(nama)):
        print("|{:^6}|{:^24}|{:^20}|".format(i+1,a[i],b[i]))
    print("="*54)

def login_sukses():
    if Username not in nama:
        nama.append(Username)
        poin.append(0)
    print("Hi, "+ Username +"!\n")
    print("Mulai\t\t[1]\nLeaderboard\t[2]")
    option = input("> Pilih menu\t: ")

    if option == "1":
        os.system('cls')
        countdown()
        hangman()
    elif option == "2":
        os.system('cls')
        print("\033[1;3mLeaderboard\033[0m\n")
        sort()
        option = input("\n> Mulai [Y]\t: ").upper()
        os.system('cls')
        if option == "Y":
            countdown()
            hangman()
        else: login_sukses()
    else:
        os.system('cls')
        login_sukses()

def login():
    global Username
    db = open("database.txt", "r")
    Username = input("> Username\t: ")
    Password = input("> Kata Sandi\t: ")

    if not len(Username or Password)<1:
        un = []
        pw = []
        for i in db:
            a,b = i.split(", ")
            b = b.strip()
            un.append(a)
            pw.append(b)
        data = dict(zip(un, pw))

        try:
            if Password == data[Username]:
                os.system('cls')
                print("Login sukses")
                login_sukses()
            else:
                os.system('cls')
                print("Username atau Kata Sandi salah, coba lagi!\n")
                mulai_permainan()
        except:
            os.system('cls')
            print("Username tidak ditemukan, coba lagi!\n")
            mulai_permainan()
    else: 
        os.system('cls')
        print("Masukkan karakter, coba lagi!\n")
        mulai_permainan()

def register():
    Username = input("> Username\t\t: ")
    Password = input("> Kata Sandi\t\t: ")
    Confirmed = input("> Ulang Kata Sandi\t: ")
    if os.path.exists("database.txt") == False:
        db = open("database.txt", "x")
    else: 
        pass
    db = open("database.txt", "r")
    un = []
    pw = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        un.append(a)
        pw.append(b)

    if Password != Confirmed:
        os.system('cls')
        print("Kata sandi tidak cocok, coba lagi!\n")
        register()
    else:
        if len(Password)<=7:
            os.system('cls')
            print("Password minimal 8 karakter, coba lagi!\n")
            register()
        elif Username in un:
            os.system('cls')
            print("Username sudah digunakan, coba lagi!\n")
            register()
        else:
            db = open("database.txt", "a")
            db.write(Username+", "+Password+"\n")
            os.system('cls')
            print("Berhasil membuat username!\n")
            db.flush()
            os.fsync(db)
            mulai_permainan()

def mulai_permainan():
    print("Daftar\t\t[1]\nLogin\t\t[2]\nMode Tamu\t[3]")
    option = input("> Pilih menu\t: ")
    os.system('cls')
    if option == "1":
        print("\033[1;3mＤａｆｔａｒ\033[0m\n")
        register()
    elif option == "2":
        print("\033[1;3mＬｏｇｉｎ\033[0m\n")
        login()
    elif option == "3":
        hangman_guest()
    else: 
        mulai_permainan()

def konsep_permainan():
    print("="*85)
    print("|{:^83}|".format(" 🕹️ \033[1;3mＣＡＲＡ ＢＥＲＭＡＩＮ\033[0m 🕹️ "))
    print("="*85)
    print("|{:<83}|".format("- Program ini akan memilih sebuah kata acak dari database yang telah tersimpan"))
    print("|{:<83}|".format("- Tebak kata tersebut dengan memasukkan satu-persatu huruf abjad [A-Z]"))
    print("|{:<83}|".format("- Kamu memiliki 7 nyawa, nyawa akan berkurang satu jika kamu salah menebak huruf"))
    print("|{:<83}|".format("- Permainan berakhir ketika kamu berhasil menebak kata ATAU ketika nyawamu habis"))
    print("|{:<83}|".format("- Jika berhasil menebak kata, maka poin bertambah satu, berlaku sebaliknya"))
    print("="*85)
    option = input("> Kembali [Y]\t: ").upper()
    os.system('cls')
    if option == "Y":
        lobby()
    else:
        konsep_permainan()

def lobby(): 
    os.system('cls')
    print("="*80)
    print("|{:^55}|".format(" \u2728 \033[1;3mＳＥＬＡＭＡＴ ＤＡＴＡＮＧ ＤＩ ＰＥＲＭＡＩＮＡＮ ＨＡＮＧＭＡＮ\033[0m \u2728 "))
    print("|{:^78}|".format(""))
    print("|{:^78}|".format("Hangman dalam bahaya!"))
    print("|{:^78}|".format("Ayo selamatkan Hangman dengan menebak kata."))
    print("|{:^78}|".format("Raihlah skor tertinggi dan banggakan orang tuamu!"))
    print("="*80)
    print("Cara Bermain\t[1]\nMulai Bermain\t[2]")
    option = input("> Pilih menu\t: ")
    if option=="1":
        os.system('cls')
        konsep_permainan()
    elif option=="2":
        print("="*19)
        mulai_permainan()
    else:
        lobby()

def countdown():
    for x in countdownNumber:
            print(countdownNumber[x])
            time.sleep(1)
            os.system('cls')

poin = []
nama = []
os.system('cls')

lobby()