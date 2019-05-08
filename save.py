#Sauvegarder un niveau
# -*- coding: iso-8859-15 -*-
def savelevel(niveau):
	save = open("levels/" + niveau.getNom() + ".lvl", 'w')
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

def addsave(niveau, rang):
        add = open("saves/save.sv", "r")
        contenu = add.read()
        contenu.remove(len(contenu)-1)
        add.close()
        ad = open("saves/save.sv", "a")
        ad.write(str(contenu[0:(len(contenu)-1)] + str("," + niveau.getNom() + ":" + str(rang) + "#")))
        ad.close()

def removesave(niveau):
	efface = open("saves/save.sv", "r")
	
	raw = efface.read()
	contenu = [i for i in raw]
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
		
	contenu.remove(len(contenu)-1)
			
	efface.close()
	efface = open("saves/save.sv", "w")
	for i in range(len(contenu)):
		efface.write(str(contenu[i]))
	efface.write("#")
	efface.close()
