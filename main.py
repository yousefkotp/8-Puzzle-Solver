import math
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

dfs_counter=0
bfs_counter=0
euclid_counter=0
manhattan_counter=0

dfs_path=[]
bfs_path=[]
euclid_path=[]
manhattan_path=[]

dfs_cost=0
bfs_cost=0
euclid_cost=0
manhattan_cost=0


def getStringRepresentation(x):
    if(int(math.log10(x))+1 == 9):
        return str(x)
    else :
        return "0"+str(x)    

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
    temp = 12345678
    while temp != inputState:
        path.append(temp)
        temp = parentMap[temp]
    path.append(inputState)
    path.reverse()
    return path
def printPath(path):
    for i in path:
        print(getStringRepresentation(i))
def goalTest(state):
    if state == 12345678:
        return True
    return False
def BFS(inputState):
    q = []
    explored = {}
    parent = {}
    integer_state=int(inputState)
    q.append(integer_state)  # here you place the input
    cnt=0
    global bfs_counter
    global bfs_path
    global bfs_cost
    while q:
        cnt+=1
        state = q.pop(0)
        explored[state] = 1
        if goalTest(state):
            path = getPath(parent,int(inputState))
            #printPath(path)
            bfs_counter=cnt
            bfs_path=path
            bfs_cost=len(path)-1
            return 1

        children = getChildren(getStringRepresentation(state))
        for child in children:
            child_int=int(child)
            if not child_int in explored:
                q.append(child_int)
                parent[child_int] = state
                explored[child_int]=1
    bfs_path=[]    
    bfs_cost=0                
    bfs_counter=cnt
    return 0


def DFS(inputState):
    stack = []
    explored = {}
    parent = {}
    integer_state=int(inputState)
    stack.append(integer_state)
    cnt=0
    global dfs_counter
    global dfs_path
    global dfs_cost
    while stack:
        cnt+=1
        state = stack[-1]
        stack.pop()
        if goalTest(state):
            path = getPath(parent,int(inputState))
            #printPath(path)
            dfs_counter=cnt
            dfs_path=path
            dfs_cost=len(path)-1
            return 1

        children = getChildren(getStringRepresentation(state))
        for child in children:
            child_int=int(child)
            if not child_int in explored:
                stack.append(child_int)
                parent[child_int]=state
                explored[child_int]=1
    dfs_path=[]    
    dfs_cost=0            
    dfs_counter=cnt            
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

def AStarSearch_manhattan(inputState):
    
    integer_state=int(inputState)
    heap = []
    explored = {}
    parent = {}
    cost_map = {}
    heapq.heappush(heap, (0, integer_state))
    cost_map[integer_state] = getManhattanDistance(inputState)
    heap_map = {}
    heap_map[integer_state] = 1
    global manhattan_counter
    global manhattan_path
    global manhattan_cost
    while heap:
        node = heapq.heappop(heap)
        state = node[1]
        string_state=getStringRepresentation(state)
        parent_cost = node[0]-getManhattanDistance(string_state)
        explored[state] = 1
        if goalTest(state):
            path = getPath(parent,int(inputState))
            #printPath(path)
            manhattan_path=path
            manhattan_counter=(len(explored))
            manhattan_cost=len(path)-1
            return 1
        
        children = getChildren(string_state)
        for child in children:
            new_cost = getManhattanDistance(child)
            child_int =int(child)
            if not child_int in explored and not child in heap_map:
                heapq.heappush(heap, (parent_cost + new_cost +1, child_int))
                heap_map[child_int] = 1
                cost_map[child_int] = parent_cost + new_cost +1
                parent[child_int] = state
            elif child_int in heap_map:
                if (new_cost + parent_cost +1) < cost_map[child_int]:
                    parent[child_int] = state
                    cost_map[child_int] = new_cost + parent_cost +1
                    heapq.heappush(heap, (parent_cost + 1 + new_cost, child_int))
    manhattan_cost=0                    
    manhattan_path=[]                    
    manhattan_counter=(len(explored))
    return 0
def AStarSearch_euclid(inputState):
    
    integer_state=int(inputState)
    heap = []
    explored = {}
    parent = {}
    cost_map = {}
    heapq.heappush(heap, (0, integer_state))
    cost_map[integer_state] = getEuclideanDistance(inputState)
    heap_map = {}
    heap_map[integer_state] = 1
    global euclid_counter
    global euclid_path
    global euclid_cost
    while heap:
        node = heapq.heappop(heap)
        state = node[1]
        string_state=getStringRepresentation(state)
        parent_cost = node[0]-getEuclideanDistance(string_state)
        explored[state] = 1
        if goalTest(state):
            path = getPath(parent,int(inputState))
            #printPath(path)
            euclid_path=path
            euclid_counter=(len(explored))
            euclid_cost=len(path)-1
            return 1
        
        children = getChildren(string_state)
        for child in children:
            new_cost = getEuclideanDistance(child)
            child_int =int(child)
            if not child_int in explored and not child in heap_map:
                heapq.heappush(heap, (parent_cost + new_cost +1, child_int))
                heap_map[child_int] = 1
                cost_map[child_int] = parent_cost + new_cost +1
                parent[child_int] = state
            elif child_int in heap_map:
                if (new_cost + parent_cost +1) < cost_map[child_int]:
                    parent[child_int] = state
                    cost_map[child_int] = new_cost + parent_cost +1
                    heapq.heappush(heap, (parent_cost + 1 + new_cost, child_int))
    euclid_cost=0
    euclid_path=[]                
    euclid_counter=(len(explored))
    return 0



# BFS("583704126")
# print("---------------")
# DFS("583704126")
# print("---------------")
# AStarSearch_euclid("583704126")
# print("---------------")
# print(AStarSearch_manhattan("583704126"))



DFS("123045678")
print("---------------")
BFS("123045678")
print("---------------")
AStarSearch_euclid("123045678")
print("---------------")
AStarSearch_manhattan("123045678")
print("---------------")

print(dfs_path)
print("---------------")
print(bfs_path)
print("---------------")
print(euclid_path)
print("---------------")
print(manhattan_path)
print("---------------")
print(str(dfs_counter)+" "+str(bfs_counter)+" "+str(euclid_counter)+" "+str(manhattan_counter))
print("---------------")
print(str(dfs_cost)+" "+str(bfs_cost)+" "+str(euclid_cost)+" "+str(manhattan_cost))

#  7,0,2,8,5,3,6,4,1 unsolvable state
print("---------------")
print(DFS("702853641"))
print("---------------")
print(AStarSearch_euclid("702853641"))
print("---------------")
print(AStarSearch_manhattan("702853641"))
print("---------------")
print(BFS("702853641"))
print(dfs_path)
print("---------------")
print(bfs_path)
print("---------------")
print(euclid_path)
print("---------------")
print(manhattan_path)
print("---------------")
print(str(dfs_counter)+" "+str(bfs_counter)+" "+str(euclid_counter)+" "+str(manhattan_counter))
print("---------------")
print(str(dfs_cost)+" "+str(bfs_cost)+" "+str(euclid_cost)+" "+str(manhattan_cost))



# print("---------------")
# n=213
# digits = int(math.log10(n))+1
# print(digits)
# print(int("123")+4)
# print(type(str(12)))

# print(getStringRepresentation(123456708))
# Test Cases
# 583704126
# heap = []
# heapq.heappush(heap, (2,"one"))
# heapq.heappush(heap, (1,"one"))

# # if (,"one") in heap:
# out=[item for item in heap if item[1] == "one"]
# print (out)
# if not out:
# print("fady")

##################### sibha hena matshelhash lhad ma2olak ##################################
#def UCS(inputState):
#     heap = []
#     explored = {}
#     parent = {}
#     cost_map = {}
#     heapq.heappush(heap, (0, inputState))
#     cost_map[inputState] = 0
#     heap_map = {}
#     heap_map[inputState] = 1
#     while heap:
#         node = heapq.heappop(heap)
#         state = node[1]
#         parent_cost = node[0]
#         explored[state] = 1
#         if goalTest(state):
#             path = getPath(parent,inputState)
#             printPath(path)
#             return 1

#         children = getChildren(state)
#         for child in children:
#             if not child in explored and not child in heap_map:
#                 heapq.heappush(heap, (parent_cost + 1, child))
#                 heap_map[child] = 1
#                 cost_map[child] = parent_cost + 1
#                 parent[child] = state
#             elif child in heap_map:
#                 if (1 + parent_cost) < cost_map[child]:
#                     parent[child] = state
#                     cost_map[child] = 1 + parent_cost
#                     heapq.heappush(heap, (parent_cost + 1, child))
#     return 0

