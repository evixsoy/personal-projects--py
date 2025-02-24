#1. rekurze
string = "hello"
cislo = 0
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return string[-1] + reverse(string[:-1])

print(reverse("hello"))

#2. rekurze
listcisel = [1,2,3,4,5,6]
def soucet(listcisel):
    if len(listcisel) == 0:
        return 0
    else:
        return listcisel[0] + soucet(listcisel[1:])
print(soucet(listcisel))
