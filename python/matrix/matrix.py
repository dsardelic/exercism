class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        return [
            int(element)
            for element in self.matrix_string.split("\n")[index - 1].split()
        ]

    def column(self, index):
        return [int(row.split()[index - 1]) for row in self.matrix_string.split("\n")]
