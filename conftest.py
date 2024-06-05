from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture(scope='function')
def burger():
    burger = Burger()

    mock_ingredient_sauce1 = Mock()
    mock_ingredient_sauce1.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient_sauce1.name = 'Сырный соус'
    mock_ingredient_sauce1.price = 39

    mock_ingredient_filling1 = Mock()
    mock_ingredient_filling1.type = INGREDIENT_TYPE_FILLING
    mock_ingredient_filling1.name = 'Лучок'
    mock_ingredient_filling1.price = 69

    burger.add_ingredient(mock_ingredient_sauce1)
    burger.add_ingredient(mock_ingredient_filling1)

    return burger


@pytest.fixture(scope='function')
def mock_ingredient_sauce1():
    mock_ingredient_sauce1 = Mock()
    mock_ingredient_sauce1.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient_sauce1.name = 'Сырный соус'
    mock_ingredient_sauce1.price = 39

    return mock_ingredient_sauce1


@pytest.fixture(scope='function')
def mock_ingredient_sauce2():
    mock_ingredient_sauce2 = Mock()
    mock_ingredient_sauce2.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient_sauce2.name = 'Кисло-сладкий соус'
    mock_ingredient_sauce2.price = 29

    return mock_ingredient_sauce2

@pytest.fixture(scope='function')
def mock_ingredient_filling1():
    mock_ingredient_filling1 = Mock()
    mock_ingredient_filling1.type = INGREDIENT_TYPE_FILLING
    mock_ingredient_filling1.name = 'Лучок'
    mock_ingredient_filling1.price = 69

    return mock_ingredient_filling1

@pytest.fixture(scope='function')
def mock_ingredient_filling2():
    mock_ingredient_filling2 = Mock()
    mock_ingredient_filling2.type = INGREDIENT_TYPE_FILLING
    mock_ingredient_filling2.name = 'Креветка'
    mock_ingredient_filling2.price = 149

    return mock_ingredient_filling2

@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = 'Крафтовая булочка'
    mock_bun.price = 129

    return mock_bun
