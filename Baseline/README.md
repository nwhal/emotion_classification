# Emotion Classification
This project uses the multi-class perceptron algorithm to classify emotions and is trained on the ISEAR dataset. The program consists of four main parts:\
* Data_Utils - A data utilities module for cleaning and preparing data
* Evaluation - An evaluation class which uses a confusion matrix to calculate precision, recall, and F1 score
* Vectorizer - A class which uses Tf-idf to create feature vectors from text
* Perceptron - A perceptron class which implements a linear classifier for training and predicting emotion labels given text input

## Data-Utils
The data utilities module, data_utils.py, contains the function, prep_data(). The function accepts two positional arguments: the path to the training ISEAR file and a path to the test ISEAR file. The function returns 4 lists:
* X_train - a list of cleaned training texts
* y_train - a list of labels corresponding to X_train
* X_test - a list of cleaned texts to validate the model
* y_test - a set of corresponding labels to X_test

The function can be used as follows:
```
X_train, y_train, X_test, y_test = prep_data(path_to_train_file, path_to_test_file)
```

## Evaluation
The Evaluation class found in evaluator.py calculates precision, recall, and F1 score for a set of predictions during validation. The class is initialized with two positional arguments:
* A list of predicted labels
* A list of true labels
The class can be initialized as follows:
```
eval = Evaluator(predictions, y_test)
```
The method self.ret_fscore() will calculate the F1 score for the predicted model output. Once this method is called, the user may view the attributes:
* self.precision
* self.recall
* self.f_score

Each of these metrics are represented as python dictionaries. 

```
eval.ret_fscore()
precision = eval.precision
recall = eval.recall
f_score = eval.f_score
```

## Vectorizer
The vectorizer folder contains the file tfidf.py, which contains a tfidf class. The tfidf object is initialized with 3 positional arguments:
* X - a list of texts to vectorize
* Y - an optional list of corresponding labels (default is None)
* train - bool set to True if class is used for training (default is False)

The method self.tf_idf() produces tf-idf encoded vectors (python dictionaries) that can be accessed through the class attribute, self.tf_idf_d. 

```
#For training:
tf_idf_model = tfidf.Tfidf(X_train, Y=y_train, train=True

#For testing:
tf_idf_model = tfidf.Tfidf(X_test)

#Dictionary of tf_idf vectors:
feature_vecs = tf_idf_model.tf_idf_d
```

## Perceptron
There are two perceptron classes in the perceptron folder: 
* perceptron_base.py - A perceptron class which uses bag of words vectorization
* perceptron_tfidf.py - A perceptron class which uses Tf-idf vectorization

We will focus on the tfidf perceptron class as this is our finished baseline.

The Perceptron class is initialized with 3 positional arguments:
* X_train - list of training texts
* y_train - list of associated training labels
* epoch - An integer, the number of epochs to train the model

The self.train() method trains the model using the input X_train and y_train lists. The self.predict() method accepts one positional argument,
X_test, and returns a list of predicted labels.
```
#Initializing
model = Perceptron(X_train, y_train, epoch=5)

#Training the model
model.train()

#Testing the model
predictions = model.predict(X_test)
```

## Quick Testing
To easily see how the model works, we have included a python notebook in the perceptron folder, perceptron_tfidf.ipynb. Before running the code in this notebook, please ensure that perceptron_tfidf.ipynb, the ISEAR data files, data_utils module, and tfidf.py are all in the same directory.










