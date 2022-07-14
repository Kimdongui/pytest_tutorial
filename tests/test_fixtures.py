from pytest import fixture
from random import randint

@fixture
def dice():
    return randint(1, 6)

def test_is_dice(dice):
    assert dice in [i for i in range(1, 3)]