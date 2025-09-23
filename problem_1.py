"""Generator yozing: 0 dan 100 gacha faqat 5 ga bo‘linadigan sonlarni chiqarsin."""

# def for_5():
#     for i in range(100):
#         if i%5==0:
#             yield i

# for j in for_5():
#     print(j)


a= (i for i in range(100) if i%5==0)

for i in a:
    print(i)