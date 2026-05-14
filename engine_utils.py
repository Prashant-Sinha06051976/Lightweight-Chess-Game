
import os
import chess
import chess.engine

ENGINE_PATH = "engine/stockfish.exe"

def get_engine():

    if not os.path.exists(ENGINE_PATH):
        return None

    return chess.engine.SimpleEngine.popen_uci(ENGINE_PATH)

def get_engine_move(board):

    engine = get_engine()

    if not engine:
        return None

    result = engine.play(
        board,
        chess.engine.Limit(time=0.2)
    )

    engine.quit()

    return result.move

def get_top_moves(board):

    engine = get_engine()

    if not engine:
        return []

    info = engine.analyse(
        board,
        chess.engine.Limit(depth=12),
        multipv=3
    )

    moves = []

    for entry in info:
        pv = entry.get("pv")

        if pv:
            moves.append(str(pv[0]))

    engine.quit()

    return moves

def evaluate_position(board):

    engine = get_engine()

    if not engine:
        return 0

    info = engine.analyse(
        board,
        chess.engine.Limit(depth=10)
    )

    score = info["score"].white().score(mate_score=10000)

    engine.quit()

    return score if score else 0
