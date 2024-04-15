def grader(y_predicted, y_real,print_grading =True):
    overall = len(y_real)
    correct = sum (y_predicted==y_real)

    accuracy =correct/overall
    if print_grading:
        print(f"Dokładność wyznaczenia wynosi {accuracy*100}% ")
    return accuracy