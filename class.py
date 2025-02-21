class Human:
    #built-in => constructor, 
    def __init__(self, name):
        self.name = name
        print("Bir human instance'i üretildi.")
    
    def __str__(self):
        return f"STR fonksiyonundan dönen değer: {self.name}"

    def talk(self, sentence):
        #self. yapmazsak name'i o kod bloğunda arar, nesnenin içindeki diğer alanlara erişmek için kullanılır.
        print(f"{self.name}: {sentence}")
    
    def walk(self):
        print(f"{self.name} is walking")

#self => this, bir class içinde fonksiyon kullanılırken self parametresi kullanılır. self yerine başka isim de kullanılabilirdi.
#instance => örnek, nesnelere ulaşabilmek için instance oluşturulur.
human1 = Human("Deniz")
human1.talk("Merhaba") #1. parametre olarak saydı, self'i rezerve parametre olarak sayıldı.
human1.walk()
print(human1)

human2 = Human("Sema")
human2.talk("Selam")
human2.walk()
print(human2)