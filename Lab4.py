class Vehicle:
    """
    Базовый класс, представляющий транспортное средство.
    """

    def __init__(self, make: str, model: str, year: int):
        """
        Конструктор для класса Vehicle.

        Параметры:
        - make (str): Марка транспортного средства.
        - model (str): Модель транспортного средства.
        - year (int): Год выпуска транспортного средства.
        """
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Строковое представление объекта Vehicle.

        Возвращает:
        str: Строка с деталями транспортного средства.
        """
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """
        Официальное строковое представление объекта Vehicle.

        Возвращает:
        str: Строка с деталями для отладки.
        """
        return f"Vehicle(make={self.make}, model={self.model}, year={self.year})"


class Car(Vehicle):
    """
    Класс, представляющий легковой автомобиль, наследующийся от класса Vehicle.
    """

    def __init__(self, make: str, model: str, year: int, num_doors: int):
        """
        Конструктор для класса Car.

        Параметры:
        - make (str): Марка автомобиля.
        - model (str): Модель автомобиля.
        - year (int): Год выпуска автомобиля.
        - num_doors (int): Количество дверей у автомобиля.
        """
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def start_engine(self) -> str:
        """
        Запуск двигателя автомобиля.

        Возвращает:
        str: Сообщение о том, что двигатель запущен.
        """
        return "Двигатель автомобиля запущен."

    def __str__(self) -> str:
        """
        Строковое представление объекта Car, переопределяя метод базового класса.

        Возвращает:
        str: Строка с деталями об автомобиле.
        """
        return f"{super().__str__()} с {self.num_doors} дверьми"

    def accelerate(self, speed: int) -> str:
        """
        Ускорение автомобиля до заданной скорости.

        Параметры:
        - speed (int): Скорость, до которой ускоряется автомобиль.

        Возвращает:
        str: Сообщение о ускорении.
        """
        return f"Автомобиль ускоряется до {speed} км/ч."

    def __repr__(self) -> str:
        """
        Официальное строковое представление объекта Car, переопределяя метод базового класса.

        Возвращает:
        str: Строка с деталями для отладки.
        """
        return f"Car(make={self.make}, model={self.model}, year={self.year}, num_doors={self.num_doors})"


if __name__ == "__main__":
    my_car = Car(make="Toyota", model="Camry", year=2022, num_doors=4)

    print(my_car)  # Вывод: 2022 Toyota Camry с 4 дверьми
    print(my_car.start_engine())  # Вывод: Двигатель автомобиля запущен.
    print(my_car.accelerate(60))  # Вывод: Автомобиль ускоряется до 60 км/ч.
