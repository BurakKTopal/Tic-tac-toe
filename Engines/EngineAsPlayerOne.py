import time
from Main import *
from Algorithm.Minimax import *
# defining the window
WIDTH = HEIGHT = 512
DIMENSION = 3
SQ_SIZE = HEIGHT // DIMENSION  # square size
MAX_FPS = 240


bit_to_co = {256: (0, 0), 128: (1, 0), 64: (2, 0), 32: (0, 1), 16: (1, 1), 8: (2, 1),
             4: (0, 2), 2: (1, 2), 1: (2, 2)}

load_images()
gs = GameState()


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    running = True
    player1 = True
    player2 = False
    # menu to ask what the persons wants to do: BOT(white, black) or multiplayer
    drawGameState(screen)
    while running:

        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                input('the game ended!')
            elif gs.threeInRow():
                input("Game ended")
                running = False
                break
            elif gs.gameIsDrawn():
                input("Draw!")
                running = False
                break
            elif player1:
                start = time.perf_counter()
                eval, best_bit_move = minimax(gs, True)
                end = time.perf_counter()
                print("---------------------------")
                print("Time to make a move:", end-start)
                gs.bitboard_player1 |= best_bit_move  # Updating the board

                col, row = bit_to_co[best_bit_move]
                drawCross(screen, col, row)

                player1, player2 = False, True

            elif e.type == p.MOUSEBUTTONDOWN and player2:
                location = p.mouse.get_pos()  # (x,y) location of the mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if gs.playMove((col, row), False):
                    drawNaught(screen, col, row)
                    player1, player2 = True, False
                else:
                    print("illegal move, try again")


        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen):
    """
    Drawing current chess board
    """
    drawBoard(screen)


def drawBoard(screen):
    """
    Drawing the current board
    """
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            square = p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            p.draw.rect(screen, 'white', square)
            border_width = 2
            p.draw.rect(screen, "black", square, border_width)
    return


def drawCross(screen, col, row):
    screen.blit(IMAGES["cross"], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
    return


def drawNaught(screen, col, row):
    screen.blit(IMAGES["naught"], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
