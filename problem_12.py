"""Dekorator yozing: funksiya argumentlarini log faylga yozib borsin."""
# biroz kamchiliklari bor
def check(func):
    def wrap(*a,**k):
        with open("qaytnoma.log","w") as f:
            f.write(f"{a,k}")
        func(*a,**k)
    return wrap

@check
def salom(a):
    pass



with open("qaytnoma.log", "r") as f:
    n= f.read()

print(n)

