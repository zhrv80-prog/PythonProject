from src.Homework1_figures.circle import Circle
from src.Homework1_figures.rectangle import Rectangle
from src.Homework1_figures.square import Square
from src.Homework1_figures.triangle import Triangle


def main():
    square = Square(50)
    print(f"1. {square.name}")
    print(f"Площадь {square.name}а {square.area}")
    print(f"Периметер {square.name}а {square.perimeter}\n")

    rectangle = Rectangle(10, 20)
    print(f"2. {rectangle.name}")
    print(f"Площадь {rectangle.name}а {rectangle.area}")
    print(f"Периметр {rectangle.name}а {rectangle.perimeter}\n")

    circle = Circle(58)
    print(f"3. {circle.name}")
    print(f"Площадь {circle.name}а {circle.area}")
    print(f"Периметр {circle.name}а {circle.perimeter}\n")

    triangle = Triangle(10, 10, 10)
    print(f"4. {triangle.name}")
    print(f"Площадь {triangle.name}а {triangle.area}")
    print(f"Периметр {triangle.name}а {triangle.perimeter}\n")

    print(square.add_area(Triangle(10, 10, 10)))
    print(circle.add_area(Rectangle(10, 10)))


if __name__ == "__main__":
    main()
