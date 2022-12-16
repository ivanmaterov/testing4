from typing import Iterable

from .board import ChessBoard
from .field import ChessField
from .interfaces import AbstractChessmanType
from .side import White


class Rook(AbstractChessmanType):
    """Representation of rook figure."""
    def is_valid_move(
        self,
        old_field: ChessField,
        new_field: ChessField,
        is_capture: bool,
        *args,
        **kwargs,
    ) -> bool:
        """Validate move."""
        board: ChessBoard = kwargs.get('board', None)
        assert board, 'Provide board for this type of figure.'
        old_field_row, old_field_col = old_field.coordinates
        new_field_row, new_field_col = new_field.coordinates

        row_field_length = old_field_row - new_field_row
        col_field_length = old_field_col - new_field_col

        # validate by cols
        if row_field_length == 0 and col_field_length != 0:
            row_index = old_field_row
            slice = (
                board.state[row_index][new_field_col: old_field_col]
                if col_field_length > 0 else
                board.state[row_index][old_field_col + 1: new_field_col + 1]
            )

        # validate by rows
        if row_field_length != 0 and col_field_length == 0:
            col_index = old_field_col
            row_list = [row[col_index] for row in board.state]
            slice = (
                row_list[new_field_row: old_field_row]
                if row_field_length > 0 else
                row_list[old_field_row + 1: new_field_row + 1]
            )

        # there is no need to check last field if it's `capture` move
        slice = slice[:-1] if is_capture else slice
        return self._check_is_busy(slice)

    def _check_is_busy(self, slice: Iterable[ChessField]) -> bool:
        for item in slice:
            if item.is_busy:
                return False
        return True


class Pawn(AbstractChessmanType):
    """Representation of pawn figure."""
    EXCHANGE_TYPES = (
        Rook,
    )
    first_move = True

    def is_valid_move(
        self,
        old_field: ChessField,
        new_field: ChessField,
        is_capture: bool,
        *args,
        **kwargs,
    ) -> bool:
        if is_capture:
            return self._validate_capture(old_field, new_field)
        return self._validate_move(old_field, new_field)

    def _validate_capture(
        self,
        old_field: ChessField,
        new_field: ChessField,
    ) -> bool:
        """Validate pawn capture."""
        old_field_row, old_field_col = old_field.coordinates
        new_field_row, new_field_col = new_field.coordinates

        length_of_move = old_field_row - new_field_row
        abs_length_of_move = abs(length_of_move)

        if all([
            abs(old_field_col - new_field_col) == 1,
            abs_length_of_move == 1,
            self._check_direction(old_field, new_field),
        ]):
            self.first_move = False
            return True
        return False

    def _validate_move(
        self,
        old_field: ChessField,
        new_field: ChessField,
    ) -> bool:
        """Validate pawn move.

        A move is valid if the pawn doesn't change col
        and make move:
            1) If first move: 1 or 2 fields
            2) If non first move: 1 fields
        Also pawn can move only one direction (up or down the board)

        """
        old_field_row, old_field_col = old_field.coordinates
        new_field_row, new_field_col = new_field.coordinates

        length_of_move = old_field_row - new_field_row
        abs_length_of_move = abs(length_of_move)
        if all([
            # check if pawn has the same row
            old_field_col == new_field_col,

            # check abs length of move
            abs_length_of_move == 2 or abs_length_of_move == 1
            if self.first_move else
            abs_length_of_move == 1,

            # check direction
            self._check_direction(old_field, new_field),
        ]):
            self.first_move = False
            return True
        return False

    def _check_direction(
        self,
        old_field: ChessField,
        new_field: ChessField,
    ) -> bool:
        """Check direction of move.

        White pawns move up the board. So length_of_move must be positive
        for White pawns

        Black pawns move down the board. Tt must be negative for Black

        Returns:
            True if direction for this pawn is correct
            False otherwise

        """
        old_field_row, _ = old_field.coordinates
        new_field_row, _ = new_field.coordinates
        length_of_move = old_field_row - new_field_row

        if self.side is White:
            return length_of_move > 0
        return length_of_move < 0
