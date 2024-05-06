import pandas as pd
def generate_map(data_column):
    uniques = pd.unique(data_column)
    binary_map = {}
    for number, value in enumerate(uniques):
        binary_map[value] = number
    return binary_map
