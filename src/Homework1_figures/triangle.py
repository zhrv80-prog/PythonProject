import math

from src.Homework1_figures.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: float, side_b: float, side_c: float, name='треугольник'):
        super().__init__(name)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        # Валидация на корректные значения сторон
        if self.side_a <= 0 or self.side_b <= 0 or self.side_c <= 0:
            raise ValueError("Стороны треугольника должны быть больше нуля")

        """
        # Проверка неравенства треугольника
        if (side_a + side_b <= side_c or
                side_a + side_c <= side_b or
                side_b + side_c <= side_a):
            raise ValueError(f"Треугольник со сторонами {side_a}, {side_b}, {side_c} не существует")
        """
        
    # Вычисляем периметр треугольника
    @property
    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c

    # Вычисляем периметр треугольника
    @property
    def area(self) -> float:
        p = self.perimeter / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))


