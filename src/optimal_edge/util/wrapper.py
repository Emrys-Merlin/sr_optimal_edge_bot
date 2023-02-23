from .math import bl_sc_select

BL_TEXT = """**Use *Breaking the Limit* (add edge pool before the role + reroll 6s)**

Your dice pool is {pool}. There is no limit.
"""
SC_TEXT = """**Use *Second Chance* (reroll all failure dice)**

Your dice pool is {pool}. Your limit still applies and is {limit}.
"""
TIE_TEXT = """**You found a I tie combination. Do whatever you want ;-)**

If you use *Breaking the Limit* your dice pool is {bl_pool}. There is no limit.
If you use *Second Chance* your dice pool is {sc_pool}. In this case, your limit still applies and is {limit}.
"""


def get_response(pool: int, edge: int, limit: int) -> str:
    """Report whether Breaking the Limit or Second Chance is superior.

    Parameters
    ----------
    interaction : _type_
        Some discord bot object
    pool : int
        The dice pool (without edge)
    edge : int
        Edge attribute
    limit : int
        Limit for the role
    """
    res = bl_sc_select(pool, edge, limit)
    if res == 1:
        text = BL_TEXT.format(pool=pool + edge)
    elif res == 0:
        text = TIE_TEXT.format(bl_pool=pool + edge, sc_pool=pool, limit=limit)
    else:
        text = SC_TEXT.format(pool=pool, limit=limit)

    return text
