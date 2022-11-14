# def afiseaza_nume_intreg(nume, prenume):
#
#      print(nume + " / " + prenume)
#
#  def constrieste_nume_intreg(nume, prenume):
#      return nume + " / " + prenume
#
#  nume1 = "Popescu"
#  nume2 = "Georgescu"
#  nume3 = "Iliescu"
#
#  prenume1 = "Adrian"
#  prenume2 = "Catalina"
#  prenume3 = "Ion"
#
#  print(nume1+prenume1)
#   print(nume2+ prenume2)
#   print(nume3+preume3)
#  inlocuit cu:
#   afiseaza_nume_intreg(nume1, prenume1)
#   afiseaza_nume_intreg(nume2,prenume2)
#  afiseaza_nume_intreg(nume3,prenume3)

# def primire_invitati(lista_invitati, mod_de_salut):
#     for invitat in lista_invitati:
#         mod_de_salutat(invitat)
#     print("Iei haina")
#
# invitati = ["andrei", "Popescu", "Dorin"]
# mod_salut = salut_informal
# tip_eveniment = input("Scrieti tipul evenimentului(formal\informal): ")
# if tip_eveniment == "formal":
#     mod_salut = salut_formal
# primire_invitati(invitati, salut_formal)

scor_A = 0
scor_B = 0

def calculeaza_scor(scor):
    """
    Calculeaza scorul în funcție de rezultatul servei și scorul anterior.
    :param scor: scorul jucătorului care a câștigat serva
    :return: scorul recalculat al jucătorului care a câștigat serva
    """
    if scor <= 15:
        scor += 15
    elif scor == 30:
        scor += 10
    elif scor >= 40:
        scor += 1
    return scor

def verifica_castigator(scor_A, scor_B):
    """
    Verifică dacă există un câștigător.
    :param scor_A: scorul jucătorului A
    :param scor_B: scorul jucătorului B
    :return: returnează jucătorul câștigător în caz că există unul sau empty string dacă nu există încă
    """
    castigator = ''
    if scor_A > 40 and scor_B < 40:
        castigator = 'A'
    elif scor_B > 40 and scor_A < 40:
        castigator = 'B'
    elif scor_A > 40 or scor_B > 40:
        if scor_A - scor_B > 1:
            castigator = 'A'
        elif scor_B - scor_A >1:
            castigator = 'B'
    return castigator

jucator_A = input('numele jucatorului A: ')
jucator_B = input('numele jucatorului B: ')

while True:

    castigator_serva = input(f'castigatorul servei ({jucator_A}/{jucator_B}): ').upper()

    if castigator_serva == jucator_A.upper():
        scor_A = calculeaza_scor(scor_A)
    elif castigator_serva == jucator_B.upper():
        scor_B = calculeaza_scor(scor_B)

    elif castigator_serva == 'QUIT':
        print('quiting')
        break

    castigator = verifica_castigator(scor_A, scor_B)
    if castigator != '':
        print(f"""Castigatorul este {jucator_A if castigator == 'A' else jucator_B}
        Scor: {scor_A} : {scor_B}""")
        break
    print(f"Scor: {scor_A} : {scor_B}")
    #sa modificam pentru 3 sau 5 seturi,la 3 seturi castiga cine castiga 2 seturi
    # 5 seturi castiga cel care castiga 3 seturi