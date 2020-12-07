# -*- coding: utf-8 -*-
#######################################################################
######################## Trading Bot Algorithm ########################
#######################################################################

Date : 21/11/2020
Author : Damien Lida, Donovan Dimanche
Language : Python 3.8
Version : 1.0

pip install yfinance

import yfinance as yf
import portefeuille, chandelier, actif


"""Liste des variables a définir:

D : période à laquelle on récupère les données (structure chandelier)

P : période de temps élémentaire

Q1 : critère de gain positif

Q2 : critère de gain négatif

H1 : une heure de fin d’achat

H2 : une heure de fin de journée et on vend ce qui reste.

"""

data = yf.Ticker("^FCHI")
dataDF = data.history(period='1d',interval='1m', start='2020-12-04')
dataDF = dataDF[['Open','Close','High','Low']]
#Boucle sur des chandeliers
candlestick_list = []
for i in range(len(dataDF.index)):
    step =  dataDF.index[i]
    c = Chandelier("1m",dataDF.loc[step,'Open'],dataDF.loc[step,'Close'],
                   dataDF.loc[step,'High'],dataDF.loc[step,'Low'])

def test_gain_pos(i,q):
    if i<15:
        return False
    else:
        step =  dataDF.index[i]
        step_b =  dataDF.index[i-15]
        can_actuel = Chandelier("1m",dataDF.loc[step,'Open'],dataDF.loc[step,'Close'],
                       dataDF.loc[step,'High'],dataDF.loc[step,'Low'])
        can_depart_p = Chandelier("1m",dataDF.loc[step_b,'Open'],dataDF.loc[step_b,'Close'],
                       dataDF.loc[step_b,'High'],dataDF.loc[step_b,'Low'])

        if (can_actuel.ouv - can_depart_p.ouv)/can_depart_p.ouv*100 >= q:
            return True
        else:
            return False
        
def test_gain_neg(i,q):
    if i<15:
        return False
    else:
        step =  dataDF.index[i]
        step_b =  dataDF.index[i-15]
        can_actuel = Chandelier("1m",dataDF.loc[step,'Open'],dataDF.loc[step,'Close'],
                       dataDF.loc[step,'High'],dataDF.loc[step,'Low'])
        can_depart_p = Chandelier("1m",dataDF.loc[step_b,'Open'],dataDF.loc[step_b,'Close'],
                       dataDF.loc[step_b,'High'],dataDF.loc[step_b,'Low'])

        if (can_actuel.ouv - can_depart_p.ouv)/can_depart_p.ouv*100 <= q:
            return True
        else:
            return False
        
def mesure_gain(i):
    if i<15:
        return False
    else:
        step =  dataDF.index[i]
        step_b =  dataDF.index[i-15]
        can_actuel = Chandelier("1m",dataDF.loc[step,'Open'],dataDF.loc[step,'Close'],
                       dataDF.loc[step,'High'],dataDF.loc[step,'Low'])
        can_depart_p = Chandelier("1m",dataDF.loc[step_b,'Open'],dataDF.loc[step_b,'Close'],
                       dataDF.loc[step_b,'High'],dataDF.loc[step_b,'Low'])

        return (can_actuel.ouv - can_depart_p.ouv)/can_depart_p.ouv*100

def test_suivant(i):
    n_step = dataDF.index[i+1]
    n_candle = Chandelier("1m",dataDF.loc[n_step,'Open'],dataDF.loc[n_step,'Close'],
                       dataDF.loc[n_step,'High'],dataDF.loc[n_step,'Low'])
    if n_candle.couleur() == 'vert':
        return True
    else:
        return False

#######################################################################
######################## Corps du main         ########################
#######################################################################

t=0
q=0.1
event = []
if len(dataDF.index)>15:
  print("la1")
  for element in dataDF.index:
    step = dataDF.index[t]
    if t>15 and t<390:
      if test_gain_pos(t,q):
        if test_suivant(t):
          event.append("On ouvre une première fois")
          c = Chandelier("1m",dataDF.loc[step,'Open'],dataDF.loc[step,'Close'],dataDF.loc[step,'High'],dataDF.loc[step,'Low'])
          capital = capital - (10*1000/c.ouv)
        else:
          event.append("On ferme une fois simple")
          c = Chandelier("1m",dataDF.loc[step,'Open'],dataDF.loc[step,'Close'],dataDF.loc[step,'High'],dataDF.loc[step,'Low'])
          capital = capital + (10*1000/c.ouv)
      else:
        if not test_gain_pos(t,q):
          event.append("On est la")#si on reste constant a définir:
        else:
          if not test_suivant(t):
            if mesure_gain(t)<-q:
              event.append("On ferme dans un scénario de perte")
            else:
              if not test_suivant(t):
                event.append("On attends et on revient plus haut")
              else:
                event.append("On ouvre un peu plus bas")       
          else:
            event.append("On ouvre plus bas")
    else:
      event.append('On temporise')
    t = t + 1
    print(capital)
else:
  event.append("On ne peut rien faire")
