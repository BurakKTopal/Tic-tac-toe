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
<img src=""/>

<p>
  In this case, the bitboard for PlayerOne would be $110000100$ and that for PlayerTwo $001010000$. The benefit of this is the efficient and concise code: less than 40 lines of code are there necessary to cover the <a href="">game logic</a>!
</p>


### Manipulating bitboards

