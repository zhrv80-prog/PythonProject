from src.Figures.figure import Figure


class Square(Figure):

    # Создаём квадрат со стороной side
    def __init__(self, side: float, name='квадрат'):
        self.side = side
        super().__init__(name)

        # Валидация на корректные значение стороны
        if self.side <= 0:
            raise ValueError("Сторона квадрата должна быть больше нуля")

    # Вычисляем площадь квадрата
    @property
    def area(self) -> float:
        return self.side ** 2

    # Вычисляем периметр квадрата
    @property
    def perimeter(self) -> float:
        return self.side * 4

