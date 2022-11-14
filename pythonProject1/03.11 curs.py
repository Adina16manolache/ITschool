# def numele_functiei():
#     print('linie printată din interiorul funcției')#nu va afisa nimic
# numele_functiei()
# print('linie printată din afara funcției')
# numele_functiei()
# def input_in_functie():
#     input('Abia după ce introduci mesajul va fi executat printul (din codul principal) de după chemarea functiei: ')
# #inca nu afiseaza nimic
#     print('a trecut de input, ăsta e printul din interiorul funcției...poți scrie orice altceva aici. nu are legătură cu inputul')
# #inca nu
# print('înainte de chemarea funcției')
# #afiseaza ce ii ceri
# input_in_functie()#am chemat si apoi afiseaza
#
# print('\nlinie printată după chemarea funcției')
# def vegas():
#     ce_se_intampla_in_vegas = 'rămâne în vegas'#nu face nimic cu variabila
#     vegas()
# #de ce nu afiseaza? functia a fost chemata?
#     print(ce_se_intampla_in_vegas)
# def variabile_globale():
#     global numele_variabilei_globale
#     numele_variabilei_globale = 1
# variabile_globale()
# print(numele_variabilei_globale)

# def scoase_cu_return():
#     de_scos = 'de data asta e un string, dar obiectul returnat poate fi de orice fel (int, bool, listă, tuple etc.)'
#     return de_scos
# print(scoase_cu_return()) #afiseaza functia nu variabila? cum stie ce este de_scos

# income = {
# 'mere': 5420,
# 'paine': 3500,
# 'pere': 6000,
# 'visine': 3323,
#  'oua': 1212,
# 'banane': 5433
# }
# vanzari_totale = 0
# for vanzari_produs in income.values():
#
#     vanzari_totale += vanzari_produs
# print(vanzari_totale)




intrebarea_1 = {
    'text intrebare': 'Care este valoare aproximativa a lui pi?',
    'variante': ['345', '14.5', '3.14'],
    'raspuns': "3"
}
intrebarea_2 = {
    "text intrebare": "Care este cel mai inalt varf din Romania?",
    "variante": ["Omu", "Moldoveanu", "Papausa"],
    "raspuns": "2"
}
intrebarea_3 = {
    "text intrebare": "Ce inaltime are pinguinul imperial in cm?",
    "variante": ["14", "120", "200"],
    "raspuns" : "2"
}
intrebarea_4 = {
    "text intrebare": "Cati km sunt de la Bucuresti la Brasov?",
    "variante": ["180km", "168km","200km"],
    "raspuns": "2"
}
intrebarea_5 = {
    "text intrebare": "Care este cel mai lung rau din lume?",
    "variante" : ["Dunarea"," Nilul","Amazon"],
    "raspuns": "2"
}
lista_intrebari = [intrebarea_1, intrebarea_2,intrebarea_3, intrebarea_4, intrebarea_5]
# while loop cu meniu - prezentare meniu + input care ia opțiunea dorită
# logică de interat prin lista cu întrebări + afișare text întrebare și variante răspuns
# input la fiecare întrebare pentru selectarea variantei de răspuns
# logică comparare răspuns cu răspunsul corect
# calculare punctaj

# Sa scriem o aplicatie de tip quiz:
# Intrebarile se afla intr-o lista de dictionare, fiecare continand:
# O cheie contine un dictionar cu 2 elemente:
#     - textul intrebarii
#     - variante de raspuns (Avem 3 raspunsuri pentru fiecare intrebare, din care doar 1 este adevarat
# Trebuie sa avem cel putin 5 intrebari
# Meniu:
# 1. Start Quiz
# 2. Show score and reset (score)
# 3. Exit
# Scor - 1 punct/raspuns corect
punctaj = 0
print("Bine ati venit la quiz\n raspunsuri cu o singura varianta corecta \n Daca doriti sa abandonati quiz-ul scrieti:'exit'")


while True:
    for intrebare in lista_intrebari:
        print(intrebare["text intrebare"])
        print(intrebare["variante"])
        scrie_raspunsul = input("Introduceti raspunsul dvs:")
        if scrie_raspunsul == "exit":
            print('La revedere')
            break
        if scrie_raspunsul == intrebare["raspuns"]:
            punctaj += 1
            print("Ati raspuns corect")
        else :
            punctaj += 0
            print("Raspuns gresit")
        print(f"Ai terminat intrebarile! Scorul dvs final este:{punctaj}")

    if punctaj == 0:
        print(f"Ai terminat intrebarile! Scorul dvs final este:{punctaj}")
        break


# reluare_quiz = input("daca doriti sa reluati quiz-ul scrieti: 'da' ").lower
# if scrie_raspunsul == "da":
    #intoarce-te la prima intrebare


















