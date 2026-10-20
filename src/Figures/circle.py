import math

from src.Figures.figure import Figure


class Circle(Figure):

    def __init__(self, radius: float, name='круг'):
        super().__init__(name)
        self.radius = radius

        # Валидация на корректное значение радиуса
        if self.radius <= 0:
            raise ValueError("Радиус круга должн быть больше нуля")

    # Вычисляем площадь круга
    @property
    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    # Вычисляем периметр круга
    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

