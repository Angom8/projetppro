# -*- coding: iso-8859-15 -*-

#Fonction permettant d'incrementer facilement fin
def parcourir(tab, nb, String):
	while nb < len(tab) and tab[nb] != String:
		nb += 1
	return nb

from Level import Level
#lecture d'un niveau a partir de la position relative de celui-ci. Le repertoire exacte doit etre indique
def lecture(pos):

	lecture = open(pos, "r")
	
	#on transforme le fichier en grand String
	contenu = lecture.read()
	
	#separateurs
	barre = '|'
	virgule = ';'
	
	
	fin = 0	#debut a 0
	fin = parcourir(contenu, fin, barre)#premiere barre (apres nom)
	nom = contenu[4 : fin]#Le nom va du caractere 4 (apres le "NOM:") jusqu'a la premiere barre

	fin = fin + 6#on saute le nom
	debut = fin
	fin = parcourir(contenu, fin, virgule)#on va au prochain point-virgule
	
	rang1 = str(contenu[debut : fin])#determination des rangs (partie fixe du fichier niveau)
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
	rang3 = int(rang3)#fin des rangs
	
	
	
	fin += 1
	debut = fin# on saute le  point virgule
	
	fin = parcourir(contenu, fin, barre)#on va a la derniere barre, apres les positions
	
	rang = contenu[debut : fin]
	position = [rang.split(',')]#on determine position en tant que tableau
	

	while contenu[fin] != '#' :
		fin += 1
		debut = fin
		if contenu[fin] != '#' :
			fin = parcourir(contenu, fin, barre)
			rang = contenu[debut : fin]
			position.append(rang.split(','))#et on lui place les bonnes valeurs


	level = Level(nom, rang1, rang2, rang3)#on cree nore fichier niveau

	level.setPosition(position)
	
	return(level)#et on le retourne 
	
#lecture du rang du niveau dans le fichier de sauvegardes du joueur, ignore le VOID:0
#Format de sauvegarde : VOID:0,nomduniveau:rang#
def lecturesave(niveau):
	#on ouvre le fichier contenant les sauvegardes du joueur
	lecture = open("saves/save.sv", "r")
	
	debut = 0
	fin = 0
	retour = 0
	
	#on transforme le fichier en grand String
	contenu = lecture.read()
	
	while str(contenu[debut+1:(fin)]) != niveau.getNom() and str(contenu[fin]) != "#":#tant que on ne l'a pas trouve ou que nous ne somme pas a la fin du fichier
		if fin != 0:
			debut = fin + 2
		fin += 1
		while str(contenu[fin]) != "#" and str(contenu[fin]) != ":":
			fin += 1
	
	if str(contenu[fin]) != "#":
		retour = int(contenu[fin+1])
		
	return(retour)
