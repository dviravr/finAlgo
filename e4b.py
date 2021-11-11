from typing import List
from Agent import Agent


def is_a_envy_b(agent_a: Agent, agent_a_values: List[int], agent_b_values: List[int]) -> bool:
    agent_a_tot_value = sum(agent_a.item_value(x) for x in agent_a_values)
    agent_a_tot_value_for_b_items = sum(agent_a.item_value(x) for x in agent_b_values)
    return agent_a_tot_value_for_b_items > agent_a_tot_value


def is_ef1(agents: List[Agent], bundles: List[List[int]]) -> bool:
    n = len(agents)
    for i in range(n):
        for j in range(n):
            if i != j:
                if is_a_envy_b(agents[i], bundles[i], bundles[j]):
                    for k in range(len(bundles[j])):
                        temp_list = list(bundles[j])
                        del temp_list[k]
                        if not is_a_envy_b(agents[i], bundles[i], temp_list):
                            break
                        if k == len(bundles[j]) - 1:
                            print('Agent {} is envy in Agent {}'.format(agents[i], agents[j]))
                            return False
    print('there is EF1')
    return True
