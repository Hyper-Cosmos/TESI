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
        for iter in range(self.params['maxIter']):
            print('iterasi ke-', iter)
            for i in range(self.params['antSize']):
                if self.start:
                    nextCity = self.start[0]
                else:
                    nextCity = random.randint(0, len(self.params['matriks'])-1)
                tabuList.append([nextCity])
            print(tabuList)
            # tabuList = []

            temp = []
            city = []
            pairedCity = []
            matriks = self.params['matriks']

            for i in range(len(matriks)-1):
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
            print(tabuList)
            print()

            for k in range(len(tabuList)):
                for l in range(len(tabuList[k])-1):
                    city.append(tabuList[k][l])
                    city.append(tabuList[k][l+1])
                    pairedCity.append(city)
                    city = []
                pairedCity.append([tabuList[k][-1], tabuList[k][0]])
                pairedDistances = self.getDistance(pairedCity)
                print(pairedCity)
                pairedCity = []
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
            print('Rute terpendek dari rumah: ')
            for i in shortestRoutes[0]:
                print(i)
            print(shortestRoutes[0][0])
            print(sum(shortestRoutes[1]), ' kilometer')


matriks = [
    [0, 5.9, 5, 5.7, 6.8, 5.1, 30],
    [5.9, 0, 3.4, 2.2, 5.4, 4, 34],
    [5, 3.4, 0, 2.1, 3.4, 2, 35],
    [5.7, 2.2, 2.1, 0, 4.2, 2.8, 35.1],
    [6.8, 5.2, 3.4, 4.2, 0, 1.7, 38],
    [5.1, 4, 2, 2.8, 1.7, 0, 37],
    [30, 34, 35, 35.1, 38, 37, 0]
]

cityNames = [
    "Rumah", "Kampus 1 UAD", "Kampus 2 UAD", "Kampus 3 UAD", "Kampus 4 UAD", "Kampus 5 UAD", "Kampus 6 UAD"
]

parameters = {
    'Q': 100,
    'rho': 0.6,
    'antSize': 15,
    'matriks': matriks,
    'maxIter': 25,
    'cityNames': cityNames
}

aco = AntColonyOptimizationTSP(parameters, start=[0])
aco.ACOTSProblem()