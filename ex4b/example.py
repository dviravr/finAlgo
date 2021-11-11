from e4b import *

if __name__ == '__main__':
    a = Agent('a')
    b = Agent('b')
    c = Agent('c')
    a.set_values({1: 45, 2: 32, 3: 20, 4: 51, 5: 10, 6: 15, 7: 10, 8: 14, 9: 17})
    b.set_values({1: 50, 2: 25, 3: 25, 4: 60, 5: 23, 6: 34, 7: 10, 8: 14, 9: 17})
    c.set_values({1: 30, 2: 40, 3: 45, 4: 60, 5: 20, 6: 20, 7: 30, 8: 20, 9: 26})

    agents = [a, b]
    print('example #1')
    bundles = [[1, 2, 3],
               [4, 5, 6]]
    print('agent', a, 'got 97 and could not get more')
    print('agent', b, 'got 117 and could not get more')
    is_ef1(agents, bundles)
    print()

    print('example #2')
    bundles = [[4, 5, 6],
               [1, 2, 3]]
    print('agent', a, 'got 76 but could get 97, but still do not envy')
    print('agent', b, 'got 100 but could get 117, but still do not envy')
    is_ef1(agents, bundles)
    print()

    agents = [a, b, c]
    print('example #3')
    bundles = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    print('agent', a, 'got 97 and could not get more')
    print('agent', b, 'got 117 and could not get more')
    print('agent', c, 'got 76 but could get 115, but still do not envy')
    is_ef1(agents, bundles)
    print()

    print('example #4')
    bundles = [[2, 3, 4],
               [1, 5, 6],
               [7, 8, 9]]
    print('agent', a, 'got 103 and could not get more')
    print('agent', b, 'got 107 but could get 110, but steel do not envy')
    print('agent', c, 'got 76 but could get 155, and there is no item that can be remove so that he will not envy')
    is_ef1(agents, bundles)
