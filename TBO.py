X = int(input("Enter The Number of States : "))
S = [input("Enter The States : ") for i in range (0,X)]
Y = int(input("Enter The Number of Keys : "))
T = [input("Enter The Keys : ") for i in range (0,Y)]
Last = input("Final State : ")
K = [0 for i in range(len(S))]
for i in range (len(S)):
    K[i] = [0 for j in range(len(T))]
    for j in range (len(T)):
        K[i][j] = input('From ' +S[i]+' If '+ T[j]+' go :')

def convert(p,q):
    li.append(K[S.index(p)][T.index(q)])
    return K[S.index(p)][T.index(q)]
while True:
    li = []
    start = S[0]
    Q = input("Enter The String to Check : ")
    for i in Q:
        start = convert(start,i)
    if(li[-1] == Last):
        print('Mesin DiTerima')
    else:
        print('Mesin DiTolak')
    