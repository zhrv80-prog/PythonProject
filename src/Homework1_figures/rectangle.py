from src.Homework1_figures.figure import Figure


class Rectangle(Figure):

    # Создаём прямоугольник со сторонами side_a и side_b
    def __init__(self, side_a: float, side_b: float, name='прямоугольник'):
        super().__init__(name)
        self.side_a = side_a
        self.side_b = side_b

        # Валидация на корректные значения сторон
        if self.side_a <= 0 or self.side_b <= 0:
            raise ValueError("Стороны прямоугольника должны быть больше нуля")

    # Вычисляем площадь прямоугольника
    @property
    def area(self) -> float:
        return self.side_a * self.side_b

    # Вычисляем периметр прямоугольника
    @property
    def perimeter(self) -> float:
        return (self.side_a + self.side_b) * 2
