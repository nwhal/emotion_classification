class Perceptron:

    def __init__(self, weight = None, size = None, vectorSpace = None, real_train_label = None, real_test_label = None, epochs = None, emotion = None):
        self.weight = weight
        self.size_of_vector = size
        self.vectorSpace = vectorSpace
        self.real_train_label = real_train_label
        self.real_test_label = real_test_label
        self.epochs = epochs
        self.emotion = emotion

    def dot_product(self, vectorSpace):
        weighted_sum = 0
        dotProduct = [a*b for a,b in zip(vectorSpace, self.weight)]
        weighted_sum += sum(dotProduct)
        return weighted_sum

    def train(self):
        for e in range(self.epochs):
            for i in range(self.size_of_vector):
                weighted_sum = self.dot_product(self.vectorSpace[i])
                if self.real_train_label[i] == self.emotion.lower() and weighted_sum < 0:
                    self.weight = [a + b for a, b in zip(self.weight, self.vectorSpace[i])]
                if self.real_train_label[i] != self.emotion.lower() and weighted_sum > 0:
                    self.weight = [a - b for a, b in zip(self.weight, self.vectorSpace[i])]
        return self.weight

    def predict(self, vectorSpace):
        self.predicted_label = []

        for sen_vec in vectorSpace:
            prediction = 0
            dotProduct = [a*b for a,b in zip(sen_vec, self.weight)]
            prediction += sum(dotProduct)

            if prediction > 0:
                self.predicted_label.append(prediction)
            else:
                self.predicted_label.append(0)

        return self.predicted_label
