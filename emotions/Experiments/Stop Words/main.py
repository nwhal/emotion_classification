from data_operations import DataOperations
from perceptron import Perceptron
from evaluation import Evaluation


class OpeartingPerceptron(DataOperations, Evaluation):

    def __init__(self, training_file_name, training_data, test_file_name, test_data):
        super().__init__()  # to avoid calling each func with a dot, made the class parent of this class, now self.func_name is enough
        self.training_file_name = training_file_name
        self.training_data = training_data
        self.test_file_name = test_file_name
        self.test_data = test_data

        # self.eval = Evaluation()  # Another way of using functions from another class, object of Evaluation, call all functions of Ecaluation as self.eval.func_name

    def main(self):
        real_train_label = self.labels_and_data(self.training_data, self.training_file_name)
        real_test_label = self.labels_and_data(self.test_data,self.test_file_name)  # to get clean data
        emotions = sorted(list(set(real_test_label)))  # sorting to make it easy to assign final label by matching index of max with the emotion in emotions list
        dict = self.dictionary(self.training_data)
        train_features = self.features_vector(self.training_data, dict)
        test_vectors = self.features_vector(self.test_data, dict)
        size = len(train_features)
        epochs = 5

        predicted_labels = []  # to store values of each perceptron on test data to take argmax later

        for emotion in emotions:
            weight = self.weight_vector(dict)
            a = Perceptron(weight, size, train_features, real_train_label, real_test_label, epochs=epochs,emotion=emotion)
            a.train()

            predictions_on_test = a.predict(test_vectors)
            predicted_labels.append(predictions_on_test)  # first element corresponds to results of 1st emotion perceptron (sorted emotions)

            tp, fp, fn, tn = self.confusion_matrix(predictions_on_test, real_test_label,emotion)  # not an object of Perceptron hence, not using a. becuase that is object of Perceptron
            precision = self.precision(tp, fp, fn, tn)
            recall = self.recall(tp, fp, fn, tn)
            f1score = self.f1score(recall, precision)

            print('\nEvaluation for', emotion, ':')
            print('Precision :', precision)
            print('Recall :', recall)
            print('F1 Score :', f1score, '\n')

        final_emotion = []

        dict_index = {}
        for i, k in enumerate(predicted_labels):
            dict_index[i] = k
        l = list(map(list, zip(*[dict_index[k] for k in sorted(dict_index)]))) #list of zipped results from each emotion perceptron

        for element in l:
            m = element.index(max(element)) #index of max answer in zipped l becuase each index corresponds to 1 emotion in emotion list
            final_emotion.append(emotions[m]) #emotion/perceptron which gave that max value
        print('Emotion assigned to sentences: ', final_emotion)

        # predicted_labels = [ [p1, p2, --------] , [p1, p2, -------] , [p1, p2, --------] , [p1, p2, --------] , [p1, p2, --------] , [p1, p2, --------] , [p1, p2, --------] ] comparing p1 (prediction for 1st sentence) of all lists (perceptrons), 2nd list gave max value, taking this index and getting the emotion on the corresponding index from emotion
        # emotion =          [     anger,                 disgust,              fear,              guilt,                joy,               sadness,             shame         ]

if __name__ == '__main__':
    training_file_name = '../isear-train.csv'
    training_data = 'data.txt'
    test_file_name = '../isear-test.csv'
    test_data = 'test_data.txt'
    op = OpeartingPerceptron(training_file_name, training_data, test_file_name, test_data)
    op.main()
