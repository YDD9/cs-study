#!/bin/python
# https://www.hackerrank.com/challenges/jack-goes-to-rapture/problem

# GOOD solution but not good to use set() as it changes order
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
from __future__ import print_function

import os
import sys
from collections import defaultdict,deque

if __name__ == '__main__':
    # g_nodes, g_edges = map(int, raw_input().split())

    # g_from = [0] * g_edges
    # g_to = [0] * g_edges
    # g_weight = [0] * g_edges

    # for g_itr in xrange(g_edges):
    #     g_from[g_itr], g_to[g_itr], g_weight[g_itr] = map(int, raw_input().split())

    #
    # Write your code here.
    #
    g_nodes = 5
    g_from = [1, 3, 1, 4, 2]
    g_to = [2, 5, 4, 5, 3]
    g_weight = [60, 70, 120, 150, 80]
    g_edges = len(g_weight)
    """
    graph dict {
        vertex1: {
            neighbor1: cost1,
            neighbor2: cost2
        },
        vertex2: {
            neighbor1: cost2,
            neighbor3: cost3
        },
    }
    """
    graph = defaultdict(defaultdict)
    for i in range(g_nodes):
        graph[g_from[i]][g_to[i]] = g_weight[i]
        graph[g_to[i]][g_from[i]] = g_weight[i]
    # print(graph)

    def cheapestPath(graph, s, e):
        open_set = [s]
        visited = []
        cost = {s: 0}
        previous = {s: None}
        while open_set:
            open_cost = [cost[v] for v in open_set]
            i_cur = open_cost.index(min(open_cost))
            cur = open_set[i_cur]
            del open_set[i_cur]
            visited.append(cur)

            if cur == e:
                return pre_cost(cur, cost, previous) + open_cost[i_cur]

            for neighbor in graph[cur].keys():
                if neighbor not in visited:
                    prev_c = pre_cost(cur, cost, previous)
                    next_c = graph[cur][neighbor] - prev_c if graph[cur][neighbor] - prev_c > 0 else 0
                    if neighbor not in open_set:
                        open_set.append(neighbor)
                        cost[neighbor] = next_c
                        previous[neighbor] = cur
                    else:
                        if next_c < cost[neighbor]:
                            cost[neighbor] = next_c
                            previous[neighbor] = cur

        return None
    # cost = {1: 0, 2: 60, 4: 120}
    # previous = {1: None, 2: 1, 4: 1}
    # cur= 2
    def pre_cost(cur, cost, previous):
        pre_cost = 0
        tmp = cur
        while tmp:
            pre_cost += cost[tmp]
            tmp = previous[tmp]
        return pre_cost
    print(pre_cost(cur, cost, previous))
    print(cheapestPath(graph, 1, 5))




    def allPath(graph, s, e):
        q = deque( [(s, [s])] )
        visited = []
        while q:
            (vertex, path) = q.popleft()
            visited.append(vertex)
            if vertex == e:
                yield path
            for neighbor in graph[vertex].keys():
                if neighbor not in visited:
                    q.append( (neighbor, path + [neighbor]) )


    def construct_Path(graph, s, e):
        paths = list(allPath(graph, s, e))
        if not paths:
            return -1
        choices = []
        for path in paths:
            cost = [0] * (len(path)-1)
            for ip in range(len(path)-1):
                cost[ip] = 0 if graph[path[ip]][path[ip+1]] - sum(cost[: ip]) < 0 \
                    else graph[path[ip]][path[ip+1]] - sum(cost[: ip])
            choices.append(sum(cost))
        choice = min(choices)
        index = choices.index(choice)
        # print(paths[index])
        return choice

    print(construct_Path(graph, 1, 4))
