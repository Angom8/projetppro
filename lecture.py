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
	
	
	fin = 0										#debut a 0
	parcourir(contenu, fin, barre)				#premiere barre (apres nom)
	nom = contenu[4 : fin]

	fin = fin + 6								#on saute le nom
	debut = fin
	fin = parcourir(contenu, fin, virgule)
	rang1 = str(contenu[debut : fin])
	rang1 = int(rang1)
	
	incrementer(fin, debut)
	fin = parcourir(contenu, fin, virgule)
	rang2 = str(contenu[debut : fin])
	rang2 = int(rang2)
	
	incrementer(fin, debut)
	fin = parcourir(contenu, fin, virgule)
	rang3 = str(contenu[debut : fin])
	rang3 = int(rang3)								#fin des rangs
	
	
	
	incrementer(fin, debut)					#saut point virgule
	fin = parcourir(contenu, fin, barre)
	rang = contenu[debut : fin]
	ligne = [0]*len(rang.split(','))
	ligne[0]= rang.split(',')
	
	i = 0
	while fin < len(contenu):
		incrementer(fin, debut)
		fin = parcourir(contenu, fin, barre)
		rang = contenu[debut : fin]
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