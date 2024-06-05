from praktikum.burger import Burger


class TestBurger:
    # 2.0 проверка на создание булочки
    def test_set_buns_correct_creation(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    # 2.1 проверка на добавление 1 ингридиента
    def test_add_ingredient_one_ingredient_correct_add(self, mock_ingredient_sauce1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce1)

        assert mock_ingredient_sauce1 in burger.ingredients

    # 2.2 проверка на удаление ингридиента
    def test_remove_ingredient_correct_index_success_remove(self, burger):
        ingredient1 = burger.ingredients[0]
        ingredient2 = burger.ingredients[1]

        burger.remove_ingredient(0)

        assert ingredient2 in burger.ingredients and ingredient1 not in burger.ingredients

    # 2.3 проверка на изменение индекса ингридиентов
    def test_move_ingredient_success_move(self, burger):
        ingredient1 = burger.ingredients[0]
        ingredient2 = burger.ingredients[1]

        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == ingredient2 and burger.ingredients[1] == ingredient1

    # 2.4 проверка на вывод конечной цены
    def test_get_price_success(self, mock_bun, mock_ingredient_sauce2, mock_ingredient_filling1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce2)
        burger.add_ingredient(mock_ingredient_filling1)
        burger.set_buns(mock_bun)

        mock_bun.get_price.return_value = 129
        mock_ingredient_sauce2.get_price.return_value = 29
        mock_ingredient_filling1.get_price.return_value = 69

        assert burger.get_price() == 356

    # 2.5 проверка на составление рецепта
    def test_get_receipt_success(self, mock_bun, mock_ingredient_sauce1, mock_ingredient_filling2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce1)
        burger.add_ingredient(mock_ingredient_filling2)
        burger.set_buns(mock_bun)

        mock_bun.get_name.return_value = 'Крафтовая булочка'
        mock_bun.get_price.return_value = 129

        mock_ingredient_sauce1.get_type.return_value = 'соус'
        mock_ingredient_filling2.get_type.return_value = 'начинка'
        mock_ingredient_sauce1.get_name.return_value = 'Сырный соус'
        mock_ingredient_filling2.get_name.return_value = 'Креветка'
        mock_ingredient_sauce1.get_price.return_value = 39
        mock_ingredient_filling2.get_price.return_value = 149

        receipt = [
            '(==== Крафтовая булочка ====)',
            '= соус Сырный соус =',
            '= начинка Креветка =',
            '(==== Крафтовая булочка ====)\n',
            'Price: 446'
        ]

        assert '\n'.join(receipt) == burger.get_receipt()