girilen_yazi = input("Lütfen herhangi bir şey yazın: ")
yazinin_tersi = ""


def tersini_alma(yazi, tersi):
    for i in range(len(yazi) - 1, -1, -1):
        tersi += yazi[i]
    return tersi

if " " in girilen_yazi:
    # Eğer girilen veri içerisinde boşluk varsa, bir cümle olarak kabul ettik
    ters_cumle = tersini_alma(girilen_yazi, yazinin_tersi)
    print("Girilen yazı bir CÜMLE.")
    print("Cümlenin tersi:", ters_cumle)

else:
    # Eğer girilen veri içerisinde boşluk yoksa, bir kelime olarak kabul ettik
    ters_kelime = tersini_alma(girilen_yazi, yazinin_tersi)
    print("Girilen yazı bir KELİME.")
    print("Kelimenin tersi:", ters_kelime)


