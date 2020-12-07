import time
start_time = time.time()
time.sleep(25)
print("--- %s seconds ---" % (time.time() - start_time))


# Alpha vantage useful commands 
ticker = 'AAPl'
keys = 'E9HWKQFDFNS3Q3CJ' #random.choice(lines)

time = TimeSeries(key = keys, output_format = 'pandas')
data = time.get_intraday(symbol = ticker, interval = '1min', outputsize = 'full')

print(data)
data.history(period='1d',interval='1m', start='2020-12-04')

# Déroulement d'une journée

hour = 9
min = 0
start_time = time.time()
print(hour)
for heure in range(9,10):
    for minute in range(5):
        
        x = datetime.datetime(2020, 12, 4, hour, min, 0)
        y = datetime.datetime(2020, 12, 4, hour, min + 1, 0)
        
        dataDF = data.history(period='1d',interval='1m', start=x, end=y)
        dataDF = dataDF[['Open','Close','High','Low']]
        
        
        
        print(x, dataDF)
        time.sleep(0.5)
        
        
        
        min = min + 1
        if hour==17 and min==30:
            break
    hour = hour + 1
    min = 0
print("--- %s seconds ---" % (time.time() - start_time))
print('fin de la journée')


data = yf.Ticker("^FCHI")
dataDF = data.history(period='1d',interval='1m', start=datetime.datetime(2020, 12, 7, 9, 0, 0), 
                      end=datetime.datetime(2020, 12, 7, 9, 1, 0))
dataDF = dataDF[['Open','Close','High','Low']]
dataDF


# lISTE DES PARAM7TRE #
periode = 60 #Période de temps élémentaire entre 
t=0 
q=0.1 # taux gain 
event = [] # liste pour contrôler les actions

min = 0
datetime.datetime(2020, 12, 7, 9, min, 0)

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