#Inheritance
#super class
class Vehicle:
    def __init__(self, model):
        self.model = model

    def start(self): #classin kendisini methoda gonderme bicimi
        print(f"{self.model} arac calistiriliyor")

class Car:
    #özellikler, fonksiyonlar
    #model= ""
    #self => classın kendisini ifade eder
    # class fonksiyonları ilk parametre olarak zorunlu self parametresi alırlar
    #constructor-yapıcı blok- reverve fonksiyon
    #encapsulation
    def __init__(self, model, year=2025):
        self.__model = model
        self.year = year
        print("Bir car nesnesi olusturuluyor.")

    def start(self): #classın kendisini methoda gönderme biçimi
        print(f"{self.__model} {self.year} araba calistiriliyor.")

    def increaseSpeed(self, speed):
        print(f"{self.__model} arabasinin hizi {speed} kadar artiriliyor.")

    def set_model(self,model):#setter
        if len(model) < 2:
            print("Model 2 haneden kisa olamaz.")
            return
        self.__model = model
    
    def get_model(self):
        return self.__model

araba = Car("BMW") #car kalıbından üretilmiş bir instance
araba.set_model("N")
print(araba.get_model()) #__model degerini okumak
araba.start()
araba.increaseSpeed(50)

araba2 = Car("Toyota", 2024)
araba2.start()
araba2.increaseSpeed(100)

#sub, self class
class Truck(Vehicle):
    def __init__(self, model, capacity):
        super().__init__(model)
        self.capacity = capacity
    
    #override
    def start(self):
        print("arac calistiriliyor")

    def load(self):
        print(f"{self.model} kamyoneti yuk yukleniyor")

truck1 = Truck("Scania",1000)
truck1.start()
