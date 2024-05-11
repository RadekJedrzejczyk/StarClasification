def grader(y_predicted, y_real,print_grading =True):

    y_predicted_sorted = y_predicted.sort_index()
    y_real_sorted = y_real.sort_index()
    
    overall = len(y_real)
    correct = sum(y_predicted_sorted.values==y_real_sorted.values)
    
    accuracy = correct/overall
    if print_grading:
        print(f"Dokładność wyznaczenia wynosi {accuracy*100}% ")
    return accuracy