import pytest

from chess.board import ChessBoard
from chess.chessman import Chessman
from chess.side import Black, White
from chess.type import Pawn, Rook


@pytest.fixture
def chess_board() -> ChessBoard:
    return ChessBoard()


@pytest.fixture
def chessman_black_pawn(chess_board: ChessBoard) -> Chessman:
    return Chessman(
        chessman_type=Pawn,
        side=Black,
        chess_board=chess_board,
    )


@pytest.fixture
def chessman_another_black_pawn(chess_board: ChessBoard) -> Chessman:
    return Chessman(
        chessman_type=Pawn,
        side=Black,
        chess_board=chess_board,
    )


@pytest.fixture
def chessman_white_pawn(chess_board: ChessBoard) -> Chessman:
    return Chessman(
        chessman_type=Pawn,
        side=White,
        chess_board=chess_board,
    )


@pytest.fixture
def chessman_black_rook(chess_board: ChessBoard) -> Chessman:
    return Chessman(
        chessman_type=Rook,
        side=Black,
        chess_board=chess_board,
    )


@pytest.fixture
def chessman_another_black_rook(chess_board: ChessBoard) -> Chessman:
    return Chessman(
        chessman_type=Rook,
        side=Black,
        chess_board=chess_board,
    )
