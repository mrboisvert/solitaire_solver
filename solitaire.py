import numpy as np

class Solitaire:
    def __init__(self, board):
        self.board = board
        self.width = board.shape[0]
        self.length = board.shape[1]
        self.domain = []
        path = []
        path.append(np.copy(board))
        self.domain.append(path)
        self.goal_spot = (self.width // 2, self.length // 2)

    def goal(self, board_state):
        if np.count_nonzero(board_state) == 17:
            if board_state[self.goal_spot[0], self.goal_spot[1]] == 1:
                return True
            else:
                return False
        else:
            return False

    def explore(self, board_state, path):
        del self.domain[-1]
        for index, value in np.ndenumerate(board_state):
            if value != 1:
                continue
            if index[0] - 2 >= 0:
                if board_state[index[0] - 1, index[1]] == 1 and board_state[index[0] - 2, index[1]] == 0:
                    new_board_state = self.step(board_state, "up", index)
                    new_path = path.copy()
                    new_path.append(new_board_state)
                    self.domain.append(new_path)
            if index[0] + 2 < self.width:
                if board_state[index[0] + 1, index[1]] == 1 and board_state[index[0] + 2, index[1]] == 0:
                    new_board_state = self.step(board_state, "down", index)
                    new_path = path.copy()
                    new_path.append(new_board_state)
                    self.domain.append(new_path)
            if index[1] - 2 >= 0:
                if board_state[index[0], index[1] - 1] == 1 and board_state[index[0], index[1] - 2] == 0:
                    new_board_state = self.step(board_state, "left", index)
                    new_path = path.copy()
                    new_path.append(new_board_state)
                    self.domain.append(new_path)
            if index[1] + 2 < self.length:
                if board_state[index[0], index[1] + 1] == 1 and board_state[index[0], index[1] + 2] == 0:
                    new_board_state = self.step(board_state, "right", index)
                    new_path = path.copy()
                    new_path.append(new_board_state)
                    self.domain.append(new_path)

    def step(self, board_state, direction, piece):
        # assumes only possible moves
        board = np.copy(board_state)
        if direction == "up":
            board[piece[0] - 1, piece[1]] = 0
            board[piece[0], piece[1]] = 0
            board[piece[0] - 2, piece[1]] = 1
        elif direction == "down":
            board[piece[0] + 1, piece[1]] = 0
            board[piece[0], piece[1]] = 0
            board[piece[0] + 2, piece[1]] = 1
        elif direction == "left":
            board[piece[0], piece[1] - 1] = 0
            board[piece[0], piece[1]] = 0
            board[piece[0], piece[1] - 2] = 1
        elif direction == "right":
            board[piece[0], piece[1] + 1] = 0
            board[piece[0], piece[1]] = 0
            board[piece[0], piece[1] + 2] = 1

        return board

    def print_path(self, path):
        for index, board in enumerate(path):
            print(board)
            if index < len(path) - 1:
                print("    |")
                print("    |")
                print("    V")
            else:
                print("")

    def solve(self): # depth first search
        while True:
            path = self.domain[-1]
            #self.print_path(path)
            if self.goal(path[-1]):
                print("Solution found")
                self.print_path(path)
                return
            self.explore(path[-1], path)
        

board = np.array([[2, 2, 1, 1, 1, 2, 2], [2, 2, 1, 1, 1, 2, 2], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [2, 2, 1, 1, 1, 2, 2], [2, 2, 1, 1, 1, 2, 2]])
game = Solitaire(board)
game.solve()
