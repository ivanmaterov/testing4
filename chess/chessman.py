from __future__ import annotations

from typing import TYPE_CHECKING, Self, Type

from .exceptions import ChangeTypeException
from .interfaces import AbstractChessman, AbstractChessmanType
from .side import Side

if TYPE_CHECKING:
    from .board import ChessBoard
    from .field import ChessField


class Chessman(AbstractChessman):
    """Implementation of AbstractChessman."""
    def __init__(
        self,
        chessman_type: Type[AbstractChessmanType],
        side: Type[Side],
        chess_board: ChessBoard,
    ):
        super().__init__()

        self.side = side
        self.type = chessman_type(side=side)
        self.board = chess_board

    def get_position(self) -> ChessField:
        """Get current position on the board."""
        return self.board.get_figure_position(chessman=self)

    def go_to_position(self, chess_field):
        """Accupate position on the board."""
        chess_field.chessman = self

    def change_type(self, type: Type[AbstractChessmanType]) -> Self:
        """Change type for Pawn.

        Raises:
            ChangeTypeException if type of chessman is not Pawn
            ChangeTypeException if exchange is not allowed

        """
        from .type import Pawn
        if not isinstance(self.type, Pawn):
            raise ChangeTypeException('Type changing is only allowed for Pawn')
        if type not in Pawn.EXCHANGE_TYPES:
            raise ChangeTypeException(f'{type} is not allowed for Pawn')
        self.type = type(side=self.side)
        return self

    def __str__(self) -> str:
        return f'{self.type} @ {self.type.side}'
