import csv
import re
import string

'''
Utility function to clean string read from csv file. The function lowercases the word
and replaces common contractions with expanded phrases.
-----------------------------------------------------------------------------------------------------------------------------
inputs: [STRING] A text to be cleaned
outputs: [STRING] Lowercased texts with common contractions replaced
with extended versions.

ex. "I'm going to the store!" -> "i am going to the store"
'''
def clean_string(text):
    text = text.lower()
    text = re.sub(r"won\'t", "will not", text)
    text = re.sub(r"can\'t", "cannot", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)

    text = ' '.join(word.strip(string.punctuation) for word in text.split())

    return text

'''
Accepts path to CSV file to be read and processed. 
-----------------------------------------------------------------------------------------------------------------------------
inputs: [STRING] File name/path to file
outputs: [LIST] 2D list where each sublist contains a label and cleaned text.

ex. "training_data.csv" -> [['anger', 'i am super mad right now'], ['sadness', 'i am super sad right now']...]
'''

def getdata(fn):
    res = []
    with open(fn, mode='r') as file:
        csv_file = csv.reader(file)

        for lines in csv_file:
            try:
                #Remove no response answers
                if re.match(r"\[(.*?)\]", lines[1]) or re.match(r'^\n(.*?)', lines[0]):
                    pass
                #Else, clean the string and add it to the results list
                else:
                    lines[1] = clean_string(lines[1])
                    res.append(lines)
            #Ignore empty lines
            except IndexError:
                continue

    # Remove strangely formated entries
    res = [i for i in res if len(i)==2]
    
    return res

'''
Counts the number of entries for each label in the training set
-----------------------------------------------------------------------------------------------------------------------------
inputs: [LIST] 2D list containing label, text pairings
outputs: [DICT] Returns dictionary where keys are labels and
values are counts for each label.

ex. [['anger', 'i am super mad right now'], ['sadness', 'i am super sad right now']] -> {anger: 1, sadness:1}
'''
def count_labels(data):
    #TODO - Add additional param for list of labels and generate initial dict instead of hard coding
    res = dict(joy=0, fear=0, anger=0, shame=0, guilt=0, sadness=0, disgust=0)
    for i in data:
        res[i[0]] += 1
    return res

'''
Builds a vocabulary list of unique tokens
-----------------------------------------------------------------------------------------------------------------------------
inputs: [LIST] 2D list containing label, text pairings
outputs: [LIST] Returns list of unique tokents from input

ex. [['anger', 'i am super mad right now'], ['sadness', 'i am super sad right now']] -> [i, am, super, mad, right now, sad]
'''
def build_vocab(data):
    res = dict()

    for i in data:
        toks = i[1].split()
        for tok in toks:
            res.update({tok:1})
    
    return res.keys()





'''
TESTING:

x = getdata('CL_S2/Team_Lab_Test/isear-train.csv')
labes = count_labels(x)
print(labes)
print(len(x))
print(sum(labes.values()))

print(build_vocab(x))

'''