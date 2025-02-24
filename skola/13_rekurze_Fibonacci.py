def fib(cislo):
    if cislo > 1:
        return fib(cislo -1) + fib(cislo -2)
    else:
        return cislo
cislo = int(input("Vložte číslo: "))
print(fib(cislo))
