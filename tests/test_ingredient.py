from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    # 4.0 проверка на корректное отображение цены
    def test_get_price_correct_price_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Сырный соус', 39)

        assert ingredient.get_price() == 39

    # 4.1 проверка на корректное отображение наименования
    def test_get_name_correct_name_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Сырный соус', 39)

        assert ingredient.get_name() == 'Сырный соус'

    # 4.2 проверка на корректное отображение типа наполнителя соус
    def test_get_type_correct_type_sauce_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Сырный соус', 39)

        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    # 4.3 проверка на корректное отображение типа наполнителя начинка
    def test_get_type_correct_type_filling_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Лучок', 69)

        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
