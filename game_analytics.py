
import pandas as pd

def build_game_analysis(board):

    piece_values = {
        "P": 1,
        "N": 3,
        "B": 3,
        "R": 5,
        "Q": 9,
        "K": 0
    }

    white_material = 0
    black_material = 0

    for piece in board.piece_map().values():

        value = piece_values.get(
            piece.symbol().upper(),
            0
        )

        if piece.color:
            white_material += value
        else:
            black_material += value

    data = {
        "Metric": [
            "White Material",
            "Black Material",
            "Legal Moves",
            "Check",
            "Game Over"
        ],
        "Value": [
            white_material,
            black_material,
            board.legal_moves.count(),
            board.is_check(),
            board.is_game_over()
        ]
    }

    return pd.DataFrame(data)
