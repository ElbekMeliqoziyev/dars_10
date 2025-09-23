"""Generator yozing: berilgan matndagi faqat unli harflarni ketma-ket qaytarsin."""

def unli(a):
    for i in a:
        if i in "aiueo":
            yield i

h = "salom dunyo"
for i in unli(h):
    print(i)

# h = "salom dunyo"

# v = (i for i in h if i in "aouie")

# for i in v:
#     print(i)