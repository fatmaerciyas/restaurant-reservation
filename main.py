import json

bilgiler = dict()


def musteri_ekle():
    global bilgiler

    with open("ornek_dosya_icerigi.txt", "r", encoding="utf-8") as file:
        try:
            bilgiler = json.load(file)
            # dosyadan verileri çek ve 'bilgiler' sözlüğüne ekle


        except ValueError:
            bilgiler = {}

    musteri = dict()  # 'bilgiler' sözlüğünün içine 'müsteri' sözlükleri olacak ve her müşteriye ait bilgileri tutacak
    bayrak = 0  # a ve bayrak yanlış bilgiler girildiğinde while ile tekrar bilgi istemek için
    a = "bos"
    while (bayrak == 0):
        print("\n" * 20)
        tarih = input("Lütfen rezervasyon yapacağınız tarihi giriniz:(Örn. :2 = Bu ayın 2 si):")

        yerler = dict()  # bu sözlüğün bi esprisi yok sadece müşteriye fiyatları göstermek için menü şeklinde ayarlandı
        yerler = {"kapalı_alan": {"2": 50, "4": 60, "6": 70, "8": 80},
                  "balkon": {"2": 75, "4": 90, "6": 100, "8": 125},
                  "teras": {"2": 90, "4": 100, "6": 150, "8": 200}}
        print("\n" * 3)

        for i, j in yerler.items():
            print("{} masaya göre fiyatları : {}".format(i, j))

        print("\n")
        print("Üç çeşit mekanımız bulunmaktadır.Teras, Balkon ve Kapalı alan.")

        yer = input("Lütfen oturacağınız mekanı yazınız:")
        bayrak2 = 0  # istenilen kişi sayısı tek ise tekrar istemek için
        while (bayrak2 == 0):

            print("\n")

            print("2,4,6 ve 8 kişilik olmak üzere masalarımız bulunmaktadır.")
            kisi_sayisi = input("Kaç kişilik masada yer ayırtmak istediğiniz giriniz:")
            if (int(kisi_sayisi) % 2 != 0):
                print("Lütfen mevcut masalardan yer ayırtınız")
            else:
                bayrak2 = 1

        for i in range(1, len(bilgiler)):
            if (bilgiler[str(i)]["Tarih"] == tarih and bilgiler[str(i)]["Mekan"] == yer and bilgiler[str(i)][
                "Masa"] == kisi_sayisi):
                print("Seçmek istediğiniz masa o tarihte dolu lütfen başka bir yer seçiniz")
                a = "bulundu"

        if (a == "bulundu"):
            bayrak = 0

        elif (a == "bos"):
            bayrak = 1

    print("\n")
    print("Seçmek istediğiniz yer o tarihte uygun")

    print("\n" * 3)

    isim = input("Müşterinin adını giriniz:")
    musteri["Ad"] = isim

    soyisim = input("Müşterinin soyadını giriniz:")
    musteri["Soyad"] = soyisim

    musteri["Tarih"] = tarih
    musteri["Mekan"] = yer
    musteri["Masa"] = kisi_sayisi

    bilgiler[len(bilgiler) + 1] = musteri  # 'bilgiler' sözlüğünün son elemanı 'müsteri' sözlüğü olsun

    print("\n" * 7)
    print("Ayın {}'inde {} de {} kişilik masanın rezervasyonu {} {} adına yapılmıştır.".format(tarih, yer, kisi_sayisi,
                                                                                               isim, soyisim))

    with open("ornek_dosya_icerigi.txt", 'w', encoding="utf-8") as file:
        json.dump(bilgiler, file, ensure_ascii=False, indent=4)  # müşteriyi dosyaya ekler

    ana_menu()


def musteri_ara():
    with open("ornek_dosya_icerigi.txt", "r", encoding="utf-8") as file:
        try:
            bilgiler = json.load(file)  # load


        except ValueError:
            bilgiler = {}

    print("\n" * 20)

    isim = input("Aranacak müşterinin adını giriniz:")
    soyisim = input("Soyadını giriniz:")
    print("\n")
    for i in range(1, len(
            bilgiler) + 1):  # 'bilgiler' sözlüğünün 0. elemanı yok 1 den başlıyor range de son elemaı almadığı için + 1 yaptım
        if (isim == bilgiler[str(i)]["Ad"] and soyisim == bilgiler[str(i)]["Soyad"]):
            print("{} {} adlı müşterinin, ayın {} ında {} de {} kişilik masa rezervasyonu bulunmaktadır.".format(isim,
                                                                                                                 soyisim,
                                                                                                                 bilgiler[
                                                                                                                     str(
                                                                                                                         i)][
                                                                                                                     "Tarih"],
                                                                                                                 bilgiler[
                                                                                                                     str(
                                                                                                                         i)][
                                                                                                                     "Mekan"],
                                                                                                                 bilgiler[
                                                                                                                     str(
                                                                                                                         i)][
                                                                                                                     "Masa"]))
        # para hesaplaması için fonk çağırılır ve rezervasyon yaptırdığı masanın ücret bilgisi de gösterilir
    ana_menu()


def musteri_guncelle():
    with open("ornek_dosya_icerigi.txt", "r", encoding="utf-8") as file:
        try:
            bilgiler = json.load(file)  # load


        except ValueError:
            bilgiler = {}

    print("\n" * 20)
    isim = input("Bilgilerini güncellemek istediğiniz müşterinin;\nAdını giriniz:")
    soyisim = input("Soyadını giriniz:")

    bayrak = 0  # müşteri bulunamadığında mesaj vermek için kullanılacak
    dolu = 0  # güncellenen yer başka müşteriye rezerve edilmiş mi onu kontrol edecek
    a = "bos"

    musteri_indisi = list()  # müşterinin kaç tane rezervasonu olduğunu tutar
    for i in range(1, len(bilgiler) + 1):
        if (isim == bilgiler[str(i)]["Ad"] and soyisim == bilgiler[str(i)]["Soyad"]):
            bayrak = 1  # Oyle bir müsteri var
            musteri_indisi.append(i)

    for i in range(1, len(bilgiler) + 1):  # 'bilgiler' sözlüğünün 0. elemanı yok 1 den başlıyor
        if (isim == bilgiler[str(i)]["Ad"] and soyisim == bilgiler[str(i)]["Soyad"]):
            if (len(musteri_indisi) == 1):
                # musterinin 1 rezervasyonu var demektir
                print("\n")
                print("Müşteri bulundu")
                print("\n" * 2)
                print("{} {} adlı müşteriye, ayın {} ında {} de {} kişilik masanın rezervasyonu yapılmıştır"
                      .format(isim, soyisim, bilgiler[str(i)]["Tarih"], bilgiler[str(i)]["Mekan"],
                              bilgiler[str(i)]["Masa"]))



            else:
                # musterinin 1 den fazla rezervasyonu var
                # hangi tarihteki güncellenmek istiyor sorulur
                for i in musteri_indisi:
                    print(
                        "{} {} adlı müşteriye, ayın {} ında {} de {} kişilik masanın rezervasyonu yapılmıştır".format(
                            isim, soyisim, bilgiler[str(i)]["Tarih"], bilgiler[str(i)]["Mekan"],
                            bilgiler[str(i)]["Masa"]))

                bul = input(
                    "Müşteri rezervasyonlarına sahip. Hangi tarihteki rezervasyonda güncelleme yapmak istediğinizi giriniz:")

                for i in range(1, len(bilgiler) + 1):
                    # tarih -> bul a atanır musteri sözlük içinde aranır
                    if (isim == bilgiler[str(i)]["Ad"] and soyisim == bilgiler[str(i)]["Soyad"] and bul ==
                            bilgiler[str(i)]["Tarih"]):
                        print("Müşteri bulundu\n")
                        print("{} {} adlı müşteriye, ayın {} ında {} de {} kişilik masanın rezervasyonu yapılmıştır"
                              .format(isim, soyisim, bilgiler[str(i)]["Tarih"], bilgiler[str(i)]["Mekan"],
                                      bilgiler[str(i)]["Masa"]))
                        break

            print("Hangi bilgiyi değiştirmek istediğinizi girin")
            print("\n")
            guncel = input(
                "Müşteri adı değiştirmek için: 1\nTarih değiştirmek için: 2\nMekan değiştirmek için: 3\nMasa değiştirmek için: 4 ' e basınız:")

            if (guncel == "1"):
                print("\n")
                yeni_ad = input("Yeni adı giriniz:")
                yeni_soyad = input("Yeni soyadı giriniz:")
                print("\n")

                bilgiler[str(i)]["Ad"] = yeni_ad
                bilgiler[str(i)]["Soyad"] = yeni_soyad
                print("Müşteri bilgileri güncellenmiştir.")
                print(
                    "{} {} adlı müşterinin rezervasyon bilgileri ayın {} ında {} de {} kişilik masa olmak üzere güncellenmiştir"
                        .format(isim, soyisim, bilgiler[str(i)]["Tarih"], bilgiler[str(i)]["Mekan"],
                                bilgiler[str(i)]["Masa"]))
                break

            elif (guncel == "2"):
                # Ad ve soyad değişikliğinde buna ihitiyacımız yoktu aynı müşteri 1 den fazla rezervasyon yapabilir
                # Ama bu değişiklik için diğer müşteri rezervasyonlarına bakılması gerekir çünkü güncellenmek istenen yer dolu olabilir

                while (dolu == 0):

                    print("\n")
                    yeni_tarih = input("Yeni tarihi giriniz:")

                    # burada güncellenmek istenen yerin dolu olup olmadığı kontrol edilir

                    for j in range(1, len(bilgiler) + 1):

                        if (bilgiler[str(j)]["Tarih"] == yeni_tarih and bilgiler[str(j)]["Mekan"] == bilgiler[str(i)][
                            "Mekan"] and bilgiler[str(j)]["Masa"] == bilgiler[str(i)]["Masa"]):
                            print("Seçmek istediğiniz masa o tarihte dolu lütfen başka bir yer seçiniz")

                            a = "bulundu"
                            break
                        else:
                            a = "bos"

                    if (a == "bulundu"):
                        dolu = 0

                    elif (a == "bos"):
                        dolu = 1

                # masa dolu değilse güncellenmek istenen bilgi alınır
                bilgiler[str(i)]["Tarih"] = yeni_tarih
                print("\n")
                print("Müşteri bilgileri güncellenmiştir.")

                print(
                    "{} {} adlı müşterinin rezervasyon bilgileri ayın {} ında {} de {} kişilik masa olmak üzere güncellenmiştir"
                        .format(isim, soyisim, bilgiler[str(i)]["Tarih"], bilgiler[str(i)]["Mekan"],
                                bilgiler[str(i)]["Masa"]))
                break


            elif (guncel == "3"):

                # Ad ve soyad değişikliğinde buna ihitiyacımız yoktu aynı müşteri 1 den fazla rezervasyon yapabilir
                # Ama bu değişiklik için diğer müşteri rezervasyonlarına bakılması gerekir çünkü güncellenmek istenen yer dolu olabilir

                while (dolu == 0):

                    print("\n")
                    yeni_mekan = input("Yeni mekan giriniz:")

                    # burada güncellenmek istenen yerin dolu olup olmadığı kontrol edilir

                    for j in range(1, len(bilgiler) + 1):

                        if (bilgiler[str(j)]["Tarih"] == bilgiler[str(i)]["Tarih"] and bilgiler[str(j)][
                            "Mekan"] == yeni_mekan
                                and bilgiler[str(j)]["Masa"] == bilgiler[str(i)]["Masa"]):
                            print("Seçmek istediğiniz masa o tarihte dolu lütfen başka bir yer seçiniz")

                            a = "bulundu"
                            break
                        else:
                            a = "bos"

                    if (a == "bulundu"):
                        dolu = 0

                    elif (a == "bos"):
                        dolu = 1

                # masa dolu değilse güncellenmek istenen bilgi alınır
                bilgiler[str(i)]["Mekan"] = yeni_mekan
                print("\n")
                print("Müşteri bilgileri güncellenmiştir.")

                print(
                    "{} {} adlı müşterinin rezervasyon bilgileri ayın {} ında {} de {} kişilik masa olmak üzere güncellenmiştir"
                        .format(isim, soyisim, bilgiler[str(i)]["Tarih"], bilgiler[str(i)]["Mekan"],
                                bilgiler[str(i)]["Masa"]))
                break

            elif (guncel == "4"):

                # Ad ve soyad değişikliğinde buna ihitiyacımız yoktu aynı müşteri 1 den fazla rezervasyon yapabilir
                # Ama bu değişiklik için diğer müşteri rezervasyonlarına bakılması gerekir çünkü güncellenmek istenen yer dolu olabilir

                while (dolu == 0):
                    print("\n")
                    yeni_masa = input("Kaç kişilik masa istediğinizi giriniz:")
                    if (int(yeni_masa) % 2 != 0):
                        print("Lütfen geçerli masa sayısı giriniz")
                        continue

                    # burada güncellenmek istenen yerin dolu olup olmadığı kontrol edilir

                    for j in range(1, len(bilgiler) + 1):

                        if (bilgiler[str(j)]["Tarih"] == bilgiler[str(i)]["Tarih"] and bilgiler[str(j)]["Mekan"] ==
                                bilgiler[str(i)]["Mekan"]
                                and bilgiler[str(j)]["Masa"] == yeni_masa):
                            print("Seçmek istediğiniz masa o tarihte dolu lütfen başka bir yer seçiniz")

                            a = "bulundu"
                            break
                        else:
                            a = "bos"

                    if (a == "bulundu"):
                        dolu = 0

                    elif (a == "bos"):
                        dolu = 1

                # masa dolu değilse güncellenmek istenen bilgi alınır
                bilgiler[str(i)]["Masa"] = yeni_masa
                print("\n")
                print("Müşteri bilgileri güncellenmiştir.")
                print(
                    "{} {} adlı müşterinin rezervasyon bilgileri ayın {} ında {} de {} kişilik masa olmak üzere güncellenmiştir"
                    .format(isim, soyisim, bilgiler[str(i)]["Tarih"], bilgiler[str(i)]["Mekan"],
                            bilgiler[str(i)]["Masa"]))
                break

    with open("ornek_dosya_icerigi.txt", 'w', encoding="utf-8") as file:
        json.dump(bilgiler, file, ensure_ascii=False, indent=4)  # müşteriyi dosyaya ekler

    if (bayrak == 0):
        print("Öyle bir müşteri rezervasyonu bulunamadı.")

    ana_menu()


def musteri_sil():
    global bilgiler

    with open("ornek_dosya_icerigi.txt", "r", encoding="utf-8") as file:
        try:
            bilgiler = json.load(file)  # load


        except ValueError:
            bilgiler = {}
    print("\n" * 20)
    isim = input("Silmek istediğiniz müşterinin adını giriniz:")
    soyisim = input("Soyadını giriniz:")

    rezervasyon_adeti = list()
    print("\n")

    for i in range(1, len(bilgiler) + 1):
        if (bilgiler[str(i)]["Ad"] == isim and bilgiler[str(i)]["Soyad"] == soyisim):
            rezervasyon_adeti.append(i)

    if (len(rezervasyon_adeti) == 1):
        # Müşterinin 1 rezervasyonu var
        anahtar = rezervasyon_adeti[0]

        for i in range(1, len(bilgiler) + 1):

            if (i == anahtar):
                del bilgiler[str(anahtar)]
                print("\n" * 2)
                print("Müşteri rezervasyonu iptal edildi")

            else:
                if (i > anahtar):
                    a = i - 1
                    bilgiler[str(a)] = bilgiler[str(i)]
                    del bilgiler[str(i)]





    elif (len(rezervasyon_adeti) > 1):
        # Müşterinin 1 den fazla rezervasyonu var
        for i in rezervasyon_adeti:
            print(bilgiler[str(i)])
        print("Olmak üzere rezervasyonlarınız bulunmaktadır.")
        tarih = input("Hangi tarihteki rezervasyonu iptal ettirmek istiyorsanız o tarihi giriniz:")

        for i in range(1, len(bilgiler)):
            if (bilgiler[str(i)]["Ad"] == isim and bilgiler[str(i)]["Soyad"] == soyisim and bilgiler[str(i)][
                "Tarih"] == tarih):
                rezervasyon_adeti.clear()  # diğer müşteri rezervasyonları iptal et
                rezervasyon_adeti.append(i)  # sadece seçilen tarihtekini listeye ekle

                anahtar = rezervasyon_adeti[0]

                for i in range(1, len(bilgiler) + 1):

                    if (i == anahtar):
                        del bilgiler[str(anahtar)]
                        print("\n" * 2)
                        print("Müşteri rezervasyonu iptal edildi")

                    else:
                        if (i > anahtar):
                            a = i - 1
                            bilgiler[str(a)] = bilgiler[str(i)]
                            del bilgiler[str(i)]

    with open("ornek_dosya_icerigi.txt", 'w', encoding="utf-8") as file:
        json.dump(bilgiler, file, ensure_ascii=False, indent=4)  # müşteriyi dosyadan siler

    ana_menu()


def fiyat_hesapla():
    with open("ornek_dosya_icerigi.txt", "r", encoding="utf-8") as file:
        try:
            bilgiler = json.load(file)


        except ValueError:
            bilgiler = {}

    print("\n" * 20)

    isim = input("Rezervasyon fiyat bilgisini öğrenmek istediğiniz müşterinin \nAdını giriniz:")
    soyisim = input("Soyadını giriniz:")

    kapalı_alan = {"2": 50, "4": 60, "6": 70, "8": 80}
    balkon = {"2": 75, "4": 90, "6": 100, "8": 125}
    teras = {"2": 90, "4": 100, "6": 150, "8": 200}

    # yer fiyatlarını sözlüklerde tuttum

    musteri_rezervasyon_sayaci = 0  # müsterinin kaç tane rezervasyonu olduğunu tutacağım

    for i in range(1, len(bilgiler) + 1):
        if (bilgiler[str(i)]["Ad"] == isim and bilgiler[str(i)]["Soyad"] == soyisim):
            musteri_rezervasyon_sayaci += 1

    tutar = 0  # toplam ödenmesi gereken
    sayac = 0  # bu müşteriye hangi tarihteki tutarı istediğini 1 kere soracak

    for i in range(1, len(bilgiler) + 1):
        if (bilgiler[str(i)]["Ad"] == isim and bilgiler[str(i)]["Soyad"] == soyisim):
            if (musteri_rezervasyon_sayaci > 1):
                # müsterinin 1 den fazla rezervasyonu varsa tarih bilgisi istenir
                if (sayac == 0):
                    tarih = input("Hangi tarihteki tutarı istiyorsanız o tarihi giriniz:")
                    sayac += 1

                else:

                    if (bilgiler[str(i)]["Ad"] == isim and bilgiler[str(i)]["Soyad"] == soyisim and bilgiler[str(i)][
                        "Tarih"] == tarih):
                        pass

                    else:
                        continue

            if (bilgiler[str(i)]["Mekan"] == "kapalı alan" or bilgiler[str(i)]["Mekan"] == "Kapalı alan"):
                a = int(bilgiler[str(i)]["Masa"])
                tutar = kapalı_alan[str(a)]
                print("\n" * 2)
                print("Ödemeniz gereken tutar {} TL.".format(tutar))

            elif (bilgiler[str(i)]["Mekan"] == "balkon" or bilgiler[str(i)]["Mekan"] == "Balkon"):
                a = int(bilgiler[str(i)]["Masa"])
                tutar = balkon[str(a)]
                print("\n" * 2)
                print("Ödemeniz gereken tutar {} TL.".format(tutar))

            elif (bilgiler[str(i)]["Mekan"] == "teras" or bilgiler[str(i)]["Mekan"] == "Teras"):
                a = int(bilgiler[str(i)]["Masa"])
                tutar = teras[str(a)]
                print("\n" * 2)
                print("Ödemeniz gereken tutar {} TL.".format(tutar))

            if (1 < musteri_rezervasyon_sayaci < 5):
                print("\n")

                print("1'den fazla rezervasyon yaptırdığınız için size özel %5 indirimimiz mevcuttur :) ")
                print("Yaptırdığınız tüm rezervasyonların fiyatlarına %5 indirim yapılır")
                yeni_tutar = tutar - (tutar * (5 / 100))
                print("\n")
                print("{} tarihinde indirimli ödemeniz gereken tutar {} TL.".format(bilgiler[str(i)]["Tarih"],
                                                                                    yeni_tutar))
                break



            elif (5 < musteri_rezervasyon_sayaci < 10):
                print("\n")
                print("Daha önce rezervasyon yaptırdığınız için size özel %5 indirimimiz mevcuttur :) ")
                yeni_tutar = tutar - (tutar * (10 / 100))
                print("\n")
                print("{} tarihinde indirimli ödemeniz gereken tutar {} TL.".format(bilgiler[str(i)]["Tarih"],
                                                                                    yeni_tutar))
                break

    if (cocuk_ozel_sayac != 0):
        # burası cocuk_ozel fonksiyonu icin eğer oradan çalıştırılıyorsa bu fonksiyon ana menüye dönmez
        return tutar

    elif (cocuk_ozel_sayac == 0):
        # ama bunun çalışmasını ana menüden istediysem tekrar ana menüye döner
        ana_menu()


cocuk_ozel_sayac = 0  # bu sayac fiyat_hesapla() fonkunun tekrar ana menüye dönmemesini sağlayacak


def cocuk_ozel():  # Çocuklar için indirimler ya da fiyatlar

    global cocuk_ozel_sayac

    with open("ornek_dosya_icerigi.txt", "r", encoding="utf-8") as file:
        try:
            bilgiler = json.load(file)


        except ValueError:
            bilgiler = {}

    print("\n" * 20)
    cocuk_ozel_sayac += 1  # fiyat hesapla fonkunda da cocuk hesapla fonksiyonunu çağıracağım

    tutar = fiyat_hesapla()

    cocuk_sayisi = int(input("Kaç adet çocuğunuz olduğunu giriniz:"))

    for i in range(cocuk_sayisi):
        print("\n")

        cocuk_yas = int(input("{}. çocuğunuzun yaşını giriniz:".format(i + 1)))

        def eglence(yas):

            if (yas < 10):
                # eğer çocuk yaşı 10 dan küçükse teklifler sunulur
                fiyat = 0
                oyun_park = input(
                    " Restoranımızda çocuklara özel oyun parkı bulunmaktadır.\n"
                    " İsterseniz rezervasyon ödemenize ek sadece 100 TL'ye oyun parkında dilediğinizce zaman geçirebilirsiniz.\n"
                    " Bu tekliften yararlanmak istiyor musunuz (Evet veya Hayır) yazınız:")

                if (oyun_park == "evet" or oyun_park == "Evet"):

                    fiyat = fiyat + 100
                    print("\n")

                    print("Oyun parkında iyi eğlenceler dileriz :)")
                    print("\n" * 2)
                    print("Bizim için en önemlisi sizin ve çocuklarınızın rahatlığı")
                    print("\n")
                    bakici = input(
                        " Yemek yerken sürekli çocuklarınıza göz kulak olmanıza gerek yok.\n"
                        " İsterseniz rezervasyon ödemenize ek sadece 100 TL'ye çocuklarınıza bakıcı hizmeti sunuyoruz.\n"
                        " Bu tekliften yararlanmak istiyor musunuz (Evet veya Hayır) yazınız:")

                    if (bakici == "evet" or bakici == "Evet"):

                        fiyat = fiyat + 100
                        print("\n")
                        print("Bizi seçtiğiniz için teşekkür eder, iyi eğlenceler dileriz :)")
                        # print("Ödemeniz gereken tutar {} Tl".format(tutar))

                    elif (bakici == "hayır" or bakici == "Hayır"):
                        print("\n")
                        print("Bizi seçtiğiniz için teşekkür ederiz :)")
                        # print("Ödemeniz gereken tutar {} Tl".format(tutar))

                elif (oyun_park == "hayır" or oyun_park == "Hayır"):
                    print("\n")
                    print("Bizi seçtiğiniz için teşekkür ederiz :)")

            else:
                pass

            return fiyat

    tutar = tutar + eglence(cocuk_yas)

    if (1 <= cocuk_sayisi <= 2):
        cocuk_ozel_sayac = 0
        print("\n" * 2)
        print("Çocuklara özel %5 indirimimizden yararlanıyorsunuz.")
        tutar = tutar - (tutar * (5 / 100))
        print("Ödemeniz gereken indirimli tutar: {} TL".format(tutar))

    elif (cocuk_sayisi > 2):
        cocuk_ozel_sayac = 0
        print("\n" * 2)
        print("Çocuklara özel %10 indirimimizden yararlanıyorsunuz.")
        tutar = tutar - (tutar * (10 / 100))
        print("Ödemeniz gereken indirimli tutar: {} TL".format(tutar))

    ana_menu()


def ana_menu():
    print("\n")
    islem = input("Ne tür bir işlem yapmak istediğinizi yazınız.\n"
                  "Yeni bir müşteri rezervasyonu eklemek için -ekle- \n"
                  "Müşteri aramak için -ara-\n"
                  "Müşteri bilgilerini güncellemek için -güncelle-\n"
                  "İptal olan rezervasyonları silmek için -sil-\n"
                  "Müşteri rezervasyon fiyatı hesaplamak için -hesapla-\n"
                  "Çocuklu müşterilerimize özel indirimler ve çocuklara özel eğlencelerden yararlanmak için -çocuk-\n"
                  "Sistemden çıkış yapmak için -çıkış- yazınız:")

    if (islem == "ekle" or islem == "Ekle"):
        musteri_ekle()

    elif (islem == "ara" or islem == "Ara"):
        musteri_ara()

    elif (islem == "güncelle" or islem == "Güncelle"):
        musteri_guncelle()

    elif (islem == "sil" or islem == "Sil"):
        musteri_sil()

    elif (islem == "hesapla" or islem == "Hesapla"):
        fiyat_hesapla()

    elif (islem == "çocuk" or islem == "Çocuk"):
        cocuk_ozel()

    elif (islem == "çıkış" or islem == "Çıkış"):

        return None


ana_menu()