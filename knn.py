from numpy import linalg,argsort
from pandas import DataFrame

class knn:
    def __init__(self,neighbours_number):
        self.neighbours_number=neighbours_number;

    def fit(self,x_train,y_train,label_searched):
        self.x_train=x_train
        self.y_train=y_train
        self.label_searched=label_searched
        
    def predict(self, x_test):
        prediction=[]
        length = len(x_test.values)
        original_indexes = x_test.index
        for tested in x_test.values:
            distances = [linalg.norm(tested - potential_neighbour) for potential_neighbour in self.x_train.values] 
            closest_indexes = argsort(distances)[:self.neighbours_number] 
            labels = [self.y_train[self.label_searched].iloc[neighbour_index] for neighbour_index in closest_indexes] 
            result = max(set(labels),key=labels.count) 
            prediction.append(result)
        prediction = DataFrame(prediction,columns=[self.label_searched],index=original_indexes)
        return prediction



