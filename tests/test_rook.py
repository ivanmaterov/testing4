import pytest

from chess.board import ChessBoard
from chess.chessman import Chessman
from chess.exceptions import CaptureException


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


def test_black_rook_capture_white_pawn(
    chess_board: ChessBoard,
    chessman_black_rook: Chessman,
    chessman_white_pawn: Chessman,
):
    """Test black rook capture a figure."""
    chessman_white_pawn_field = chess_board.state[4][0]

    chess_board.state[0][0].chessman = chessman_black_rook
    chessman_white_pawn_field.chessman = chessman_white_pawn

    chess_board.move_figure(chessman_black_rook, chessman_white_pawn_field)


def test_black_rook_capture_another_black_rook(
    chess_board: ChessBoard,
    chessman_black_rook: Chessman,
    chessman_another_black_rook: Chessman,
):
    """Test one black rook tries to capture another black rook.

    This move should lead to `CaptureException`.

    """
    chessman_another_black_rook_field = chess_board.state[2][0]

    chess_board.state[0][0].chessman = chessman_black_rook
    chessman_another_black_rook_field.chessman = chessman_another_black_rook

    with pytest.raises(CaptureException):
        chess_board.move_figure(
            chessman=chessman_black_rook,
            field=chessman_another_black_rook_field,
        )
