for i in range(2):

    szo = input("Írj be egy szót: ")
    karakter = len(szo)

    print(f"A szóban {karakter} karakter van.")
    print()
    print()

print("Regisztrálj, ha még több karaktert szeretnél számoltatni.")
print("Írd:")
kerdes = input("ok / nemok: ")

if kerdes == "ok":
    print()
    input("Legnagyobb titkod: ")
    input("Személyes adataid: ")

    for i in range(200):

        szo = input("Írj be egy szót: ")
        karakter = len(szo)

        print(f"A szóban {karakter} karakter van.")
        print()
        print()

