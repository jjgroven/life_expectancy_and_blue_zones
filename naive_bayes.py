# -*- coding: utf-8 -*-
"""ML Project - Naive Bayes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dPbrMlmdItkUKPbD_DPWXovlArfR4sSY
"""

#MULTINOMIAL NAIVE BAYES CLASSIFICATION
import pandas as pd

df = pd.read_csv("/content/lifeExpectancyARM.csv")
targetDf = df["Life expectancy change groups"]
df = df.drop("Life expectancy change groups", axis=1)
X = df
X

targetDf.unique()

#One Hot encode Categories
df_encoded = pd.get_dummies(df)
X=df_encoded
X

X.to_csv("lifeExpectancyARMEncoded.csv")

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

labels = ['Negative Change', 'Low Change', 'Moderate Change', 'High Change']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, targetDf, test_size=0.3, random_state=41)

X_train.head(5)

X_test.head(5)

y_train.head(5)

y_test.head(5)

# Initialize and fit the Multinomial Naive Bayes model
mnb = MultinomialNB()
mnb.fit(X_train, y_train)

# Predict on test data
y_pred = mnb.predict(X_test)

# Model accuracy
accuracy = mnb.score(X_test, y_test)
print("Multinomial Naive Bayes accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for Multinomial Naive Bayes")
plt.show()

##BERNOULLI NAIVE BAYES CLASSIFICATION

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

labels = ['Negative Change', 'Low Change', 'Moderate Change', 'High Change']

X_train, X_test, y_train, y_test = train_test_split(X, targetDf, test_size=0.3, random_state=11)

# training the model on training set
bern = BernoulliNB()
bern.fit(X_train, y_train)

# making predictions on the testing set
y_pred = bern.predict(X_test)

# comparing actual response values (y_test) with predicted response values (y_pred)
print("Bernoulli Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred))

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for Bernoulli Naive Bayes")
plt.show()

#Clean Continuous data
import pandas as pd

df = pd.read_csv("/content/lifeExpectancyMaster.csv")
targetDf = df["Life expectancy at birth, total (years)"]
targetDf = pd.DataFrame(targetDf)
bins = [0, 60, 70, 80, 90]
targetDf["Life expectancy groups"] = pd.cut(targetDf["Life expectancy at birth, total (years)"],
                                            bins,labels=['Low LE', 'Low Middle LE', 'Middle High LE', "High LE"])
df = df.drop(["Year", "Country Name","Life expectancy at birth, total (years)"], axis=1)
X = df
targetDf = targetDf["Life expectancy groups"]

targetDf.value_counts()

#GAUSSIAN NAIVE BAYES CLASSIFICATION
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

labels = ['Low LE', 'Low Middle LE', 'Middle High LE', "High LE"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X,targetDf, test_size=0.3, random_state=9)

X_train.head(5)

X_test.head(5)

y_train.head(5)

y_test.head(5)

# Initialize and fit the Gaussian Naive Bayes model
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Predict on test data
y_pred = gnb.predict(X_test)

# Model accuracy
accuracy = gnb.score(X_test, y_test)
print("Gaussian Naive Bayes accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for Gaussian Naive Bayes")
plt.show()
