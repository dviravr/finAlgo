from typing import List

eps = 1 / 100


def highest_value(values: List[float]) -> List[bool]:
    max_value = max(values)
    return [x == max_value for x in values]


def hundred_and_higher(values: List[float]) -> List[bool]:
    return [x >= 100 for x in values]


def payments(values: List[float], choice_rule) -> List[float]:
    # return the payment for every player.

    """
    :param values: List[float]
    :param choice_rule: func
    :return List[float]

    >>> payments([8, 5, 13, 9, 20], highest_value)
    [0, 0, 0, 0, 13.0]

    >>> payments([80, 50, 130, 90, 200], hundred_and_higher)
    [0, 0, 100.0, 0, 100.0]

    >>> payments([147, 99, 100, 1000, 1], hundred_and_higher)
    [100.0, 0, 100.0, 100.0, 0]
    """

    players_payments = []
    choices = choice_rule(values)
    for i, choice in enumerate(choices):
        if choice:
            values_copy = values
            while choices[i]:
                values_copy[i] = round(values_copy[i] - eps, 2)
                choices = choice_rule(values_copy)
            values_copy[i] += eps
            players_payments.append(values_copy[i])
        else:
            players_payments.append(0)

    return players_payments


if __name__ == '__main__':
    import doctest

    doctest.testmod()