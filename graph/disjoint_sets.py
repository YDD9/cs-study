# https://www.hackerrank.com/challenges/journey-to-the-moon/problem

# Algo disjoint sets: find and union via list
# https://www.youtube.com/watch?v=VJnUwsE4fWA
# @11:17
from collections import defaultdict

class DisjoinSets():
    def __init__(self, n):
        """
        parents:    0   1   2   3
        x:          0   1   2   3
        ranks:      0   0   0   0
        """
        self.parents = range(n)
        self.ranks = [0] * n

    def find(self, x):
        """
        if element x's parent is not itself, find the root parents
        also update x's parents to compress/flat the tree structure
        """
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        """
        First, find parent of x and y, unioned parent use the parent with a higher rank
        If ranks are equal, use parent of x and increase ranks of x by 1
        """
        rx, ry = self.find(x), self.find(y)
        if self.ranks[rx] > self.ranks[ry]:
            self.parents[ry] = rx
        if self.ranks[rx] < self.ranks[ry]:
            self.parents[rx] = ry
        if self.ranks[rx] == self.ranks[ry]:
            self.parents[ry] = rx
            self.ranks[rx] += 1


def journeyToMoon(n, astronaut):
    disjoinsets = DisjoinSets(n)
    for pair in astronaut:
        disjoinsets.union(pair[0], pair[1])
    # {country1: 4, country2: 6, country3: 1...}
    country_nbAstronauts = defaultdict(int)
    for p in range(n):
        country_nbAstronauts[disjoinsets.find(p)] += 1

    res = 0 # 4*6 + 4*1 + 4*1 + 6*1...
    while len(country_nbAstronauts) >= 2:
        curr_country = country_nbAstronauts.keys()[0]
        curr_nb_astron = country_nbAstronauts.pop(curr_country)
        for country in country_nbAstronauts:
            res = res + curr_nb_astron * country_nbAstronauts[country]
    return res

if __name__ == '__main__':
    n = 4
    disjoinsets = DisjoinSets(n)
    disjoinsets.union(0, 2)
    print(disjoinsets.parents, disjoinsets.ranks)
    disjoinsets.union(1, 3)
    print(disjoinsets.parents, disjoinsets.ranks)
    disjoinsets.union(0, 3)
    print(disjoinsets.parents, disjoinsets.ranks)

    print(disjoinsets.find(3))
    print(disjoinsets.parents, disjoinsets.ranks)

    print(disjoinsets.find(2))
    print(disjoinsets.parents, disjoinsets.ranks)

    n = 10
    astronaut = [[0, 2],[1, 8],[1, 4],[2, 8],[2, 6],[3, 5],[6, 9]]
    print(journeyToMoon(n, astronaut))