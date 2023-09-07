def CountingPositions(gamestate, maximizingPlayer):
    counts = 0
    result = gamestate.threeInRow()
    if result or gamestate.gameIsDrawn():
        return 1

    for bit_move in gamestate.possibleMoves():
        if maximizingPlayer:
            gamestate.bitboard_player1 |= bit_move  # Playing Move
            counts += CountingPositions(gamestate, False)
            gamestate.bitboard_player1 ^= bit_move  # Undoing move

        else:
            gamestate.bitboard_player2 |= bit_move  # Playing Move
            counts += CountingPositions(gamestate, True)
            gamestate.bitboard_player2 ^= bit_move  # Undoing move
    return counts