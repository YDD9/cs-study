# undirection graph
graph1 = {'A': ['B', 'C'],
            'B': ['A', 'C', 'D'],
            'C': ['A', 'B', 'D', 'F'],
            'D': ['B', 'C'],
            'E': ['F'],
            'F': ['C', 'E']}

def findDist(graph, s):
    if s not in graph:
        return None
    nodes = set()
    for key in graph.keys():
        map(nodes.add, [key] + graph[key])
    mapping = {}
    for i, n in enumerate(sorted(nodes)):
        mapping[i] = n
        mapping[n] = i

    q = [mapping[s]]
    visited = [-1] * len(nodes)
    distance = [-1] * len(nodes)
    distance[mapping[s]] = 0
    while q:
        cur_num = q.pop(0)
        visited[cur_num] = 1
        for item in graph[mapping[cur_num]]:
            if visited[mapping[item]] == -1:
                q.append(mapping[item])
                visited[mapping[item]] = 0
                distance[mapping[item]] = distance[cur_num] + 1
    return distance

print findDist(graph1, 'A')


# direction graph
graph = {'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']
        }
def findPath(graph, s, e):
    if s not in graph:
        return None
    q = [[s, 0]]
    visited = []
    meta = {s: [0, None]}   # node: [distance, previous node]
    while q:
        cur, dis = q.pop(0)
        visited.append(cur)
        if cur == e:
            print True
            return meta
        for neighbor in graph[cur]:
            if neighbor not in visited and neighbor not in [x[0] for x in q]:
                q.append([neighbor, dis+1])
                meta[neighbor] = [dis+1, cur]
            else:
                for i in range(len(q)):
                    if neighbor == q[i][0] and dis+1 < q[i][1]:
                            q[i][1] = dis+1
                            meta[neighbor] = [q[i][1], cur]

    print False
    return meta

def constructPath(e, meta):
    action = [e]
    while True:
        row = meta[e]
        if row[1]:
            action.append(row[1])
            e = row[1]
        else:
            break
    action.reverse()  # an inplace reversed list
    return action
    # reversed(action)  generator object.


e = 'D'
print constructPath(e, findPath(graph, 'A', e))
