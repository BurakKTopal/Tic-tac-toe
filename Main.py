import pygame as p
from GameLogic.RulesImplementation import *
# Defining the window
WIDTH = HEIGHT = 512
DIMENSION = 3
SQ_SIZE = HEIGHT // DIMENSION  # square size
MAX_FPS = 128
IMAGES = {}

# loading the images
def load_images():
    IMAGES["cross"] = p.transform.scale(p.image.load("Images/Tic-tac-toe-cross.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES["naught"] = p.transform.scale(p.image.load("Images/Tic-tac-toe-naught.png"), (SQ_SIZE, SQ_SIZE))
    return

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
    drawGameState(screen)
    while running:

        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                input('the game ended!')

            elif e.type == p.MOUSEBUTTONDOWN and player1:
                location = p.mouse.get_pos()  # (x,y) location of the mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if gs.playMove((col, row), True):
                    drawCross(screen, col, row)
                    player1, player2 = False, True
                else:
                    print("illegal move, try again")

            elif e.type == p.MOUSEBUTTONDOWN and player2:
                location = p.mouse.get_pos()  # (x,y) location of the mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if gs.playMove((col, row), False):
                    drawNaught(screen, col, row)
                    player1, player2 = True, False
                else:
                    print("illegal move, try again")

            elif gs.threeInRow():
                input("Game ended")
                running = False
                break
            elif gs.gameIsDrawn():
                input("Draw!")
                running = False
                break
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
            border_width = 1
            p.draw.rect(screen, "black", square, border_width)
    return

def drawCross(screen, col, row):
    screen.blit(IMAGES["cross"], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
    return


def drawNaught(screen, col, row):
    screen.blit(IMAGES["naught"], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
    return

if __name__ == '__main__':
    main()
