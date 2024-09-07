"""
Random Function Utility

This module consists of the Random function utilities
"""

import random


def random_utility(func_type, params={}):
    """Random Functions Wrapper for Dataset Generation Scripts"""
    random_func_dict = {
        "choice": random.choice,
        "uniform": random.uniform,
        "randint": random.randint,
    }
    return random_func_dict[func_type](**params)


def weighted_random(priority_value, secondary_value, weight=0.8):
    """This function returns one of two values with a weighted probability."""
    random_value = random_utility("uniform", {"a": 0, "b": 1})
    if random_value < weight:
        return priority_value
    else:
        return secondary_value
