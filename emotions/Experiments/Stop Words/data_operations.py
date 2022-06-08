import random

class DataOperations:

    def labels_and_data(self, data, file_name):

        stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                      "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
                      "itself",
                      "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                      "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                      "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because",
                      "as",
                      "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
                      "through",
                      "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on",
                      "off",
                      "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why",
                      "how",
                      "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
                      "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
                      "should",
                      "now"]

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
                    string = string.lower()

                    cleaned_sents = []

                    sent = string.split()
                    sent = [i for i in sent if i not in stop_words]
                    new_sent = ' '.join(sent)
                    cleaned_sents.append(new_sent)

                    string = ' '.join([str(item) for item in cleaned_sents])

                    data_file.write(string)
                    data_file.write('\n')

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
