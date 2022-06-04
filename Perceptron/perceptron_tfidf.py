import random
import tfidf

# Class definition for perceptron contains methods init, train, and predict
class Perceptron:
    def __init__(self, X_train, y_train, epoch):
        self.X_train = X_train
        self.y_train = y_train
        self.epoch = epoch
        # These will be updated below
        self.weight_vecs = None
        self.labels = None

        #TF_IDF
        tf_idf_model = tfidf.Tfidf(self.X_train, Y=self.y_train, train=True)
        tf_idf_model.tf_idf()
        self.feature_vecs = tf_idf_model.tf_idf_d
        # Get unique labels
        self.labels = list(set(y_train))

        # Create weight vectors length of vocabulary for each label. This is a 2D dictionary where:
        # Keys are labels and values are dictionaries containing a weight (initialized to value between 0-1) for each feature (word) in our vocabulary.
        self.weight_vecs = {key: dict() for key in self.labels}
        for key in self.weight_vecs:
            for i in tf_idf_model.unique_tokens:
                self.weight_vecs[key][i] = random.randint(0,1)
  
    def train(self):
        # We iterate over the model for the specified number of epochs
        for i in range(self.epoch):
            for sent in self.feature_vecs:
                # Initialize a dictionary to hold each dot product calculation
                emotion_scores = dict(joy=0, fear=0, guilt=0, anger=0, disgust=0, sadness=0, shame=0)
                # Calculate the dot product
                for label in self.labels:
                    dot_product = 0
                    for feature in self.feature_vecs[sent]:
                        if feature != 'LABEL':
                            dot_product += self.feature_vecs[sent][feature] * self.weight_vecs[label][feature]
                    
                    emotion_scores[label] = dot_product

                # Find the argmax
                argmax = max(emotion_scores, key=emotion_scores.get)
                correct_label = self.feature_vecs[sent]['LABEL']
                
                # Reward/Penalty update step
                if argmax != correct_label:
                    for feature in self.feature_vecs[sent]:
                        if feature != 'LABEL':
                            self.weight_vecs[correct_label][feature] += self.feature_vecs[sent][feature]
                            self.weight_vecs[argmax][feature] -= self.feature_vecs[sent][feature]
                         

    # Returns list of predicted labels given X_test parameter
    def predict(self, X_test):
        test_model = tfidf.Tfidf(X_test)
        test_model.tf_idf()
        train_vecs = test_model.tf_idf_d

        predictions = []
        for sent in train_vecs:
            emotion_scores = dict(joy=0, fear=0, guilt=0, anger=0, disgust=0, sadness=0, shame=0)
            for label in self.labels:
                dot_product = 0
                for feature in train_vecs[sent]:
                    if feature in self.weight_vecs[label]:
                        dot_product += train_vecs[sent][feature] * self.weight_vecs[label][feature]
                emotion_scores[label] = dot_product
            argmax = max(emotion_scores, key=emotion_scores.get)
            predictions.append(argmax)
        
        return predictions