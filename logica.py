import pandas as pd
import random

name  = []
km = []
price = []

def readCsv():
    data = pd.read_csv('Datos.csv')
    for i in range(len(data['NOMBRE'])):
        print(i)
        name.append(data['NOMBRE'][i])
        km.append(float(data['KILOMETROS'][i]))
        price.append(float(data['PRECIO'][i]))
    print(name, km, price)

def proceso():
    # name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    initialPopulation = 15 #Comentar
    populationLimit = 20 #Comentar
    mutationIndividual = random.uniform(0.0, 0.9) #Comentar
    chromosomeMutation = random.uniform(0.0, 0.09) #Comentar
    resolution = random.uniform(0.0, 0.09) #Comentar
    generacion = 20

def main():
    readCsv()
    proceso()

main()