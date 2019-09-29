from math import math
from random import random
from numpy import numpy as np
from collections import collections
from abc import ABC

Gene = collections.namedtuple('Gene', 'characteristics value')

class Population(list, ABC):
    def __init__(self, key, mutation_key, n_characteristics=10, population_size=30):
        super().__init__()
        self.evaluation_function = key
        for i in range(population_size):
            self.append(np.random.rand(n_characteristics))

    def get_parents(self):
        aux = random.sample(0, population_size, 4)
        return [max(aux[0], aux[1]), max(aux[2],aux[3])]

    @abstractmethod
    def advance_generation(self):
        raise NotImplementedError

    def mutate_element(self, sigma=0.3, element=None):
        if not self:
            raise Exception('Can\'t mutate an element on a empty list')

        element = np.random.randint(len(self))
        mutated_characts = mutation_function(self[element])

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
