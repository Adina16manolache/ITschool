#scrieti un program care primeste de la utilizator o suma, o moneda de input si
# o moneda in care vrea sa schimbe si afiseaza suma pe care trebuie
#sa o primeasca  in noua moneda
#ce moneda doriti sa schimbati?ron
#ce suma?
#in ce moneda doriti sa schimbati?euro
ron = 1
eur = 5
lira = 5.66
euro_in_lira = 0.87
lira_in_euro = 1.15
#conditie de iterare
while True:

    print("daca doriti sa renuntati scrie gata")
    suma = int(input("ce suma doriti sa schimbati?"))
    moneda_din_portofel = input("Alege moneda ron , euro , lira: ")  # intrebam utilizatorul din ce moeda vrea sa schimbe
    if moneda_din_portofel == "gata":
        print("Doamne ajuta")
        break
    moneda_de_schimb = input("Moneda in care vreti sa schimbati , ron, euro, lira: ")
    if moneda_din_portofel == "eur" and moneda_de_schimb == "ron":
        rezultat_conversie = suma * eur
        print(rezultat_conversie)

    elif moneda_din_portofel == "lira" and moneda_de_schimb == "ron":
        rezultat_conversie = suma * lira
        print(rezultat_conversie)

    elif moneda_din_portofel == "euro" and moneda_de_schimb == "lira":
        rezultat_conversie = suma * euro_in_lira
        print(rezultat_conversie)

    elif moneda_din_portofel == "lira" and moneda_de_schimb == "euro":
        rezultat_conversie = suma * lira_in_euro
        print(rezultat_conversie)

    elif moneda_din_portofel == "ron" and moneda_de_schimb == "lira":
        rezultat_conversie = suma / lira
        print(rezultat_conversie)

    elif moneda_din_portofel == "ron" and moneda_de_schimb == "euro":
        rezultat_conversie = suma / eur
        print(rezultat_conversie)

    else:
        print("Nu exista moneda introdusa")


# text = input("introdu textul: ")
# print(text[::-1])


