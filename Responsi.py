import random
import sys


class AntColonyOptimizationTSP:
    def __init__(self, parameters, start):
        self.params = parameters
        self.start = start

    def getDistance(self, pairedCities):
        rets = []
        for i in pairedCities:
            for j in range(len(self.params['matriks'])):
                for k in range(len(self.params['matriks'][j])):
                    if i[0] == j and i[1] == k:
                        rets.append(self.params['matriks'][j][k])
        return rets

    def getProbNextCities(self, distancePaired, feromon):
        ret = []
        for distance in distancePaired:
            if distance == 0:
                val = 0
            else:
                val = (1/distance)*feromon
            ret.append(val)
        return ret

    def getNextCities(self, probNextCities, r):
        tmp = 0
        for i in range(len(probNextCities)):
            if sum(probNextCities) != 0:
                tmp += (probNextCities[i]/sum(probNextCities))
            else:
                tmp = 0
            if r < tmp:
                i
                break
        return i

    def getPairedCityNames(self, tabuList):
        rets = []
        for i in tabuList:
            for j in range(len(self.params['cityNames'])):
                if i == j:
                    rets.append(self.params['cityNames'][j])
        return rets

    def ACOTSProblem(self):
        tabuList = []
        feromon = 1/len(self.params['matriks'])
        finalDistance = []
        allDistances = []
        finalResults = []
        bestSolutions = []
        for i in range(self.params['maxIter']):
            # print('iterasi ke-', iter)
            for j in range(self.params['antSize']):
                if self.start:
                    nextCity = self.start[0]
                else:
                    nextCity = random.randint(0, len(self.params['matriks'])-1)
                tabuList.append([nextCity])
            # print(tabuList)
            # tabuList = []

            temp = []
            city = []
            pairedCity = []
            matriks = self.params['matriks']

            for matrik in range(len(matriks)-1):
                for j in range(len(tabuList)):
                    r = random.uniform(0, 1)
                    # print(tabuList[j])

                    for cityID in range(len(matriks)):
                        for k in tabuList[j]:
                            temp.append(k)
                            temp.append(cityID)
                        if temp.count(cityID) == len(tabuList[j]):
                            city.append(tabuList[j][-1])
                            city.append(cityID)
                        else:
                            city.append(cityID)
                            city.append(cityID)
                        pairedCity.append(city)
                        temp = []
                        city = []
                    pairedDistances = self.getDistance(pairedCity)
                    pairedCity = []
                    probNextCities = self.getProbNextCities(
                        pairedDistances, feromon)
                    nextCities = self.getNextCities(probNextCities, r)
                    tabuList[j].append(nextCities)
            # print(tabuList)
            # print()

            for k in range(len(tabuList)):
                for l in range(len(tabuList[k])-1):
                    city.append(tabuList[k][l])
                    city.append(tabuList[k][l+1])
                    pairedCity.append(city)
                    city = []
                pairedCity.append([tabuList[k][-1], tabuList[k][0]])
                pairedDistances = self.getDistance(pairedCity)
                # print(pairedCity)
                # pairedCity = []
                names = self.getPairedCityNames(tabuList[k])
                finalDistance.append([names, pairedDistances])
                allDistances.append(sum(pairedDistances))
                pairedCity = []
            # print(allDistances)
            minIndex = allDistances.index(min(allDistances))
            finalResults.append(finalDistance[minIndex])
            bestSolutions.append(min(allDistances))
            finalDistance = []
            allDistances = []
            tabuList = []
        shortestRoutes = finalResults[bestSolutions.index(
                min(bestSolutions))]
            # print('Rute terpendek dari rumah: ')
        for i in shortestRoutes[0]:
                # print(i)
            # print(shortestRoutes[0][0])
            # print(sum(shortestRoutes[1]), ' kilometer')
            return (sum(shortestRoutes[1]))

matriks = [
    [0, 360, 185, 335, 160, 340, 334, 362, 163, 204],
    [360, 0, 293, 579, 269, 601, 583, 610, 370, 318],
    [185, 293, 0, 405, 261, 408, 409, 202, 80.6, 21.4],
    [335, 579, 405, 0, 313, 4, 24, 56.5, 164, 241],
    [160, 269, 26.1, 313, 0, 383, 382, 225, 104, 45.8],
    [340, 601, 408, 4, 383, 0, 22.5, 56.5, 164, 244],
    [334, 583, 409, 24, 382, 22.5, 0, 75.9, 181, 336],
    [362, 610, 202, 56.5, 225, 56.5, 75.9, 0, 120, 200],
    [163, 370, 80.6, 164, 104, 164, 181, 120, 0, 80.9],
    [204, 318, 21.4, 241, 45.8, 244, 336, 200, 80.9, 0]
]

cityNames = [
    "Jogja", "Sunan Gunung Jati (Cirebon)", "Sunan Kudus", "Sunan Giri (Gresik)", "Sunan Kalijaga (Demak)", "Sunan Gresik", "Sunan Ampel (Surabaya)", "Sunan Drajat (Lamongan)", "Sunan Bonang (Tuban)", "Sunan Muria (Kudus)"
]


maxIter = 10
LimitmaxIter = 80
for i in range(maxIter):
    if maxIter <= LimitmaxIter:
        print('MaxIter Ke-',maxIter)
        parameters = {
        'Q': 100,
        'rho': 0.6,
        'antSize': 15,
        'matriks': matriks,
        'maxIter': maxIter,
        'cityNames': cityNames,
        'MaxRun': 10
    }

    aco = AntColonyOptimizationTSP(parameters, start=[0])
    for i in range(parameters['antSize']):
        result = aco.ACOTSProblem()
        print(result)
    print(' ')
    maxIter += 10