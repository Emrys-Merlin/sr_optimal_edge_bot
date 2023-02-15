import pytest

from optimal_edge.util import bl_sc_select


def no_limit_select(pool: int, edge: int) -> int:
    """Prediction, if we can ignore the limit

    Parameters
    ----------
    pool : int
        Dice pool (wihtout edge)
    edge : int
        Edge attribute

    Returns
    -------
    int
        1: BL, 0: Tie, -1: SC
    """
    cutoff = 7 / 18

    frac = edge / pool

    if frac == cutoff:
        return 0

    if frac < cutoff:
        return -1

    return 1


@pytest.mark.parametrize(
    argnames=["pool", "edge", "limit"],
    argvalues=[
        [20, 1, 20],
        [5, 5, 5],
        [18, 7, 18],
        [18, 6, 18],
        [18, 8, 18],
    ],
)
def test_bl_sc_select_high_limit(pool: int, edge: int, limit: int):
    assert bl_sc_select(pool, edge, limit) == no_limit_select(pool, edge)


@pytest.mark.parametrize(
    argnames=["pool", "edge"],
    argvalues=[
        [20, 1],
        [5, 5],
        [18, 3],
        [18, 7],
    ],
)
def test_bl_sc_select_zero_limit(pool: int, edge: int):
    assert bl_sc_select(pool, edge, 0) == 1
