"""Generator yozing: Fibonachchi ketma-ketligini cheksiz qaytarib bersin."""
import time

def fibonachi():
    a=0
    b=1
    while True:
        c=a
        time.sleep(1)
        yield a
        a=b
        b+=c


for i in fibonachi():
    print(i)




