import math
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

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
def getPath(parentMap,inputState):
    path = []
    temp = "012345678"
    while temp != inputState:
        path.append(temp)
        temp = parentMap[temp]
    path.append(inputState)
    path.reverse()
    return path
def printPath(path):
    for i in path:
        print(i)
def goalTest(state):
    if state =="012345678":
        return True
    return False
def BFS(inpt):
    q = []
    explored = {}
    parent = {}
    q.append(inpt)  # here you place the input
    while q:
        state = q.pop(0)
        explored[state] = 1
        if goalTest(state):
            path = getPath(parent,inpt)
            printPath(path)
            return 1

        children = getChildren(state)
        for child in children:
            if not child in explored:
                q.append(child)
                parent[child] = state
                explored[child]=1
    return 0


def DFS(inpt):
    stack = []
    explored = {}
    parent = {}
    stack.append(inpt)
    while stack:
        state = stack[-1]
        stack.pop()
        if goalTest(state):
            path = getPath(parent,inpt)
            printPath(path)
            return 1

        children = getChildren(state)
        for child in children:
            if not child in explored:
                stack.append(child)
                parent[child]=state
                explored[child]=1
    return 0


def checkValid(i, j):
    if i >= 3 or i < 0 or j >= 3 or j < 0:
        return 0
    return 1


def getManhattanDistance(state):
    sum = 0
    for i in range(1, 9):
        goalX = int(i / 3)
        goalY = i % 3
        idx = state.index(str(i))
        itemX = int(idx / 3)
        itemY = idx % 3
        sum += (abs(goalX - itemX) + abs(goalY - itemY))
    return sum


def getEuclideanDistance(state):
    sum = 0
    for i in range(1, 9):
        goalX = int(i / 3)
        goalY = i % 3
        idx = state.index(str(i))
        itemX = int(idx / 3)
        itemY = idx % 3
        sum += math.sqrt(pow((goalX - itemX), 2) + pow((goalY - itemY), 2))
    return sum


def AStarSearch(inpt):
    heap = []
    explored = {}
    parent = {}
    cost_map = {}
    heapq.heappush(heap, (0, inpt))
    cost_map[inpt] = 0
    heap_map = {}
    heap_map[inpt] = 1
    k = 0
    while heap:
        node = heapq.heappop(heap)
        state = node[1]
        parent_cost = node[0]
        explored[state] = 1
        if goalTest(state):
            path = getPath(parent,inpt)
            printPath(path)
            return 1

        children = getChildren(state)
        for child in children:
            if not child in explored and not child in heap_map:
                heapq.heappush(heap, (parent_cost + 1, child))
                heap_map[child] = 1
                cost_map[child] = parent_cost + 1
                parent[child] = state
            elif child in heap_map:
                if (1 + parent_cost) < cost_map[child]:
                    parent[child] = state
                    cost_map[child] = 1 + parent_cost
                    heapq.heappush(heap, (parent_cost + 1, child))
    return 0


def AStarSearch_euclid(inpt):
    heap = []
    explored = {}
    parent = {}
    cost_map = {}
    heapq.heappush(heap, (0, inpt))
    cost_map[inpt] = 0
    heap_map = {}
    heap_map[inpt] = 1

    while heap:
        node = heapq.heappop(heap)
        state = node[1]
        parent_cost = node[0]
        explored[state] = 1
        if goalTest(state):
            path = getPath(parent,inpt)
            printPath(path)
            return 1

        children = getChildren(state)
        for child in children:
            new_cost = getEuclideanDistance(child)
            if not child in explored and not child in heap_map:
                heapq.heappush(heap, (parent_cost + new_cost, child))
                heap_map[child] = 1
                cost_map[child] = parent_cost + new_cost
                parent[child] = state
            elif child in heap_map:
                if (new_cost + parent_cost) < cost_map[child]:
                    parent[child] = state
                    cost_map[child] = new_cost + parent_cost
                    heapq.heappush(heap, (parent_cost + 1, child))
    return 0


def AStarSearch_manhattan(inpt):
    heap = []
    explored = {}
    parent = {}
    cost_map = {}
    heapq.heappush(heap, (0, inpt))
    cost_map[inpt] = 0
    heap_map = {}
    heap_map[inpt] = 1
    while heap:
        node = heapq.heappop(heap)
        state = node[1]
        parent_cost = node[0]
        explored[state] = 1
        if goalTest(state):
            path = getPath(parent,inpt)
            printPath(path)
            return 1
        children = getChildren(state)
        for child in children:
            new_cost = getManhattanDistance(child)
            if not child in explored and not child in heap_map:
                heapq.heappush(heap, (parent_cost + new_cost, child))
                heap_map[child] = 1
                cost_map[child] = parent_cost + new_cost
                parent[child] = state
            elif child in heap_map:
                if (new_cost + parent_cost) < cost_map[child]:
                    parent[child] = state
                    cost_map[child] = new_cost + parent_cost
                    heapq.heappush(heap, (parent_cost + 1, child))

    return 0



if AStarSearch_euclid("583704126"):
    print("solvable")
else:
    print("unsolvable")

# Test Cases
# 583704126,


# heap = []
# heapq.heappush(heap, (2,"one"))
# heapq.heappush(heap, (1,"one"))

# # if (,"one") in heap:
# out=[item for item in heap if item[1] == "one"]
# print (out)
# if not out:
# print("fady")