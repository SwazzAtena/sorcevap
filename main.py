import webbrowser
from colorama import init, Fore, Style
import time
import random
from motivational_quotes import motivational_quotes

print("Kontrol Yapılıyor")

try:
    from colorama import Fore, Style
    print(Fore.GREEN + "Kurulum tamamlandı!" + Style.RESET_ALL)
except ImportError:
    print("Gerekli kütüphaneler bulunamadı. Kurulum yapılıyor...")
    import os
    os.system("pip install colorama")
    os.system("pip install random")
    print("Gerekli kurulumlar başarıyla yapıldı program açılıyor!")
    print("")

init()

print(Fore.LIGHTMAGENTA_EX)
print("---------------------------------------------------------------------------------------------------------------")

def ilk_soru():
    while True:
        print("Hoşgeldinnn")
        print(Fore.LIGHTBLUE_EX)
        genel_soru = input("Naber nasılsınn(iyiyim/kötüyüm): ").lower()
        if genel_soru == "iyiyim":
            print(Fore.LIGHTGREEN_EX)
            print("Süperrrr")
            print("Senin için şunları yapabilirim ._.")
            time.sleep(1.5)
            ikinci_soru()
            break
        elif genel_soru == "kötüyüm":
            print(Fore.LIGHTRED_EX)
            print("ow kötü olmuş")
            time.sleep(1)
            print(Fore.LIGHTCYAN_EX)
            print("Sanırım Seni Nasıl Mutlu Edeceğimi Biliyorum :)")
            time.sleep(1)
            webbrowser.open("https://www.youtube.com/watch?v=_HFy-zrjSTM&list=WL&index=20&ab_channel=Guinnes.luis")
            time.sleep(14)
            print("Hala mutlu olmadıysan git şu playlistteki şarkılar dinle koş!!!")
            time.sleep(4)
            webbrowser.open("https://open.spotify.com/playlist/6MP2c3JQKapdQxbOIvp1vE?si=411cdf39f2f94ce7")
            print("...")
            time.sleep(1)
            exit()
            break
        else:
            print("Ne Demek İstediğinizi Anlamadım :/")
            time.sleep(1)

def ikinci_soru():
    print("""
1) Şarkı Öner
2) Film Öner
3) Motive Edici Söz Söyle
4) Çıkış Yap
""")
    sec = input("Seçim yapınız (1/2/3): ")

    if sec == "1":
        webbrowser.open("https://open.spotify.com/playlist/6MP2c3JQKapdQxbOIvp1vE?si=49d27bdeab754459")
        k = input("Başka İsteğiniz Varmı? (evet/hayır): ").lower()
        if k == "evet":
            ikinci_soru()
        if k == "hayır":
            print("Çıkış Yapılıyor...")
            exit()

    elif sec == "2":
        films = [
            {
                "ad": "Matrix",
                "tur": "Bilim Kurgu",
                "puan": 8.7,
                "yil": 1999,
            },
            {
                "ad": "3 İdiots",
                "tur": "Komedi",
                "puan": 8.4,
                "yil": 2009,
            },
            {
                "ad": "G.O.R.A",
                "tur": "Yerli Komedi",
                "puan": 8.0,
                "yil": 2004,
            },
            {
                "ad": "Bright",
                "tur": "Bilim Kurgu",
                "puan": 6.3,
                "yil": 2017,
            },
            {
                "ad": "Extraction 2",
                "tur": "Aksiyon",
                "puan": 7.1,
                "yil": 2023,
            },
            {
                "ad": "Hababam Sınıfı Yeniden",
                "tur": "Yerli Komedi",
                "puan": 2.2,
                "yil": 2019,
            },
            {
                "ad": "Esaretin Bedeli",
                "tur": "Drama",
                "puan": 9.3,
                "yil": 1994,
            },
            {
                "ad": "The Godfather",
                "tur": "Polisiye",
                "puan": 9.2,
                "yıl": 1972,
            },
            {
                "ad": "Oppenheimer",
                "tur": "Biyografi",
                "puan": 8.7,
                "yıl": 2023,
            },
            {
                "ad": "Barbie",
                "tur": "Komedi",
                "puan": 7.5,
                "yıl": 2023,
            },
            {
                "ad": "Ölümcül Hesaplaşma",
                "tur": "Aksiyon",
                "puan": 8.0,
                "yıl": 2023,
            },
            {
                "ad": "Hababam Sınıfı",
                "tur": "Yerli Komedi",
                "puan": 9.2,
                "yil": 1975,
            },
            {
                "ad": "Inception",
                "tur": "Bilim Kurgu",
                "puan": 8.8,
                "yil": 2010,
            },
            {
                "ad": "Forrest Gump",
                "tur": "Drama",
                "puan": 8.8,
                "yil": 1994,
            },
            {
                "ad": "The Dark Knight",
                "tur": "Aksiyon",
                "puan": 9.0,
                "yil": 2008,
            },
        ]

        print("Film Öneri Programı")
        print("--------------------")
        # Kullanıcıdan sorulara verilen cevapları al
        tur_soru = "Hangi türde bir film arıyorsunuz? (Bilim Kurgu, Aksiyon, Drama, Yerli Komedi, Polisiye, Komedi, Biyografi): "
        puan_soru = "Minimum kaç puan üstü filmler önerilsin? (0 ile 10 arasında bir değer girin): "
        yil_soru = "Hangi yıldan daha yeni filmler önerilsin? (Yıl olarak 1970 ile 2023 arasında bir değer girin): "

        hedef_tur = input(tur_soru)
        hedef_puan = float(input(puan_soru))
        hedef_yil = int(input(yil_soru))

        onerilen_filmler = []
        for film in films:
            if film["tur"].lower() == hedef_tur.lower() and film.get("puan", 0) >= hedef_puan and film.get("yil",
                                                                                                           0) >= hedef_yil:
                onerilen_filmler.append(film)

        if len(onerilen_filmler) == 0:
            print("Üzgünüz, sizin için uygun bir film bulamadık.")
        else:
            print("Önerilen Filmler:")
            for film in onerilen_filmler:
                print(film["ad"], "(" + film["tur"] + ") - Puan: " + str(film.get("puan", 0)) + " - Yıl: " + str(
                    film.get("yil", 0)))

        a = input("Başka bir isteğiniz var mı? (evet/hayır): ").lower()
        if a == "evet":
            ikinci_soru()
        if a == "hayır":
            print("Görüşürüz")
            time.sleep(1)
            exit()

    elif sec == "3":
        print(random_quote())
        b = input("Başka bir isteğiniz varmı? (evet/hayır): ").lower()
        if b == "evet":
            ikinci_soru()
        if b == "hayır":
            print("Görüşürüz :)")
            time.sleep(1)
            exit()
        if sec == "4":
            print("Görüşürüzzz :)")
            time.sleep(1)
            exit()

def random_quote():
    return random.choice(motivational_quotes)

if __name__ == "__main__":
    ilk_soru()
