from praktikum.bun import Bun


class TestBun:
    # 1.0 проверка на корректное отображение наименования
    def test_get_name_correct_name_success(self):
        bun = Bun('Булочка бриошь', 129)

        assert bun.get_name() == 'Булочка бриошь'

    # 1.1 проверка на корректное отображение цены
    def test_get_price_correct_price_success(self):
        bun = Bun('Булочка бриошь', 129)

        assert bun.get_price() == 129
        