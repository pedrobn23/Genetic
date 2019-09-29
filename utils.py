from numpy import numpy as np

def simple_real_mutation(element):
    mutation = np.random.randint(len(self[0]))
    deviation =  np.random.normal(0.5, sigma)
    mutated_characts = self[element].characteristics

    a = mutated_characts[mutation] + deviation
    a = 0 if a < 0 else a if a < 1 else 1  # normalize
    mutated_characts[mutation] = a

    return mutated_characts



