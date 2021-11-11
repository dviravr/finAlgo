import random


class Agent:

    def __init__(self, name: str):
        self.values_dict = {}
        self.name = name

    def set_values(self, value_dict: dict):
        self.values_dict = value_dict

    def item_value(self, item_index: int) -> float:
        if self.values_dict.get(item_index) is None:
            self.values_dict[item_index] = round(random.uniform(1, 100), 2)
        return self.values_dict.get(item_index)

    def __str__(self):
        return self.name
