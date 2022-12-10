from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Type

from .side import Side

# питон кусок трижды переваренного кала
if TYPE_CHECKING:
    from .field import ChessField


class AbstractChessman(ABC):
    """Abstract class for chessman."""
    status: bool

    def __init__(self):
        self.status = True

    def capture(self):
        self.status = False

    @abstractmethod
    def get_position(self) -> ChessField:
        """Get current position for figure.

        Returns:
            Current position of figure.

        """

    @abstractmethod
    def go_to_position(self, chess_field: ChessField):
        """Go to position on the chess board.

        Attributes:
            chess_fields: an instance of chess field>

        """


class AbstractChessmanType(ABC):
    """Abstract class for chessman type."""
    def __init__(self, side: Type[Side]):
        self.side = side

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def is_valid_move(
        self,
        old_field: ChessField,
        new_field: ChessField,
        is_capture: bool,
        *args,
        **kwargs,
    ) -> bool:
        """Returns whenever chessman can move to the new field.

        Attributes:
            old_field a field to move from
            new_field a field to move in

        Returns:
            True - If chessman can move
            False - otherwise

        """

    def __str__(self) -> str:
        return self.name
