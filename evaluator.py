import random
class Evaluator:
    def __init__(self) -> None:
        self.precision = dict()
        self.recall = dict()
        self.f_score = dict()
        self.conf_matrix = {'joy':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                           'fear':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                          'guilt':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                          'anger':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                        'disgust':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                        'sadness':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                          'shame':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                          }
        
        for key in self.conf_matrix:
            for sub_key in self.conf_matrix[key]:
                self.conf_matrix[key][sub_key] = random.randint(1, 15)
    
    def get_precision(self):
        for key in self.conf_matrix:
            tp = self.conf_matrix[key]['tp']
            fp = self.conf_matrix[key]['fp']
            self.precision[key] = tp/(tp + fp)
    
    def get_recall(self):
        for key in self.conf_matrix:
            tp = self.conf_matrix[key]['tp']
            fn = self.conf_matrix[key]['fn']
            self.recall[key] = tp/(tp+fn)
    
    def get_fscore(self):
        self.get_precision()
        self.get_recall()
        for key in self.conf_matrix:
            p = self.precision[key]
            r = self.recall[key]
            self.f_score[key] = (2 * p * r)/(p + r)



#Testing:
x = Evaluator()
print(x.conf_matrix)
x.get_fscore()
print(x.precision)
print(x.recall)
print(x.f_score)