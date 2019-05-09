# -*- coding: iso-8859-15 -*-

class Level(object):
	#Chaque niveau possede un nom et 3 entiers definissants les temps max en secondes pour les rangs 1 2 et 3
	def __init__(self, nom, rang1, rang2, rang3):
		self.nom = nom
		self.rang1 = rang1
		self.rang2 = rang2
		self.rang3 = rang3
		self.position = []


	#Getter de Rang. Retourne la valeur en seconde en specifiant le rang voulu.
	def getRang(self, rang):
		if rang == 1:
			return self.rang1
		elif rang == 2:
			return self.rang2
		else:
			return self.rang3

	#Getter du Nom
	def getNom(self):
		return self.nom

	#Getter du tableau de positions des blocs
	def getPosition(self):
		return self.position

	#Getter setPosition pour la creation de niveau
	def setPosition(self, tab) :
		self.position = tab
	
	#Pas utile. Permet d'afficher la description du niveau
	def _str_(self):
		result = 'Niveau :' + self.nom + 'de rang 1 : ' + self.rang1 + ', rang 2 : ' + self.rang2 + ' et de rang 3 : ' + self.rang3
		return result
