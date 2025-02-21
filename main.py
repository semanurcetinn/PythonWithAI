print("Kodlamaio")
baslik = "Tasit Kredisi"
print(baslik)
baslik = "Ihtiyac Kredisi"
print(baslik)
vade = 36
ekVade = 6
vade2 = "36"

aylikOdeme = 200.50
yukselisteMi = True

print("**********************")

print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

print(5 * 5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(10 / 2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20
print(yeniVade)
print(indirimliFiyat)

print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

print("**********************")

print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

print(1 < 2 or 5 > 2)
print(1 < 2 and 5 > 2)
print(1 < 2 or 5 > 2 and 3 > 2)
print(1 < 2 and 5 > 2 and 3 > 2)
print(2 < 1 or 1 > 2 and 3 > 2)

print("**********************")

sayi1 = 15
sayi2 = 15
if sayi1 <= sayi2:
    print("Sayi1 sayi2'den buyuktur.")
elif sayi2 == sayi1:
    print("iki sayi esittir")
else :
    print("sayi1 sayi2'den buyuktur.")