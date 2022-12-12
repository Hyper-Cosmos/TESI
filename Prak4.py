from operator import index
import random, sys
from collections import deque

class GeneticAlgorithm:
    def __init__(self, parameters):
        self.numOfChromosome = parameters['numOfChromosome']
        self.numOfDimension = parameters['numOfDimension']
        self.lowerBound = parameters['lowerBound']
        self.upperBound = parameters['upperBound']
        self.maxGeneration = parameters['maxGen']
        self.stoppingFitness = parameters['stoppingFitness']
        self.cr = parameters['crossoverRate']
        self.mr = parameters['mutationRate']

    def sumSquareTestFunction(self, chromosome):
        sumResult = 0 
        for i in range(len(chromosome)):
            sumResult = sumResult + ((i+1) * pow(chromosome[i],2))
        return abs(sumResult)

    def calcFitnessValue(self, objectiveValue):
        return 1 / (1+objectiveValue)

    def replaceChromosomesElement(self, chromosomes, chromosome, index):
        chromosomes[index] = chromosome
        return chromosomes

    def selectCandidateChromosomes(self, probCumulatives, chromosomes):
        rets = []
        for i in range(len(probCumulatives)):
            randomValue = random.uniform(0,1)
            if randomValue > probCumulatives[i] and randomValue <= probCumulatives[i+1]:
                rets.append({'index' : i,'chromosome' : chromosomes[i+1]})
        return rets
    
    def selectRoletteWheelChromosome(self, fitnessValues, chromosomes):
        probCumulative = 0
        probCumulatives = []
        for fitnessValue in fitnessValues:
            probability = fitnessValue / sum(fitnessValues)
            probCumulative = probCumulative + probability
            probCumulatives.append(probCumulative)
        # print(probability)]
        selectedCandidateChromosomes = self.selectCandidateChromosomes(probCumulatives,chromosomes)
        # print(selectedCandidateChromosomes)
        while len(selectedCandidateChromosomes) == 0:
            selectedCandidateChromosomes = self.selectCandidateChromosomes(probCumulatives,chromosomes)
        return selectedCandidateChromosomes
    
    def generateRandomValues(self):
        rets = []
        for i in range(self.numOfChromosome):
            if random.uniform(0,1) < self.cr:
                rets.append(i)
        return rets

    def mainGA(self):
        varValues = []
        chromosomes = []
        for _ in range(self.numOfChromosome):
            for _ in range(self.numOfDimension):
                randomvalue = random.uniform(self.lowerBound,self.upperBound)
                varValues.append(randomvalue)
            chromosomes.append(varValues)
            varValues = [] 
        # print(chromosomes)

        objectiveValues = []
        for chromosome in chromosomes :
            objectiveValues.append(self.sumSquareTestFunction(chromosome))
        # print(objectiveValues)

        fitnessValues = []
        for objectiveValue in objectiveValues:
            fitnessValues.append(self.calcFitnessValue(objectiveValue))
        # print(fitnessValues)

        candidateNewChromosomes = self.selectRoletteWheelChromosome(fitnessValues, chromosomes)
        for candidateNewChromosome in candidateNewChromosomes:
            chromosome = self.replaceChromosomesElement(chromosomes, candidateNewChromosome['chromosome'], candidateNewChromosome['index'])
        # print(chromosome)
    
        for k in range(self.maxGeneration):
            print('Generation-',k)
            randomIndexValues = self.generateRandomValues()
            # print(randomIndexValues)
            while len(randomIndexValues) <= 1:
                randomIndexValues = self.generateRandomValues()
            # print(randomIndexValues)
            selectedChromosomesToCrossover = []
            for i in randomIndexValues:
                selectedChromosomesToCrossover.append({'chromosomes':chromosomes[i],'index':i})
            # print(selectedChromosomesToCrossover)

            parentCandidateIndex = []
            for i in selectedChromosomesToCrossover:
                for j in selectedChromosomesToCrossover:
                    if i['index'] != j['index']:
                        parentCandidateIndex.append([i['index'],j['index']]) 
            # print(parentCandidateIndex)             
          

            sortedParentIndexes = []
            for parentIndex in parentCandidateIndex:
                parentIndex.sort()
                sortedParentIndexes.append(parentIndex)
            # print(sortedParentIndexes)
            finalParentIndexes = []
            for sortedParentIndex in sortedParentIndexes:
                if sortedParentIndex not in finalParentIndexes:
                    finalParentIndexes.append(sortedParentIndex)
            # print(finalParentIndexes)
            
            tempOffsets = []
            offsets = []
            for parentIndex in finalParentIndexes:
                cutPointIndex = random.randint(0,self.numOfDimension-1)
                if cutPointIndex == self.numOfDimension-1:
                    for i in range(self.numOfDimension):
                        if i < self.numOfDimension-1:
                            tempOffsets.append(chromosomes[parentIndex[1]][i])
                        else:
                            tempOffsets.append(chromosomes[parentIndex[0]][cutPointIndex])
                else:
                    for i in range(self.numOfDimension):
                        if i <= cutPointIndex:
                            tempOffsets.append(chromosomes[parentIndex[0]][i])
                        else:
                            tempOffsets.append(chromosomes[parentIndex[1]][i])
                # print(chromosomes[parentIndex[0]],' X ',chromosomes[parentIndex[1]])
                # print(tempOffsets)
                # sys.exit()
                offsets.append(tempOffsets)
                tempOffsets = []
            # print(offsets)
            # sys.exit()


            tempChromosomes = []
            chromosomesOffsets = chromosomes + offsets
            for chromosome in chromosomesOffsets:
                objectiveValue = self.sumSquareTestFunction(chromosome)
                fitnessValue = self.calcFitnessValue(objectiveValue)
                tempChromosomes.append([fitnessValue, chromosome])  
            # print(tempChromosomes)
            # sys.exit()
            tempChromosomes.sort(reverse=True)
            # print(tempChromosomes)
            # sys.exit()
            chromosomes = []
            for i in range(len(tempChromosomes)):
                if i <= self.numOfChromosome-1:
                    chromosomes.append(tempChromosomes[i][1])
            tempChromosomes = []
            numOfMutation = round(self.mr * (self.numOfChromosome * self.numOfDimension))
            # print('Before')
            # print(chromosomes)
            # print()
            # sys.exit()
            for i in range(numOfMutation):
                selectedChromosomeIndex = random.randint(0, self.numOfChromosome-1)
                selectedGenIndex = random.randint(0, self.numOfDimension-1)
                mutatedChromosome = chromosomes[selectedChromosomeIndex]
                mutatedChromosome[selectedGenIndex] = random.uniform(self.lowerBound, self.upperBound)
                chromosomes[selectedChromosomeIndex] = mutatedChromosome
            # print(chromosomes)
            # sys.exit()
            for chromosome in chromosomes:
                objectiveValue = self.sumSquareTestFunction(chromosome)
                fitnessValues = self.calcFitnessValue(objectiveValue)
                tempChromosomes.append([fitnessValues, chromosome, objectiveValue])

            bestChromosome = max(tempChromosomes)
            print(bestChromosome)
            if self.stoppingFitness <= bestChromosome[0]:
                break
            tempChromosomes = []



parameters = {
    'numOfChromosome' : 10,
    'lowerBound' : -10,
    'upperBound' : 10,
    'numOfDimension' : 3,
    'crossoverRate' : 0.25,
    'mutationRate' : 0.1,
    'maxGen' : 80,
    'stoppingFitness': 0.95
}

runGA = GeneticAlgorithm(parameters)
runGA.mainGA()