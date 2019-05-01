# -*- coding: iso-8859-15 -*-

def parcourir(tab, nb, String):
	while nb < len(tab) and tab[nb] != String:
		nb += 1
	return nb

def incrementer(nb1, nb2):
	nb1 += 1
	nb2 = nb1


import Level
def lecture(nomLvl):
	nom = nomLvl

	lecture = open('saves/'+nom+'.lvl', "r")

	contenu = lecture.read()
	barre = '|'
	virgule = ';'
	
	
	compte = 0										#debut a 0
	parcourir(contenu, compte, barre)				#premiere barre (apres nom)
	nom = contenu[4 : compte]

	compte = compte + 6								#on saute le nom
	compte1 = compte
	parcourir(contenu, compte, virgule)
	rang1 = str(contenu[compte1 : compte])
	rang1 = int(rang1)
	
	incrementer(compte, compte1)
	parcourir(contenu, compte, virgule)
	rang2 = str(contenu[compte1 : compte])
	rang2 = int(rang2)
	
	incrementer(compte, compte1)
	parcourir(contenu, compte, virgule)
	rang3 = str(contenu[compte1 : compte])
	rang3 = int(rang3)								#fin des rangs
	
	
	
	incrementer(compte, compte1)					#saut point virgule
	compte = parcourir(contenu, compte, barre)
	rang = contenu[compte1 : compte]
	ligne = [0]*len(rang.split(','))
	ligne[0]= rang.split(',')
	
	i = 0
	while compte < len(contenu):
		incrementer(compte, compte1)
		parcourir(contenu, compte, barre)
		rang = contenu[compte1 : compte]
		ligne[i] = rang.spit(',')
		i += 1

	position = []
	for x in range(i):
		position.append(ligne[x])
	
	
	
	print str(rang1) + str(rang2) + str(rang3)
	print str(position)


	level = Level(nom, rang1, rang2, rang3)

	level.setPosition(position)


	return level