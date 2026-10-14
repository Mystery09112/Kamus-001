word = input("Masukan kata")

if len(word) > 10:
    print(word[:10]+"...")
else:
    print(word)
