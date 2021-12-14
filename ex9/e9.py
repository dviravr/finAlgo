import random
import numpy as np
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def get_marginal_cost(players_order: list, payments: dict):
    payments_by_order = {}
    for i in range(len(players_order)):
        this_group = ''.join(sorted(players_order[0:i + 1]))
        prev_group = ''.join(sorted(players_order[0:i]))
        if prev_group == '':
            payments_by_order[players_order[i]] = payments.get(this_group)
        else:
            payments_by_order[players_order[i]] = payments.get(this_group) - payments.get(prev_group)
    return payments_by_order


def random_shapley(players: list, payments: dict):
    num_of_iter = 10000
    total_payments = {}
    for p in players:
        total_payments[p] = 0
    for i in range(num_of_iter):
        random_order = list(np.random.permutation(players))
        temp_payments = get_marginal_cost(random_order, payments)
        logger.debug(str(('for order', random_order, 'the payment is:', temp_payments)))
        for p in players:
            total_payments[p] = total_payments[p] + temp_payments[p]
    for p in players:
        total_payments[p] = total_payments[p] / num_of_iter
        logger.info('the final payment for player {} is {}'.format(p, total_payments[p]))
    return total_payments


def check_3_players():
    group_payments = {'a': 10, 'b': 15, 'c': 25, 'ab': 20, 'ac': 25, 'bc': 30, 'abc': 37}
    players_list = ['a', 'b', 'c']
    tot_payments = random_shapley(players_list, group_payments)
    real_total_payments = {'a': 6.5, 'b': 11.5, 'c': 19}
    for p in players_list:
        logger.info('the diff of player {} from the real payment is {}'.format(p, abs(
            real_total_payments[p] - tot_payments[p])))


# def get_real_air_plains_payments(air_plains_list: list, air_plains_dict: dict):
#     real_payments = {}
#     for a in air_plains_list:
#         real_payments[a] = 0
#     lengths_set = sorted(set(air_plains_dict.values()))
#     num_of_plains_for_length = {}
#     for l in lengths_set:
#         counter = 0
#         for i in air_plains_dict.values():
#             if i >= l:
#                 counter += 1
#         num_of_plains_for_length[l] = counter
#     payment_for_km = 10
#
#     print(lengths_set)
#     for i in range(1, len(lengths_set)):
#         print(lengths_set[i])
#     print(num_of_plains_for_length)
#     print(real_payments)
#     return 'a'


# def check_30_players():
#     lengths_list = np.arange(1, 9)
#     num_of_air_plains = 5
#     air_plains_dict = {}
#     for i in range(num_of_air_plains):
#         air_plains_dict[i] = random.choice(lengths_list)
#     air_plains_list = list(air_plains_dict.keys())
#     tot_payments_for_air_plains = random_shapley(air_plains_list, air_plains_dict)
#     real_payments_for_air_plains = get_real_air_plains_payments(air_plains_list, air_plains_dict)
#     print(tot_payments_for_air_plains)


if __name__ == '__main__':
    logger.info('check for 3 players')
    check_3_players()

    # part 3 don't work

    # logger.info('check for 30 players')
    # check_30_players()
