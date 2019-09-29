from math import math
from random import random
from numpy import numpy as np
from collections import collections
from abc import ABC

Gene = collections.namedtuple('Gene', 'characteristics value')

class Population(list, ABC):
    def __init__(self, key, n_characteristics=10, population_size=30):
        super().__init__()
        self.evaluation_function = key
        self.value_list = []
        for i in range(population_size):
            self.append(np.random.rand(n_characteristics))

    def get_parents(self):
        aux = random.sample(0, population_size, 4)
        return [max(aux[0], aux[1]), max(aux[2],aux[3])]

    @abstractmethod
    def advance_generation(self):
        pass

    def mutate_element(self, sigma=0.3, element=None):
        if not self:
            raise Exception('Can\'t mutate an element on a empty list')

        element = np.random.randint(len(self))
        mutation = np.random.randint(len(self[0]))
        deviation =  np.random.normal(0.5, sigma)
        mutated_characts = self[element].characteristics

        a = mutated_characts[mutation] + deviation
        a = 0 if a < 0 else a if a < 1 else 1  # normalize
        mutated_characts[mutation] = a

        self.pop(element)
        self.append(mutated_characts)

    def append(self, element):
        x = Gene(charasteristics=element,
                 value=self.evaluation_function(element))
        lo = 0
        hi = len(self)
        while lo < hi:
            mid = (lo+hi)//2
            if self[mid].value < x.value: lo = mid+1
            else: hi = mid
        self.insert(lo,x)


#Ejemplos de Uso
class StationaryPopulation(Population):
    def __init__(self, reproduction_operator, evaluation_key, n_characteristics=10, population_size=30):
        super().__init__(key=evaluation_key, n_characteristics=10, population_size=30)
        self.reproduction_operator = reproduction_operator

    def advance_generation(self):
        parents = self.get_parents()         # Generamos los padres e hijos
        hijos = self.reproduction_operator(self[parents[0]], self[partens[1]])
        for h in hijos: self.append(h)         # Añadimos a la poblacion
        del self[:2]  # Quitamos los dos peores

class GenerationalPopulation(Population):
    def __init__(self, reproduction_operator, evaluation_key, p_repro = 0.7,
                 n_characteristics=10, population_size=30):
        super().__init__(key=evaluation_key, n_characteristics=10, population_size=30)

        self.repro = reproduction_operator
        self.pairs = math.floor(self.size*p_cruze/2)

    def advance_generation(self):
        # Generamos los padres e hijos
        for i in range(pairs):
            parents = self.get_parents()
            hijos = self.reproduction_operator(self[parents[0]], self[partens[1]])
            for h in hijos: self.append(h)         # Añadimos a la poblacion
        del self[:pairs*2]

