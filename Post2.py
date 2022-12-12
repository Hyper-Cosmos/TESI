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

    def getSolution(self, VariableDesignX, VariableDesignY):
        return VariableDesignX**2 + VariableDesignY**2

    def getInitTemperature(self):
        ret = 0
        for _ in range(self.numOfInitSolution):
            randomVariableDesignX = random.uniform(self.lowerBound, self.upperBound)
            randomVariableDesignY = random.uniform(self.lowerBound, self.upperBound)
            solution = self.getSolution(randomVariableDesignX,randomVariableDesignY)
            ret = ret + solution
        initTemperature = ret/self.numOfInitSolution
        return initTemperature

    def createNeighbor (self):
        randomValue = random.uniform(0,1)
        newVariableDesign = varRanges[0] + randomValue * (varRanges[1] - varRanges[0])
        return newVariableDesign

    def createNewRanges(self, variable):
        newlowerBound = -6 + variable
        newupperBound = 6 + variable
        # if newlowerBound < self.lowerBound:
        #     varRanges[0] = newlowerBound
        # if newupperBound > self.upperBound:
        #     varRanges[1] = newupperBound
        return [newlowerBound,newupperBound]


    def mainSA(self):
        solist = []
        randomValue = random.uniform(0,1)
        temperature = self.getInitTemperature()
        print('Temperature Awal : ',temperature)
        print("Range Awal : ", [self.lowerBound, self.upperBound]) 
        randomVariableDesignX = random.uniform(self.lowerBound, self.upperBound)
        randomVariableDesignY = random.uniform(self.lowerBound, self.upperBound)
        solution = self.getSolution(randomVariableDesignX, randomVariableDesignY)
        print("Solusi Awal : ",solution)
        
        while temperature > self.stoppingValue:            
             for i in range(self.maxIter):
                print('Iterasi Ke-',i)
                candidateVariableDesignX = self.createNeighbor()
                candidateVariableDesignY = self.createNeighbor()
                candidatesolution = self.getSolution(candidateVariableDesignX,candidateVariableDesignY)
                deltaE = candidatesolution - solution
                print('DeltaE :', deltaE)
                if deltaE <=0 :
                    solution = candidatesolution
                    newRanges = self.createNewRanges(candidateVariableDesignX)
                    varRanges = newRanges
                    print('New Ranges : ', varRanges)
                    print('Variable Design X : ', candidateVariableDesignX)
                    print('Variable Design Y : ', candidateVariableDesignY)
                    print('Solusi : ', solution)
                    print('Metropolis : ----')
                    print('Move : Yes')
                    solist.append(solution)
                else:
                    metropolis = exp(-deltaE/temperature)
                    if randomValue < metropolis:
                        solution = candidatesolution
                        varRanges = newRanges
                        print('New Ranges : ', newRanges)
                        print('Variable Design X : ', candidateVariableDesignX)
                        print('Variable Design Y : ', candidateVariableDesignY)
                        print('Solusi : ', solution)
                        print('Metropolis : ', metropolis)
                        print('Move : Yes')
                        solist.append(solution)                  
                    else:
                        print('New Ranges : ', varRanges)
                        print('Variable Design X : ', candidateVariableDesignX)
                        print('Variable Design Y : ', candidateVariableDesignY)
                        print('Solusi : ', solution)
                        print('Metropolis : ', metropolis)
                        print('Move : No')
                        solist.append(solution)   


             temperature = 0.8 * temperature

        print('\nMinimal Solusi : ', min(solist))
       
varRanges = [-5.12,5.12]
numOfInitSolution = 4
maxIter = 2
stoppingValue = 5
minTemperature = 1

run = SimulatedAnnealing(varRanges, numOfInitSolution, maxIter, stoppingValue, minTemperature)

run.mainSA()