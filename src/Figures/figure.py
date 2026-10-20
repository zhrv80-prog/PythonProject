from abc import abstractmethod


class Figure:
    def __init__(self, name: str):
        self.name = name

    @property
    def area(self):
        pass

    @property
    def perimeter(self):
        pass


    def add_area(self, other_figure):
        # self.area — это площадь текущей фигуры
        # other_figure.area — это площадь переданной фигуры
        if not isinstance(other_figure, Figure):
            raise ValueError("Объект не является фигурой")
        return self.area + other_figure.area
