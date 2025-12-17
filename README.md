# Tree Based Search
This Python program uses a tree-based search to solve mazes.
It first creates a maze and then applies a specific algorithm to find the solution path.
You can run this program to explore tree-based search methods for navigating mazes.

## Search Strategy
In this Program, there have some of the search strategy:
- Uninformed Search
    - DFS (Depth-First Search)
    - BFS (Breadth-First Search)
    - CUS1 (Custom 1 Search)
- Informed Search
    - GBFS (Greedy Best-First Search)
    - A* (A Star Search)
    - CUS2 (Custom Search 2)

### Depth-FIrst Search
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.
It explores as far as possible along each branch before backtracking.
DFS is a recursive algorithm that uses backtracking, meaning it moves forward as much as possible and then backtracks if needed to explore other paths. 

### Breadth-First Search
Breadth-first search (BFS) is a graph traversal algorithm that explores a graph or tree level by level,
starting from a given source node. It visits all neighbors of the current node before moving on to their neighbors.
This systematic approach makes BFS useful for finding the shortest paths in unweighted graphs and exploring tree-like structures. 

### Greedy Best-First Search
Greedy Best-First Search (GBFS) is a pathfinding and graph traversal algorithm that expands the most promising node according to a heuristic function.
It is not optimal and not complete in general,
but it's fast and often used when an approximate solution is acceptable.

### A* Search
A* Search (A-Star Search) is a complete, optimal, and efficient pathfinding algorithm that combines features of Dijkstra's Algorithm and Greedy Best-First Search.

### Depth-Limited Search
Depth-Limited Search (DLS) is a search algorithm that modifies Depth-First Search (DFS) by imposing a maximum depth limit on the search tree.
This prevents the algorithm from exploring indefinitely in potentially infinite or very large search spaces, as DFS can do.
DLS explores nodes recursively, going as deep as the specified limit, and then backtracking. 

### Dijkstra's Search
Dijkstra's Search Algorithm is a classical graph traversal algorithm used to find the shortest path from a starting node to all other nodes in a weighted graph.
It guarantees the optimal path as long as all edge weights are non-negative.
The algorithm works by maintaining a priority queue of nodes to explore,
always choosing the node with the lowest cumulative cost from the start, denoted as g(n).
Initially, the distance to the start node is zero and to all others is infinity.
As the algorithm progresses, it updates these distances whenever a shorter path is found.
Dijkstra's algorithm continues until the shortest path to the goal node is found.
Unlike A* search, Dijkstra's does not use a heuristic function,
making it less efficient in some cases, but reliable when no good heuristic is available.
It's commonly used in routing, mapping applications, and network analysis.

## CLI Running
To start this program, you can use the command line interface (CLI)
such as PowerShell, CMD, or even the Python interpreter itself.
First, you'll need to navigate to the program's location within the CLI.

```commandline
cd path/to/your/file
```
Once you've found the program's file path,
you can run the main program in the command line by using:
```commandline
python main.py
```

### Help
To get more information about how this program works,
simply run the command below.
This will display the program's help instructions.

```commandline
python main.py --help
```

### Search Strategy
If you want to run the program with **Breadth-First Search (BFS)**, you can run like this:
\
\
*Notice: CLI only accept small letter*
```commandline
python main.py --strategy bfs
```
\
**List for the Search Strategy:**

Code | Search Strategy
:---: | ---
dfs | Depth-First Search
bfs | Breadth-First Search
gbfs | Greedy Best-First Search
as | A Star Search
cus1 | Depth-Limited Search
cus2 | Dijkstra's Search

### Reading File
By default, the program looks for a text file named **file.txt**.
If you haven't specified a different filename, this could lead to an error.

```text
Searching for the file...
Unable to detect the file 'file.txt'. Please double check the file nam and try again.
```

For setting the file name, just use this command:
```commandline
python main.py --readfile your_file_name.txt
```

If the program successfully finds the file, the output will look something like this:
```text
Searching for the file...
Found the file:	    your_file_name.txt
```
### Solution Output
By default, this program saves the solution to a file named **file_sol.txt**.
If you want to disable this feature, just use the following command:

```commandline
python main.py --no-generate
```

If you prefer to name the solution file yourself,
rather than using the default **file_sol.txt**,
you can manually set the filename with a command similar to this:
```commandline
python main.py --writefile your_file_name.txt
```

### Window Generate
In default, the Program will generate the output window for look.
\
[Maze Window](image/window.png)

If you want to disable it, you can just enter in CLI like this:
```commandline
python main.py --no-window 
```

## Program Running
If the file is detect successful, it will print out the information for the maze:
```text
Tree Based Details:
    Maze Size:          [11, 5]
    Start Position:     (0, 1)
    End Position 1:     (7, 0)
    End Position 2:     (10, 3)
    Wall 1 Position:    (2, 0, 2, 2)
    Wall 2 Position:    (8, 0, 1, 2)
    Wall 3 Position:    (10, 0, 1, 1)
    Wall 4 Position:    (2, 3, 1, 2)
    Wall 5 Position:    (3, 4, 3, 1)
    Wall 6 Position:    (9, 3, 1, 1)
    Wall 7 Position:    (8, 4, 2, 1)
```

And it will also print out the search strategy and the details:
```text
Search Method:  Depth First Search
Description:    Select one option, try it, go back when there are no more options.
```

Once the maze has been read, processed, and the solution found,
the program will output the solution steps. Each step will be clearly presented with
its corresponding coordinate and the direction of movement taken to reach that coordinate.
\
\
For example:
```text
[(0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3), (4, 2), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (6, 3), (6, 4), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0)]
['Down', 'Down', 'Down', 'Right', 'Up', 'Up', 'Right', 'Right', 'Down', 'Right', 'Up', 'Up', 'Up', 'Right', 'Down', 'Down', 'Down', 'Right', 'Down', 'Right', 'Up', 'Up', 'Up', 'Up']
```
\
If the maze have error and can`t found the path, it will output this:
```text
No goal is reachable.
```
\
Once the maze is solved and the option to save the solution is turned on,
the program will write the solution to an output file. If this file doesn't exist,
the program will create a new text file. If the file already exists,
its previous contents will be deleted before the new solution is written into it.

```text
Search Method:	Depth First Search
Description:	Select one option, try it, go back when there are no more options.


[(0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3), (4, 2), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (6, 3), (6, 4), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0)]

['Down', 'Down', 'Down', 'Right', 'Up', 'Up', 'Right', 'Right', 'Down', 'Right', 'Up', 'Up', 'Up', 'Right', 'Down', 'Down', 'Down', 'Right', 'Down', 'Right', 'Up', 'Up', 'Up', 'Up', 'Down', 'Down', 'Down', 'Right', 'Up', 'Up', 'Right', 'Right', 'Down', 'Right', 'Up', 'Up', 'Up', 'Right', 'Down', 'Down', 'Down', 'Right', 'Down', 'Right', 'Up', 'Up', 'Up', 'Up']
```

## Resource
### Reference
[CS205: Breadth First Search Algorithm | Saylor Academy | Saylor Academy](https://learn.saylor.org/mod/page/view.php?id=80814)\
[Breadth-First Search (BFS) - Shortest Paths in Unweighted Graphs | Interview Cake](https://www.interviewcake.com/concept/java/bfs)\
[Weighted A∗search – unifying view and application](https://www.sciencedirect.com/science/article/pii/S000437020900068X)\
[Algorithms](https://cs.stanford.edu/people/eroberts/courses/soco/projects/2003-04/intelligent-search/astar.html)\
[A* (star) Search Algorithm](https://www.educba.com/a-star-search-algorithm/)\
[Performance Comparison of Depth Limited](https://www.e3s-conferences.org/articles/e3sconf/pdf/2023/28/e3sconf_icmed-icmpc2023_01140.pdf)\
[What is depth-limited search · Classic Search](https://ai-master.gitbooks.io/classic-search/content/what-is-depth-limited-search.html)\
[Depth-First Search in Python: Traversing Graphs and Trees](https://www.datacamp.com/tutorial/depth-first-search-in-python)\
[Dijkstra's Algorithm](https://www.programiz.com/dsa/dijkstra-algorithm)\
[Depth First Search - Neo4J Graph Data Science](https://neo4j.com/docs/graph-data-science/current/algorithms/dfs/)\
[Implementing the Dijkstra Algorithm in Python: A Step-by-Step Tutorial](https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python)

### Youtube Video
[YouTube Video: Depth-First Search](https://youtu.be/1NW9wWswaMk?si=HtdtQjRLVmio85id)\
[YouTube Video: Breadth-First Search](https://youtu.be/ZuHW4fS60pc?si=_QbBHKemkaJan_01)\
[Toutube Video: Depth-First Search, Breadth-First Search, A* Search](https://youtu.be/b1vKhR7ZHzk?si=ihu5uJO4PsaVXtel)