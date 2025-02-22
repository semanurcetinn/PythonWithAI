faiz = 1.59
vade = "36"
krediAdi = "Ihtiyac Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
faiz = str(faiz)
print(type(faiz))

vade = int(input("Lutfen istediginiz vade sayisini giriniz:"))
print(type(vade))
vade = vade + 12

print("Sectiginiz vade sonucu ortaya cikan vade: " + str(vade))
print("Sectiginiz vade sonucu ortaya cikan vade: {vadeSayisi}".format(vadeSayisi = vade))

isim = "Sema"
metin = "Merhaba {name}".format(name = "Sema")
print(metin)

metin = f"Hosgeldiniz {1+1}"
print(metin)

krediler = ["Ihtiyac Kredisi", "Tasit Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])
print(len(krediler))

krediler.append("Ozel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0) #index sayısı ile siler
print(krediler)

krediler.remove("Tasit Kredisi") #index sayısına göre bulduğu ilk değeri siler birden fazla aynı değerden eleman varsa
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"]) #birden fazla değeri listeye ekler.
print(krediler)

for i in range(10):
    print("xx")
    print(i)
print("**********************")
for i in range(5,11):
    print(i)
print("**********************")
for i in range(0,51,10):
    print(i)
print("**********************")
for i in range(5,10):
    forVariable  = 5
    print(i)
print("**********************")
for kredi in krediler:
    print(kredi)
print("**********************")

for i in range(len(krediler)):
    print(krediler[i])
print("**********************")

i = 0
while i < 10:
    print("x")
    i += 1
print("y")

while True:
    print("X")
    break
print("**********************")

# i = 0
# while i < len(krediler):
#     i += 1
#     print(i)
#     print(krediler[i])
#     if krediler[i] == "Konut Kredisi":
#         break

fiyat = 100
indirim = 20

def calculate():
    print(100-20)
calculate()

def CalculateWithParams(fiyat, indirim):
    print(fiyat-indirim)

CalculateWithParams(50,5)

def sayHello(name):
    print(f"Merhaba {name}")
sayHello("Sema")

#default parametreler her zaman zorunlu parametrelerden sonra gelmelidir.
def calculateAndReturn(price, discount=5):
    return price - discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)

def sum(*args): # Sınırsız sayıda parametreli fonksiyon oluşturmak için * koyulur
    if len(args) <= 0:
        print("En az 1 sayı göndermek zorundasınız")
    sonuc = 0
    for sayi in args:
        sonuc += sayi
    return sonuc

print(sum(10,20,30,40,50,60,70))
print(sum(1))

# **kwargs, fonksiyonu çağırırken anahtar değer ilişkisiyle çağırabiliriz.
# lambda fonks, anonim tek satır, bir başka fonksiyon içinde kullanıldığında anlam kazanır.

topla = lambda a,b: a+b
print(topla(1,2))

selamla = lambda isim: print(f"Merhaba {isim}")
selamla("Sema")