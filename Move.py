import heapq


# Calculate the Manhattan geometry
def Manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class Move:
    def __init__(self, size, start, end_list, wall_list):
        self.size = size
        self.start = start
        self.end_list = end_list
        self.wall_list = wall_list
        self.move_list = []
        self.step_list = []

    # Get the nearest of the end point location
    def GetNearEnd(self):
        location = self.start[0], self.start[1]
        for end in self.end_list:
            if Manhattan(self.start,end) < Manhattan(self.start,location) or Manhattan(self.start,location) == 0:
                location = end[0], end[1]
        return location


    # Check the location is valid
    # If the location is outside the maze or at the wall, it will return False, otherwise return True
    def Valid(self,location):
        if location[0] < 0 or location[1] < 0 or location[0] >= self.size[0] or location[1] >= self.size[1]:
            return False
        for wall in self.wall_list:
            if location[0] == wall[0] and location[1] == wall[1]:
                return False
        return True


    # Depth-First Seaarch
    def DFS(self):
        current = self.start
        frontier_list = [self.start]
        visited_list = [self.start]
        solution_dictionary = {}

        while frontier_list:
            new_list = [(current[0] - 1, current[1]),(current[0] + 1, current[1]),(current[0], current[1] - 1),(current[0], current[1] + 1)]
            for new in new_list:
                if self.Valid(new) and new not in visited_list:
                    frontier_list.append(new)
                    solution_dictionary[new] = current
            current = frontier_list[-1]
            visited_list.append(current)
            frontier_list.pop(-1)

        if self.GetNearEnd() in solution_dictionary:
            previous = self.GetNearEnd()
            while previous != self.start:
                for i in solution_dictionary:
                    if previous == self.start:
                        break
                    if i == previous:
                        self.move_list.append(i)
                        previous = solution_dictionary[i]
            self.move_list = self.move_list[::-1]


    def BFS(self):
        frontier_list = [self.start]
        visited_list = [self.start]
        solution_dictionary = {}

        while frontier_list:
            current = frontier_list[0]
            new_list = [(current[0] - 1, current[1]),(current[0] + 1, current[1]),(current[0], current[1] - 1),(current[0], current[1] + 1)]
            for new in new_list:
                if self.Valid(new) and new not in visited_list:
                    frontier_list.append(new)
                    solution_dictionary[new] = current
            visited_list.append(current)
            frontier_list.pop(0)

        if self.GetNearEnd() in solution_dictionary:
            previous = self.GetNearEnd()
            while previous != self.start:
                for i in solution_dictionary:
                    if previous == self.start:
                        break
                    if i == previous:
                        self.move_list.append(i)
                        previous = solution_dictionary[i]
            self.move_list = self.move_list[::-1]


    def GBFS(self):
        frontier_list = []
        solution_dictionary = {self.start: None}
        heapq.heappush(frontier_list, (Manhattan(self.start, self.GetNearEnd()), self.start))

        while frontier_list:
            _, current = heapq.heappop(frontier_list)

            if current == self.GetNearEnd():
                break

            new_list = [(current[0] - 1, current[1]),(current[0] + 1, current[1]),(current[0], current[1] - 1),(current[0], current[1] + 1)]
            for new in new_list:
                if self.Valid(new) and new not in solution_dictionary:
                    distance = Manhattan(self.GetNearEnd(), new)
                    heapq.heappush(frontier_list, (distance, new))
                    solution_dictionary[new] = current

        if self.GetNearEnd() in solution_dictionary:
            previous = self.GetNearEnd()
            while previous != self.start:
                self.move_list.append(previous)
                previous = solution_dictionary[previous]
            self.move_list.append(self.start)
            self.move_list.reverse()


    def AS(self):
        frontier_list = []
        solution_dictionary = {self.start: None}
        heapq.heappush(frontier_list, (Manhattan(self.start, self.GetNearEnd()), self.start))

        while frontier_list:
            _, current = heapq.heappop(frontier_list)

            if current == self.GetNearEnd():
                break

            new_list = [(current[0] - 1, current[1]), (current[0] + 1, current[1]), (current[0], current[1] - 1),
                        (current[0], current[1] + 1)]
            for new in new_list:
                if self.Valid(new) and new not in solution_dictionary:
                    distance = Manhattan(self.GetNearEnd(), new) + Manhattan(self.start , new)
                    heapq.heappush(frontier_list, (distance, new))
                    solution_dictionary[new] = current

        if self.GetNearEnd() in solution_dictionary:
            previous = self.GetNearEnd()
            while previous != self.start:
                self.move_list.append(previous)
                previous = solution_dictionary[previous]
            self.move_list.append(self.start)
            self.move_list.reverse()


    # Depth-Limited Search (DLS)
    def CUS1(self):
        limit = self.size[0] * self.size[1] * 4
        depth = 0
        frontier_list = [self.start]
        visited_list = [self.start]
        solution_dictionary = {}

        while frontier_list and depth <= limit:
            current = frontier_list[0]
            new_list = [(current[0] - 1, current[1]),(current[0] + 1, current[1]),(current[0], current[1] - 1),(current[0], current[1] + 1)]
            for new in new_list:
                if self.Valid(new) and new not in visited_list:
                    frontier_list.append(new)
                    solution_dictionary[new] = current
                    depth += 1
            visited_list.append(current)
            frontier_list.pop(0)

        if self.GetNearEnd() in solution_dictionary:
            previous = self.GetNearEnd()
            while previous != self.start:
                for i in solution_dictionary:
                    if previous == self.start:
                        break
                    if i == previous:
                        self.move_list.append(i)
                        previous = solution_dictionary[i]
            self.move_list = self.move_list[::-1]

    # Dijkstra's Search
    def CUS2(self):
        frontier_list = []
        heapq.heappush(frontier_list, (0, self.start))
        distance_dictionary = {}
        solution_dictionary = {self.start: None}

        # Setting whole position of the direction to infinite
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                distance_dictionary[(i,j)] = float('inf')

        # Set the start direction to zero
        distance_dictionary[self.start] = 0

        while frontier_list:
            current_distance, current = heapq.heappop(frontier_list)
            if current == self.GetNearEnd():
                break

            if current_distance > distance_dictionary[current]:
                continue

            new_list = [(current[0] - 1, current[1]), (current[0] + 1, current[1]), (current[0], current[1] - 1),
                        (current[0], current[1] + 1)]
            for new in new_list:
                if self.Valid(new) and new not in solution_dictionary:
                    new_distance = current_distance + 1
                    if new_distance < distance_dictionary[new]:
                        distance_dictionary[new] = new_distance
                        solution_dictionary[new] = current
                        heapq.heappush(frontier_list, (new_distance, new))

        if self.GetNearEnd() in solution_dictionary:
            current = self.GetNearEnd()
            while current != self.start:
                self.move_list.append(current)
                current = solution_dictionary[current]
            self.move_list.append(self.start)
            self.move_list.reverse()

    def GetMoveList(self):
        if self.move_list:
            return self.move_list
        else:
            return 'No goal is reachable.'


    # Convert the Move List to the List that showing direction
    def GetStepList(self):
        if self.move_list:
            current = self.start
            for move in self.move_list:
                if current[0] - 1 is move[0] and current[1] is move[1]:
                    self.step_list.append('Left')
                if current[0] + 1 is move[0] and current[1] is move[1]:
                    self.step_list.append('Right')
                if current[0] is move[0] and current[1] - 1 is move[1]:
                    self.step_list.append('Up')
                if current[0] is move[0] and current[1] + 1 is move[1]:
                    self.step_list.append('Down')
                current = move
            return self.step_list
        else:
            return ''