import random

class DataOperations:

    def labels_and_data(self, data, file_name):

        data_file = open(data, 'w')
        label = []
        with open(file_name) as fp:
            for line in fp:
                x = line.split(",", 1)  # split on 1st comma to separate label and its sentence
                if len(x) == 2:
                    label.append(x[0].strip('\n'))  # label list

                    # removing unwanted characters from sentences and making lower case
                    string = x[1].replace('"', '').replace('(', '').replace(')', '').replace('[', '').replace(']',
                                                                                                              '').replace(
                        '.', '').replace(',', '').replace('-', '').replace('?', '').replace('&', '').replace('$',
                                                                                                             '').replace(
                        '!', '').replace('%', '').replace('\'', '').replace(':', '').replace('/', '')
                    string = ''.join([i for i in string if not i.isdigit()])  # removing digits
                    data_file.write(string.lower())

                else:
                    pass
            data_file.close()

        return label

    def tokens(self, training_data):
        with open(training_data, 'r') as f:
            list_of_tokens = []
            for line in f:
                strip_lines = line.strip()
                sentence_as_list = strip_lines.split()  # each sentence into a list

                # each word in the list of that sentence = token
                for i in sentence_as_list:
                    list_of_tokens.append(i)

        return list_of_tokens

    def dictionary(self, training_data):
        list_of_tokens = self.tokens(training_data)
        dict_ = sorted(list(set(list_of_tokens)))
        return dict_

    def weight_vector(self, dict):
        weight = []
        for i in range(len(dict)):
            n = random.randint(0, 1)
            weight.append(n)
        return weight

    # MAKING FEATURE VECTOR OF EACH SENTENCE
    def features_vector(self, data, dict):
        all_features = []

        # MAKING SENTENCE VECTORS
        with open(data, 'r') as f:
            for sentence in f:
                feature_vector_per_sentence = []
                tokens_of_sentence = sentence.split()

                for term in dict:
                    if term in tokens_of_sentence:
                        feature_vector_per_sentence.append(1)
                    else:
                        feature_vector_per_sentence.append(0)

                all_features.append(feature_vector_per_sentence)


        return all_features
