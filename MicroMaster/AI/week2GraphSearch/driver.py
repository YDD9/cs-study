# http://interviewcat.com/2015/05/05/post-1-python-graphs-and-searching/
# https://pymotw.com/2/resource/
# https://www.redblobgames.com/pathfinding/a-star/implementation.html
import sys
import json
from collections import deque
from time import time
import heapq
# import resource

class State():
    def __init__(self, root):
        # root = '125304678'
        # {'125304678': \
        # ['105324678', '125374608', '125034678', '125340678']}
        self.root = root
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
        # Left: not outside box and most left column can not move left
        if l <= izero - 1 <= r and izero not in range(l, r, n) :
            # self.data[self.root]['L'] = child(1)
            self.data[self.root].append(child(1))
        else:
            self.data[self.root].append(None)
        # Right: not outside box and most right column cant not move right
        if l <= izero + 1 <= r and izero not in range(n-1, r+1, n):
            # self.data[self.root]['R'] = child(-1)
            self.data[self.root].append(child(-1))
        else:
            self.data[self.root].append(None)

def bfs(initState, goalState='012345678'):
    q = deque([initState])
    visited = set()
    # initalState depth 0
    prev = {initState:[None, None, 0]}  # stores {node: [prev_node, move, depth]}
    moveMap = {0:'Up',
                1:'Down',
                2:'Left',
                3:'Right'}
    max_search_depth = 0
    while q:
        # dequeue
        cur = q.popleft()
        visited.add(cur)
        if cur == goalState:
            res = goalPath(prev, initState, goalState)
            with open('./prev.json', 'w') as f:
                json.dump(prev, f)
            # moves   , depth of goal,    , max depth ,   node expanded
            # return res, prev[res[-1]][2], bfsMaxSearchDepth(q, prev), len(visited)-1
            return res, prev[res[-1]][2], max_search_depth, len(visited)-1
        # neighbors = (State(cur).data)[cur].values()
        neighbors = (State(cur).data)[cur]
        for move, node in enumerate(neighbors):
            if node and node not in visited and node not in q:
                # enqueue
                q.extend([node])
                # update prev info
                prev[node] = [cur, moveMap[move], prev[cur][2]+1]
                max_search_depth = max(max_search_depth, prev[cur][2]+1)
    return -1

def goalPath(prev, initState, goalState):
    res = deque([goalState])
    cur = goalState
    while cur != initState:
        res.appendleft(prev[cur])
        cur = prev[cur][0]

    return res

def bfsMaxSearchDepth(q, prev):
    if q:
        return prev[q[-1]][2]
    else:
        return prev[goalState][2]

def dfs(initState, goalState='012345678'):
    stack = deque([initState])
    visited = set()
    # initalState depth 0
    prev = {initState:[None, None, 0]}  # stores {node: [prev_node, move, depth]}
    # Depth-First Search. Push onto the stack in reverse-UDLR order;
    # popping off results in UDLR order.
    moveMap = {0:'Up',
                1:'Down',
                2:'Left',
                3:'Right'}
    max_search_depth = 0
    while stack:
        cur = stack.pop()
        visited.add(cur)
        if cur==goalState:
            res = goalPath(prev, initState, goalState)
            with open('./prev.json', 'w') as f:
                json.dump(prev, f)
            return res, prev[res[-1]][2], max_search_depth, len(visited)-1
        neighbors = (State(cur).data)[cur]
        for move, node in reversed(list(enumerate(neighbors))):
            if node and node not in visited and node not in stack:
                stack.append(node)
                prev[node]=[cur, moveMap[move], prev[cur][2]+1]
                max_search_depth = max(max_search_depth, prev[cur][2]+1)

    retrun -1

def mhd(strState, goalState='012345678'):
    res = 0
    for i in range(len(strState)):
        res += abs(int(strState[i])//3 - int(goalState[i])//3) + abs(int(strState[i])%3 - int(goalState[i])%3)
    return res

# https://codereview.stackexchange.com/questions/110429/8-puzzle-using-a-and-manhattan-distance
def ast(initState, goalState='012345678'):
    h = []
    heapq.heappush(h, [0, initState])
    hNodes = set([initState])
    visited = set()
    # initalState depth 0
    prev = {initState:[None, None, 0]}  # stores {node: [prev_node, move, depth]}
    # Depth-First Search. Push onto the stack in reverse-UDLR order;
    # popping off results in UDLR order.
    moveMap = {0:'Up',
                1:'Down',
                2:'Left',
                3:'Right'}
    max_search_depth = 0
    while h:
        cur = (heapq.heappop(h))[1]
        visited.add(cur)
        hNodes.remove(cur)
        if cur==goalState:
            res = goalPath(prev, initState, goalState)
            with open('./prev.json', 'w') as f:
                json.dump(prev, f)
            return res, prev[res[-1]][2], max_search_depth, len(visited)-1
        neighbors = (State(cur).data)[cur]
        for move, node in enumerate(neighbors):
            if not node or node in visited:
                continue
            if node in hNodes:
                for i, item in enumerate(h):
                    if node == item[1] and item[0] > prev[cur][2]+1+mhd(node):
                        h[i][0] = prev[cur][2]+1+mhd(node)
                        prev[node]=[cur, moveMap[move], prev[cur][2]+1]
                        max_search_depth = max(max_search_depth, prev[cur][2]+1)
                        break
            else:
                hNodes.add(node)
                heapq.heappush(h, [prev[cur][2]+1+mhd(node), node])
                prev[node]=[cur, moveMap[move], prev[cur][2]+1]
                max_search_depth = max(max_search_depth, prev[cur][2]+1)

    retrun -1

if __name__=='__main__':
    # method = sys.argv[1]
    # initState = sys.argv[2]
    # initState = initState.replace(',','')
	# usage = resource.getrusage(resource.RUSAGE_SELF)

    # method = 'bfs'
    # method = 'dfs'
    method = 'ast'
    # initState = '1,2,5,3,4,0,6,7,8'.replace(',', '')
    initState = '6,1,8,4,0,2,7,3,5'.replace(',', '')
    # initState = '8,6,4,2,1,3,5,7,0'.replace(',', '')

    start = time()
    fullState = State(initState)
    # print(fullState)
    if method == 'bfs':
        res, search_depth, max_search_depth, nodes_expanded = bfs(initState)
        stop = time()
        running_time = stop - start
        # max_ram_usage = getattr(usage, 'ru_maxrss')
        print('path_to_goal {}'.format(res))
        print('search_depth {}'.format(search_depth))
        print('nodes_expanded {}'.format(nodes_expanded))
    if method == 'dfs':
        res, search_depth, max_search_depth, nodes_expanded = dfs(initState)
        stop = time()
        running_time = stop - start
        # max_ram_usage = getattr(usage, 'ru_maxrss')
        print('path_to_goal {}'.format(res))
    if method == 'ast':
        res, search_depth, max_search_depth, nodes_expanded = ast(initState)
        stop = time()
        running_time = stop - start
        # max_ram_usage = getattr(usage, 'ru_maxrss')
        print('path_to_goal {}'.format(res))

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

    s = 'path_to_goal: {}\ncost_of_path: {}\nnodes_expanded: {}\nsearch_depth: {}\nmax_search_depth: {}\nrunning_time: {}\nmax_ram_usage: {}\n'.format(path_to_goal,cost_of_path,nodes_expanded,search_depth,max_search_depth,running_time,0)

    with open('output.txt', 'w') as f:
        f.write(s)