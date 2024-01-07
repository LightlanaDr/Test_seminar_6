class NumbersList:
    """Класс для проверки списков чисел"""

    def __init__(self, list_num: list[int]):
        self.list_num = list_num
        self.avg_num = 0

    def average_numbers(self) -> float:
        """Метод определения среднего значения"""
        try:
            sum_numbers = 0
            for number in self.list_num:
                sum_numbers += number
            self.avg_num = round(sum_numbers / len(self.list_num), 2)
            return self.avg_num
        except Exception:
            print("Список пуст")


def compare_values(num1: float, num2: float) -> str:
    """Метод для определения разности длины списков"""
    result = None
    if num1 == num2:
        result = "Средние значения равны"
    if num1 > num2:
        result = "Первый список имеет большее среднее значение"
    if num1 < num2:
        result = "Второй список имеет большее среднее значение"
    return result


if __name__ == '__main__':
    """Проверка кода"""
    list_num1 = NumbersList([1, 2, 4, 6])
    print(list_num1.average_numbers())

    list_num2 = NumbersList([5, 8, 9, 12])
    print(list_num2.average_numbers())

    print(compare_values(list_num1.avg_num, list_num2.avg_num))

    list_num3 = NumbersList([])
    list_num3.average_numbers()
