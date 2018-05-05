# https://www.hackerrank.com/challenges/dijkstrashortreach/problem
# https://codereview.stackexchange.com/questions/79025/dijkstras-algorithm-in-python/193629#193629

# https://stackoverflow.com/questions/30431495/dijkstra-algorithm-python

from heapq import *
from collections import defaultdict

def shortestReach(n, edges, s):
    # undirected graph with lowest cost for the same edge inputs
    graph = defaultdict(dict)
    for l, r, c in edges:
        if l in graph and r in graph[l]:
            graph[l][r] = min(c, graph[l][r])
        else:
            graph[l][r] = c

        if r in graph and l in graph[r]:
            graph[r][l] = min(c, graph[r][l])
        else:
            graph[r][l] = c

    q = [(0, s)]
    visited = {}
    while q:
        cost, v = heappop(q)
        # ignore the higher cost visited node in q
        if v in visited: continue
        visited[v] = cost
        for neighbor in graph[v]:
            if neighbor not in visited:
                # push cost with neighbor even if neighbor already exists in q
                heappush(q, (cost+graph[v][neighbor], neighbor))
    res = []
    # avoid range in Hackerrank to get passed.
    for v in xrange(1, n+1):
        if v != s:
            res.append(visited.get(v, -1))
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        nm = raw_input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in xrange(m):
            edges.append(map(int, raw_input().rstrip().split()))

        s = int(raw_input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()