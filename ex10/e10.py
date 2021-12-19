from typing import List
import cvxpy
import functools


def condition_otelitry_budget(total: float, subject: List[str], pref: List[List[str]]):
    allocations = cvxpy.Variable(len(subject))
    utilities = []
    for player in pref:
        utility = 0
        for p in player:
            utility += allocations[subject.index(p)]
        utilities.append(utility)
    donations = []
    for i in range(len(pref)):
        donations.append(total / len(pref))
    sum_of_logs = cvxpy.sum([cvxpy.log(u) for u in utilities])
    positivity_constraints = [v >= 0 for v in allocations]
    sum_constraint = [cvxpy.sum(allocations) == sum(donations)]
    problem = cvxpy.Problem(
        cvxpy.Maximize(sum_of_logs),
        constraints=positivity_constraints + sum_constraint)
    problem.solve()
    utility_values = [u.value for u in utilities]
    print("BUDGET: a={}, b={}, c={}, d={}".format(*allocations.value))
    print("UTILS : {}, {}, {}, {}, {}".format(*utility_values))
    utility_product = functools.reduce(lambda a, b: a * b, utility_values)
    print("PRODUCT: {}".format(utility_product))

    for i in range(len(pref)):
        for j in range(len(subject)):
            if subject[j] in pref[i]:
                print("Citizen {} gives {} to {}".format(i, allocations[j].value * donations[i] / utilities[i].value, subject[j])),


if __name__ == '__main__':
    tot = 500
    sub = ['a', 'b', 'c', 'd']
    util = [['b', 'd'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['a']]
    condition_otelitry_budget(tot, sub, util)
