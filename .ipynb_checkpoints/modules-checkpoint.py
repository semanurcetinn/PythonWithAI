#alias => as 
#import math #bütün math modulunu alır
from math import sqrt as karekok #mat kütüphanesinden sadece sqrt'u al
from oop import Truck # type: ignore
import requests

print(karekok(8))

truck2 = Truck("Scania",1000)
truck2.start

response = requests.get("https://google.com")
print(response.status_code)
