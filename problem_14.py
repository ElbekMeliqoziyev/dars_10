"""Generator yozing: matndagi so‘zlarni teskari qilib, 
faqat palindromlarni qaytarsin."""

def palindrom(x):
    if type(x) == str:
        for i in x.split():
            if i == i[::-1]:
                yield i

n="salom arra kiyik alla dunyo"  

for i in palindrom(n):
    print(i)