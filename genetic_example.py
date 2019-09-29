from genetic import *

class StationaryGenetic(Genetic):
    def __init__(self, reproduction_operator, evaluation_key):
        population = StationaryPopulation(reproduction_operator,
                                          evaluation_key)


class SimpleGenerationalMemetic(Genetic):
    def __init__(self, reproduction_operator, evaluation_key):
        self.key = evaluation_key
        population = GenerationalPopulation(reproduction_operator,
                                            evaluation_key)
        super().__init__(population)

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
            alt_value = self.key(alt_mutated)
            if alt_value > value:
                mutated = alt_mutated
        self.pop(element)
        self.append(mutated)
