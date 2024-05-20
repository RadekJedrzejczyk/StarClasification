from sklearn.neighbors import KNeighborsClassifier

def findBestNeighboursNumber(x_train,x_test,y_train,y_test,max_number_of_neighbours):
    solution_list =[]
    for n in range(1, max_number_of_neighbours):
        knn_lib=KNeighborsClassifier(n)
        knn_lib.fit(x_train,y_train.values.ravel())
        solution_list.append(knn_lib.score(x_test,y_test))
        print(f"{n}/{max_number_of_neighbours}")
    
    max_value = max(solution_list)
    max_index = solution_list.index(max_value)
    return max_index, solution_list