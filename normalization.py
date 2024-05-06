def _normalization_min_max(minimum, maximum, data_column):
    column =[]
    if maximum == minimum:
        return [0.5] * len(data_column)
        print("WARNING: minimum equals maximum during normalisation")
    for element in data_column:
        new_element = (element - minimum)/(maximum - minimum)
        column.append(new_element)
    return column

def _transpose(data): 
    rows_number=len(data)
    columns_number = len(data[0])
    transposed_data =  [[0]*rows_number for _ in range(columns_number)]
    for i in range(rows_number):
       for j in range(columns_number):
           transposed_data[j][i] = data[i][j]
    return transposed_data

def min_max(data_set, titles,local=True):
    new_table =[]
    data_set=_transpose(data_set)
    if local:
        for column in data_set:
            maximum = max(column)
            minimum = min(column)
            new_column = _normalization_min_max(minimum, maximum, column)
            new_table.append(new_column)
    else:
        maximum= max(max(column) for column in data_set)
        minimum =min(min(column) for column in data_set)
        for column in data_set:
            new_column = _normalization_min_max(minimum, maximum, column)
            new_table.append(new_column)
    return_dictionary = {title: column for title, column in zip(titles, new_table)}
    return return_dictionary 