from cmath import exp
from math import exp
import random
import sys

class SimulatedAnnealing:
    def __init__(self, varRanges, numOfInitSolution, maxIter, stoppingValue, minTemperature):
        self.lowerBound = varRanges[0]
        self.upperBound = varRanges[1]
        self.numOfInitSolution = numOfInitSolution
        self.maxIter = maxIter
        self.stoppingValue = stoppingValue
        self.minTemperature = minTemperature

    def getSolution(self, designVariable):
        return designVariable**2

    def getInitTemperature(self):
        ret = 0
        for _ in range(self.numOfInitSolution):
            randomVariableDesign = random.uniform(self.lowerBound, self.upperBound)
            solution = self.getSolution(randomVariableDesign)
            #print("Variabel Desain : ", randomVariableDesign, "Solusi : ", solution, "Jumlah : ", ret)
            ret = ret + solution
        initTemperature = ret/self.numOfInitSolution
        return initTemperature

    def createNeighbor (self, lowerBound, upperBound, randomValue):
        newVariableDesign = lowerBound + randomValue * (upperBound-lowerBound)
        return newVariableDesign

    def createNewRanges(self, newlowerBound, newupperBound):
        newlowerBound = 6 - self.lowerBound
        newupperBound = 6 + self.upperBound
        if newlowerBound < self.lowerBound:
            varRanges[0] = newlowerBound
        if newupperBound > self.upperBound:
            varRanges[1] = newupperBound
        return [newlowerBound,newupperBound]


    def mainSA(self):
        randomValue = random.uniform(0,1)
        #solusi awal
        temperature = self.getInitTemperature()
        # print(temperature)
        # sys.exit()
        randomVariableDesign = random.uniform(self.lowerBound, self.upperBound)
        solution = self.getSolution(randomVariableDesign)
        print("Range Lama : ",varRanges)
        print("Solusi Lama : ", randomVariableDesign, solution)
        newRanges = self.createNewRanges(self.lowerBound,self.upperBound)
        while temperature > self.minTemperature:            
             print('Temperature : ', temperature)
             for i in range(self.maxIter):
                # print(i)
                
                candidateVariableDesign = self.createNeighbor(self.lowerBound, self.upperBound, randomValue)
                candidatesolution = self.getSolution(candidateVariableDesign)

                deltaE = candidatesolution - solution
                print('DeltaE :', deltaE)
                if deltaE <=0 :
                    solution = candidatesolution
                    print('New Ranges : ', newRanges, 'Variable Design : ', candidateVariableDesign, 'Solusi : ', solution, 'p','---','r', 'Move : Yes' )
                else:
                    metropolis = exp(-deltaE/temperature)
                    # print(metropolis, randomValue)
                    # sys.exit()
                    if randomValue < metropolis:
                        solution = candidatesolution
                        print('New Ranges : ', newRanges, 'Variable Design : ', candidateVariableDesign, 'Solusi : ', solution, 'Metropolis : ',metropolis, 'r :',randomValue, 'Move : Yes' )
                    else:
                        print('New Ranges : ', newRanges, 'Variable Design : ', candidateVariableDesign, 'Solusi : ', solution, 'Metropolis : ',metropolis, 'r :',randomValue, 'Move : No' )


             temperature = 0.8 * temperature

        #solusi baru
        # randomValue = random.uniform(0,1)
        # candidateVariableDesign = self.createNeighbor(self.lowerBound, self.upperBound, randomValue)
        # candidateSolution = self.getSolution(candidateVariableDesign)
        # print("Solusi Baru : ",candidateVariableDesign,candidateSolution)

        # deltaE = candidateSolution - solution
        # if deltaE <= 0:
        #     solution = candidateSolution
        #     randomVariableDesign = candidateVariableDesign
        #     print("Solusi Saat ini : ", randomVariableDesign, solution)
        # else:
        #     print("Hitung Metropolis")

        
varRanges = [-5,5]
numOfInitSolution = 4
maxIter = 2
stoppingValue = 0.005
minTemperature = 1

run = SimulatedAnnealing(varRanges, numOfInitSolution, maxIter, stoppingValue, minTemperature)

run.mainSA()