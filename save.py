# -*- coding: iso-8859-15 -*-


#Sauvegarder un niveau avec le format suivant
#NOM:nomduniveau|RANG:10;20;30;1,1,2,2,3|1,4,5,5,3|1,4,5,5,3|1,4,5,5,3|6,6,6,6,3|#
def savelevel(niveau):

	save = open("levels/" + niveau.getNom() + ".lvl", 'w')
	
	save.write('NOM:' + niveau.getNom() +'|')

	save.write('RANG:' + str(niveau.getRang(1)) + ";" + str(niveau.getRang(2)) + ";" + str(niveau.getRang(3)) + ";")

	l = 0
	c = 0
	positions =  niveau.getPosition()
	for l in range(len(positions)) :
		for c in range(len(positions[l])) :
			save.write(str(positions[l][c]))
			if c+1 < len(positions[l]): 
				save.write(",")
		save.write("|")
	save.write("#")
	save.close()

#Sauvegarder la progression d'un niveau
def addsave(niveau, rang):

        add = open("saves/save.sv", "r")
        raw = add.read()
	x = raw.find(niveau.getNom())

	if x != -1 :
		x += len(niveau.getNom())
		x += 1
		contenu = [i for i in raw]#on convertit en tableau
		contenu[x] = str(rang) 
		add.close()
      		#on ecrase le fichier
      		ad = open("save.sv", "w")
        	for c in range(len(contenu)):
        		ad.write(str(contenu[c]))
       		ad.close()
	
	else:
		contenu = [i for i in raw]#on convertit en tableau
       	 	#on definit la nouvelle fin du fichier 
       	 	contenu.remove('#')
        	if contenu.count('\n') > 0
        		contenu.remove('\n')
		add.close()  
		retour = ""
		#on ecrase le fichier
		for c in range(len(contenu)):
        		retour += str(contenu[c])
		ad = open("save.sv", "w")
		ad.write(retour + "," + niveau.getNom() + ":" + str(rang) + "#")
		ad.close()
#Effacer la progression d'un niveau
def removesave(niveau):

	efface = open("saves/save.sv", "r")
	
	raw = efface.read()
	contenu = [i for i in raw]#on convertit en tableau
	debut = 0
	fin = 0
	
	while str(contenu[debut+1:(fin)]) != niveau.getNom() and str(contenu[fin]) != "#":#tant que on ne l'a pas trouve ou que nous ne somme pas a la fin du fichier
		if fin != 0:
			debut = fin + 2
		fin += 1
		while str(contenu[fin]) != "#" and str(contenu[fin]) != ":":
			fin += 1
	
	if contenu[fin] != "#":
		while contenu[debut] != "," or contenu[debut] != "#":
			contenu.remove(debut)
			
	#on definit la nouvelle fin du fichier
	contenu.remove(len(contenu)-1)
			
	efface.close()
	efface = open("saves/save.sv", "w")
	for i in range(len(contenu)):
		efface.write(str(contenu[i]))
	efface.write("#")
	efface.close()
