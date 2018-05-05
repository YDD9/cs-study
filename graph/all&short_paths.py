# https://www.python.org/doc/essays/graphs/

graph = {'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']}

def findPath(graph, s, e, path=[]):
    path = path + [s]
    if s not in graph:
        return None
    if s == e:
        return path

    for item in graph[s]:
        if item not in path:
            newPath = findPath(graph, item, e, path)
            if newPath: return newPath
    return None

print findPath(graph, 'A', 'D', [])


def findAllPath(graph, s, e, path=[]):
    path = path + [s]  # you can't use shorthand path += [s], result will only keep one path???
    if s not in graph:
        return None
    if s == e:
        return [path]
    all_paths = []
    for item in graph[s]:
        if item not in path:
            newPaths = findAllPath(graph, item, e, path)
            for newPath in newPaths:
                all_paths.append(newPath)
    return all_paths

print findAllPath(graph, 'A', 'D', [])



def findShortPath(graph, s, e, path=[]):
    path = path + [s]
    if s not in graph:
        return None
    if s == e:
        return path
    short_path = None
    for item in graph[s]:
        if item not in path:
            newPath = findShortPath(graph, item, e, path)
            if newPath:
                if not short_path or len(newPath) < len(short_path):
                    short_path = newPath
    return short_path

print findShortPath(graph, 'A', 'D', [])