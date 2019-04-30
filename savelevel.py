#Sauvegarder un niveau
# -*- coding: iso-8859-15 -*-
def savelevel(niveau):
	from os import chdir
	chdir ("saves/")
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
			save.write(str(positions[l][c]) + ",")
		save.write("|")
	save.close()
