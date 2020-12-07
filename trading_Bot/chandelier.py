class Chandelier:
  """Structure de données  """
  def __init__(self, per, ouv, clo, hau, bas):
        self.per = per
        self.ouv = ouv
        self.clo = clo
        self.hau = hau  
        self.bas = bas
    
  def couleur(self):
        if (self.ouv>self.clo):
          return "vert"
        else:
          return "rouge"