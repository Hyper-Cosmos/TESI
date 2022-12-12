import random, sys


class AntColonyOptimizationTSP:
    def __init__(self, parameters, start):
        self.param = parameters
        self.start = start

    def getDistance(self, pairedCities):
        rets = []
        for i in pairedCities:
            for j in range(len(self.param['matriks'])):
                for k in range(len(self.param['matriks'][j])):
                    if i[0] == j and i[1] == k:
                        rets.append(self.param['matriks'][j][k])
        return rets
    
    def getProbNextCities(self, distancePaired, feromon):
        ret = []
        for distance in distancePaired:
            if distance == 0:
                val = 0
            else:
                val = (1/distance) * feromon
            ret.append(val)
        return ret
            
    def getNextCities(self, probNextCities, r):
        tmp = 0
        for i in range(len(probNextCities)):
            if sum(probNextCities) != 0:
                tmp = tmp + (probNextCities[i]/sum(probNextCities))
            else:
                tmp = 0
            if r < tmp:
                i
                break
        return i 

    def getPairedCityName(self, tabulist):
        rets = []
        for i in tabulist:
            for j in range(len(self.param['cityNames'])):
                if i == j:
                    rets.append(self.param['cityNames'][j])
        return rets

    def mainACO(self):
        tabulist = []
        feromon = 1/len(self.param['matriks'])
        for i in range(self.param['maxIter']):
            #print('iterasi ke-', i)
            for j in range(self.param['antSize']):
                if self.start:
                    nextCity = self.start[0]
                else:
                    nextCity = random.randint(
                        0, len(self.param['matriks']) - 1)
                tabulist.append([nextCity])
            print(tabulist)
            #tabuList = []
            # sys.exit()

            temp = []; city = []; pairedCity = []; matriks = self.param['matriks']
            for i in range(len(matriks)):
                print('Kota', i)
                for j in range(len(tabulist)):
                    r = random.uniform(0,1)
                    print(tabulist[j])
                    for cityID in range(len(matriks)):
                        for k in tabulist[j]:
                            temp.append(k)
                            temp.append(cityID)
                        if temp.count(cityID) == len(tabulist[j]):
                            city.append(tabulist[j][-1])
                            city.append(cityID)
                        else:
                            city.append(cityID)
                            city.append(cityID)
                        pairedCity.append(city)
                        city = []; temp = []
                    # print(pairedCity)
                    pairedDistances = self.getDistance(pairedCity)
                    pairedCity = [] 
                    probNextCities = self.getProbNextCities(pairedDistances, feromon)
                    nextCities = self.getNextCities(probNextCities, r)
                    tabulist[j].append(nextCities) 
                    # print(probNextCities, sum(probNextCities))   
                    # print(pairedDistances)
            print(tabulist)
            print()
                # pairedDistances = []
            # sys.exit()
            for k in range(len(tabulist)):
                for l in range(len(tabulist[k])-1):
                    city.append(tabulist[k][l])
                    city.append(tabulist[k][l+1])
                    pairedCity.append(city)
                    city = []
                pairedCity.append([tabulist[k][-1], tabulist[k][0]])
                pairedCity = self.getDistance(pairedCity)
                print(pairedDistances)
                pairedCity = []
                name = self.getPairedCityName(tabulist[k])
                print(name)
                print(pairedDistances, sum(pairedDistances), 'Kilometer')
                pairedCity = [pairedCity]
            sys.exit()
               

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

cityNames = {"Jogja", "Sunan Gunung Jati (Cirebon)", "Sunan Kudus", "Sunan Giri (Gresik)", "Sunan Kalijaga (Demak)", "Sunan Gresik", "Sunan Ampel (Surabaya)", "Sunan Drajat (Lamongan)", "Sunan Bonang (Tuban)", "Sunan Muria(Kudus)"}

parameters = {
    'Q': 100,
    'rho': 0.6,
    'antSize': 15,
    'matriks' : matriks,
    'maxIter' : 25,
    'cityNames' : cityNames
}

        

run = AntColonyOptimizationTSP(parameters,start = [0])

run.mainACO()

