from enum import Enum


class Field(Enum):
    PLAYER_O = "O"
    PLAYER_X = "X"
    EMPTY = "."


class ConnectGame:
    allowed_offsets = ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0))

    def __init__(self, board):
        self.board = self.parse_rect_board(board)

    def get_winner(self):
        return self.bfs_player_o() or self.bfs_player_x()

    @staticmethod
    def parse_rect_board(par_board_str):
        return [
            [Field(char) for char in row]
            for row in par_board_str.replace(" ", "").split("\n")
        ]

    def bfs_player_o(self):
        visited = [
            (0, coordy)
            for coordy, field in enumerate(self.board[0])
            if field == Field.PLAYER_O
        ]
        if visited and len(self.board) == 1:
            return Field.PLAYER_O.value
        return self.bfs(visited, Field.PLAYER_O)

    def bfs_player_x(self):
        visited = [
            (coordx, 0)
            for coordx, row in enumerate(self.board)
            if row[0] == Field.PLAYER_X
        ]
        if visited and len(self.board[0]) == 1:
            return Field.PLAYER_X.value
        return self.bfs(visited, Field.PLAYER_X)

    def bfs(self, visited, player_field):
        def victory(coordx, coordy, player_field):
            if player_field == Field.PLAYER_O:
                return coordx == len(self.board) - 1
            if player_field == Field.PLAYER_X:
                return coordy == len(self.board[0]) - 1
            return False

        to_check = list(visited)
        while to_check:
            new_to_check = []
            for coordx, coordy in to_check:
                for offsetx, offsety in self.allowed_offsets:
                    new_coordx, new_coordy = coordx + offsetx, coordy + offsety
                    if (
                        self.are_valid_coords(new_coordx, new_coordy)
                        and self.board[new_coordx][new_coordy] == player_field
                        and (new_coordx, new_coordy) not in visited
                    ):
                        if victory(new_coordx, new_coordy, player_field):
                            return player_field.value
                        new_to_check.append((new_coordx, new_coordy))
                        visited.append((new_coordx, new_coordy))
            to_check = new_to_check
        return ""

    def are_valid_coords(self, pointx, pointy):
        return 0 <= pointx < len(self.board) and 0 <= pointy < len(self.board[0])
