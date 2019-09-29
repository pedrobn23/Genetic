from population import *
from math import math

class Genetic(object, ABC):
    def __init__(self, n_evaluaciones=15000):
        self.n_evaluaciones=n_evaluaciones
        self.initialize_population()

    @abstractmethod
    def initialize_population(self):
        raise NotImplementedError

    def local_search(self):
        pass

    def run(self):
        i = 0
        #Fijar numero de cuentas
        while i < self.n_evaluaciones:
            i+=1
            self.population.advance_generation()

            if i%30 == 0:
                self.population.mutate_element()
            if i%10 == 0:
                self.local_search()

#Ejemplos de uso
class StationaryGenetic(Genetic):
    def __init__(self, reproduction_operator, evaluation_key,
                 n_evaluaciones=15000):
        super().__init__(n_evaluaciones)

    def initialize_population(self):
        self.population =
        StationaryPopulation(self, reproduction_operator,
                             evaluation_key, n_characteristics=10,
                             population_size=30)



class SimpleGenerationalMemetic(Genetic):
    def __init__(self, reproduction_operator, evaluation_key,
                 n_evaluaciones=15000):
        super().__init__(n_evaluaciones)
        key = evaluation_key

    def initialize_population(self):
        self.population =
        GenerationalPopulation(self, reproduction_operator,
                               evaluation_key, p_repro=0.7
                               n_characteristics=10,
                               population_size=30)

    def __mutate_vector(vector):
        mutation = np.random.randint(len(vector))
        deviation =  np.random.normal(0.5, 0.3)
        variated_vector = np.copy(vector)

        a = variated_vector[mutation] + deviation
        a = 0 if a < 0 else a if a < 1 else 1  # normalize
        variated_vector[mutation] = a

        return variated_vector

    def local_search(self):
        element = np.random.randint(len(self))
        mutated = np.copy(self.population[element].characteristics)
        value = key(mutated)
        for i in range(500):
            alt_mutated = self.__mutate_vector(mutated)
            alt_value = key(alt_mutated)
            if alt_value > value:
                mutated = alt_mutated
        self.pop(element)
        self.append(mutated)

