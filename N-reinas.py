from __future__ import annotations


def profundidad_primera_busqueda(
    posible_casilla: list[int],
    colisiones_diagonal_dcha: list[int],
    colisiones_diagonal_izq: list[int],
    casillas: list[list[str]],
    n: int,
) -> None:
    """
    >>> casilas = []
    >>> profumdidas_primera_busqueda([], [], [], casillas, 4)
    >>> for casilla in casillas:
    ...     print(casilla)
    ['. Q . . ', '. . . Q ', 'Q . . . ', '. . Q . ']
    ['. . Q . ', 'Q . . . ', '. . . Q ', '. Q . . ']
    """

    # Get next row in the current board (posible_casilla) to fill it with a queen
    row = len(posible_casilla)

    # If row is equal to the size of the board it means there are a queen in each row in
    # the current board (posible_casilla)
    if row == n:
        # We convert the variable posible_casilla that looks like this: [1, 3, 0, 2] to
        # this: ['. Q . . ', '. . . Q ', 'Q . . . ', '. . Q . ']
        casillas.append([". " * i + "Q " + ". " * (n - 1 - i) for i in posible_casilla])
        return

    # We iterate each column in the row to find all possible results in each row
    for col in range(n):

        # We apply that we learned previously. First we check that in the current board
        # (posible_casilla) there are not other same value because if there is it means
        # that there are a collision in vertical. Then we apply the two formulas we
        # learned before:
        #
        # 45º: y - x = b or 45: row - col = b
        # 135º: y + x = b or row + col = b.
        #
        # And we verify if the results of this two formulas not exist in their variables
        # respectively.  (colisiones_diagonal_dcha, colisiones_diagonal_izq)
        #
        # If any or these are True it means there is a collision so we continue to the
        # next value in the for loop.
        if (
            col in posible_casilla
            or row - col in colisiones_diagonal_dcha
            or row + col in colisiones_diagonal_izq
        ):
            continue

        # If it is False we call dfs function again and we update the inputs
        profundidad_primera_busqueda(
            posible_casilla + [col],
            colisiones_diagonal_dcha + [row - col],
            colisiones_diagonal_izq + [row + col],
            casillas,
            n,
        )


def n_reinas_solucion(n: int) -> None:
    casillas: list[list[str]] = []
    profundidad_primera_busqueda([], [], [], casillas, n)

    # Print all the casillas
    for casilla in casillas:
        for column in casilla:
            print(column)
        print("")

    print(len(casillas), "solutions were found.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    n_reinas_solucion(4)