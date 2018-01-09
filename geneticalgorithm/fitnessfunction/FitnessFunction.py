def decimal(bit):
    result = 0

    m = len(bit)
    for i in range(m):
        result += bit[i] * (2 ** (m-1-i))

    return result

class FitnessFunction:
    def __init__(self, f = lambda x: x):
        self.f = f

    def __call__(self, individual):
        return self.f(decimal(individual))