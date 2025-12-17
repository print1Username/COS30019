from File import File
from List import List
from Move import Move
from Parser import Parser
from Window import Window

def CheckFile(filename, detectfile):
    output = 'Searching for the file...\n'
    if detectfile:
        output += f'Found the file:\t\t{filename}\n'
    else:
        output += f'Unable to detect the file \'{filename}\'. Please double check the file name and try again.\n'

    return output

def PrintList(size, start, end_list, wall_list):
    output = f'''Tree Based Details:
\tMaze Size:\t\t\t{size}
\tStart Position:\t\t{start}
'''
    for i, end in enumerate(end_list, start=1):
        output += f'\tEnd Position {i}:\t\t{end}\n'
    for i, wall in enumerate(wall_list, start=1):
        output += f'\tWall {i} Position:\t{wall}\n'
    return output

def SearchStrategy(search):
    output = 'Search Method:\t'
    match search:
        case 'dfs':
            output += 'Depth First Search\n'
            output += 'Description:\tSelect one option, try it, go back when there are no more options.\n'
        case 'bfs':
            output += 'Breadth First Search\n'
            output += 'Description:\tExpand all options one level at a time.\n'
        case 'gbfs':
            output += 'Greedy Best-First Search\n'
            output += 'Description:\tUse only the cost to reach the goal from the current node to evaluate the node.\n'
        case 'as':
            output += 'A* (A Star) Search\n'
            output += 'Description:\tUse both the cost to reach the goal from the current node and the cost to reach this node to evaluate the node.\n'
        case 'cus1':
            output += 'Custom Search 1\n'
            output += '\t\tDepth-Limited Search (DLS)\n'
            output += 'Description:\tIt\'s a variant of Depth-First Search (DFS) with a predetermined limit on the depth of the search tree.\n'
        case 'cus2':
            output += 'Custom Search 2\n'
            output += '\t\tDijkstra\'s Search\n'
            output += 'Description:\tIs a classic graph search algorithm used to find the shortest path from a source node to all other nodes in a weighted graph.\n'
        case _:
            output += 'ERROR Search Strategy. Please check the program and try again.\n'
    return output


if __name__ == '__main__':
    args = Parser()
    file = File(args.ParserReadfile(),args.ParserWriteFile())

    print(CheckFile(args.ParserReadfile(),file.DetectFile()))

    if file.DetectFile():
        treelist = List(file.ReadFile())
        move = Move(treelist.GetSizeList(), treelist.GetStartList(), treelist.GetEndList(), treelist.ConvertWallList())

        print(PrintList(treelist.GetSizeList(),treelist.GetStartList(),treelist.GetEndList(),treelist.GetWallList()))
        print(SearchStrategy(args.ParserSearchStrategy()))

        if args.ParserSearchStrategy() == 'dfs':
            move.DFS()
        elif args.ParserSearchStrategy() == 'bfs':
            move.BFS()
        elif args.ParserSearchStrategy() == 'gbfs':
            move.GBFS()
        elif args.ParserSearchStrategy() == 'as':
            move.AS()
        elif args.ParserSearchStrategy() == 'cus1':
            move.CUS1()
        elif args.ParserSearchStrategy() == 'cus2':
            move.CUS2()

        print(move.GetMoveList())
        print(move.GetStepList())

        if args.ParserWriteFile():
            file.WriteFile(str(SearchStrategy(args.ParserSearchStrategy())))
            file.AddFile(str(move.GetMoveList()))
            file.AddFile(str(move.GetStepList()))
            print('\nFile Write Successfully.')

        if args.ParserCreateWindow():
            window = Window(900, 600, 'Tree Based Search', treelist.GetSizeList())
            window.CreateWindow()
            window.CreateMaze()
            window.CreateSteps(move.GetMoveList())
            window.CreateStart(treelist.GetStartList())
            window.CreateEnd(treelist.GetEndList())
            window.CreateWall(treelist.GetWallList())
            window.LoopWindow()