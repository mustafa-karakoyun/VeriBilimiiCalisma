import random
import statistics as stat
kitaplar = [ 
{"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021}, 
{"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 
2020}, 
{"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019}, 
{"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022}, 
{"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018}, 
{"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, 
"yil": 2021}, 
{"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022} 
]
#Fonsiyon İşlemleri
def encok_satan(kitaplar):
    max_satis=max(kitap["satis"] for kitap in kitaplar)
    enCokSatanKitaplar=[kitap for kitap in kitaplar if kitap["satis"]==max_satis]
    print(enCokSatanKitaplar)
    
def yazar_satislari(kitaplar):
    yazar_satis={}
    for kitap in kitaplar:
        yazar=kitap["yazar"]
        satis=kitap["satis"]
        yazar_satis[yazar]=satis
    print(yazar_satis)



#Liste İşlemleri
turler=set(kitap["tur"] for kitap in kitaplar)

coksatan=set(kitap["isim"] for kitap in kitaplar if kitap["satis"]>1000)

#Lambda işlemleri
soncıkan=list(filter(lambda x: x["yil"]>2020,kitaplar))

satisartıs=list(map(lambda x: x["satis"]*1.10,kitaplar))

#print(sorted(kitaplar, key=lambda x:x["satis"],reverse=True))

#İSTATİSTİK
satislar = [kitap["satis"] for kitap in kitaplar]
ortalama_satis = stat.mean(satislar)
print("Ortalama satış:", ortalama_satis)

turler = {}
for kitap in kitaplar:
    tur = kitap["tur"]
    turler[tur] = turler.get(tur, 0) + kitap["satis"]

en_cok_satan_tur = max(turler, key=turler.get)
print("En çok satış yapan tür:", en_cok_satan_tur)

satis_sapma = stat.stdev(satislar)
print("Satışların standart sapması:", satis_sapma)

#TEST

train_size = int(len(kitaplar) * 0.7)
train = random.sample(kitaplar, train_size)
test = [kitap for kitap in kitaplar if kitap not in train]

# yazarların ortalama satışını hesapla
yazar_satis = {}
yazar_kitap_sayisi = {}

for kitap in train:
    yazar = kitap["yazar"]
    yazar_satis[yazar] = yazar_satis.get(yazar, 0) + kitap["satis"]
    yazar_kitap_sayisi[yazar] = yazar_kitap_sayisi.get(yazar, 0) + 1

yazar_ortalama = {yazar: yazar_satis[yazar]/yazar_kitap_sayisi[yazar] for yazar in yazar_satis}
print("\nEğitim verisinde yazarların ortalama satışları:")
for y, ort in yazar_ortalama.items():
    print(f"{y}: {ort}")

#  ortalamanın üzerinde satış yapan kitaplar
print("\nTest verisinde ortalamanın üzerinde satış yapan kitaplar:")
for kitap in test:
    yazar = kitap["yazar"]
    if yazar in yazar_ortalama and kitap["satis"] > yazar_ortalama[yazar]:
        print(f"{kitap['isim']} ({yazar}) - Satış: {kitap['satis']})")

# print(soncıkan)
# print(satisartıs)
# yazar_satislari(kitaplar)
# encok_satan(kitaplar)
# print("Türler:",turler)
# print(coksatan)