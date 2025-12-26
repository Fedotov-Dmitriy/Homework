def curry(func, arrity):
    if not callable(func):
        raise TypeError("Первый аргумент должен быть функцией")

    if not isinstance(arrity, int):
        raise TypeError("Арность должна быть целым числом")

    if arrity < 0:
        raise ValueError("Арность не может быть отрицательной")

    def currying(*args):
        if len(args) >= arrity:
            return func(*args[:arrity])
        else:

            def continu(*next_args):
                combinied_args = args + next_args
                return currying(*combinied_args)

            return continu

    return currying


def uncurry(curruied_func, arrity):
    if not callable(curruied_func):
        raise TypeError("Первый аргумент должен быть функцией")

    if not isinstance(arrity, int):
        raise TypeError("Арность должна быть целым числом")

    if arrity < 0:
        raise ValueError("Арность не может быть отрицательной")

    def uncurried(*args):
        current_res = curruied_func
        for arg in args:
            current_res = current_res(arg)
        return current_res

    return uncurried
