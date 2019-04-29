def savelevel(niveau)
	from os import chdir
	chdir ("saves/")
	save = open('levels.lvl', 'a')
	"separateur inter-niveaux"
	save.write('################################')
	"nom"
	save.write('NOM:' + niveau.getNom() +'|')
	"rangs et temps"
	save.write('RANG:' + "RANG1;" + niveau.getRang(1) + ",RANG2;" + niveau.getRang(2) + ",RANG3;"+ niveau.getRang(3) +'|')
	"le niveau en lui-même"
	l, c = 0
	positions =  niveau.getPosition()
	while l < positions.len()
		while c < l < positions.len()
			save.write(positions[l][c])
			c++
		l++
	save.close()
