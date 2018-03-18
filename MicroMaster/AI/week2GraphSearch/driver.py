# http://interviewcat.com/2015/05/05/post-1-python-graphs-and-searching/
# https://pymotw.com/2/resource/
import sys
from collections import deque
from time import time
# import resource

class State():
    def __init__(self, root):
        # root = '123045678'
        # {'125340678': \
        # {'R': '125346078', 'U': '120345678', 'D': '125348670', 'L': '125304678'}}
        # {'125346078', '120345678', '125348670', '125304678'}}
        self.root = root
        # self.data = {root:dict()}
        self.data = {root:deque()}
        self.updateChildren()

    def __str__(self):
        return "{}".format(self.data)

    def updateChildren(self):
        l = 0
        r = 8
        n = 3
        indexedData = {}
        for i, v in enumerate(self.data.keys()[0]):
            indexedData[i] = v
            if v=='0':
                izero = i

        def child(stepSize):
            indexedDataCopy = indexedData.copy()
            tmp = indexedDataCopy[izero-stepSize]
            indexedDataCopy[izero-stepSize] = '0'
            indexedDataCopy[izero] = tmp
            s = ''
            for i in indexedDataCopy.keys():
                s += indexedDataCopy[i]
            return s
        # using U D L R order
        # Up
        if l <= izero - n <= r:
            # self.data[self.root]['U'] = child(n)
            self.data[self.root].append(child(n))
        else:
            self.data[self.root].append(None)
        # Down
        if l <= izero + n <= r:
            # self.data[self.root]['D'] = child(-n)
            self.data[self.root].append(child(-n))
        else:
            self.data[self.root].append(None)
        # Left
        if l <= izero - 1 <= r:
            # self.data[self.root]['L'] = child(1)
            self.data[self.root].append(child(1))
        else:
            self.data[self.root].append(None)
        # Right
        if l <= izero + 1 <= r:
            # self.data[self.root]['R'] = child(-1)
            self.data[self.root].append(child(-1))
        else:
            self.data[self.root].append(None)

def bfs(initState, goalState='012345678'):
    q = deque([initState])
    visited = set()
    prev = {initState:[]}  # stores {node: [prev_node, move]}
    moveMap = {0:'Up',
                1:'Down',
                2:'Left',
                3:'Right'}
    while q:
        # dequeue
        cur = q.popleft()
        visited.add(cur)
        if cur == goalState:
            return bfsPath(prev, initState, goalState), len(visited)
        # neighbors = (State(cur).data)[cur].values()
        neighbors = (State(cur).data)[cur]
        for move, node in enumerate(neighbors):
            if node and node not in visited and node not in q:
                # enqueue
                q.extend([node])
                prev[node] = [cur, moveMap[move]]
    return -1

def bfsPath(prev, initState, goalState):
    res = deque([goalState])
    cur = goalState
    while cur != initState:
        res.appendleft(prev[cur])
        cur = prev[cur][0]
    return res

if __name__=='__main__':
    method = sys.argv[1]
    initState = sys.argv[2]
    print method
    print initState

    # usage = resource.getrusage(resource.RUSAGE_SELF)

    # method = 'bfs'
    # initState = '125340678'

    start = time()
    fullState = State(initState)
    # print(fullState)
    if method == 'bfs':
        res,nodes_expanded = bfs(initState)
        stop = time()
        running_time = stop - start
        # max_ram_usage = getattr(usage, 'ru_maxrss')
        print res
        print nodes_expanded


# path_to_goal: the sequence of moves taken to reach the goal
# cost_of_path: the number of moves taken to reach the goal
# nodes_expanded: the number of nodes that have been expanded
# search_depth: the depth within the search tree when the goal node is found
# max_search_depth:  the maximum depth of the search tree in the lifetime of the algorithm
# running_time: the total running time of the search instance, reported in seconds
# max_ram_usage: the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss attribute in the resource module, reported in megabytes

# State {'125340678': deque(['120345678', '125348670', '125304678', '125346078'])}
# res deque([['125340678', 'Up'], ['120345678', 'Left'], ['102345678', 'Left'], '012345678'])

    cost_of_path = len(res) - 1
    path_to_goal = [res[i][1] for i in range(cost_of_path)]
    search_depth = cost_of_path
    max_search_depth = cost_of_path+1


    s = 'path_to_goal: {}\ncost_of_path: {}\nnodes_expanded: {}\nsearch_depth: {}\nmax_search_depth: {}\nrunning_time: {}\nmax_ram_usage: {}\n'.format(path_to_goal,cost_of_path,nodes_expanded,search_depth,max_search_depth,running_time,0)

    with open('.output.txt', 'w') as f:
        f.write(s)