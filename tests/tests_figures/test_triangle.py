from src.Figures.triangle import Triangle


class TestTriangle:

    # Проверяем, что стороны сохранились правильно и конструктор создаёт треугольник с заданными сторонами
    def test_triangle_validation(self):
        triangle = Triangle(10, 12, 15)
        assert triangle.side_a == 10
        assert triangle.side_b == 12
        assert triangle.side_c == 15

    # Проверяем, что правильно передалось имя треугольника
    def test_triangle_name(self):
        triangle = Triangle(10, 10, 10)
        assert triangle.name == "треугольник"

    # Проверяем, что нельзя создать треугольник со стороной меньше 0
    def test_triangle_side_a(self):
        try:
            triangle = Triangle(10, 10, -10)
            assert False, "Исключение не выброшено"
        except ValueError as e:
            assert  "Стороны треугольника должны быть больше нуля" in str(e)
