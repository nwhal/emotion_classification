import random
import data_utils as du

# Class definition for perceptron contains methods init, fit, and predict

class Perceptron:
    def __init__(self, X_train, y_train, epoch):
        self.X_train = X_train
        self.y_train = y_train
        self.epoch = epoch
        # These will be updated below
        self.features = None
        self.weight_vecs = None
        self.labels = None

        # Create dictionary where features are keys and values are indices
        self.features = du.build_vocab(X_train)
        
 
        # Get unique labels
        self.labels = list(set(y_train))

        # Create weight vectors length of vocabulary for each label. This is a 2D dictionary where:
        # Keys are labels and values are dictionaries containing a weight (initialized to value between 0-1) for each feature (word) in our vocabulary.
        self.weight_vecs = {key: dict() for key in self.labels}
        for key in self.weight_vecs:
            for i in self.features.keys():
                self.weight_vecs[key][i] = random.random()
    
  
    def fit(self):
        # We iterate over the model for the specified number of epochs
        for i in range(self.epoch):
            '''We take the argmax of the dot product of our weights + feature vectors. Since we have 1 for word occurance and 0 for 
            non-occurance, we will simply take the sum of weights'''
            for j in range(len(self.X_train)):
                emotion_scores = dict(joy=0, fear=0, guilt=0, anger=0, disgust=0, sadness=0, shame=0)
                text = self.X_train[j].split()
                for label in self.labels:
                    dot_product = 0
                    for word in text:
                        dot_product += self.weight_vecs[label][word]
                    emotion_scores[label] = dot_product
                
                predicted_label = max(emotion_scores, key=emotion_scores.get)
                true_label = self.y_train[j]
                if predicted_label != true_label:
                    for word in text:
                        self.weight_vecs[predicted_label][word] -= 1
                        self.weight_vecs[true_label][word] += 1
    
    # Returns list of predicted labels given X_test parameter
    def predict(self, X_test):
        y_predict = []
        for i in range(len(X_test)):
            emotion_scores = dict(joy=0, fear=0, guilt=0, anger=0, disgust=0, sadness=0, shame=0)
            text = X_test[i].split()
            for label in self.labels:
                dot_product = 0
                for word in text:
                    if word in self.features.keys():
                        dot_product += self.weight_vecs[label][word]
                emotion_scores[label] = dot_product
            
            predicted_label = max(emotion_scores, key=emotion_scores.get)      
            y_predict.append(predicted_label)
            
        return y_predict




        