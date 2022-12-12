from math import exp
import random
import sys


class SimulatedAnnealing:
    def __init__(self, varRanges, numOfInitSolution, maxIter, stoppingValue, minTemperature):
        self.varRanges = varRanges
        self.numOfInitSolution = numOfInitSolution
        self.maxIter = maxIter
        self.stoppingValue = stoppingValue
        self.minTemperature = minTemperature

    def getSolution(self, var):
        return var**2

    def getInitTemperature(self):
        ret = 0
        for _ in range(self.numOfInitSolution):
            solution = self.getSolution(random.uniform(
                self.varRanges[0], self.varRanges[1]))
            ret += solution
        return ret / self.numOfInitSolution

    def getCandidate(self, varRanges):
        u = random.uniform(0, 1)
        val = varRanges[0] + u * (varRanges[1] - varRanges[0])
        return val

    def getNewVarRanges(self, candidate):
        lowerBound = -6 + candidate
        upperBound = 6 + candidate
        if lowerBound < self.varRanges[0]:
            lowerBound = self.varRanges[0]
        if upperBound > self.varRanges[1]:
            upperBound = self.varRanges[1]

        return [lowerBound, upperBound]

    def mainSA(self):
        temperature = self.getInitTemperature()
        print('temperature awal : ', temperature)

        print('rentang awal : ', self.varRanges)
        solutionVals = random.uniform(self.varRanges[0], self.varRanges[1])
        print('variable design awal: ', solutionVals)

        solution = self.getSolution(solutionVals)
        print('solusi awal : ', solution)

        candidate = self.getCandidate(self.varRanges)
        print('\nvariable design baru : ', candidate)

        varRanges = self.getNewVarRanges(candidate)
        print(varRanges)

        while temperature > self.stoppingValue:
            for i in range(self.maxIter):
                candidate = self.getCandidate(self.varRanges)
                varRanges = self.getNewVarRanges(candidate)

                neighbor = self.getSolution(candidate)
                deltaE = neighbor - solution
                print('Hasil delta E : ', deltaE)
                metropolis = exp(-deltaE/temperature)
                print('Metropolis : ', metropolis)

                if deltaE <= 0 or random.uniform(0, 1) < metropolis:
                    solutionVals, solution = candidate, neighbor
                    print(candidate, neighbor)

            if solution < self.stoppingValue and temperature <= self.minTemperature:
                print(solution, solutionVals)
                break
            else:
                temperature = 0.8 * temperature


varRanges = [-5, 5]
numOfInitSolution = 4
maxIter = 2
stoppingValue = 0.005
minTemperature = 5

run = SimulatedAnnealing(varRanges, numOfInitSolution,
                         maxIter, stoppingValue, minTemperature)

run.mainSA()