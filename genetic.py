from population_examples import *
from math import math

class Genetic(object, ABC):
    @abstractmethod
    def __init__(self, *, population):
        self.population = population

    def local_search(self):
        pass

    def run(self, *, n_evaluaciones=15000):
        i = 0
        #Fijar numero de cuentas
        while i < n_evaluaciones:
            i+=1
            self.population.advance_generation()

            if i%30 == 0:
                self.population.mutate_element()
            if i%10 == 0:
                self.local_search()
