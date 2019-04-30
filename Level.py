#Un niveau, avec 3 rangs et un nom definissant l'emplacement du fichier
# -*- coding: iso-8859-15 -*-
class Level(object):
	"""docstring for Level"""
	def __init__(self, nom, rang1, rang2, rang3):
		self.nom = nom
		self.rang1 = rang1
		self.rang2 = rang2
		self.rang3 = rang3
		self.position = []


	"""getters"""
	def getRang(self, rang):
		if rang == 1:
			return self.rang1
		elif rang == 2:
			return self.rang2
		else:
			return self.rang3


	def getNom(self):
		return self.nom


	def getPosition(self):
		return self.position
		
	def setPosition(self, tab) :
		self.position = tab
