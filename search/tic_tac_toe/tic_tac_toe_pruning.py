class Board:
    def __init__(self, board=None):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        if board:
            new_board = []
            for row in board.board:
                new_board.append(row[:])
            self.board = new_board

    def move(self, action, player):
        self.board[action[1]][action[0]] = player

    def winner(self):
        # row won
        has_zero = False
        for row in self.board:
            if abs(sum(row)) == 3:
                return row[0]
            if 0 in row:
                has_zero = True
        # column won
        for x in range(3):
            if abs(sum([self.board[0][x], self.board[1][x], self.board[2][x]])) == 3:
                return self.board[0][x]
        # diagonal won
        if abs(sum([self.board[0][0], self.board[1][1], self.board[2][2]])) == 3:
            return self.board[1][1]
        if abs(sum([self.board[2][0], self.board[1][1], self.board[0][2]])) == 3:
            return self.board[1][1]
        # draw
        if not has_zero:
            return 0
        return None

    def is_terminal(self):
        winner = self.winner()
        return winner != None

    def print(self):
        for i, row in enumerate(self.board):
            print("|".join(list(map(lambda x: str(x).rjust(2, " ").ljust(3), row))))
            if i < 2:
                print("-----------")
        print("")


class MinimaxPlayer:

    def __init__(self, is_min: bool, board: Board):
        self.is_min = is_min
        self.board = board

    def actions(self, board: Board):
        options = []
        for y, row in enumerate(board.board):
            for x, value in enumerate(row):
                if value == 0:
                    options.append((x, y))
        return options

    def player_number(self):
        if self.is_min:
            return -1
        return 1

    def minimax(self, board: Board, depth: int, alpha: int, beta: int, player: int):
        if depth == 0 or board.is_terminal():
            return board.winner()  # static evaluation

        if player == 1:  # maximizing player
            maxEval = -999
            for action in self.actions(board):
                newBoard = Board(board)
                newBoard.move(action, player)
                eval = self.minimax(newBoard, depth-1, alpha, beta, -1)
                maxEval = max(maxEval, eval)
                # alpha = best value maximizing player can guarantee
                alpha = max(alpha, eval)
                if beta <= alpha:  # prune if minimizing player already has a better move
                    break
            return maxEval
        else:  # minimizing player
            minEval = 999
            for action in self.actions(board):
                newBoard = Board(board)
                newBoard.move(action, player)
                eval = self.minimax(newBoard, depth-1, alpha, beta, 1)
                minEval = min(minEval, eval)
                # beta = best value minimizing player can guarantee
                beta = min(beta, eval)
                if beta <= alpha:  # prune if maximizing player already has a better move
                    break
            return minEval

    def make_move(self):
        player = self.player_number()
        actions = self.actions(board)
        evals = []
        for action in actions:
            newBoard = Board(board)
            newBoard.move(action, player)
            if newBoard.is_terminal():
                evals.append(newBoard.winner())
            else:
                evals.append(self.minimax(newBoard, 100, -999, 999, player*-1))

        # pick best move
        if player == 1:
            self.board.move(actions[evals.index(max(evals))], 1)
        else:
            self.board.move(actions[evals.index(min(evals))], -1)


if __name__ == "__main__":
    board = Board()

    playerOne = MinimaxPlayer(is_min=True, board=board)
    playerTwo = MinimaxPlayer(is_min=False, board=board)

    # init board with some step
    board.move((1, 1), 1)
    board.print()

    while True:
        playerOne.make_move()
        board.print()
        if board.is_terminal():
            break
        playerTwo.make_move()
        board.print()
        if board.is_terminal():
            break

    winner = board.winner()
    print("Draw" if winner == 0 else "Max Player" if winner == 1 else "Min Player")
