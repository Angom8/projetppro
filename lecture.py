# -*- coding: iso-8859-15 -*-

def parcourir(tab, nb, String):
	while nb < len(tab) and tab[nb] != String:
		nb += 1
	return nb

from Level import Level
def lecture(pos):# pos = repertoire du fichier avec nom deja indique

	lecture = open(pos, "r")

	contenu = lecture.read()
	barre = '|'
	virgule = ';'
	
	
	fin = 0										#debut a 0
	fin = parcourir(contenu, fin, barre)				#premiere barre (apres nom)
	nom = contenu[4 : fin]

	fin = fin + 6								#on saute le nom
	debut = fin
	fin = parcourir(contenu, fin, virgule)
	rang1 = str(contenu[debut : fin])
	rang1 = int(rang1)
	
	fin += 1
	debut = fin
	
	fin = parcourir(contenu, fin, virgule)
	rang2 = str(contenu[debut : fin])
	rang2 = int(rang2)
	
	fin += 1
	debut = fin
	fin = parcourir(contenu, fin, virgule)
	rang3 = str(contenu[debut : fin])
	rang3 = int(rang3)								#fin des rangs
	
	
	
	fin += 1
	debut = fin					#saut point virgule
	fin = parcourir(contenu, fin, barre)
	rang = contenu[debut : fin]
	position = [rang.split(',')]
	

	while contenu[fin] != '#' :
		fin += 1
		debut = fin
		if contenu[fin] != '#' :
			fin = parcourir(contenu, fin, barre)
			rang = contenu[debut : fin]
			position.append(rang.split(','))


	level = Level(nom, rang1, rang2, rang3)

	level.setPosition(position)
	
	return(level)
	
def lecturesave(niveau):

	lecture = open("saves/save.sv", "r")
	
	retour = 0
	contenu = lecture.read()
	debut = 0
	fin = 0
	
	while str(contenu[debut+1:(fin)]) != niveau.getNom() and str(contenu[fin]) != "#":#tant que on ne l'a pas trouve ou que nous ne somme pas a la fin du fichier
		if fin != 0:
			debut = fin + 2
		fin += 1
		while str(contenu[fin]) != "#" and str(contenu[fin]) != ":":
			fin += 1
	
	if str(contenu[fin]) != "#":
		retour = int(contenu[fin+1])
		
	return(retour)
	
			
	
