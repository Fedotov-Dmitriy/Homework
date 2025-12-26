import pytest


from curry import curry, uncurry


# Тестовые функции
def add_two(a, b):
    return a + b


def multiply_three(a, b, c):
    return a * b * c


def test_curry_basic():
    # Базовый тест каррирования
    curried_add = curry(add_two, 2)
    assert curried_add(5)(3) == 8

    curried_mult = curry(multiply_three, 3)
    assert curried_mult(2)(3)(4) == 24


def test_curry_multiple_args():
    # Тест передачи нескольких аргументов за раз
    curried_add = curry(add_two, 2)
    assert curried_add(5, 3) == 8

    curried_mult = curry(multiply_three, 3)
    assert curried_mult(2, 3, 4) == 24
    assert curried_mult(2, 3)(4) == 24
    assert curried_mult(2)(3, 4) == 24


def test_curry_partial_application():
    # Тест частичного применения
    curried_mult = curry(multiply_three, 3)

    multiply_by_2 = curried_mult(2)
    multiply_by_2_and_3 = multiply_by_2(3)

    assert multiply_by_2_and_3(4) == 24
    assert multiply_by_2(3)(4) == 24


def test_curry_extra_args():
    # Тест игнорирования лишних аргументов
    curried_add = curry(add_two, 2)
    assert curried_add(5, 3, 10, 20) == 8


def test_uncurry_basic():
    # Базовый тест uncurry
    curried_add = curry(add_two, 2)
    uncurried_add = uncurry(curried_add, 2)
    assert uncurried_add(5, 3) == 8

    curried_mult = curry(multiply_three, 3)
    uncurried_mult = uncurry(curried_mult, 3)
    assert uncurried_mult(2, 3, 4) == 24


def test_uncurry_errors():
    # Тест обработки ошибок uncurry
    with pytest.raises(TypeError, match="Первый аргумент должен быть функцией"):
        uncurry("not a function", 2)

    with pytest.raises(TypeError, match="Арность должна быть целым числом"):
        uncurry(add_two, "2")

    with pytest.raises(ValueError, match="Арность не может быть отрицательной"):
        uncurry(add_two, -1)


def test_curry_uncurry_round_trip():
    # Тест полного цикла каррирование в uncurry
    original_result = multiply_three(2, 3, 4)

    curried_mult = curry(multiply_three, 3)
    curried_result = curried_mult(2)(3)(4)

    uncurried_mult = uncurry(curried_mult, 3)
    uncurried_result = uncurried_mult(2, 3, 4)

    assert original_result == curried_result == uncurried_result == 24


def test_round_trip_with_partial():
    # Тест цикла с частичным применением
    curried_mult = curry(multiply_three, 3)

    multiply_by_2_and_3 = curried_mult(2)(3)

    uncurried_partial = uncurry(multiply_by_2_and_3, 1)
    result = uncurried_partial(4)

    assert result == 24
