from typing import List


def is_budget_fair_to_groups(total_budget: float, citizen_votes: List[List],
                             final_budget_division: List[float]) -> bool:
    # return true the budget is fair for groups.

    """
    :param total_budget: float,
    :param citizen_votes: List[List],
    :param final_budget_division: List[float]
    :return bool

    >>> is_budget_fair_to_groups(1000, [[1000, 0, 0], [0, 0, 1000],
    ...                                [0, 1000, 0], [0, 1000, 0],
    ...                                [1000, 0, 0], [0, 1000, 0],
    ...                                [1000, 0, 0], [0, 0, 1000],
    ...                                [1000, 0, 0], [0, 0, 1000]],
    ...                             [400, 300, 300])
    True

    >>> is_budget_fair_to_groups(1000, [[0, 1000, 0], [0, 0, 1000],
    ...                                [0, 1000, 0], [0, 1000, 0],
    ...                                [1000, 0, 0], [0, 1000, 0],
    ...                                [1000, 0, 0], [0, 0, 1000],
    ...                                [1000, 0, 0], [0, 0, 1000]],
    ...                             [400, 300, 300])
    False
    """
    count_list = [0] * len(citizen_votes[0])
    for citizen in citizen_votes:
        for index, vote in enumerate(citizen):
            count_list[index] += vote / len(citizen_votes)
    return count_list == final_budget_division


if __name__ == '__main__':
    import doctest

    doctest.testmod()
