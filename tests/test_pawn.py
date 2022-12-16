import pytest

from chess.board import ChessBoard
from chess.chessman import Chessman
from chess.exceptions import BadMoveException, CaptureException
from chess.type import Rook


def test_pawn_move(
    chess_board: ChessBoard,
    chessman_black_pawn: Chessman,
):
    """Test base move of figure."""
    new_field = chess_board.state[1][0]
    chess_board.state[0][0].chessman = chessman_black_pawn
    chess_board.move_figure(chessman_black_pawn, new_field)

    assert new_field.chessman is chessman_black_pawn


def test_pawn_move_to_wrong_direction(
    chess_board: ChessBoard,
    chessman_black_pawn: Chessman,
):
    """Test pawn move to wrong direction.

    Pawn can move only in one direction.

    """
    new_wrong_field = chess_board.state[0][0]

    chess_board.state[1][0].chessman = chessman_black_pawn
    with pytest.raises(BadMoveException):
        chess_board.move_figure(chessman_black_pawn, new_wrong_field)


def test_pawn_move_to_wrong_side(
    chess_board: ChessBoard,
    chessman_black_pawn: Chessman,
):
    """Test pawn move to wrong side.

    Pawn can't move left of right.

    """
    new_wrong_field = chess_board.state[1][1]

    chess_board.state[0][0].chessman = chessman_black_pawn
    with pytest.raises(BadMoveException):
        chess_board.move_figure(chessman_black_pawn, new_wrong_field)


def test_pawn_move_to_the_same_field(
    chess_board: ChessBoard,
    chessman_black_pawn: Chessman,
):
    """Test pawn move to the same field.

    This move is also prohibited in this implementation.

    """
    chess_board.state[0][0].chessman = chessman_black_pawn

    with pytest.raises(BadMoveException):
        chess_board.move_figure(chessman_black_pawn, chess_board.state[0][0])


def test_white_pawn_move(
    chess_board: ChessBoard,
    chessman_white_pawn: Chessman,
):
    """Test white pawn basic move."""
    new_field = chess_board.state[6][0]

    chess_board.state[7][0].chessman = chessman_white_pawn
    chess_board.move_figure(
        chessman=chessman_white_pawn,
        field=new_field
    )

    assert new_field.chessman is chessman_white_pawn


def test_black_pawn_capture_white_pawn(
    chess_board: ChessBoard,
    chessman_white_pawn: Chessman,
    chessman_black_pawn: Chessman,
):
    """Test one pawn capture another.

    Check that field is occupied by black pawn.
    Check that old field is empty.
    Check that white pawn has False status.

    """
    black_pawn_field = chess_board.state[4][0]
    white_pawn_field = chess_board.state[5][1]

    black_pawn_field.chessman = chessman_black_pawn
    white_pawn_field.chessman = chessman_white_pawn

    chess_board.move_figure(
        chessman=chessman_black_pawn,
        field=white_pawn_field,
    )

    assert white_pawn_field.chessman is chessman_black_pawn
    assert black_pawn_field.chessman is None
    assert not chessman_white_pawn.status


def test_black_pawn_wrong_capture_white_pawn(
    chess_board: ChessBoard,
    chessman_white_pawn: Chessman,
    chessman_black_pawn: Chessman,
):
    """Test pawn can't capture another pawn out of its range."""
    black_pawn_field = chess_board.state[2][0]
    white_pawn_field = chess_board.state[1][1]

    black_pawn_field.chessman = chessman_black_pawn
    white_pawn_field.chessman = chessman_white_pawn

    with pytest.raises(BadMoveException):
        chess_board.move_figure(
            chessman=chessman_black_pawn,
            field=white_pawn_field,
        )


def test_pawn_exchanging_into_rook(
    chess_board: ChessBoard,
    chessman_white_pawn: Chessman,
):
    """Test pawn exchanges into rook."""
    new_field = chess_board.state[0][0]

    chess_board.state[1][0].chessman = chessman_white_pawn
    chessman_rook = chess_board.exchange_pawn(
        pawn=chessman_white_pawn,
        field=new_field,
        type=Rook,
    )

    assert isinstance(chessman_rook.type, Rook)
    assert new_field.chessman is chessman_rook


def test_black_pawn_capture_another_black_pawn(
    chess_board: ChessBoard,
    chessman_black_pawn: Chessman,
    chessman_another_black_pawn: Chessman,
):
    """Test black pawn tries to capture another black pawn.

    This move should lead to `CaptureException`.

    """
    chessman_another_black_pawn_field = chess_board.state[1][1]

    chess_board.state[0][0].chessman = chessman_black_pawn
    chessman_another_black_pawn_field.chessman = chessman_another_black_pawn

    with pytest.raises(CaptureException):
        chess_board.move_figure(
            chessman=chessman_black_pawn,
            field=chessman_another_black_pawn_field,
        )
