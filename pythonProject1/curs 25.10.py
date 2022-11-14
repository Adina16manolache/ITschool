
# def afiseaza_nume_intreg(nume, prenume):
#
#     print(nume + " / " + prenume)
#
# def constrieste_nume_intreg(nume, prenume):
#     return nume + " / " + prenume
#
# nume1 = "Popescu"
# nume2 = "Georgescu"
# nume3 = "Iliescu"
#
# prenume1 = "Adrian"
# prenume2 = "Catalina"
# prenume3 = "Ion"
#
# # print(nume1+prenume1)
# # print(nume2+ prenume2)
# # print(nume3+preume3)
# #inlocuit cu:
# # afiseaza_nume_intreg(nume1, prenume1)
# # afiseaza_nume_intreg(nume2,prenume2)
# # afiseaza_nume_intreg(nume3,prenume3)
#
# print(constrieste_nume_intreg(nume1, prenume1))
#4 functii adunare, scadere, inmultire, impartire

# a = int(input("cat este a?:"))
# b = int(input("cat este b?:"))
# def afisare_adunare(a, b):
#     rezultat = a + b
#     print(rezultat)
#
# afisare_adunare(a, b)
# afisare_adunare(5, 3)
# afisare_adunare(8, 2)
#
# def afisare_scadere(a, b):
#     rezultat = a - b
#     print(rezultat)
#
# afisare_scadere(a, b)

text1 = input("textul care se va cauta:")
text2 = input("textul in care se va cauta:")

def tema(text1, text2):
    if text1 in text2:
        print("s-a gasit!")
    else:
        print("nu s-a gasit!")
tema(text1, text2)






















