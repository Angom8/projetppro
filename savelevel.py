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
	while l < len(positions):
		while c < len(positions[0]):
			save.write(str(positions[l][c]))
			c += 1
		save.write("|")
		l += 1
		c = 0 
	save.close()
