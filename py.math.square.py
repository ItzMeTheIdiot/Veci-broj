def VeciBroj(a, b):
    if a > b:
        return a
    else:
        return b


def main():
    broj1 = int(input("Unesi broj: "))
    broj2 = int(input("Unesi broj: "))
    print("Veci broj je", VeciBroj(broj1, broj2))

main()
