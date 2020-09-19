class node:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.isWall = False
        self.isStar = False
        self.isDest = False
