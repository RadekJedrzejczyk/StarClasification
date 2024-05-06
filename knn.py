from numpy import linalg,argsort

class knn:
    def __init__(self,neighbours_number):
        self.neighbours_number=neighbours_number;

    def fit(self,x_train,y_train,new_neighbours_number=None):
        self.x_train=x_train
        self.y_train=y_train
        if new_neighbours_number:
            self.neighbours_number=new_neighbours_number
        
    def predict(self, x_test):
        prediction=[]
       # i=0
        length = len(x_test.values)
        for tested in x_test.values:
            distances = [linalg.norm(tested - potential_neighbour) for potential_neighbour in self.x_train.values] #odległość tested od każdego innego
            closest_indexes = argsort(distances)[:self.neighbours_number] #wyznacza sąsiadów (określoną ilość)
            labels = [self.y_train['class'].iloc[neighbour_index] for neighbour_index in closest_indexes] 
            result = max(set(labels),key=labels.count) 
            prediction.append(result)
         #   print(f"{i} / {length}", end='\t', flush=True)
         #   i+=1
        return prediction


"""
def predict(self, x_test):
        prediction=[]
        for tested in x_test.values:
            distances = [linalg.norm(tested - potential_neighbour) for potential_neighbour in self.x_train.values] #odległość tested od każdego innego
            closest = argsort(distances)[:self.neighbours_number] #wyznacza sąsiadów (określoną ilość)
            labels = [self.y_train.iloc[element] for element in closest] 
            result = max(set(labels),key=labels.count) 
            prediction.append(result)
        return prediction
"""

