class Gene(object):
    def __init__(self, prodrate, gamma):
        self.k = prodrate
        self.gamma = gamma
    
    def getk(self):
        return self.k
    
    def getgamma(self):
        return self.gamma

    def updateK(self, newk):
        self.k = newk
    
    def updateGamma(self, newg):
        self.gamma = newg



class AffectedGene(Gene):
    def __init__(self, prodrate, gamma, c_cte, n_cte):
        self.c_cte = c_cte
        self.n_cte = n_cte

        Gene.__init__(self, prodrate, gamma)

    def getn(self):
        return self.n_cte
    
    def getc(self):
        return self.c_cte
    
    # TODO: test update functions for c_cte, and n_cte
    def updateC(self, newC):
        self.c_cte = newC

    def updateN(self, newN):
        self.n_cte = newN

    def HillRepression(self, G1):
        return pow(self.c_cte, self.n_cte)/ (pow(self.c_cte, self.n_cte) + pow(G1, self.n_cte))

    def HillActivation(self, G):
        return (G**self.n_cte)/((self.c_cte**self.n_cte) + (G**self.n_cte))