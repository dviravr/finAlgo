import networkx as nx


def vcg_cheapest_path(graph, source, target):
    """
    :param target: Node
    :param source: Node
    :param graph: Graph
    :return total_payment

    # >>> g = nx.Graph()
    # >>> g.add_nodes_from(['A', 'B', 'C', 'D'])
    # >>> g.add_edge('A', 'B', weight=3)
    # >>> g.add_edge('A', 'C', weight=5)
    # >>> g.add_edge('A', 'D', weight=10)
    # >>> g.add_edge('B', 'C', weight=1)
    # >>> g.add_edge('B', 'D', weight=4)
    # >>> g.add_edge('C', 'D', weight=1)
    # >>> vcg_cheapest_path(g, 'A', 'D')
    # cheapest payment: 5
    # without ('A', 'B') the path is ['A', 'C', 'D'] the amount is: 6 for payment: 4
    # without ('B', 'C') the path is ['A', 'C', 'D'] the amount is: 6 for payment: 2
    # without ('C', 'D') the path is ['A', 'B', 'D'] the amount is: 7 for payment: 3
    # total_payment: 9
    #
    # >>> g = nx.Graph()
    # >>> g.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
    # >>> g.add_edge('A', 'B', weight=1)
    # >>> g.add_edge('A', 'C', weight=1)
    # >>> g.add_edge('A', 'D', weight=1)
    # >>> g.add_edge('A', 'E', weight=1)
    # >>> g.add_edge('B', 'C', weight=1)
    # >>> g.add_edge('B', 'D', weight=1)
    # >>> g.add_edge('B', 'E', weight=1)
    # >>> g.add_edge('C', 'D', weight=1)
    # >>> g.add_edge('C', 'E', weight=1)
    # >>> g.add_edge('D', 'E', weight=1)
    # >>> vcg_cheapest_path(g, 'A', 'E')
    # cheapest payment: 1
    # without ('A', 'E') the path is ['A', 'B', 'E'] the amount is: 2 for payment: 2
    # total_payment: 2
    """

    length, shortest_path = nx.single_source_dijkstra(graph, source, target)
    path_tuple = []
    for i in range(len(shortest_path) - 1):
        path_tuple.append((shortest_path[i], shortest_path[i + 1]))
    print('cheapest payment:', length)
    total_payment = 0
    for u, v, a in graph.edges(data=True):
        if (u, v) in path_tuple:
            g_copy = nx.Graph(graph)
            g_copy.remove_edge(u, v)
            new_length, new_shortest_path = nx.single_source_dijkstra(g_copy, source, target)
            for_payment = new_length - (length - a['weight'])
            total_payment += for_payment
            print('without', (u, v), 'the path is', new_shortest_path, 'the amount is:', new_length, 'for payment:',
                  for_payment)
    print('total_payment:', total_payment)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
