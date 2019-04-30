def parcourir(tab, nb, String):
	while nb < len(tab) and tab[nb] != String:
        nb += 1
    return nb

def incrementer(nb1, nb2):
	nb2 = nb1
	nb1 += 1


import Level
def lecture(nomLvl):
	nom = nomLvl

	lecture = open('saves/'+nom+'.lvl', "r")

	contenu = lecture.read()
	barre = '|'
	virgule = ';'

    compte = 0
    parcourir(contenu, compte, barre)
	nom = contenu[4 : compte]

	compte1 = compte + 6
	parcourir(contenu, compte, virgule)
    rang1 = int(contenu[compte1 : compte])

    incrementer(compte, compte1)
    parcourir(contenu, compte, virgule)
    rang2 = int(contenu[compte1 : compte])

    incrementer(compte, compte1)
    parcourir(contenu, compte, virgule)
    rang3 = int(contenu[compte1 : compte])


    i = 0
    while compte len(contenu)
    	incrementer(compte, compte1)
    	parcourir(contenu, compte, barre)
    	rang = contenu[compte1 : compte]
    	ligne[i] = rang.spit(',')
    	i += 1

    position = []
    for x in range(i)
    	position.append(ligne[x])




    level = Level(nom, rang1, rang2, rang3)

    level.setPosition(position)


    return level