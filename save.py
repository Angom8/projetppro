#Sauvegarder un niveau
# -*- coding: iso-8859-15 -*-
def savelevel(niveau):
	from os import chdir
	chdir ("levels/")
	save = open(niveau.getNom() + ".lvl", 'w')
	save.write('NOM:' + niveau.getNom() +'|')
	"rangs et temps"
	save.write('RANG:' + str(niveau.getRang(1)) + ";" + str(niveau.getRang(2)) + ";" + str(niveau.getRang(3)) + ";")
	"le niveau en lui-même"
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
	
def removesave(niveau):
	efface = open("saves/save.sv", "w")
	
	contenu = lecture.read()
	debut = 0
	fin = 4
	
	while str(contenu[debut:fin]) != niveau.getNom() and tab[fin] != "#":#tant que on ne l'a pas trouve ou que nous ne somme pas a la fin du fichier
		debut = fin
		while contenu[fin] != "#" and contenu[fin] != ",":
			fin += 1
	
	if contenu[fin] != "#":
		while contenu[debut] != "," or contenu[debut] != "#":
			contenu.remove(debut)
			i += 1
			
	efface.close
	efface = open("saves/save.sv", "a")
	efface.write(str(contenu))
	
