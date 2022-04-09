class Individual():
    
    def __init__(self, name, genotipo, fenotipo, aptitud):
        self.name = name
        self.genotipo = genotipo
        self.fenotipo = fenotipo
        self.aptitud = aptitud
        # pass

    def __str__(self):
        return self.name, self.genotipo, self.fenotipo, self.aptitud
    
class IndividuoCruza():
    def __init__(self, name, genotipo):
        self.name = name
        self.genotipo = genotipo
    
    def __str__(self):
        return self.name, self.genotipo