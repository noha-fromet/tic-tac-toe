import random


def make_ai_move(self):
    if self.ai_difficulty == "Easy":
        # Easy difficulty: choose a random move
        possible_moves = [(i,j) for i in range(3) for j in range(3) if not self.board[i][j]]
        if possible_moves:
            i,j = random.choice(possible_moves)
            self.make_move(i,j)
    elif self.ai_difficulty == "Medium":
        # Medium difficulty: try to block opponent's winning moves
        pass # TODO: implement medium difficulty logic
    elif self.ai_difficulty == "Hard":
        # Hard difficulty: use advanced algorithm to choose best move
        pass # TODO: implement hard difficulty logic