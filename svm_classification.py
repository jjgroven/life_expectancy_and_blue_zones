# -*- coding: utf-8 -*-
"""ML Project - SVM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZFcMlYk_l1f1ap3CKmt6ysboNd9-ihja
"""

#SVM Data must be numerical and normalized and preferably binary labels
#Clean Continuous data
import pandas as pd

df = pd.read_csv("/content/lifeExpectancyMaster.csv")
targetDf = df["Life expectancy at birth, total (years)"]
targetDf = pd.DataFrame(targetDf)
bins = [0, 70,90]
targetDf["Life expectancy groups"] = pd.cut(targetDf["Life expectancy at birth, total (years)"],
                                            bins,labels=['LE <= 70 Years', 'LE > 70 years'])
df

df = df.drop(["Year", "Country Name","Life expectancy at birth, total (years)"], axis=1)
df.to_csv("SVM_data.csv")
X = df
targetDf = targetDf["Life expectancy groups"]

X

targetDf.value_counts()

#Normalize data columns
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaledDF = scaler.fit_transform(X)

X = pd.DataFrame(scaledDF,  columns=X.columns)
sampledata = X.merge(targetDf, left_index=True, right_index=True)
sampledata.to_csv("SVM_sample_data.csv")
X.head(5)

#SVM CLASSIFICATION
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

targetDf = targetDf.replace({"LE <= 70 Years":-1, "LE > 70 years":1})
targetDf = pd.DataFrame(targetDf)
# Split data
X_train, X_test, y_train, y_test = train_test_split(X,targetDf, test_size=0.3, random_state=9)

X_train = pd.DataFrame(X_train)
X_test = pd.DataFrame(X_test)
y_train = pd.DataFrame(y_train)
y_test = pd.DataFrame(y_test)
X_train.to_csv("SVM_X_train.csv")
X_train.head(5)

y_train.to_csv("SVM_y_train.csv")
y_train.head(5)

X_test.to_csv("SVM_X_test.csv")
X_test.head(5)

y_test.to_csv("SVM_y_test.csv")
y_test.head(5)

"""#SVM RBF

"""

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=1, kernel="rbf", verbose=False) #Linear, poly, rbf
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model accuracy
accuracyRBF1 = clf.score(X_test, y_test)
print("SVM (rbf kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (rbf kernel: C = 1)")
plt.show()

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=5, kernel="rbf", verbose=False) #Linear, poly, rbf
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model accuracy
accuracyRBF5 = clf.score(X_test, y_test)
print("SVM (rbf kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (rbf kernel: C = 5)")
plt.show()

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=10, kernel="rbf", verbose=False) #Linear, poly, rbf
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model accuracy
accuracyRBF10 = clf.score(X_test, y_test)
print("SVM (rbf kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (rbf kernel: C = 10)")
plt.show()

"""#SVM Linear"""

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=1, kernel="linear", verbose=False) #Linear, poly, rbf
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model accuracy
accuracyLIN1 = clf.score(X_test, y_test)
print("SVM (linear kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (linear kernel: C = 1)")
plt.show()

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=5, kernel="linear", verbose=False) #Linear, poly, rbf
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model accuracy
accuracyLIN5 = clf.score(X_test, y_test)
print("SVM (linear kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (linear kernel: C = 5)")
plt.show()

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=10, kernel="linear", verbose=False) #Linear, poly, rbf
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model accuracy
accuracyLIN10 = clf.score(X_test, y_test)
print("SVM (linear kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (linear kernel: C = 10)")
plt.show()

"""#SVM Polynomial"""

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=1, kernel="poly", verbose=False) #Linear, poly, rbf
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model accuracy
accuracyPOLY1 = clf.score(X_test, y_test)
print("SVM (poly kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (poly kernel: C = 1)")
plt.show()

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=5, kernel="poly", verbose=False) #Linear, poly, rbf
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model accuracy
accuracyPOLY5 = clf.score(X_test, y_test)
print("SVM (poly kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (poly kernel: C = 5)")
plt.show()

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=10, kernel="poly", verbose=False) #Linear, poly, rbf
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model accuracy
accuracyPOLY10 = clf.score(X_test, y_test)
print("SVM (poly kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (poly kernel: C = 10)")
plt.show()

accuracies = [accuracyRBF1, accuracyRBF5, accuracyRBF10, accuracyLIN1, accuracyLIN5, accuracyLIN10, accuracyPOLY1, accuracyPOLY5, accuracyPOLY10]

plt.bar(range(len(accuracies)), accuracies)
plt.xlabel("Kernel - Cvalue")
plt.xticks(range(len(accuracies)), ['RBF C=1', 'RBF C=5', 'RBF C=10', 'LIN C=1', 'LIN C=5','LIN C=10', 'POLY C=1','POLY C=5','POLY C=10'])
plt.xticks(rotation=45)
plt.title("SVM Accuracy")
plt.ylabel("Accuracy")
plt.show()

#plotting the decision boundary: https://scikit-learn.org/dev/auto_examples/svm/plot_svm_kernels.html
from sklearn import svm
from sklearn.inspection import DecisionBoundaryDisplay

X_train_short = X_train[["Cause of death, by non-communicable diseases (% of total)", "People using safely managed drinking water services (% of population)"]]
def plot_training_data_with_decision_boundary(
    kernel, ax=None, long_title=True, support_vectors=True
):
    # Train the SVC
    clf = svm.SVC(kernel=kernel, gamma=2).fit(X_train_short, y_train)

    # Settings for plotting
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 7))
    x_min, x_max, y_min, y_max = -3, 2, -3, 2
    ax.set(xlim=(x_min, x_max), ylim=(y_min, y_max))

    # Plot decision boundary and margins
    common_params = {"estimator": clf, "X": X_train_short, "ax": ax}
    DecisionBoundaryDisplay.from_estimator(
        **common_params,
        response_method="predict",
        plot_method="pcolormesh",
        alpha=0.3,
    )
    DecisionBoundaryDisplay.from_estimator(
        **common_params,
        response_method="decision_function",
        plot_method="contour",
        levels=[-1, 0, 1],
        colors=["k", "k", "k"],
        linestyles=["--", "-", "--"],
    )

    if support_vectors:
        # Plot bigger circles around samples that serve as support vectors
        ax.scatter(
            clf.support_vectors_[:, 0],
            clf.support_vectors_[:, 1],
            s=150,
            facecolors="none",
            edgecolors="k",
        )

    # Plot samples by color and add legend
    labels = [-1,1]
    colors = ["red", "blue"]
    for x in [0,1]:
        if x == 0:
            currentLabel = -1
        else:
            currentLabel = 1
        X_train_short_class = X_train_short[y_train["Life expectancy groups"] == currentLabel]
        ax.scatter(X_train_short_class["Cause of death, by non-communicable diseases (% of total)"], X_train_short_class["People using safely managed drinking water services (% of population)"], c = colors[x], s=30, edgecolors="k")
    if long_title:
        ax.set_title(f" Decision boundaries of {kernel} kernel in SVC")
    else:
        ax.set_title(kernel)
    labels = ["Support Vectors","LE <= 70 years", "LE > 70 years"]
    ax.legend(labels, loc="upper left", title="Classes")

    #ax.scatter(X_train_short[:, 0], X_train_short[:, 1], c=["red", "blue"], s=30, edgecolors="k")


    if ax is None:
        plt.show()

plot_training_data_with_decision_boundary("rbf")

plot_training_data_with_decision_boundary("linear")

plot_training_data_with_decision_boundary("poly")

X_test_short = X_test[["Cause of death, by non-communicable diseases (% of total)", "People using safely managed drinking water services (% of population)"]]

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=1, kernel="rbf", verbose=False) #Linear, poly, rbf
clf.fit(X_train_short, y_train)
y_pred = clf.predict(X_test_short)

# Model accuracy
accuracy = clf.score(X_test_short, y_test)
print("SVM (rbf kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (rbf kernel)")
plt.show()

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=1, kernel="linear", verbose=False) #Linear, poly, rbf
clf.fit(X_train_short, y_train)
y_pred = clf.predict(X_test_short)

# Model accuracy
accuracy = clf.score(X_test_short, y_test)
print("SVM (linear kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (linear kernel)")
plt.show()

#Train and test SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
clf = SVC(C=1, kernel="linear", verbose=False) #Linear, poly, rbf
clf.fit(X_train_short, y_train)
y_pred = clf.predict(X_test_short)

# Model accuracy
accuracy = clf.score(X_test_short, y_test)
print("SVM (linear kernel) accuracy:", accuracy)

#Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

labels = ["LE <= 70 years", "LE > 70 years"]
#Display the confusion matrix using ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size if needed
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Confusion Matrix for SVM (linear kernel)")
plt.show()

