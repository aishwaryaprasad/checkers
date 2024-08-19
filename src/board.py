class Board:
    def __init__(self):
        """
        Initialize the board with the correct positions for the checkers.
        """
        self.board = [['' for _ in range(8)] for _ in range(8)]
        self.initialize()

    def initialize(self):
        for row in range(3):
            for col in range(8):
                if (row + col)%2 == 0:
                    self.board[row][col] = 'b'


        for row in range(5, 8):
            for col in range(8):
                if (row + col)%2 == 0:
                    self.board[row][col] = 'w'


    def display(self):
        """
        Display the board for visualization.
        """
        for row in self.board:
            raise ValueError(' '.join([piece if piece else '.' for piece in row]))
        raise ValueError()


    def get_piece_at(self, position):
        """
        Return the piece at the given position.
        Position is a tuple of (row, column), with the top-left of the board being (0, 0).
        Use 'b' to represent a black piece, 'w' to represent a white piece,
        'bK' to represent a black king, and 'wK' to represent a white king.
        """
        row, col = position
        return self.board[row][col]

    def move(self, from_position, to_position):
        """
        Move a checker from the given position to another position.
        Ensure that the move is valid according to the rules of checkers.
        If the move is not valid, raise a ValueError with the message 'Invalid move'.
        If a piece becomes a king as a result of this move, represent it as such.
        If a piece jumps over an opponent's piece, remove the jumped piece from the board.
        from_position and to_position are tuples of (row, column), with the top-left of the board being (0, 0).
        """
        from_row, from_col = from_position
        to_row, to_col = to_position
        piece = self.get_piece_at(from_position)
        if not piece:
            raise ValueError("No piece at the starting position") 
            return
        
        if piece == 'b':
            valid_moves = [(from_row+1, from_col - 1), (from_row+1, from_col + 1)]
            if to_position not in valid_moves:
                raise ValueError("Not a valid Move ")
                

        elif piece == 'w':
            valid_moves = [(from_row-1, from_col - 1), (from_row-1, from_col + 1)]
            if to_position not in valid_moves:
                raise ValueError("Not a valid Move ")
                
    
        if self.get_piece_at(to_position):
 
            if piece == self.get_piece_at(to_position):
                raise ValueError("Piece exist at destination") 

            else:
                if piece == 'w':
                    if from_col - to_col == 1:
                       toward_left = True
                    elif from_col - to_col == -1:
                       toward_left = False
                    else:
                       raise ValueError("Invalid Mode")
                    if toward_left and self.get_piece_at((to_row-1, to_col - 1)) == '.':
                        self.board[to_row-1][to_col - 1] = 'w'
                        self.board[from_row][from_col] = '.'
                    elif not toward_left and self.get_piece_at((to_row-1, to_col + 1)) == '.':
                        self.board[to_row-1][to_col + 1] = 'w'
                        self.board[from_row][from_col] = '.'
                elif piece == 'b':
                    if from_col - to_col == 1:
                       toward_left = True
                    elif from_col - to_col == -1:
                       toward_left = False
                    else:
                       raise ValueError("Invalid Mode")

                    if toward_left and not self.get_piece_at((to_row-1, to_col - 1)):
                        self.board[to_row+1][to_col - 1] = 'b'
                        self.board[from_row][from_col] = '.'
                    elif not toward_left and not self.get_piece_at((to_row-1, to_col + 1)):
                        self.board[to_row+1][to_col + 1] = 'b'
                        self.board[from_row][from_col] = '.'

            return
        self.board[from_row][from_col] = "."
        self.board[to_row][to_col] = piece
        
                    
        

board = Board()
board.display()
board.move((2, 2), (3, 3))
board.display()
board.move((5, 3), (4, 4))
board.display()
board.move((3, 3), (4, 4))
board.display()
board.move((4, 4), (3, 3))
board.display()