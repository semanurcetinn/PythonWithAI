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

def calculateAndReturn(price, discount):
    return price - discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)