import pytest
from program_hw import NumbersList, compare_values


def test_average_numbers():
    list_test = NumbersList([3, 4, 5])
    assert list_test.average_numbers() == 4, "Среднее значение равно 3"

def test_average_numbers_empty_list():
    list_test = NumbersList([])
    assert Exception, "Список пуст"


def test_compare_values():
    assert compare_values(3, 3) == "Средние значения равны"
    assert compare_values(4, 3) == "Первый список имеет большее среднее значение"
    assert compare_values(3, 7) == "Второй список имеет большее среднее значение"


if __name__ == '__main__':
    pytest.main(['-v'])
