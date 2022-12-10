from chess.board import ChessBoard
from chess.chessman import Chessman


def test_rook_move_by_rows_down(
    chess_board: ChessBoard,
    chessman_black_rook: Chessman,
):
    """Test rook move by rows down."""
    new_field = chess_board.state[7][3]

    chess_board.state[0][3].chessman = chessman_black_rook
    chess_board.move_figure(chessman_black_rook, new_field)

    assert new_field.chessman is chessman_black_rook


def test_rook_move_by_rows_up(
    chess_board: ChessBoard,
    chessman_black_rook: Chessman,
):
    """Test rook move by rows up."""
    new_field = chess_board.state[0][0]

    chess_board.state[7][0].chessman = chessman_black_rook
    chess_board.move_figure(chessman_black_rook, new_field)
    assert new_field.chessman is chessman_black_rook


def test_rook_move_by_cols_right(
    chess_board: ChessBoard,
    chessman_black_rook: Chessman,
):
    """Test rook move by rows right."""
    new_field = chess_board.state[0][7]

    chess_board.state[0][0].chessman = chessman_black_rook
    chess_board.move_figure(chessman_black_rook, new_field)

    assert new_field.chessman is chessman_black_rook


def test_rook_move_by_cols_left(
    chess_board: ChessBoard,
    chessman_black_rook: Chessman,
):
    """Test rook move by rows left."""
    new_field = chess_board.state[0][0]

    chess_board.state[0][7].chessman = chessman_black_rook
    chess_board.move_figure(chessman_black_rook, new_field)

    assert new_field.chessman is chessman_black_rook
