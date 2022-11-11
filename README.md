# 8-Puzzle-Solver
8 Puzzle solver using different search functions as DFS, BFS and A*.
## Table of Content
- [8-Puzzle-Solver](#8-puzzle-solver)
  * [Deployment](#deployment)
  * [Data Structure Used](#data-structure-used)
    + [DFS](#dfs)
    + [BFS](#bfs)
    + [A*](#a)
  * [State Representation](#state-representation)
  * [Algorithms Used](#algorithms-used)
    + [BFS](#bfs-1)
    + [DFS](#dfs-1)
    + [A*](#a-1)
      - [Heuristic Functions](#heuristic-functions)
        * [Manhattan Distance](#manhattan-distance)
        * [Euclidean Distance](#euclidean-distance)
        * [Which One is better?](#which-one-is-better)
  * [Analysis for Different Algorithms.](#analysis-for-different-algorithms)
  * [Graphical Interface](#graphical-interface)
  * [Contributors](#contributors)
  
## Deployment
- The project was built using [Python 3.9](https://www.python.org/downloads/release/python-390/), make sure you configure your python interpreter correctly
- You should run the "interface.py" python file inside the "GUI" folder, you can do that by running the following command inside the "GUI" folder
 ```bash
  python interface.py
 ```

## Data Structure Used

### DFS
- Stack to store the states in frontier
- Hash Map to check if the state is either in frontier or explored or not
- Hash Map to get the parent of each state (used to get path)
- Hash Map to get the cost of each state
### BFS
- Queue to store the states in frontier
- Hash Map to check if the state is either in frontier or explored or not
- Hash Map to get the parent of each state (used to get path)
- Hash Map to get the cost of each state
### A*
- Priority Queue to store the states in frontier
- Hash Map to check if the state is explored or not
- Hash Map to get the parent of each state (used to get path)
- Hash Map to get the cost of each state

## State Representation
- The state is represented as a single number starting from first row and first column as the most significant digit, and the bottom right as least significant digit, so the following state is represented as the number "102345678"
<table align="center">
  <tr>
    <td>1</td>
    <td>0</td>
    <td>2</td>
  </tr>
  <tr>
    <td>3</td>
    <td>4</td>
    <td>5</td>
  </tr>
  <tr>
    <td>6</td>
    <td>7</td>
    <td>8</td>
  </tr>
</table>

- The state is stored as integer to reduce the amount of space the application uses, integer is stored in 4 bytes while storing the state as string would cost 9 bytes.
- The state is then converted to a string to be easily proccessed.
- Getting string representation of a state is done through a simple function
  ```python
  def getStringRepresentation(x):
      if(int(math.log10(x))+1 == 9):
          return str(x)
      else :
          return "0"+str(x)   
  ```
- Getting the next possible states is done throught a simple algorithm which goes as follows
  * Convert the index of character "0" in state to 2D index
    ```python
    idx = state.index('0')
    i = int(idx / 3)
    j = int(idx % 3)
    ```
  * Get the possible moves in all 4 directions
    ```python
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(0, 4):
        nx = i + dx[x]
        ny = j + dy[x]
    ```
  * Check if the new 2D index is a valid index 
    ```python
    def checkValid(nx, ny):
    if nx >= 3 or nx < 0 or ny >= 3 or ny < 0:
        return 0
    return 1
    ```
  * Convert the index of possible moves to 1D 
    ```python
    nwIdx = int(nx * 3 + ny)
    ```
  * The next state is a new string where charachter "0" and the charachter at the new index are swapped

## Algorithms Used

### BFS
- The Pseudo Code is as follows
<div align="center">
  <img src="https://user-images.githubusercontent.com/41492875/198839559-d55a264e-4255-446b-b0d7-fd1b7f19ff62.png">
</div>

### DFS
- The Pseudo Code is as follows
<div align="center">
  <img src="https://user-images.githubusercontent.com/41492875/198839573-e99d6fd4-abcf-4981-9872-a6a55db53741.png">
</div>

### A*
- The Pseudo Code is as follows
<div align="center">
  <img src="https://user-images.githubusercontent.com/41492875/198839586-5200fea8-8c5e-4c43-82d9-553e1ef9a1c1.png">
</div>

#### Heuristic Functions
- The heuristic functions are used in A* search to give a priority to each state to make the "probably" best state to be explored first.
##### Manhattan Distance
- It is the sum of absolute values of differences in the goal’s x and y coordinates and the current cell’s x and y coordinates respectively, the function value for each state is done through a simple function 
```python
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
```
##### Euclidean Distance
- It is the distance between the current cell and the goal cell using the following formula
    
    ![image](https://user-images.githubusercontent.com/41492875/199301510-907d43f7-c97a-45a0-9927-1f56c9660cae.png)


- The value of Euclidean Distance function for each state is done through this function
```python
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
```
##### Which One is better?
- Both of the heuristic functions used are admissible, but we want to know which one of them is better and more effiecient 
- According to the analysis done in [Analysis Section](#analysis-for-different-algorithms), Manhatten Distance is a better admissible function at it expands less number of states than Euclidean Distance. That will result in making the values of Manhatten Distance function values closer to the optimal function much more than the Euclidean Distance.

## Analysis for Different Algorithms.
- For the following random test case:
<table align="center">
  <tr>
    <td>7</td>
    <td>0</td>
    <td>2</td>
  </tr>
  <tr>
    <td>8</td>
    <td>5</td>
    <td>3</td>
  </tr>
  <tr>
    <td>6</td>
    <td>1</td>
    <td>4</td>
  </tr>
</table>
<table align="center">
  <tr>
    <th>Algorithm</th>
    <th>Cost of Path</th>
    <th>Nodes Expanded</th>
    <th>Search Depth</th>
    <th>Running time</th>
  </tr>
  <tr>
    <td>BFS</td>
    <td>27</td>
    <td>174386</td>
    <td>27</td>
    <td>1.27s</td>
  </tr>
  <tr>
    <td>DFS</td>
    <td>54497</td>
    <td>63397</td>
    <td>54497</td>
    <td>0.29s</td>
  </tr>
  <tr>
    <td>A* Manhattan</td>
    <td>27</td>
    <td>3495</td>
    <td>27</td>
    <td>0.07s</td>
  </tr>
  <tr>
    <td>A* Euclidean</td>
    <td>27</td>
    <td>11639</td>
    <td>27</td>
    <td>0.513s</td>
  </tr>
</table>

- In the last test case, the DFS algorithm was lucky enough to have search depth = cost of path, usually the algorithm will have higher search depth than cost of path.
## Graphical Interface

![image](https://user-images.githubusercontent.com/41492875/199296576-d3a2f02f-df99-499c-b9cc-85bddb3f46dc.png)

## Contributors
1- [Yousef Kotp](https://github.com/yousefkotp)

2- [Adham Mohammed](https://github.com/adhammohamed1)

3- [Mohammed Farid](https://github.com/MohamedFarid612)
