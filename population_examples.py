from population import *

class StationaryPopulation(Population):
    def __init__(self, reproduction_operator, evaluation_key,
                 mutation_key, n_characteristics=10, population_size=30):
        super().__init__(evaluation_key, mutation_key,
                         n_characteristics=10, population_size=30)
        self.reproduction_operator = reproduction_operator

    def advance_generation(self):
        parents = self.get_parents()         # Generamos los padres e hijos
        hijos = self.reproduction_operator(self[parents[0]], self[partens[1]])
        for h in hijos: self.append(h)         # Añadimos a la poblacion
        del self[:2]  # Quitamos los dos peores

class GenerationalPopulation(Population):
    def __init__(self, reproduction_operator, evaluation_key, mutation_key,
                 p_repro = 0.7, n_characteristics=10, population_size=30):
        super().__init__(evaluation_key, mutation_key,
                         n_characteristics=10, population_size=30)
        self.repro = reproduction_operator
        self.pairs = self.size*p_cruze//2

    def advance_generation(self):
        for i in range(pairs):
            parents = self.get_parents()        # Generamos los padres e hijos
            hijos = self.reproduction_operator(self[parents[0]], self[partens[1]])
            for h in hijos: self.append(h)         # Añadimos a la poblacion
        del self[:pairs*2]

