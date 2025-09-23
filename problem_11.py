"""Dekorator yozing: har safar funksiya chaqirilganda 
uni nechinchi marta chaqirilganini hisoblab bersin."""

def check(func):
    c=0
    def wrap():
        nonlocal c
        c+=1
        print(c)
        func()
    return wrap

@check
def salom():
    pass

salom()
salom()
salom()
salom()