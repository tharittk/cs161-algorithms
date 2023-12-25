def read_input(inputFile):
    stream = []
    with open(inputFile) as f:
        n_vertices = int(f.readline())

        lines = f.readlines()
        for line in lines:
            stream.append(int(line.strip()))

    return n_vertices, stream

class WIS():
    def __init__(self, n, w):
        self.n = n
        self.w = [float('-inf')]
        for iw in w:
            self.w.append(iw)
        self.A = [None for i in range(n+1)] # for indexiing start with 1
        
        self.A[0] = 0
        self.A[1] = self.w[1]

    def forward_run (self, i):
        #print('calling i:', i)
        # caching
        if self.A[i] != None:
            return self.A[i]
        elif i == 1 or i == 0:
            return self.A[i]

        else:       
            self.A[i] = max(self.forward_run(i - 1), self.forward_run(i - 2) + self.w[i])
            return self.A[i]

    def reconstruction(self):
        S = []
        i = self.n
        while i >= 1:
            # case 1 wins 
            if self.A[i-1] >= self.A[i-2] + self.w[i]:
                i = i -1
            # case 2 wins
            else:
                S.append(i)
                i = i -2
        return S

if __name__ == "__main__":
    import sys

    sys.setrecursionlimit(800000)
    n_vertices, weights = read_input('./mwis.txt')
    #n_vertices, weights = read_input('./mwis_small.txt')

    #print(n_vertices, weights)
    #n_vertices = 5
    #weights = [1,4,5,4,3]

    wis = WIS(n_vertices, weights)
    #print(wis.w)

    wis.forward_run(n_vertices)
    #print(wis.A)

    S = wis.reconstruction()

    #print(S)

    #max_sum = 0
    #print(wis.w)
    #for i in S:
    #    max_sum += wis.w[i]
    #    print(i, wis.w[i])
    #print('max sum: ', max_sum)
    
    probe = [1,2,3,4,17,117,517,997]

    ans = []

    for k in probe:
        if k in S:
            ans.append(1)
        else:
            ans.append(0)
    print(ans)
