def minimax(gamestate, maximizingPlayer):
    if gamestate.threeInRow() == 1:
        return 1, None
    elif gamestate.threeInRow() == 0b10:
        return -1, None
    elif gamestate.gameIsDrawn():
        return 0, None

    best_bit_move = None
    best_eval = float('-inf') if maximizingPlayer else float('inf')

    for bit_move in gamestate.possibleMoves():
        if maximizingPlayer:
            gamestate.bitboard_player1 |= bit_move  # Playing Move
            eval, _ = minimax(gamestate, False)
            gamestate.bitboard_player1 ^= bit_move  # Undoing move
            if eval > best_eval:
                best_eval = eval
                best_bit_move = bit_move
        else:
            gamestate.bitboard_player2 |= bit_move  # Playing Move
            eval, _ = minimax(gamestate, True)
            gamestate.bitboard_player2 ^= bit_move  # Undoing move
            if eval < best_eval:
                best_eval = eval
                best_bit_move = bit_move

    return best_eval, best_bit_move
