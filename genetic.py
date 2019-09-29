from population_examples import *
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
