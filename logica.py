from cv2 import FileNode_INT
import pandas as pd
import random

from datosAntena import Individual

nameData  = []
kmData = []
priceData = []
poblacion = []

def readCsv():
    data = pd.read_csv('Datos.csv')
    for i in range(len(data['NOMBRE'])):
        nameData.append(data['NOMBRE'][i])
        kmData.append(float(data['KILOMETROS'][i]))
        priceData.append(float(data['PRECIO'][i]))
    # print(nameData, kmData, priceData)

def proceso(areaCubrir, antenasOcupar):
    areaCubrir
    name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    initialPopulation = random.randint(5, 15) #Comentar
    populationLimit = random.randint(10, 15) #Comentar
    mutationIndividual = random.uniform(0.0, 0.9) #Comentar
    chromosomeMutation = random.uniform(0.0, 0.09) #Comentar
    generacion = random.randint(10, 27)
    individual = []

    # Creación de nuestra poblacion
    for i in range(0, initialPopulation):
        genotipo, fenotipo, aptitud = creacionGenotipo(antenasOcupar)
        ind = Individual(name[i], genotipo, fenotipo, aptitud)
        individual.append(ind)
    
    # Impresiones de nuestros individuos
    for i in range(len(individual)):
        print('id =', individual[i].name, 'Genotipo =', individual[i].genotipo, 'Fenotipo =', individual[i].fenotipo, 'Aptitud =', individual[i].aptitud)
    
    # Guardar individuos en la poblacion
    for i in range(len(individual)):
        poblacion.append(individual[i])
    
    # Realizacion de la 
    # for i in range(0, generacion):
    #     # gene = []
    #     print('Genracion cmp:', i+1)
    #     gene = cmp(poblacion, mutationIndividual, chromosomeMutation, intervalX[0], intervalY[0], resolution, numberValue, populationLimit)
    #     # print(gene[i][1])
    #     generacionSinPoda.append([i + 1, gene[0]])
    #     generacionPeor.append([i + 1, gene[1]])
    #     generacionPromedio.append([i + 1, gene[2]])
    #     generacionMejor.append([i + 1, gene[3]])

def creacionGenotipo(antenas):
    genotipo = []
    fenotipo = 0
    aptitud = 0.0
    for i in range(0, antenas):
        name = random.randint(0, len(nameData) - 1)
        # print('Vuelta', i, 'Random', name)
        genotipo.append(nameData[name])
        fenotipo += kmData[name]
        aptitud += priceData[name]
    return genotipo, fenotipo, aptitud

def main():
    readCsv()
    proceso(23, 6)

main()