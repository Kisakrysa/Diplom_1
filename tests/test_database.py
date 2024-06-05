from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    # 3.0 проверка на получение результата по булкам
    def test_available_buns_success_return(self):
        data = Database()
        data_buns = data.available_buns()

        assert data_buns[2].get_name() == 'red bun' and data_buns[2].get_price() == 300

    # 3.1 проверка на получение результата по соусам
    def test_available_ingredients_sauce_success_return(self):
        data = Database()
        data_ingredients = data.available_ingredients()

        assert (
                data_ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE and
                data_ingredients[2].get_name() == 'chili sauce' and
                data_ingredients[2].get_price() == 300
        )

    # 3.2 проверка на получение результата по начинкам
    def test_available_ingredients_filling_success_return(self):
        data = Database()
        data_ingredients = data.available_ingredients()

        assert (
                data_ingredients[4].get_type() == INGREDIENT_TYPE_FILLING and
                data_ingredients[4].get_name() == 'dinosaur' and
                data_ingredients[4].get_price() == 200
        )
