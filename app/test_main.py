from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "accepted values [0, 0] == [0, 0]",
        "accepted values [14, 14] == [0, 0]",
        "accepted values [15, 15] == [1, 1]",
        "accepted values [23, 23] == [1, 1]",
        "accepted values [24, 24] == [2, 2]",
        "accepted values [27, 27] == [2, 2]",
        "accepted values [28, 28] == [3, 2]",
        "accepted values [100, 100] == [21, 17]"

    ]

)
def test_get_human_age(cat_age, dog_age, result):
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (
            (10, 10, [0, 0]),
            (50, 20, [8, 1]),
            (0, 100, [0, 17])
        )
    ]
)
def test_get_human_age_list(cat_age: int, dog_age: int, result) -> None:
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
