"""Generator yozing: har safar chaqirilganda 
vaqtning hozirgi sekund qiymatini qaytarsin."""

from datetime import datetime

def vaqt():
    a = datetime.now().second
    yield a


for i in vaqt():
    print(i)

