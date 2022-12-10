from typing import Optional

from .chessman import Chessman


class ChessField:
    """Class represents field for chess board."""
    cols = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    rows = tuple(sorted(
        map(str, range(1, 9)),
        reverse=True
    ))

    def __init__(
        self,
        row: str,
        col: str,
        chessman: Optional[Chessman] = None
    ):
        """Init position of field and set up chessman."""
        if col not in self.cols or row not in self.rows:
            ValueError('There is no such field.')
        self.row = row
        self.col = col
        self.chessman = chessman

    @property
    def coordinates(self) -> tuple[int, int]:
        """Get relative coordinates."""
        return len(self.rows) - int(self.row), self.cols.index(self.col)

    @property
    def is_busy(self) -> bool:
        """Get if the field is busy or not."""
        return self.chessman is not None

    def __repr__(self) -> str:
        return f'{self.col}{self.row}'
