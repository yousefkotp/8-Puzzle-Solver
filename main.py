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
def BFS(inpt):
    q = []
    explored = {}
    parent = {}
    q.append(inpt)  # here you place the input
    while q:
        state = q.pop(0)
        explored[state] = 1
        if state == "012345678":
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
        if state == "012345678":
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
        # print(state)
        parent_cost = node[0]
        explored[state] = 1
        if state == "012345678":
            # Preparing the path
            path = []
            temp = "012345678"
            while temp != inpt:
                path.append(temp)
                temp = parent[temp]
            path.append(inpt)

            # Reversing the path
            path.reverse()
            # Printing the path
            for i in path:
                print(i)
            return 1

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
                newString = ''.join(listTemp)
                # if k<=3 :
                #     print("----------"+newString)
                #     k+=1

                # out=[item for item in heap if item[1] == newString]
                if not newString in explored and not newString in heap_map:
                    heapq.heappush(heap, (parent_cost + 1, newString))
                    heap_map[newString] = 1
                    cost_map[newString] = parent_cost + 1
                    parent[newString] = state
                elif newString in heap_map:
                    if (1 + parent_cost) < cost_map[newString]:
                        parent[newString] = state
                        cost_map[newString] = 1 + parent_cost
                        heapq.heappush(heap, (parent_cost + 1, newString))

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
    k = 0
    while heap:

        node = heapq.heappop(heap)
        state = node[1]
        # print(state)
        parent_cost = node[0]
        explored[state] = 1
        if state == "012345678":
            # Preparing the path
            path = []
            temp = "012345678"
            while temp != inpt:
                path.append(temp)
                temp = parent[temp]
            path.append(inpt)

            # Reversing the path
            path.reverse()
            # Printing the path
            for i in path:
                print(i)
            return 1

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
                newString = ''.join(listTemp)
                # if k<=3 :
                #     print("----------"+newString)
                #     k+=1

                # out=[item for item in heap if item[1] == newString]

                new_cost = getEuclideanDistance(newString)
                if not newString in explored and not newString in heap_map:
                    heapq.heappush(heap, (parent_cost + new_cost, newString))
                    heap_map[newString] = 1
                    cost_map[newString] = parent_cost + new_cost
                    parent[newString] = state
                elif newString in heap_map:
                    if (new_cost + parent_cost) < cost_map[newString]:
                        parent[newString] = state
                        cost_map[newString] = new_cost + parent_cost
                        heapq.heappush(heap, (parent_cost + 1, newString))

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
    k = 0
    while heap:

        node = heapq.heappop(heap)
        state = node[1]
        # print(state)
        parent_cost = node[0]
        explored[state] = 1
        if state == "012345678":
            # Preparing the path
            path = []
            temp = "012345678"
            while temp != inpt:
                path.append(temp)
                temp = parent[temp]
            path.append(inpt)

            # Reversing the path
            path.reverse()
            # Printing the path
            for i in path:
                print(i)
            return 1

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
                newString = ''.join(listTemp)
                # if k<=3 :
                #     print("----------"+newString)
                #     k+=1

                # out=[item for item in heap if item[1] == newString]
                new_cost = getManhattanDistance(newString)
                if not newString in explored and not newString in heap_map:
                    heapq.heappush(heap, (parent_cost + new_cost, newString))
                    heap_map[newString] = 1
                    cost_map[newString] = parent_cost + new_cost
                    parent[newString] = state
                elif newString in heap_map:
                    if (new_cost + parent_cost) < cost_map[newString]:
                        parent[newString] = state
                        cost_map[newString] = new_cost + parent_cost
                        heapq.heappush(heap, (parent_cost + 1, newString))

    return 0


# BFS("123845670")
# print("------------------------")
# AStarSearch("123845670")
# print("====================")
# AStarSearch_euclid("123845670")
# print("------------------------")
# AStarSearch_manhattan("123845670")


# if BFS("103245678"):
#     print("solvable")
# else :
#     print("unsolvable")
# print("------------------------")
if BFS("583704126"):
    print("solvable")
else:
    print("unsolvable")
# print("====================")
# AStarSearch_euclid("583704126")
# print("------------------------")
# AStarSearch_manhattan("583704126")


# map={}
# map[1]=2
# print(map[2])


# heap = []
# heapq.heappush(heap, (2,"one"))

# heapq.heappush(heap, (1,"one"))


# # if (,"one") in heap:
# out=[item for item in heap if item[1] == "one"]
# print (out)
# if not out:
# print("fady")