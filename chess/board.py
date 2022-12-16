from __future__ import annotations

from typing import Type

from .chessman import Chessman
from .exceptions import (
    BadMoveException,
    CaptureException,
    FigureIsCapturedException
)
from .field import ChessField
from .interfaces import AbstractChessmanType


class ChessBoard:
    """Class represents chess board with state.

    Board can operates by chessmans.

    """
    def __init__(self):
        """Init state."""
        self.state = [
            [
                ChessField(row=row, col=col)
                for col in ChessField.cols
            ]
            for row in ChessField.rows
        ]

    @classmethod
    def initialize_game(cls) -> ChessBoard:
        """Initialize standard game board.

        TODO: finish the method when all figure will be implemented

        """
        return NotImplemented

    def _validate_chessman(self, chessman: Chessman):
        """Check chessman status.

        Raises:
            FigureIsCapturedException if chessman was captured.

        """
        if not chessman.status:
            raise FigureIsCapturedException(f'{chessman}')

    def _validate_move(self, chessman: Chessman, field: ChessField):
        """Validate chessman move.

        Raises:
            BadMoveException if chessmen try to move on the wrong field or
            performs wrong capture.

        """
        is_valid = chessman.type.is_valid_move(
            old_field=chessman.get_position(),
            new_field=field,
            is_capture=bool(field.chessman),
            board=self,
        )
        if not is_valid:
            raise BadMoveException(
                f'{chessman} move to {field} is not possible.',
            )

    def move_figure(self, chessman: Chessman, field: ChessField):
        """Move figure to field.

        Run chessman validation and set up new position.

        Raises:
            CaptureException if chessman tries to capture a figure with the
            same side.

        """
        self._validate_chessman(chessman)
        self._validate_move(chessman, field)

        chessman.get_position().chessman = None

        if field.chessman:
            if chessman.side is field.chessman.side:
                raise CaptureException(
                    f'Figure {chessman} tries to capture a figure with'
                    f' the same side ({chessman.side})'
                )
            field.chessman.capture()
        field.chessman = chessman

    def exchange_pawn(
        self,
        pawn: Chessman,
        field: ChessField,
        type: Type[AbstractChessmanType],
    ) -> Chessman:
        """Move pawn and change type."""
        self.move_figure(pawn, field)
        return pawn.change_type(type)

    def get_figure_position(self, chessman: Chessman) -> ChessField:
        """Get current position for figure."""
        for rows in self.state:
            for field in rows:
                if field.chessman is chessman:
                    return field
        raise FigureIsCapturedException(f'{chessman} was captured')
