"""Dekorator yozing: faqat dushanba kuni ishlaydigan 
qilib qo‘ying (hafta kunini tekshiradi)."""

def check(func):
    def wrap():
        if "dushanba" == input(": ").lower():
            func()
        else:
            print("Faqat dushanba ish kuni")
    return wrap


@check
def work():
    print("Bugun ish kuni")

work()