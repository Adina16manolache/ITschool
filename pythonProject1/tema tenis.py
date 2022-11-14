jucator_A = input('numele jucatorului A: ')
jucator_B = input('numele jucatorului B: ')
scor_A = 1
scor_B = 1

while scor_A > 6 and scor_B >= 5 :
    print(scor_A , scor_B)
    if scor_A == 6:
        break
    scor_A += 1
else:
    print("a castigat jucator_B ")

