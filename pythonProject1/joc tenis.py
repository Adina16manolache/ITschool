#2 jucatori
#1 game
# scor = [0,15,30,40]
# jucatori = ['jucator1', 'jucator2']
# jucator1 = int(input("jucator1:"))
# jucator2 = int(input("jucator2:"))
#   while True:
#      nume = input("nume_jucator1":)
#      if scor > 40:
#          print("castigator jucatorul 1")

# an = int(input("anul:"))
# if an % 4 == 0 and an % 100 != 0 or an % 400 == 0:
#     print("anul este bisect")
# else:
#     print("anul nu este bisect")
# print(type(an))

# numar = int(input("Numar:"))
#
# suma = 0
# pas = 1
# while pas <= numar:
#    suma += pas
#    print( "Am adaugat" , pas , " la suma")
#    print("suma a devenit", suma)
#    pas += 1
# print(suma )

# numar = int(input("Numar:"))
#
# pas = 1
# while pas <= numar:
#    patrat = pas ** 2
#    print(patrat)
#    pas += 1

#exercitiul nr 1

# nume = input("Numele este:")
# varsta = int(input("varsta:"))
# anul = 2022 - varsta + 100
# print("numele tau este " + nume )
# print( nume, "vei avea 100 de ani in anul", " " + str(anul))

#exercitul 2

# numarul_introdus = int(input('numarul'))
# creste_cu_unu = 0
# while numarul_introdus > 0:
#      numarul_introdus = int(numarul_introdus / 10)
#      creste_cu_unu = creste_cu_unu + 1
# print("numarul de cifre este:", creste_cu_unu)

#exercitiul3
#Scrieti un program care sa citeasca un numar de la tastatura si sa intoarca inversul lui (1234 -> 4321)

# numar = int(input("introduceti un numar:"))
# inversul_numarului = 0
# while numar > 0:
#     inversul_numarului = (numar % 10) + inversul_numarului * 10
#     numar = int(numar / 10)
# print(inversul_numarului)
#alta varianta
# text = input("introdu textul: ")
# print(text[::-1])

# print(132 / 10)
# print(int(132 / 10))
# print(132 % 10)

# lista_de_cumparaturi = ["mezeluri", "parjituri", "fructe", "vin", "paine"]
# sterge = input("ce doriti sa stergeti:")
# print(lista_de_cumparaturi.remove(sterge))
# print(lista_de_cumparaturi)
# lista_de_cumparaturi.remove("paine")
# print(lista_de_cumparaturi)
# print(lista_de_cumparaturi[-1]) #???
# lista_de_cumparaturi.append("biscuiti")
# print(lista_de_cumparaturi)
# daca nu stiu ce cuprinde lista?
# lista_de_cadouri = []
# print(lista_de_cadouri)


# text_numar = "introduceti un numar:"
# print(f"tipul variabilei text_numar este: {type(text_numar)}")
# numar = int(input(text_numar))
# print(f"tipul variebilei numar este: {type(numar)}")
# #conditie de iterare
# while numar > 0:
#     #ce se executa la fiecare pas
#     ultima_cifra = numar % 10
#     print(ultima_cifra)
#     #cum trec la pasul urmator
#     numar = numar // 10


#de la ce plec
cifra = 1
numar = 0
#conditia de iterare
while cifra > 0:
    # cum trec la pasul urmator
    cifra = int(input("cifra introdusa"))
    #ce se executa la fiecare pas
    numar = numar * 10 + cifra
    print(numar)















