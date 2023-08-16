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
    if film["tur"].lower() == hedef_tur.lower() and film.get("puan", 0) >= hedef_puan and film.get("yil", 0) >= hedef_yil:
        onerilen_filmler.append(film)

if len(onerilen_filmler) == 0:
    print("Üzgünüz, sizin için uygun bir film bulamadık.")
else:
    print("Önerilen Filmler:")
    for film in onerilen_filmler:
        print(film["ad"], "(" + film["tur"] + ") - Puan: " + str(film.get("puan", 0)) + " - Yıl: " + str(film.get("yil", 0)))
