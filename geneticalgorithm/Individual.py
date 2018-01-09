class Individual:
    def __init__(self, m, v):
        self.m = m
        self.v = v

        self.fitness = None

        self.chromosome = []
        for i in range(m):
            self.chromosome.append(-1)

    def __setitem__(self, i, gene):
        if(gene>=self.v):
            raise AssertionError()

        self.chromosome[i] = gene

    def __getitem__(self, i):
        return self.chromosome[i]

    def __len__(self):
        return len(self.chromosome)

    def __str__(self):
        return str(self.chromosome)

    def __iter__(self):
        return iter(self.chromosome)