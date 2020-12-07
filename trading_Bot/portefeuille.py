class Portefeuille:
    """ Pour gérer les interactions ordre/capital """
    def __init__(self, capital, actif):
      self.capital = capital
      self.actif = actif
      self.unit = 0
    
    def ouv_pos(self, ouv, risk):
      self.capital = self.capital - risk
      actif = actif + risk
      unit = unit + risk/ouv

    def clo_pos(self, clo, risk):
      self.capital = self.capital + clo*unit
      actif = actif - clo*unit
