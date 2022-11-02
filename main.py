import heapq
import math
import time

# Used for states generation (getChildren())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# Global variables holding algorithms
dfs_counter = 0
bfs_counter = 0
euclid_counter = 0
manhattan_counter = 0

dfs_path = []
bfs_path = []
euclid_path = []
manhattan_path = []

dfs_cost = 0
bfs_cost = 0
euclid_cost = 0
manhattan_cost = 0

dfs_depth = 0
bfs_depth = 0
euclid_depth = 0
manhattan_depth = 0

time_dfs = 0
time_bfs = 0
time_euclid = 0
time_manhattan = 0


# function to get String representation
def getStringRepresentation(x):
    if int(math.log10(x)) + 1 == 9:
        return str(x)
    else:
        return "0" + str(x)


# function to generate all valid children of a certain node
def getChildren(state):
    children = []
    idx = state.index('0')
    i = int(idx / 3)
    j = int(idx % 3)
    for x in range(0, 4):
        nx = i + dx[x]
        ny = j + dy[x]
        nwIdx = int(nx * 3 + ny)
        if checkValid(nx, ny):
            listTemp = list(state)
            listTemp[idx], listTemp[nwIdx] = listTemp[nwIdx], listTemp[idx]
            children.append(''.join(listTemp))
    return children


# function to get the path to the goal state
def getPath(parentMap, inputState):
    path = []
    temp = 12345678
    while temp != inputState:
        path.append(temp)
        temp = parentMap[temp]
    path.append(inputState)
    path.reverse()
    return path


# function to print the path to goal
def printPath(path):
    for i in path:
        print(getStringRepresentation(i))


# function to check the goal state
def goalTest(state):
    if state == 12345678:
        return True
    return False


# function to check if the start state solvable or not
def isSolvable(digit):
    count = 0
    for i in range(0, 9):
        for j in range(i, 9):
            if digit[i] > digit[j] and digit[i] != 9:
                count += 1
    return count % 2 == 0


# breadth first search algorithm
def BFS(inputState):
    # generating start states of variables and data structures used in the algorithm
    start_time = time.time()
    q = []
    explored = {}
    parent = {}
    parent_cost = {}
    integer_state = int(inputState)
    q.append(integer_state)  # here you place the input
    cnt = 0
    global bfs_counter
    global bfs_path
    global bfs_cost
    global bfs_depth
    global time_bfs
    bfs_depth = 0
    parent_cost[integer_state] = 0
    while q:
        cnt += 1
        state = q.pop(0)
        explored[state] = 1
        bfs_depth = max(bfs_depth, parent_cost[state])
        if goalTest(state):
            path = getPath(parent, int(inputState))
            # printPath(path)
            bfs_counter = cnt
            bfs_path = path
            bfs_cost = len(path) - 1
            time_bfs = float(time.time() - start_time)
            return 1
        # generating childeren
        children = getChildren(getStringRepresentation(state))
        for child in children:
            child_int = int(child)
            if child_int not in explored:
                q.append(child_int)
                parent[child_int] = state
                explored[child_int] = 1
                parent_cost[child_int] = 1 + parent_cost[state]
    bfs_path = []
    bfs_cost = 0
    bfs_counter = cnt
    time_bfs = float(time.time() - start_time)
    return 0


def DFS(inputState):
    # generating start states of variables and data structures used in the algorithm
    start_time = time.time()
    stack = []
    explored = {}
    parent = {}
    parent_cost = {}
    integer_state = int(inputState)
    parent_cost[integer_state] = 0
    explored[integer_state] = 1
    stack.append(integer_state)
    cnt = 0
    global dfs_counter
    global dfs_path
    global dfs_cost
    global dfs_depth
    global time_dfs
    dfs_depth = 0
    while stack:
        cnt += 1
        state = stack[-1]
        stack.pop()
        dfs_depth = max(dfs_depth, parent_cost[state])
        if goalTest(state):
            path = getPath(parent, int(inputState))
            # printPath(path)
            dfs_counter = cnt
            dfs_path = path
            dfs_cost = len(path) - 1
            time_dfs = float(time.time() - start_time)
            return 1
        # generating childeren
        children = getChildren(getStringRepresentation(state))
        for child in children:
            child_int = int(child)
            if child_int not in explored:
                stack.append(child_int)
                parent[child_int] = state
                explored[child_int] = 1
                parent_cost[child_int] = 1 + parent_cost[state]
    dfs_path = []
    dfs_cost = 0
    dfs_counter = cnt
    time_dfs = float(time.time() - start_time)
    return 0


# function checking if state is valid or out of bounds
def checkValid(i, j):
    if i >= 3 or i < 0 or j >= 3 or j < 0:
        return 0
    return 1


# heuristic function using manhattan distance
def getManhattanDistance(state):
    tot = 0
    for i in range(1, 9):
        goalX = int(i / 3)
        goalY = i % 3
        idx = state.index(str(i))
        itemX = int(idx / 3)
        itemY = idx % 3
        tot += (abs(goalX - itemX) + abs(goalY - itemY))
    return tot


# heuristic function using manhattan distance

def getEuclideanDistance(state):
    tot = 0
    for i in range(1, 9):
        goalX = int(i / 3)
        goalY = i % 3
        idx = state.index(str(i))
        itemX = int(idx / 3)
        itemY = idx % 3
        tot += math.sqrt(pow((goalX - itemX), 2) + pow((goalY - itemY), 2))
    return tot


def AStarSearch_manhattan(inputState):
    # generating start states of variables and data structures used in the algorithm
    start_time = time.time()
    integer_state = int(inputState)
    heap = []
    explored = {}
    parent = {}
    cost_map = {}
    heapq.heappush(heap, (getManhattanDistance(inputState), integer_state))
    cost_map[integer_state] = getManhattanDistance(inputState)
    heap_map = {}
    heap_map[integer_state] = 1
    global manhattan_counter
    global manhattan_path
    global manhattan_cost
    global manhattan_depth
    global time_manhattan
    manhattan_depth = 0
    while heap:
        node = heapq.heappop(heap)
        state = node[1]
        string_state = getStringRepresentation(state)
        parent_cost = node[0] - getManhattanDistance(string_state)
        # handling the nodes that was renewed
        if not state in explored:
            manhattan_depth = max(parent_cost, manhattan_depth)
        explored[state] = 1

        if goalTest(state):
            path = getPath(parent, int(inputState))
            # printPath(path)
            manhattan_path = path
            manhattan_counter = (len(explored))
            manhattan_cost = len(path) - 1
            time_manhattan = float(time.time() - start_time)

            return 1

        # generating childeren
        children = getChildren(string_state)
        for child in children:
            new_cost = getManhattanDistance(child)
            child_int = int(child)
            if child_int not in explored and child not in heap_map:
                heapq.heappush(heap, (parent_cost + new_cost + 1, child_int))
                heap_map[child_int] = 1
                cost_map[child_int] = parent_cost + new_cost + 1
                parent[child_int] = state
            elif child_int in heap_map:
                if (new_cost + parent_cost + 1) < cost_map[child_int]:
                    parent[child_int] = state
                    cost_map[child_int] = new_cost + parent_cost + 1
                    heapq.heappush(heap, (parent_cost + 1 + new_cost, child_int))
    manhattan_cost = 0
    manhattan_path = []
    manhattan_counter = (len(explored))
    time_manhattan = float(time.time() - start_time)

    return 0


def AStarSearch_euclid(inputState):
    # generating start states of variables and data structures used in the algorithm
    start_time = time.time()
    integer_state = int(inputState)
    heap = []
    explored = {}
    parent = {}
    cost_map = {}
    heapq.heappush(heap, (getEuclideanDistance(inputState), integer_state))
    cost_map[integer_state] = getEuclideanDistance(inputState)
    heap_map = {}
    heap_map[integer_state] = 1
    global euclid_counter
    global euclid_path
    global euclid_cost
    global euclid_depth
    global time_euclid
    euclid_depth = 0
    while heap:
        node = heapq.heappop(heap)
        state = node[1]
        string_state = getStringRepresentation(state)
        parent_cost = node[0] - getEuclideanDistance(string_state)
        # handling the nodes that was renewed
        if not state in explored:
            euclid_depth = max(parent_cost, euclid_depth)
        explored[state] = 1

        if goalTest(state):
            path = getPath(parent, int(inputState))
            # printPath(path)
            euclid_path = path
            euclid_counter = (len(explored))
            euclid_cost = len(path) - 1
            time_euclid = float(time.time() - start_time)

            return 1
        # generating childeren
        children = getChildren(string_state)
        for child in children:
            new_cost = getEuclideanDistance(child)
            child_int = int(child)
            if child_int not in explored and not child in heap_map:
                heapq.heappush(heap, (parent_cost + new_cost + 1, child_int))
                heap_map[child_int] = 1
                cost_map[child_int] = parent_cost + new_cost + 1
                parent[child_int] = state
            elif child_int in heap_map:
                if (new_cost + parent_cost + 1) < cost_map[child_int]:
                    parent[child_int] = state
                    cost_map[child_int] = new_cost + parent_cost + 1
                    heapq.heappush(heap, (parent_cost + 1 + new_cost, child_int))
    euclid_cost = 0
    euclid_path = []
    euclid_counter = (len(explored))
    time_euclid = float(time.time() - start_time)

    return 0

# start_time=time.time()
# for i in range(0,10000):
#     print(1)
# print(start_time-time.time())

# print(DFS("702853641"))
# print(time_dfs)
# print(BFS("702853641"))
# print(time_bfs)
# print(AStarSearch_euclid("702853641"))
# print(time_euclid)
# print(AStarSearch_manhattan("702853641"))
# print(time_manhattan)


# unsolvable 103245678, 702853641
