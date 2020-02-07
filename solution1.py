etoile_number = 1
input = 5

def print_char(number, char):
    for i in range(0,number):
        print(char, end='')

def calcul_nbre_espace(number_etoile, number_etage):
    number_etoile_base = number_etage * 2 - 1
    return int((number_etoile_base - number_etoile)/2)
    
    
for i in range(0,input):
    print_char(calcul_nbre_espace(etoile_number,input), " ")
    print_char(etoile_number, "*")
    print_char(calcul_nbre_espace(etoile_number,input), " ")
    etoile_number = etoile_number +2
    print("\n")
