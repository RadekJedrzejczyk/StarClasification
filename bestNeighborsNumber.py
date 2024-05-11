from knn import knn
from grader import grader

def findBestNeighboursNumber(x_train, x_test, y_train, y_test,max_number_of_neighbours,label_searched):
    solution_list =[]
    knn_lib=knn(1)

    for n in range(1, max_number_of_neighbours):
        knn_lib.neighbours_number=n
        knn_lib.fit(x_train,y_train,label_searched)
        y_predicted = knn_lib.predict(x_test)
        solution_list.append(grader(y_predicted,y_test,False))
        print(f"{n}/{max_number_of_neighbours}")
    
    max_value = max(solution_list)
    max_index = solution_list.index(max_value)
    return max_index, solution_list