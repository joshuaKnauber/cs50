import time


class Board:
    def __init__(self, board: list[list[int]]):
        self.board = []
        for row in board:
            self.board.append(row[:])

    def move(self, x: int, y: int, number: int):
        self.board[y][x] = number

    def print(self):
        print("-"*25)
        for y, row in enumerate(self.board):
            line = "|"
            for x, num in enumerate(row):
                line += f" {num}"
                if (x+1) % 3 == 0 and x < len(row)-1:
                    line += " |"
            print(line + " |")
            if (y+1) % 3 == 0 and y < len(self.board)-1:
                print("|" + "-"*23 + "|")
        print("-"*25)

    def is_valid_move(self, x: int, y: int, number: int):
        row = self.board[y]
        col = []
        for i in range(9):
            col.append(self.board[i][x])
        square = []
        for y1 in range(y//3 * 3, y//3 * 3 + 3):
            for x1 in range(x//3 * 3, x//3 * 3 + 3):
                square.append(self.board[y1][x1])
        return not number in row and not number in col and not number in square

    def solved(self):
        full_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        # test rows
        for row in self.board:
            if set(row) != full_set:
                return False
        # test columns
        for x in range(9):
            col_set = set()
            for row in self.board:
                col_set.add(row[x])
            if col_set != full_set:
                return False
        # test squares
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                test_set = {
                    self.board[y][x], self.board[y][x+1], self.board[y][x+2],
                    self.board[y+1][x], self.board[y +
                                                   1][x+1], self.board[y+1][x+2],
                    self.board[y+2][x], self.board[y +
                                                   2][x+1], self.board[y+2][x+2]
                }
                if test_set != full_set:
                    return False
        return True

    def get_empty_count(self):
        empty = 0
        for row in self.board:
            empty += row.count(0)
        return empty


class Node:
    def __init__(self, state: Board, action):
        self.state = state
        self.action = action
        self.steps = 0


class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node: Node):
        self.frontier.append(node)

    def contains_state(self, state: Board):
        return any(node.state.board == state.board for node in self.frontier)

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


def heuristic_num_constraints(node: Node):
    """ Count of how many cells are already influencing the current cell """
    if node.action is None:
        return 0
    x = node.action[0]
    y = node.action[1]
    row = node.state.board[y]
    col = []
    for i in range(9):
        col.append(node.state.board[i][x])
    square = []
    for y1 in range(y//3 * 3, y//3 * 3 + 3):
        for x1 in range(x//3 * 3, x//3 * 3 + 3):
            square.append(node.state.board[y1][x1])

    # amount of numbers constraining number
    # score = 26 - ((9-row.count(0)) + (9-col.count(0)) + (9-square.count(0)))

    # amount of options
    numSet = set()
    for num in row + col + square:
        numSet.add(num)
    score = 9 - len(numSet)
    return score


class GreedyBestFirstFrontier(QueueFrontier):

    def empty_count(self, node):
        return node.state.get_empty_count()

    def remove(self) -> Node:
        if self.empty():
            raise Exception("Frontier is empty")
        else:
            scores = list(
                map(lambda node: self.empty_count(node), self.frontier))
            node = self.frontier.pop(scores.index(min(scores)))
            return node


class Solver:

    def __init__(self):
        pass

    def actions(self, state: Board) -> list[tuple[int, int, int]]:
        actions = []
        for y in range(9):
            for x in range(9):
                for n in range(1, 10):
                    if state.is_valid_move(x, y, n):
                        actions.append((x, y, n))
        return actions

    def solve(self, sudoku: Board, frontier):
        num_explored = 0
        explored = set()

        start = Node(state=sudoku, action=None)
        frontier.add(start)

        t1 = time.time()
        while True:
            if frontier.empty():
                raise Exception("No Solution")

            node = frontier.remove()
            num_explored += 1

            # found solution
            if node.state.solved():
                node.state.print()
                print(f"{frontier} explored {num_explored} states")
                return node

            explored.add(node.state)

            # add neighbours to frontier
            for x, y, number in self.actions(node.state):
                new_board = Board(node.state.board)
                new_board.move(x, y, number)
                if not frontier.contains_state(new_board) and new_board not in explored:
                    child = Node(state=new_board, action=(x, y, number))
                    child.steps = node.steps + 1
                    frontier.add(child)

            if num_explored % 25 == 0:
                node.state.print()
                print(f"Last steps took {time.time()-t1}s")
                print(f"Frontier has {len(frontier.frontier)} items")
                print(
                    f"Last evaluated has {node.state.get_empty_count()} empty cells")
                t1 = time.time()


class SolverBacktracking:
    def solve(self, board: Board):
        return self.backtracking(board)

    def find_empty(self, board: Board):
        for y in range(9):
            for x in range(9):
                if board.board[y][x] == 0:
                    return x, y
        return None

    def backtracking(self, board: Board):
        empty_pos = self.find_empty(board)
        if empty_pos is None: # assignment complete
            board.print()
            return

        x, y = empty_pos # select unassigned variables
        for num in range(1, 10): # for all values in vars domain
            if board.is_valid_move(x, y, num): # check if var meets constraints
                board.move(x, y, num) # add var to assignment
                if self.backtracking(board): # recursively backtrack
                    return True # if assignment complete return true
                board.move(x, y, 0)  # if failed, reset var


if __name__ == "__main__":
    # load sudokus
    sudokus = []
    with open("sudoku.txt", "r") as f:
        sudoku = []
        for line in f.readlines()[1:]:
            if line.startswith("Grid"):
                if sudoku:
                    sudokus.append(Board(sudoku))
                sudoku = []
            else:
                sudoku.append(list(map(int, list(line.strip()))))

    sudoku = sudokus[1]
    sudoku.print()

    # solver = Solver()
    # frontier = GreedyBestFirstFrontier() # this works but only for a few of the sudokus
    # frontier = QueueFrontier()
    # frontier = StackFrontier()
    # solver.solve(sudoku, frontier)

    solver = SolverBacktracking()
    solver.solve(sudoku)
