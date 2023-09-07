# Tic-tac-toe
Shortest GameLogic code ever?

## Setup
For cloning this repository open your prompt, choose the directory to clone in and enter:

  ```
git clone https://github.com/BurakKTopal/Tic-tac-toe.git
  ```
For the necessary packages:

  ```
pip install time pygame
  ```

## Game Logic

### Concept of bitboard
<p>
After I've recently programmed <a href="">chess</a>, I wanted to apply a concept to Tic-tac-toe which I came accros while coding; bitboards. Bitboards are essentially n-bit values representing the current board, depending on the board. For Tic-tac-toe, I've used two 9-bit values for describing the state of PlayerOne(crosses) and the state of PlayerTwo(naughts). 1 represents that the square is occupied, 0 that it's empty. As an example, consider following state:
</p>
<img src="\Media\bitboard-example.png", width = "50%"/>
<p>
  In this case, the bitboard for PlayerOne would be $110000100$ and that for PlayerTwo $001010000$. The benefit of this is the efficient and concise code: less than 40 lines of code are there necessary to cover the <a href="https://github.com/BurakKTopal/Tic-tac-toe/blob/main/GameLogic/RulesImplementation.py">game logic</a>!
</p>


### Manipulating bitboards
Updating the bitboards can be done by bit manipulations. Suppose that in the last positions, PlayerTwo plays between the two crosses. This move is happened on the square with index '3', counting from left->right, up->down, can be represented by a bit shift: 

  ```
move_bit = 1<<3  # Making move
  ```
Consequently, the bitboard of PlayerTwo can be updated with the OR operator:

  ```
gs.bitboard_player2 |= move_bit  # Making move
  ```
We can not only make a move, but we could also undo the move by making use of the XOR:

  ```
gs.bitboard_player2 ^= move_bit  # Undoing move
  ```
Checking if one of the players have won, we can map the current bitboards to the possible winning sequences. These are:
<ul>
<li>$100100100$ for vertically in first column</li>
<li>$010010010$ for vertically in second column</li>
<li>$001001001$ for vertically in third column</li>
<li>$111000000$ for horizontally in first row</li>
<li>$000111000$ for horizontally in second row</li>
<li>$000000111$ for horizontally in third row</li>
<li>$100010001$ for diagonally from left upper corner, to right down corner</li>
<li>$001010100$ for diagonally from right upper corner, to left down corner</li>
</ul>
With this, we can AND the current bitboards of the players with the possible configurations, if one of the operations would give back the possible configuration, then the game ends:

```
  def threeInRow(self):
      for element in self.possible_configs:
          if self.bitboard_player1 & element == element:
              return 1  # Player one wins
          elif self.bitboard_player2 & element == element:
              return 0b10  # Player two wins
      return 0
```

With all of this, checking for a draw is pretty straightforward:

```
    def gameIsDrawn(self):
        if self.bitboard_player1 | self.bitboard_player2 == 0b111111111:
            return 1
        return 0
```

With this use of bits, the possible moves can be given by looking at the ensemble of the bitboards and check which squares are empty by looking for a zero:

```
    def possibleMoves(self):
        occupied_squares_bit = (self.bitboard_player2 | self.bitboard_player1)  # Occupied squares
        return [1 << i for i in range(9) if not occupied_squares_bit & (1 << i)]
```
