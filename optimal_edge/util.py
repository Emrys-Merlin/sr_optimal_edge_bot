from math import comb as binomial
from typing import Optional


def expected_value_bl(pool: int, edge: int, limit: Optional[int] = None) -> float:
    """Compute expected value of succeses for Breaking the Limit

    Parameters
    ----------
    pool : int
        Dice pool (without edge)
    edge : int
        Edge attribute
    limit : int | None, optional
        Limit (ignored), by default None

    Returns
    -------
    float
        Expected value
    """
    return 0.4 * (pool + edge)


def p_sc(n: int, k: int) -> float:
    """Probability for k successes with n dice using Second Chance

    This method ignores limits.
    This method implements a binomial distribution with p = 5/9

    Parameters
    ----------
    n : int
        Dice pool
    k : int
        Number of successes

    Returns
    -------
    float
        Probability for k successes in n throws.
    """
    return binomial(n, k) * (5 / 9) ** k * (1 - 5 / 9) ** (n - k)


def expected_value_sc(pool: int, edge: int, limit: int) -> float:
    """Compute expected value of succeses for Second Chance

    Parameters
    ----------
    pool : int
        Dice pool (without edge)
    edge : int
        Edge attribute (ignored)
    limit : int, optional
        Limit, by default None

    Returns
    -------
    float
        Expected value
    """

    ev = 5 / 9 * pool
    residue = sum((k - limit) * p_sc(pool, k) for k in range(limit + 1, pool + 1))
    return ev - residue


def bl_sc_select(pool: int, edge: int, limit: int) -> int:
    """Check whether Breaking the Limit or Second Chance is superior or if there is a tie

    1: BL
    0: Tie
    -1: SC

    Parameters
    ----------
    pool : int
        Dice pool (without edge)
    edge : int
        Edge attribute
    limit : int
        Limit

    Returns
    -------
    int
        1: BL, 0: Tie, -1: SC
    """
    ev_bl = expected_value_bl(pool, edge, limit)
    ev_sc = expected_value_sc(pool, edge, limit)

    if ev_bl > ev_sc:
        return 1

    if ev_bl == ev_sc:
        return 0

    return -1
