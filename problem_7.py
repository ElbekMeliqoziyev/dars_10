"""Generator yozing: listdagi natural sonlarning raqamlar yig‘indisini qaytarsin."""

def natural(x):
    for i in x:
        s=0
        a=0
        if i>0:
            while i!=0:
                a=i%10
                s+=a
                i//=10
            yield s

l = [12,34,5,67,-11,123,91]

for i in natural(l):
    print(i)
    


