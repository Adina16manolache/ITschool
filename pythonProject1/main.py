# #lista_caracter = ["*", "*","*", "*","*","*","*","*"]
# #for caracter in lista_caracter:
#     #print( "*", end="")
#     #print(" ")
#     #if lista_caracter == 7:
#         #print("*, *, *, *, *,*")
#
# #for row in range(12):
#     #for col in range(9):
#         #if col == 0 or (row == 11  and col > 0):
#            # print("*", end=" ")
#     #else:
#         #print(  end=" ")
#     #print()
#
# #while True: # 0<1
#        # numar = input("Numarul tau:")
#
#         #if numar == "-1":
#             #break
#
# nume_introduse = []
# note_romana = []
# note_mate = []
# note_optional = []
# while True:
#     nume = input("Nume :")
#     if nume == "gata":
#         participant_curent = 0
#         while participant_curent < len (nume_introduse):
#            media_notelor = (note_romana[participant_curent] + note_mate[participant_curent] + note_optional[participant_curent]) / 3
#            if media_notelor >= 6 and note_romana[participant_curent] >= 5 and note_mate[participant_curent] >= 5 and note_optional[participant_curent] :
#                print(f"{nume_introduse[participant_curent]}admis")
#            else:
#                print(f"{nume_introduse[participant_curent]}respins")
#         participant_curent += 1
#         break
#
#     nota_romana = int(input("nota romana:"))
#     nota_mate = int(input("nota mate:"))
#     nota_optional = int(input("nota optional:"))
#
#
#     nume_introduse.append(nume)
#     note_romana.append(nota_romana)
#     note_mate.append(nota_mate)
#     note_optional.append(nota_optional)
#  # print(nume_introduse):
#  # print(note_romana):
#  # print(note_mate):
#  # print(note_optional):
# scor_A = 0
# scor_B = 0
# scor_set_A = 0
# scor_set_B = 0
# def calculeaza_scor(scor):
#     """
#     Calculeaza scorul în funcție de rezultatul servei și scorul anterior.
#     :param scor: scorul jucătorului care a câștigat serva
#     :return: scorul recalculat al jucătorului care a câștigat serva
#     """
#     if scor <= 15:
#         scor += 15
#     elif scor == 30:
#         scor += 10
#     elif scor >= 40:
#         scor += 1
#     return scor
#
# def verifica_castigator(scor_A, scor_B):
#     """
#     Verifică dacă există un câștigător.
#     :param scor_A: scorul jucătorului A
#     :param scor_B: scorul jucătorului B
#     :return: returnează jucătorul câștigător în caz că există unul sau empty string dacă nu există încă
#     """
# castigator = " "
# if scor_A > 40 and scor_B < 40:
#     castigator = 'A'
# elif scor_B > 40 and scor_A < 40:
#     castigator = 'B'
# elif scor_A > 40 or scor_B > 40:
#     if scor_A - scor_B > 1:
#         castigator = 'A'
#     elif scor_B - scor_A > 1:
#         castigator = 'B'
#     return castigator
# #def calculeaza_scor_set(scor):
# #3 seturi din care castigatorul are 2 seturi castigate
# if scor_set_A >= 6 and scor_set_B < 5:
#         castigator = "A"

intrebarea_1 = {
    'text_intrebare': 'Care este valoare aproximativa a lui pi?',
    'variante': ['345', '14.5', '3.14'],
    'raspuns': "3"
}
intrebarea_2 = {
    "text_intrebare": "Care este cel mai inalt varf din Romania?",
    "variante": ["Omu", "Moldoveanu", "Papausa"],
    "raspuns": "2"
}
intrebarea_3 = {
    "text_intrebare": "Ce inaltime are pinguinul imperial in cm?",
    "variante": ["14", "120", "200"],
    "raspuns" : "2"
}
intrebarea_4 = {
    "text_intrebare": "Cati km sunt de la Bucuresti la Brasov?",
    "variante": ["180km", "168km","200km"],
    "raspuns": "2"
}
intrebarea_5 = {
    "text_intrebare": "Care este cel mai lung rau din lume?",
    "variante" : ["Dunarea"," Nilul","Amazon"],
    "raspuns": "2"
}
lista_intrebari=[intrebarea_1,intrebarea_2,intrebarea_3,intrebarea_4,intrebarea_5]
punctaj = 0
def quiz(intrebarea_1, intrebarea_2, intrebarea_3, intrebarea_4,intrebarea_5):
    print(intrebare["text intrebare"])
    print(intrebare["variante"])
    scrie_raspunsul = input("Intruduceti raspunsul dvs:")
    quiz(intrebarea_1, intrebarea_2, intrebarea_3, intrebarea_4,intrebarea_5)
    return
while True: #functia in
    for intrebare in lista_intrebari:
            print(intrebare["text_intrebare"])
            print(intrebare["variante"])
            scrie_raspunsul = input("Intruduceti raspunsul dvs:")
            if scrie_raspunsul == "exit":
                print('La revedere')
                break
            if scrie_raspunsul == intrebare["raspuns"]:
                punctaj += 1
                print("Ati raspuns corect")
            else:
                punctaj += 0
                print("Raspuns gresit")
            if lista_intrebari[2]:
                break













