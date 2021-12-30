from typing import List
import networkx as nx
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def find_trading_cycle(preference: List[List[int]]) -> List[int]:
    cycle_list: List[int] = []
    e: List[tuple] = []
    for i, p in enumerate(preference):
        j = 0
        while j < len(p) and p[j] == -1:
            j += 1
        if j < len(p):
            e.append((i, p[j]))
            e.append((i, i))
    G = nx.DiGraph(e)
    cycle = nx.find_cycle(G)
    for c in cycle:
        cycle_list.append(c[0])
    cycle_list.append(cycle[-1][1])

    black_edges = [edge for edge in G.edges() if edge not in cycle]
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=cycle, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
    if logging.getLogger(__name__).level == logging.DEBUG:
        plt.show()
    return cycle_list


def trading_cycle_algorithm(preference: List[List[int]]) -> List[List[int]]:
    # return list of trading cycles.

    """
    :param preference: List[List[int]],
    :return List[List[int]]

    >>> trading_cycle_algorithm([[2, 1, 0, 3], [3, 2, 1, 0], [0, 1, 3, 2], [3, 0, 1, 2]])
    [[0, 2, 0], [1, 1], [3, 3]]

    >>> trading_cycle_algorithm([[1, 2, 0], [2, 0, 1], [0, 1, 2]])
    [[0, 1, 2, 0]]

    >>> trading_cycle_algorithm([[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [3, 0, 1, 2]])
    [[0, 0], [3, 3], [2, 2], [1, 1]]

    >>> trading_cycle_algorithm([[3, 0, 1, 2], [0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1]])
    [[0, 3, 2, 1, 0]]

    >>> trading_cycle_algorithm([[0, 3, 1, 2], [0, 3, 2, 1], [0, 1, 2, 3], [0, 1, 3, 2]])
    [[0, 0], [1, 3, 1], [2, 2]]
    """

    trading_list: List[List[int]] = []
    happy_players = set()
    pref_copy = preference.copy()
    while len(happy_players) != len(preference):
        new_cycle = find_trading_cycle(pref_copy)
        trading_list.append(new_cycle)
        for c in new_cycle:
            pref_copy[c] = [-1 for x in pref_copy[c]]
            for p in pref_copy:
                p[c] = -1
            happy_players.add(c)
        logger.debug(happy_players)
    logger.info(trading_list)
    return trading_list


if __name__ == '__main__':
    import doctest

    doctest.testmod()