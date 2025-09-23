"""Generator yozing: har safar chaqirilganda kvadrat sonlarni qaytarsin (1², 2², 3² …)."""

def kv(n):
    for i in range(1,n+1):
        yield i**2


for i in kv(int(input(": "))):
    print(i)