def VeciBroj(a, b, c):
    if a > b > c:
        return a
    elif a < b > c:
        return b
    else:
        return c


def main():
    broj1 = int(input("Unesi broj: "))
    broj2 = int(input("Unesi broj: "))
    broj3 = int(input("Unesi broj: "))
    print("Najeci broj je", VeciBroj(broj1, broj2, broj3))

main()
