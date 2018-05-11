from collections import defaultdict,deque

class Graph():
    def __init__(self):
        self.graph = defaultdict(deque)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * len(self.graph)
        queue = deque()
        result = deque()

        # starting from point s
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.popleft() # dequeue the first in queue
            print s,

            for point in self.graph[s]:
                if not visited[point]:
                    visited[point] = True
                    queue.append(point)
            result.append(s)
        # print result

    def BFS2(self, s):
        visited = [False] * len(self.graph)
        queue = deque()
        result = deque()

        # starting from point s
        queue.append(s)
        # visited[s] = True

        while queue:
            s = queue.popleft() # dequeue the first in queue
            print s,
            visited[s] = True

            for point in self.graph[s]:
                # if not visited[point]:
                if not visited[point] and point not in queue:
                    # visited[point] = True
                    queue.append(point)
            result.append(s)
        # print result


    def DFS(self, s):
        visited = [False] * len(self.graph)
        stack = deque() # DFS use stack not queue
        result = deque()

        # starting from point s
        stack.append(s)
        visited[s] = True

        while stack:
            s = stack.pop()  # output the top of the stack, last appended
            print s,

            for point in self.graph[s]:
                if not visited[point]:
                    stack.append(point)
                    visited[point] = True
            result.append(s)
        # print result


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 3)

print "Following is Breadth First Traversal (starting from vertex 2)"
g.BFS2(2) # 2 0 1 3
print '\n====================\n'

h = Graph()
h.addEdge(0, 1)
h.addEdge(0, 2)
h.addEdge(1, 0)
h.addEdge(1, 3)
h.addEdge(2, 0)
h.addEdge(2, 4)
h.addEdge(2, 5)
h.addEdge(3, 1)
h.addEdge(4, 2)
h.addEdge(4, 6)
h.addEdge(5, 2)
h.addEdge(6, 4)

h.DFS(0)



# http://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/
# https://www.youtube.com/watch?v=0Zsabo7ires&list=PLZxB91HFa5ASQG-Fs5i3qPaf4VsHFMyEI&index=6

