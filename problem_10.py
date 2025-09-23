"""Dekorator yozing: funksiya natijasini string tipiga o‘girib qaytarsin."""

def check(func):
    def wrap():
        a=func()
        return str(a)
    return wrap
    

@check
def how():
    return 10
        
print(how())
