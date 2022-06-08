import matplotlib.pyplot as plt
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

    def plot(self,  f1score, epoch):
        return plt.scatter(epoch, f1score)

    def main(self):
        real_train_label = self.labels_and_data(self.training_data, self.training_file_name)
        real_test_label = self.labels_and_data(self.test_data,self.test_file_name)  # to get clean data
        emotions = sorted(list(set(real_test_label)))  # sorting to make it easy to assign final label by matching index of max with the emotion in emotions list
        dict = self.dictionary(self.training_data)
        train_features = self.features_vector(self.training_data, dict)
        test_vectors = self.features_vector(self.test_data, dict)
        size = len(train_features)
        epochs = 3

        weight = self.weight_vector(dict)
        # updated weight to give weight value to train
        updated_weight = {e:weight for e in emotions}
        # to save results for each epoch
        metrics = ['precision', 'recall', 'f1_score']
        results = {e: {'precision': [], 'recall': [], 'f1_score': []} for e in emotions}
        #print(results)

        for e in range(epochs):
           # print(f"{'=' * 10}\n\n epoch: {e}")
            for emotion in emotions:
                #print(f'training emotion: {emotion}')
                weight = updated_weight[emotion]
                #print(f'Previous weight: {weight[:20]}')
                a = Perceptron(size, train_features, real_train_label, real_test_label, emotion=emotion)

                updated_weight[emotion]= a.train(weight)
                #print(f'Updated weight: {updated_weight[emotion][:20]}')

                predictions_on_test = a.predict(test_vectors, updated_weight[emotion])
                tp, fp, fn, tn = self.confusion_matrix(predictions_on_test, real_test_label,
                                                       emotion)  # not an object of Perceptron hence, not using a. becuase that is object of Perceptron
                evaluations = [self.precision(tp, fp, fn, tn), self.recall(tp, fp, fn, tn)]
                evaluations.append(self.f1score(evaluations[1], evaluations[0]))

                # if(e == epochs -1):
                #     print('\nEvaluation for', emotion, ':')
                #     print('Precision :', evaluations[0])
                #     print('Recall :', evaluations[1])
                #     print('F1 Score :', evaluations[2], '\n')

                for idx, metric in enumerate(metrics):
                    results[emotion][metric].append(evaluations[idx])

        fig, axes = plt.subplots(1, 3, figsize=(50, 10))
        for plt_idx, metric in enumerate(metrics):
            axes[plt_idx].title.set_text(metric)
            for emotion in results:
                axes[plt_idx].plot(results[emotion][metric])
            plt.legend(list(results.keys()))
            plt.xlabel('Epochs')
            plt.ylabel('Score')
        fig.show()
        fig.savefig('Plot-test.png')


if __name__ == '__main__':
    training_file_name = 'isear-train.csv'
    training_data = 'data.txt'
    test_file_name = 'isear-test.csv'
    test_data = 'test_data.txt'
    op = OpeartingPerceptron(training_file_name, training_data, test_file_name, test_data)
    # TOODO
    op.main()
