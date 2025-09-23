"""Generator yozing: berilgan ro‘yxatdan faqat unikal elementlarni ketma-ket qaytarsin."""

def unikal(a):
    for i in a:
        if a.count(i)==1:
            yield i

l=[1,2,3,2,3,5,6,8,9,5,6,9,8,9,4,10,2,2,]

for i in unikal(l):
    print(i)