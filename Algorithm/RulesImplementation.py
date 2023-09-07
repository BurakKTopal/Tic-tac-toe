class GameState:
    def __init__(self):
        # player one is the player with the cross, player two is the one playing the Naughts
        self.bitboard_player1 = 0
        self.bitboard_player2 = 0
        # Possible end-game configurations
        self.possible_configs = {0b100100100, 0b010010010, 0b001001001, 0b111000000, 0b000111000, 0b000000111,
                                 0b100010001, 0b001010100}

    def playMove(self, square_coordinate, player_one):
        coordinate_transformation = {(0, 0): 8, (1, 0): 7, (2, 0): 6, (0, 1): 5, (1, 1): 4, (2, 1): 3,
                                     (0, 2): 2, (1, 2): 1, (2, 2): 0}
        move_bit = (1 << coordinate_transformation[square_coordinate])
        if move_bit & (self.bitboard_player2 | self.bitboard_player1):
            return 0
        if player_one:
            self.bitboard_player1 |= move_bit
            return 1
        else:
            self.bitboard_player2 |= move_bit
            return 1

    def threeInRow(self):
        for element in self.possible_configs:
            if self.bitboard_player1 & element == element:
                return 1  # Player one wins
            elif self.bitboard_player2 & element == element:
                return 0b10  # Player two wins
        return 0

    def gameIsDrawn(self):
        if self.bitboard_player1 | self.bitboard_player2 == 0b111111111:
            return 1
        return 0

    def possibleMoves(self):
        occupied_squares_bit = (self.bitboard_player2 | self.bitboard_player1)  # Occupied squares
        return [1 << i for i in range(9) if not occupied_squares_bit & (1 << i)]
