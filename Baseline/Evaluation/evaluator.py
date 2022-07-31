'''
Simple evaluator class for perceptron classification of ISEAR data.
'''
class Evaluator:
    '''
    This initializer sets precision, recall, and f_score dictionaries 
    to 0 for each of the seven emotions. The method builds a confusion 
    matrix for each label.
    -----------------------------------------------------------------
    Inputs: [LIST] list of predicted labels, [LIST] list of true labels.
    Outputs: None
    '''
    def __init__(self, predictions, true_labels):
        self.precision = dict(joy=0, fear=0, guilt=0, anger=0, disgust=0, sadness=0, shame=0)
        self.recall = dict(joy=0, fear=0, guilt=0, anger=0, disgust=0, sadness=0, shame=0)
        self.f_score = dict(joy=0, fear=0, guilt=0, anger=0, disgust=0, sadness=0, shame=0)
        self.conf_matrix = {'joy':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                           'fear':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                          'guilt':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                          'anger':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                        'disgust':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                        'sadness':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                          'shame':{'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0},
                          }
        
        labels = list(zip(predictions, true_labels))

        for label in labels:
            # If the prediction matches the truth we add 1 to true positives
            if label[0] == label[1]:
                self.conf_matrix[label[0]]['tp'] += 1
                # We add one to true negatives for each of the remaining labels
                for key in self.conf_matrix:
                    if key != label[0]:
                        self.conf_matrix[key]['tn'] += 1
            else:
                # If the prediction is incorrect, add 1 to false positive for wrong label
                self.conf_matrix[label[0]]['fp'] += 1
                # Add one to false negative to correct label
                self.conf_matrix[label[1]]['fn'] += 1

    '''
    This method calculates precision score for each emotion.
    -----------------------------------------------------------------
    Inputs: None
    Outputs: None
    '''
    def ret_precision(self):
        # For each emotion, find true positive and false negative
        for key in self.conf_matrix:
            tp = self.conf_matrix[key]['tp']
            fp = self.conf_matrix[key]['fp']
            # Use precision formula
            prec = tp/(tp + fp)
            # Update precision dictionary for emotion with precision score
            self.precision[key] = prec
    
    '''
    This method calculates the recall score for each emotion.
    -----------------------------------------------------------------
    Inputs: None
    Outputs: None
    '''
    def ret_recall(self):
        # For each emotion, find true positives and false negatives
        for key in self.conf_matrix:
            tp = self.conf_matrix[key]['tp']
            fn = self.conf_matrix[key]['fn']
            # Use recall formula
            rec = tp/(tp+fn)
            # Update recall dictionary for emotion with recall score
            self.recall[key] = rec

    '''
    This method calculates the F1 score for each emotion.
    -----------------------------------------------------------------
    Inputs: None
    Outputs: None
    '''
    def ret_fscore(self):
        # First, calculate precision and recall
        self.ret_precision()
        self.ret_recall()
        # For each emotion, set precision and recall
        for key in self.conf_matrix:
            p = self.precision[key]
            r = self.recall[key]
            # Use F1 Score formual
            f_score = (2 * p * r)/(p + r)
            # Update F1 score dictionary with calculated F1 score
            self.f_score[key] = f_score
    

    def accuracy(self):
        total_tp = 0
        total_tn = 0
        total_fp = 0
        total_fn = 0

        labels = list(set(self.conf_matrix.keys()))

        for label in labels:
            print(label)
            total_tp += self.conf_matrix[label]['tp']
            total_tn += self.conf_matrix[label]['tn']
            total_fp += self.conf_matrix[label]['fp']
            total_fn += self.conf_matrix[label]['fn']
        
        trues = total_tp + total_tn
        falses = total_fp + total_fn

        acc = trues/(trues + falses)

        return acc




