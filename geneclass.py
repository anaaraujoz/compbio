class Gene(object):
    def __init__(self, prodrate, gamma):
        self.k = prodrate
        self.gamma = gamma
    
    def getk(self):
        return self.k
    
    def getgamma(self):
        return self.gamma


class ActivatedGene(Gene):
    def __init__(self, prodrate, gamma, c_cte, n_cte):
        self.c_cte = c_cte
        self.n_cte = n_cte

        Gene.__init__(self, prodrate, gamma)

    def getn(self):
        return self.n_cte
    
    def getc(self):
        return self.c_cte
    