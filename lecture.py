
def lecture(Level level):
	nom = level.getNom()

	lecture = open("saves/"+nom+".lvl", "r")

	contenu = lecture.read()

	nom = [4 : ]