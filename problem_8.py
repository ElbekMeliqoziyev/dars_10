"""Generator yozing: random kutubxonasidan foydalanib 
har safar yangi random son chiqarsin (1–100 oralig‘ida)."""

from random import randint

def ixtiyoriy_son():
    a = randint(1,100)
    yield a

for i in ixtiyoriy_son():
    print(i)

