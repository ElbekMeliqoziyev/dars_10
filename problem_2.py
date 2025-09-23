"""Generator yozing: berilgan matndagi har bir so‘zni alohida qaytarsin."""

def matn(b):
    for i in b.split():
        yield i

a= "salom dunyo, what's up"

for i in matn(a):
    print(i)




# a= "salom dunyo, what's up"

# v= (i for i in a.split())

# for i in v:
#     print(i)