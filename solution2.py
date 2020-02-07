etoile_number = 1
input = 5

def print_char(nb_espace, nb_etoile):
    chaine= ""
    for i in range(0,nb_espace):
        chaine = chaine + " "
    for i in range(0,nb_etoile):
        chaine = chaine + "*"
    for i in range(0,nb_espace):
        chaine = chaine + " "
        
    print(chaine + "\n")
    
#***************

def calcul_nbre_espace(number_etoile, number_etage):
    number_etoile_base = number_etage * 2 - 1
    return int((number_etoile_base - number_etoile)/2)
    
    
for i in range(0,input):
    print_char(calcul_nbre_espace(etoile_number,input), etoile_number)
    etoile_number = etoile_number +2
