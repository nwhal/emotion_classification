import data_utils as du
import math
'''
Class definition for TFIDF vectorizor. Builds a dictionary representation of TFIDF
encoded vectors.  
'''
class Tfidf:
    '''
    Initilze method for TFIDF class.
    --------------------------------
    Inputs: [LIST] X - a list of texts to vectorize, [LIST] Y - a list of labels for the text
    Outputs: None
    '''
    def __init__(self, X, Y=None, train=False):
        self.X = X
        self.Y = Y
        self.train = train
        self.num_docs = len(X)
        self.doc_ids = [i for i in range(len(X))]
        self.collection = list(zip(self.doc_ids, self.X))
        self.unique_tokens = set()
        for i in X:
            sent = i.split()
            for word in sent:
                self.unique_tokens.add(word)
    '''
    The tf method calculates term frequency values for each word 
    in each text. The tf_dict is a 2D dictionary containing term
    frequencies for each word in each sentence.
    ------------------------------------------------------------
    Input: None
    Output: None
    '''
    def tf(self):
        #Initialize tf dict
        self.tf_dict = dict()
        #Initialize the sub dictionaries for each doc
        for sent in self.collection:
            self.tf_dict[sent[0]] = dict()

        #Create dictionary of term frequencies for each doc
        for sent in self.collection:
            words = sent[1].split()
            sent_length = len(words)

            # Ad tf value to dictionary
            for word in set(words):
                word_freq = words.count(word)
                tf_val = word_freq/sent_length
                self.tf_dict[sent[0]][word] = tf_val
    '''
    The idf method calculates inverse doc frequency for each
    word. The idf_dict contains an inverse doc frequency value
    for each word in the vocabulary.
    ------------------------------------------------------------
    Input: None
    Output: None
    '''
    def idf(self):
        # Initialize dictionary
        self.idf_dict = {k:0 for k in self.unique_tokens}
        # Calculate log of inverse doc frequency
        for word in self.unique_tokens:
            doc_freq = 0
            for doc in self.tf_dict:
                if word in self.tf_dict[doc]:
                    doc_freq += 1
            
            idf_val = math.log(self.num_docs/doc_freq)
            self.idf_dict[word] = idf_val
    '''
    The tf_idf method calculates calculates the tfidf value by
    for each word in each sentence by multiplying the tf values
    by the idf values for each word. Additionally, we add a key
    to the tf_idf_d dictionary containing the correct label for
    the text.
    ------------------------------------------------------------
    Input: None
    Output: None
    '''
    
    def tf_idf(self):
        self.tf()
        self.idf()
        # Initialize TF_IDF vector dict
        self.tf_idf_d = self.tf_dict.copy()

        for doc in self.tf_idf_d:
            for word in self.tf_idf_d[doc]:
                self.tf_idf_d[doc][word] = self.tf_idf_d[doc][word] * self.idf_dict[word]
        
        if self.train == True:
            # Add correct label to vector
            for i in range(len(self.Y)):
                self.tf_idf_d[i]['LABEL'] = self.Y[i]