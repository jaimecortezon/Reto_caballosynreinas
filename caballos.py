from __future__ import annotations


def posicion_valida(posicion: tuple[int, int], n: int) -> list[tuple[int, int]]:
    """
    Find all the valid positions a knight can move to from the current position.
    >>> posicion_valida((1, 3), 4)
    [(2, 1), (0, 1), (3, 2)]
    """

    y, x = posicion
    posiciones = [
        (y + 1, x + 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 1, x - 2),
        (y + 2, x + 1),
        (y + 2, x - 1),
        (y - 2, x + 1),
        (y - 2, x - 1),
    ]
    posiciones_permitidas = []

    for posicion in posiciones:
        y_test, x_test = posicion
        if 0 <= y_test < n and 0 <= x_test < n:
            posiciones_permitidas.append(posicion)

    return posiciones_permitidas


def esta_completo(board: list[list[int]]) -> bool:
    """
    Check if the board (matrix) has been completely filled with non-zero values.
    >>> esta_completo([[1]])
    True
    >>> esta_completo([[1, 2], [3, 0]])
    False
    """

    return not any(elem == 0 for row in board for elem in row)


def caballos_ayudante(
    board: list[list[int]], pos: tuple[int, int], curr: int
) -> bool:
    """
    Helper function to solve knight tour problem.
    """

    if esta_completo(board):
        return True

    for position in posicion_valida(pos, len(board)):
        y, x = position

        if board[y][x] == 0:
            board[y][x] = curr + 1
            if caballos_ayudante(board, position, curr + 1):
                return True
            board[y][x] = 0

    return False


def abrir_caballos(n: int) -> list[list[int]]:
    """
    Find the solution for the knight tour problem for a board of size n. Raises
    ValueError if the tour cannot be performed for the given size.
    >>> abrir_caballos(1)
    [[1]]
    >>> abrir_caballos(2)
    Traceback (most recent call last):
        ...
    ValueError: Open Kight Tour cannot be performed on a board of size 2
    """

    board = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            board[i][j] = 1
            if caballos_ayudante(board, (i, j), 1):
                return board
            board[i][j] = 0

    raise ValueError(f"Open Kight Tour cannot be performed on a board of size {n}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()