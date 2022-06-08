class Perceptron:

    def __init__(self, size = None, vectorSpace = None, real_train_label = None, real_test_label = None, emotion = None):
        self.size_of_vector = size
        self.vectorSpace = vectorSpace
        self.real_train_label = real_train_label
        self.real_test_label = real_test_label
        self.emotion = emotion

    def dot_product(self, vectorSpace, weight):
        weighted_sum = 0
        dotProduct = [a*b for a,b in zip(vectorSpace, weight)]
        weighted_sum += sum(dotProduct)
        return weighted_sum

    def train(self, weight):
        for i in range(self.size_of_vector):
            weighted_sum = self.dot_product(self.vectorSpace[i], weight)
            if self.real_train_label[i] == self.emotion.lower() and weighted_sum < 0:
                weight = [a + b for a, b in zip(weight, self.vectorSpace[i])]
            if self.real_train_label[i] != self.emotion.lower() and weighted_sum > 0:
                weight = [a - b for a, b in zip(weight, self.vectorSpace[i])]

        return weight

    def predict(self, vectorSpace, weight):
        self.predicted_label = []

        for sen_vec in vectorSpace:
            prediction = 0
            dotProduct = [a*b for a,b in zip(sen_vec, weight)]
            prediction += sum(dotProduct)

            if prediction > 0:
                self.predicted_label.append(prediction)
            else:
                self.predicted_label.append(0)

        return self.predicted_label
