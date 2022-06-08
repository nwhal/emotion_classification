


def labels_and_data(data, file_name, labels, stop_words):
    data_file = open(data, 'w')
    label_file = open(labels, 'w')
    label = []
    with open(file_name) as fp:
        for line in fp:
            x = line.split(",", 1)  # split on 1st comma to separate label and its sentence
            #if x = 'none'
            if len(x) == 2:
                if x[1].lower() != 'no response' or x[1].lower() != 'none':

                    label.append(x[0].strip('\n'))  # label list
                    label_file.write(x[0].strip('\n').lower())
                    label_file.write('\n')

                    #removing unwanted characters from sentences and making lower case

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

                    print(f'Updated sent: {cleaned_sents}')

                    string = ' '.join([str(item) for item in cleaned_sents])

                    # print(f'Data = {string}')
                    # words = string.split()
                    # print(f'words: {words}')
                    # temp_words = words
                    #
                    #
                    # for word in words:
                    #     print(f'word right now is: {word}')
                    #     #print(f'word: {word}')
                    #     if word in stop_words:
                    #         print(f'stop word found: {word}')
                    #         temp_words.remove(word)
                    #         print(f'temp_words after removing: {temp_words}')
                    #         print(f'words after removing: {words}')
                    #
                    # #words = temp_words
                    # print(f'updated_words: {temp_words}')


                    data_file.write(string)
                    data_file.write('\n')
                    #print('string: ',string)
                    #break
                else:
                    pass

            else:
                pass
        data_file.close()

    return label

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

data = 'removing_stop_words.txt'
file_name = 'isear-train.csv'
label_file = 'labels.txt'
labels_and_data(data, file_name, label_file, stop_words)



