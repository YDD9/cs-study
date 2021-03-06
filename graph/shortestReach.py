#!/bin/python

# https://www.hackerrank.com/challenges/bfsshortreach/problem
import sys

from collections import defaultdict
from heapq import *
def bfs(n, m, edges, s):
    # Complete this function
    adjList = defaultdict(set)
    for f, t in edges:
        adjList[f].add(t)
        adjList[t].add(f)

    queue = [(0, s)]
    # {node: distance to s}
    visited = {}
    while queue:
        dis, cur = heappop(queue)
        # ignore higher cost node in queue when it's popped again
        if cur in visited: continue
        visited[cur] = dis

        for neighbor in adjList[cur]:
            if neighbor not in visited:
                # insert a neighbor with different cost in queue
                # although the same neighbor presents already in queue
                heappush(queue, (dis+6, neighbor))

    res = []
    # Hackerrank python2: xrange less memory
    for n in xrange(1, n+1):
        if n != s:
            res.append(visited.get(n, -1))

    return res

# most simple and clear
import sys
def bfs2(n, m, edges, s):
    dictio = [set([]) for i in range(n)]
    Q = [s-1]
    for k,l in edges:
        dictio[k-1] = dictio[k-1].union({l-1})
        dictio[l-1] = dictio[l-1].union({k-1})
    visit = [-1 for i in range(n)]
    dist = [-1 for i in range(n)]
    dist[s-1] = 0
    while(len(Q)):
        j = Q.pop(0)
        visit[j] = 1
        for k in dictio[j]:
            if visit[k] == -1:
                visit[k] = 0
                dist[k] = dist[j] + 6
                Q.append(k)
    dist.remove(0)
    return dist

# # most structured
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.connectedto = []
#         self.distance = -1

#     def ConnectNode(self, key):
#         self.connectedto.append(key)

# class Graph:
#     def __init__(self, n):
#         self.graph = {}
#         for i in range(1,n+1):
#             self.graph[i] = Node(i)

#     def connect(self, key1, key2):
#         self.graph[key1].ConnectNode(key2)
#         self.graph[key2].ConnectNode(key1)

# def bfs(n, m, edges, s):
#     G = Graph(n)
#     G.graph[s].distance = 0  # set distance of starting node to 0
#     for i, j in edges:
#         G.connect(i, j)

#     Queue = [s]
#     nodes_visited = [s]
#     while len(Queue) != 0:
#         current_node = Queue.pop()      # pop from front of queue
#         for next_node in G.graph[current_node].connectedto:
#             if next_node not in nodes_visited:
#                 nodes_visited.append(next_node)
#                 Queue.insert(0, next_node)  # insert into front of queue
#                 G.graph[next_node].distance = G.graph[current_node].distance + 6

#     distances = []
#     for i in range(1, n+1):
#         if i != s:
#             distances.append(G.graph[i].distance)
#     return distances

if __name__ == "__main__":
    # q = int(raw_input().strip())
    # for a0 in xrange(q):
    #     n, m = raw_input().strip().split(' ')
    #     n, m = [int(n), int(m)]
    #     edges = []
    #     for edges_i in xrange(m):
    #         edges_temp = map(int,raw_input().strip().split(' '))
    #         edges.append(edges_temp)
    #     s = int(raw_input().strip())
    #     result = bfs(n, m, edges, s)
    #     print " ".join(map(str, result))

    n, s = 4, 1
    edges = [[1, 2], [1, 3]]
    # edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 2], [4, 3]]
    # edges = [[1, 2], [1, 4], [2, 4], [3, 4], [4, 2], [4, 3]]

    # n, s = 6, 1
    # edges = [[1, 2], [1, 3], [2, 3], [2, 4], [4, 3], [3, 6], [6, 5]]

    # n, s = 3, 2
    # edges = [[2, 3]]


    m = len(edges)
    result = bfs(n, m, edges, s)
    print result