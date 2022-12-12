import random
from math import exp
import sys


class SimulatedAnnealing:
    # buat constructor
    def __init__(self, varRanges, numOfInitSolution, maxIter, stoppingValue, minTemperature):

        self.lowerBound = varRanges[0]
        self.upperBound = varRanges[1]
        self.numInitSolution = numOfInitSolution
        self.maxIter = maxIter
        self.stoppingValue = stoppingValue
        self.minTemperature = minTemperature

    # membuat fungsi objektif f(x,y) = x**2 + y**2
    def solution(self, variableDesignX, variableDesignY):
        return variableDesignX**2 + variableDesignY**2

     # membuat fungsi untuk menghitung temperature awal
    def getInitTemperature(self):
        # buat variable untuk menampung hasil rerata
        average = 0
        for _ in range(self.numInitSolution):
            # bangkitkan nilai acak dari batas yg sudah ada
            randomVariableDesignX = random.uniform(
                self.lowerBound, self.upperBound)
            randomVariableDesignY = random.uniform(
                self.lowerBound, self.upperBound)
            # solusi
            solusi = self.solution(randomVariableDesignX,
                                   randomVariableDesignY)

            # jumlahkan nilai hasil fungsi objektif
            average += solusi
            # kembalikan nilai solusi yang sudah dibagi nilai N
        return average / self.numInitSolution

    # fungsi solusi baru sebagai solusi tetangga
    def createCandidate(self):
        randomValue = random.uniform(0, 1)
        val = varRanges[0] + randomValue * (varRanges[1] - varRanges[0])
        return val

    def createNewVarRanges(self, candidate):
        lowerBound = -6 + candidate
        upperBound = 6 + candidate
        # if lowerBound < self.varRanges[0]:
        #     lowerBound = self.varRanges[0]
        # if upperBound > self.varRanges[1]:
        #     upperBound = self.varRanges[1]
        return [lowerBound, upperBound]

    # fungsi main untuk menjalankan program
    def mainSA(self):
        solusiList = []
        temperature = self.getInitTemperature()
        print('==== SIMULATED ANNEALING PROGRAM ====')
        print('temperature awal : ', temperature)
        print('rentang awal : [', self.lowerBound, self.upperBound, ']')
        randomVariableDesignX = random.uniform(
            self.lowerBound, self.upperBound)
        randomVariableDesignY = random.uniform(
            self.lowerBound, self.upperBound)
        solusi = self.solution(randomVariableDesignX, randomVariableDesignY)
        print('nilai x awal: ', randomVariableDesignX)
        print('nilai y awal: ', randomVariableDesignY)
        print('solusi awal: ', solusi)

        while temperature > self.stoppingValue:
            for i in range(self.maxIter):
                print('\niterasi ke ', i)
                candidateVariableDesignX = self.createCandidate()
                candidateVariableDesignY = self.createCandidate()
                candidateSolution = self.solution(
                    candidateVariableDesignX, candidateVariableDesignY)
                deltaE = candidateSolution - solusi
                print('Hasil delta E : ', deltaE)
                metropolis = exp(-deltaE/temperature)
                print('Metropolis : ', metropolis)

                u = random.uniform(0, 1)
                print('nilai acak: ', u)
                if deltaE <= 0 or u < metropolis:
                    newVarRanges = self.createNewVarRanges(
                        candidateVariableDesignX)
                    varRanges = newVarRanges
                    randomVariableDesignX = candidateVariableDesignX
                    randomVariableDesignY = candidateVariableDesignY
                    solusi = candidateSolution
                    print('Variable design x baru : ', randomVariableDesignX)
                    print('Variable design y baru : ', randomVariableDesignY)
                    print('Solusi baru : ', solusi)
                    print('Move: yes')
                    print('rentang baru : ', varRanges)
                    solusiList.append(solusi)
                else:
                    print('rentang : ', varRanges)
                    print('variable design x : ', randomVariableDesignX)
                    print('variable design y: ', randomVariableDesignY)
                    print('solusi: ', solusi)
                    solusiList.append(solusi)
                    print('Move: no')
            if solusi < self.stoppingValue and temperature <= self.minTemperature:
                print('variable design x : ', randomVariableDesignX)
                print('variable design y: ', randomVariableDesignY)
                print('solusi: ', solusi)
                print('Move: no')
                break
            else:
                temperature = 0.8 * temperature
                print('\ntemperature baru : ', temperature)
        print('\nMinimal Solusi : ', min(solusiList))


# inisialisasi variable
varRanges = [-5.12, 5.12]  # ranges variable design
numOfInitSolution = 4
maxIter = 2
stoppingValue = 5
minTemperature = 1

# run program
run = SimulatedAnnealing(varRanges, numOfInitSolution,
                         maxIter, stoppingValue, minTemperature)
run.mainSA()
