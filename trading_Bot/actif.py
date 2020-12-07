class Actif:
	""" Une classe pour définir les sous jacents qui seront tradés """
	def __init__(self, type_actif):
		self.type_actif = type_actif


class Action (Actif):
	""" Une classe qui étend la notion d'actif """
	def __init__(self, type_actif, nominal):
		actif.__init__(self, type_actif)
		self.nominal = nominal
