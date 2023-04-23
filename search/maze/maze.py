class Node:
    def __init__(self, state: tuple[int, int], parent, action):
        self.state = state
        self.parent = parent
        self.action = action

        self.steps = 0


class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node: Node):
        self.frontier.append(node)

    def contains_state(self, state: tuple[int, int]):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self) -> Node:
        if self.empty():
            raise Exception("Frontier is empty")
        else:
            node = self.frontier.pop(0)
            return node


class StackFrontier(QueueFrontier):

    def remove(self) -> Node:
        if self.empty():
            raise Exception("Frontier is empty")
        else:
            node = self.frontier.pop(-1)
            return node


class GreedyBestFirstFrontier(QueueFrontier):

    def __init__(self, end: tuple[int, int]):
        self.frontier: list[Node] = []
        self.end = end

    def manhattan_distance(self, a: tuple[int, int], b: tuple[int, int]):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def remove(self) -> Node:
        if self.empty():
            raise Exception("Frontier is empty")
        else:
            scores = list(map(lambda node: self.manhattan_distance(
                node.state, self.end), self.frontier))
            node = self.frontier.pop(scores.index(min(scores)))
            return node


class AStarFrontier(GreedyBestFirstFrontier):

    def __init__(self, end: tuple[int, int]):
        self.frontier: list[Node] = []
        self.end = end

    def remove(self) -> Node:
        if self.empty():
            raise Exception("Frontier is empty")
        else:
            scores = []
            for node in self.frontier:
                score = self.manhattan_distance(
                    node.state, self.end) + node.steps
                scores.append(score)
            node = self.frontier.pop(scores.index(min(scores)))
            return node


class Maze():
    def __init__(self, path: str):
        self.start = (0, 0)
        self.end = (0, 0)
        self.maze = []

        with open(path, "r") as f:
            for y, line in enumerate(f.readlines()):
                line = line.strip()
                self.maze.append(list(line))
                for x, char in enumerate(line):
                    if char == "A":
                        self.start = (x, y)
                    elif char == "B":
                        self.end = (x, y)

    def neighbours(self, state: tuple[int, int]) -> list[tuple[int, int], str]:
        options = {
            "up": (0, -1),
            "down": (0, 1),
            "right": (1, 0),
            "left": (-1, 0)
        }
        neighbours = []
        for key, action in options.items():
            if state[0] + action[0] >= 0 and state[0] + action[0] < len(self.maze[0]) and \
                    state[1] + action[1] >= 0 and state[1] + action[1] < len(self.maze):
                neighbour_x = state[0] + action[0]
                neighbour_y = state[1] + action[1]
                if self.maze[neighbour_y][neighbour_x] != "#":
                    neighbours.append(((neighbour_x, neighbour_y), key))
        return neighbours

    def print_cells(self, states: list[tuple[int, int]]):
        new_maze = self.maze[:]
        for [x, y] in states:
            if not (x, y) == self.end:
                new_maze[y][x] = "*"
        for row in new_maze:
            print("".join(row))

    def solve(self, frontier):
        num_explored = 0
        explored = set()

        start = Node(state=self.start, action=None, parent=None)
        frontier.add(start)

        while True:
            if frontier.empty():
                raise Exception("No Solution")

            node = frontier.remove()
            num_explored += 1

            # found solution
            if node.state == self.end:
                states = []

                while node.parent is not None:
                    states.append(node.state)
                    node = node.parent
                states.reverse()

                print(f"{frontier} explored {num_explored} states")
                return states

            explored.add(node.state)

            # add neighbours to frontier
            for state, action in self.neighbours(node.state):
                if not frontier.contains_state(state) and state not in explored:
                    child = Node(state=state, parent=node, action=action)
                    child.steps = node.steps + 1
                    frontier.add(child)


if __name__ == "__main__":
    maze = Maze("maze3.txt")

    bfs = QueueFrontier()
    dfs = StackFrontier()
    gbfs = GreedyBestFirstFrontier(maze.end)
    astar = AStarFrontier(maze.end)

    maze.solve(bfs)
    maze.solve(dfs)
    maze.solve(gbfs)
    solution = maze.solve(astar)

    maze.print_cells(solution)
