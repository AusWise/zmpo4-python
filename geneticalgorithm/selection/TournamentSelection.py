from . import Selection
from .. import Population

import random

class TournamentSelection(Selection, object):
    def __init__(self, tournamentSize):
        self.tournamentSize = tournamentSize

    def __call__(self, population, Np):
        super(TournamentSelection, self).__call__(population, Np)
        result = Population()

        for i in range(Np):
            result.append(self._tournament(population))

        return result

    def _tournament(self, population):
        tournament = Population()

        for i in range(self.tournamentSize):
            tournament.append(random.choice(population))

        return max(tournament, key=lambda x: x.fitness)