import pytest

from optimal_edge.util import get_response


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
def test_get_response(pool: int, edge: int, limit: int):
    assert isinstance(get_response(pool, edge, limit), str)
