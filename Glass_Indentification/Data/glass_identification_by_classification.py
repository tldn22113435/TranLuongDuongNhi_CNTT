# -*- coding: utf-8 -*-
"""Glass_identification_by_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18foLIcaL8RMd9Q2b0Rzj3O_MyXeKwizx
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from collections import Counter
from IPython.core.display import display, HTML
sns.set_style('darkgrid')

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import io

data = pd.read_csv('/content/drive/MyDrive/Dataset/glass.csv')
data.head()
p=data.columns
data

p = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']

p={}
for i in range(len(p)-1):
  p.append(p[i])

#correlation
cor=data.corr()
#Plot figsize
fig, ax = plt.subplots(figsize=(10, 8))
#Generate Heat Map, allow annotations and place floats in map
sns.heatmap(cor, cmap='coolwarm', annot=True, fmt=".2f")
#Apply xticks
plt.xticks(range(len(cor.columns)), cor.columns);
#Apply yticks
plt.yticks(range(len(cor.columns)), cor.columns)
plt.show()

X= data.drop('Type', axis = 1).values
y= data['Type'].values.reshape(-1,1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state = 42)

print("Shape of X_train: ", X_train.shape)
print("Shape of X_test: ", X_test.shape)
print("Shape of y_train: ", y_train.shape)
print("Shape of y_test: ", y_test.shape)

"""**Logistic Regression**"""

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

classifier_lg = LogisticRegression()
steps = [
    ('scalar', StandardScaler()),
    ('model', LogisticRegression())
]
lg_pipe = Pipeline(steps)

parameters = {
    'model__C' : [1,10,100,1000,10000],
    'model__fit_intercept' : [True],
    'model__multi_class' : ['auto'],
    'model__tol' : [0.0001],
    'model__solver' : ['newton-cg','lbfgs','sag','saga'],
    'model__n_jobs' : [-1],
    'model__max_iter' : [5000],
    'model__random_state' : [42]
}
classifier_lg = GridSearchCV(lg_pipe, parameters, cv = 3)
classifier_lg = classifier_lg.fit(X_train, y_train.ravel())

from sklearn.metrics import accuracy_score

y_pred_lg_train = classifier_lg.predict(X_train)
accuracy_lg_train = accuracy_score(y_train,y_pred_lg_train)
print("Train set accuracy: ", accuracy_lg_train)

y_pred_lg_test = classifier_lg.predict(X_test)
accuracy_lg_test = accuracy_score(y_test,y_pred_lg_test)
print("Test set accuracy: ", accuracy_lg_test)

print(y_pred_lg_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
sns.heatmap(confusion_matrix(y_test, y_pred_lg_test), annot=True, cmap='viridis', fmt='.0f')
plt.show()
import math
print(classification_report(y_test, y_pred_lg_test, digits=3))

import math
print('mean squared error = ', mean_squared_error(y_test,y_pred_lg_test))
print('RMSE = ', math.sqrt(mean_squared_error(y_test,y_pred_lg_test)))

data.head

"""**KNN K-NEAREST NEGIBHOURS**"""

#KNN K-NEAREST NEGIBHOURS
# Fitting classifier to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier_knn = KNeighborsClassifier()
steps = [
    ('scalar', StandardScaler()),
    ('model', KNeighborsClassifier())
]
knn_pipe = Pipeline(steps)

parameters = {  'model__algorithm' : ['brute'],
                'model__leaf_size' : [30,50,70,90,110],
                'model__metric' : ['minkowski'],
                'model__p':[1],
                'model__n_neighbors' : [3,5,11,19],
                'model__weights' : ['uniform', 'distance'],
                'model__n_jobs' : [-1]
}
classifier_knn = GridSearchCV(knn_pipe, parameters, cv = 3)
classifier_knn = classifier_knn.fit(X_train, y_train.ravel())

y_pred_knn_train = classifier_knn.predict(X_train)
accuracy_knn_train = accuracy_score(y_train, y_pred_knn_train)
print("Training set accuracy: ", accuracy_knn_train)

y_pred_knn_test = classifier_knn.predict(X_test)
accuracy_knn_test = accuracy_score(y_test, y_pred_knn_test)
print("Test set accuracy: ", accuracy_knn_test)

from sklearn.metrics import confusion_matrix
sns.heatmap(confusion_matrix(y_test, y_pred_knn_test), annot=True, cmap = 'viridis', fmt='.0f')
plt.show()
import math
print(classification_report(y_test, y_pred_knn_test, digits=3))

"""**Support vector machiene SVM**"""

#Support vector machiene SVM
from sklearn.svm import SVC
classifier_svm = SVC()
steps = [
      ('scalar', StandardScaler()),
      ('model', SVC())
]
svm_linear_pipe = Pipeline(steps)

parameters = {'model__kernel':['linear'],
              'model__C' : [1,10,100,1000,10000],
              'model__random_state' : [42]
}
classifier_svm_linear = GridSearchCV(svm_linear_pipe, parameters, cv = 3)
classifier_svm_linear = classifier_svm_linear.fit(X_train, y_train.ravel())

y_pred_svm_linear_train = classifier_svm_linear.predict(X_train)
accuracy_svm_linear_train = accuracy_score(y_train, y_pred_svm_linear_train)
print("Training set accuracy: ", accuracy_svm_linear_train)

y_pred_svm_linear_test = classifier_svm_linear.predict(X_test)
accuracy_svm_linear_test = accuracy_score(y_test, y_pred_svm_linear_test)
print("Test set accuracy: ", accuracy_svm_linear_test)

from sklearn.metrics import confusion_matrix
sns.heatmap(confusion_matrix(y_test, y_pred_svm_linear_test), annot=True, cmap = 'viridis', fmt='.0f')
plt.show()
import math
print(classification_report(y_test, y_pred_svm_linear_test, digits=3))

"""**DECISSION** **TREE**"""

#DECISSION TREE CLASSIFIER CART
# Fitting classifier to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier_dt = DecisionTreeClassifier()

steps = [
    ('scalar', StandardScaler()),
    ('model', DecisionTreeClassifier())
]
dt_pipe = Pipeline(steps)

# Applying Grid Search to find the best model and the best parameters
parameters = [{ "model__max_depth": np.arange(1,21),
                "model__min_samples_leaf": [1, 5, 10, 20, 50, 100],
                "model__min_samples_split": np.arange(2, 11),
                "model__criterion": ["gini"],
                "model__random_state" : [42]
              }
]
classifier_dt = GridSearchCV(estimator = dt_pipe,
                             param_grid = parameters,
                             cv = 3,
                             n_jobs = -1)
classifier_dt = classifier_dt.fit(X_train, y_train.ravel())

from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

feature_names = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']

dot_data=StringIO()
export_graphviz(DecisionTreeClassifier().fit(X_train, y_train),
                out_file=dot_data,
                filled=True, rounded=True,
                feature_names = feature_names,
                special_characters=True)
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())

y_pred_dt_train = classifier_dt.predict(X_train)
accuracy_dt_train = accuracy_score(y_train, y_pred_dt_train)
print("Training set accuracy: ", accuracy_dt_train)

y_pred_dt_test = classifier_dt.predict(X_test)
accuracy_dt_test = accuracy_score(y_test, y_pred_dt_test)
print("Test set accuracy: ", accuracy_dt_test)

from sklearn.metrics import confusion_matrix
sns.heatmap(confusion_matrix(y_test, y_pred_dt_test), annot=True, cmap = 'viridis', fmt='.0f')
plt.show()
import math
print(classification_report(y_test, y_pred_dt_test, digits=3))

"""**RANDOMFOREST CLASSIFICATION**"""

#RANDOMFOREST CLASSIFICATION
# Fitting Random Forest Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
classifier_rf = RandomForestClassifier()
steps = [
    ('scalar', StandardScaler()),
    ('model', RandomForestClassifier())
]
rf_pipe = Pipeline(steps)

parameters = {"model__n_estimators": [int(x) for x in np.linspace(start =50, stop = 500, num = 10)],
              "model__max_features": ["auto", "sqrt"],
              "model__max_depth": [int(x) for x in np.linspace(10, 110, num = 11)],
              "model__min_samples_split": [2, 5, 10],
              "model__min_samples_leaf": [1, 2, 4],
              "model__bootstrap": [True, False],
              "model__criterion": ["gini"],
              "model__random_state" : [42] }

classifier_rf = RandomizedSearchCV(estimator = rf_pipe,
                                  param_distributions = parameters,
                                  n_iter= 100,
                                  cv = 3,
                                  random_state=42,
                                  verbose = 4,
                                  n_jobs = -1)
classifier_rf = classifier_rf.fit(X_train, y_train.ravel())

y_pred_rf_train = classifier_rf.predict(X_train)
accuracy_rf_train = accuracy_score(y_train, y_pred_rf_train)
print("Training set accaracy: ", accuracy_rf_train)

y_pred_rf_test = classifier_rf.predict(X_test)
accuracy_rf_test = accuracy_score(y_test, y_pred_rf_test)
print("Training set accaracy: ", accuracy_rf_test)

from sklearn.metrics import confusion_matrix
sns.heatmap(confusion_matrix(y_test, y_pred_rf_test), annot=True, cmap = 'viridis', fmt='.0f')
plt.show()
import math
print(classification_report(y_test, y_pred_rf_test, digits=3))

"""**NAIVE BAYES**

**1. GAUSSIAN**
"""

print(X.shape, y.shape)
print(X_test.shape, y_test.shape)
print(y_test_hat)

# training
from sklearn import naive_bayes
model = naive_bayes.GaussianNB()
model.fit(X, y)
# evaluation
from sklearn import metrics
y_test_hat = model.predict(X_test)
print(y_test_hat)
print(metrics.accuracy_score(y_test, y_test_hat))

# Print F1 score with micro average
print("MICRO")
print(metrics.f1_score(y_test, y_test_hat, average='micro'))

# Print F1 score with macro average
print("MACRO")
print(metrics.f1_score(y_test, y_test_hat, average='macro'))

# Print F1 score with weighted average
print("WEIGHTED")
print(metrics.f1_score(y_test, y_test_hat, average='weighted'))

print(model.predict_proba(X_test))

metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_test_hat, labels=[True, False], colorbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Testing set')
plt.show()

"""**2. CATEGORICAL**"""

# training
from sklearn import naive_bayes
model = naive_bayes.CategoricalNB(alpha=0) #not-smoothing
model.fit(X, y)
# evaluation
from sklearn import metrics
y_test_hat = model.predict(X_test)
print(y_test_hat)
print(metrics.accuracy_score(y_test, y_test_hat))
print(model.predict_proba(X_test))

"""**3. BERNOULLI**"""

# training
from sklearn import naive_bayes
model = naive_bayes.BernoulliNB(alpha=0) #not-smoothing
model.fit(X, y)
# evaluation
from sklearn import metrics
y_test_hat = model.predict(X_test)
print(y_test_hat)
print(metrics.accuracy_score(y_test, y_test_hat))
print(model.predict_proba(X_test))

"""**4. MULTINOMIAL**"""

# training
from sklearn import naive_bayes
model = naive_bayes.MultinomialNB()
model.fit(X, y)
# evaluation
from sklearn import metrics
y_test_hat = model.predict(X_test)
print(y_test_hat)
print(metrics.accuracy_score(y_test, y_test_hat))
print(model.predict_proba(X_test))

"""**NEURAL NETWORK**"""

#ANN (ARTIFICIAL NEURAL NETHORK)
# Importing the Keras libraries and packases
import keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# sc_X= StandardScaler()
# X_train_scaled = sc_X.fit_transform(X_train)
# X_test_scaled = sc_X.fit_transform(X_test)
print(X_train_scaled.shape)
print(X_test_scaled.shape)

# Defining a function to encode output column
from keras.utils import to_categorical

def encode(data):
    print('Shape of data (BEFORE encode): %s' % str(data.shape))
    encoded = to_categorical (data)
    print('Shape of data (AFTER encode): %s\n' % str(encoded.shape))
    return encoded

y_train_encoded = encode(y_train)

y_test_encoded = encode(y_test)

y_train_encoded = np.delete(y_train_encoded, [0,4] , axis = 1)
y_test_encoded = np.delete(y_test_encoded, [0,4], axis = 1)
print(y_train_encoded[2])
print(y_test_encoded[2])

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 9, kernel_initializer = 'uniform',activation = 'relu'))

# Adding the second hidden layer
classifier.add(Dense(units = 5, kernel_initializer = 'uniform',activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform',activation = 'softmax'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
# Fitting the ANN to the Training set
history = classifier.fit(X_train_scaled, y_train_encoded, validation_data=(X_test_scaled, y_test_encoded), batch_size = 100, epochs = 1150)

f, axes = plt.subplots(1,2,figsize=(14,4))
axes[0].plot(history.history['loss'])
axes[0].plot(history.history['val_loss'])
axes[0].set_xlabel('Loss', fontsize=14)
axes[0].set_ylabel('Epuch', fontsize=14)
axes[0].yaxis.tick_left()
axes[0].legend(['Train', 'Test'], loc='upper left')

axes[1].plot(history.history['accuracy'])
axes[1].plot(history.history['val_accuracy'])
axes[1].set_xlabel('Accuracy', fontsize=14)
axes[1].set_ylabel('Epoch', fontsize=14)
axes[1].yaxis.set_label_position("right")
axes[1].yaxis.tick_right()
axes[1].legend(['Train', 'Test'], loc='upper left')

plt.show()

print("Training  set accuracy: ", history.history.get('accuracy')[-1])
print("Test set accuracy: ", history.history.get('val_accuracy')[-1])

"""**COMPARING THE HODELS**"""

#COMPARING THE HODELS
models = [('Logistic Regression', accuracy_lg_train, accuracy_lg_test),
          ('KNN', accuracy_knn_train, accuracy_knn_test),
          ('SVM (Linear)', accuracy_svm_linear_train, accuracy_svm_linear_test),
          ('Decision Tree Classification', accuracy_dt_train, accuracy_dt_test),
          ('Random Forest Classification', accuracy_rf_train, accuracy_rf_test),
          ('ANN', history.history.get('accuracy')[-1], history.history.get('val_accuracy')[-1]),
]

predict = pd.DataFrame(data = models, columns=['Model','Training Accuracy','Test Accuracy'])
predict

#VISUALIZING MODELS PERFORMANCE

f, axes = plt.subplots(2,1, figsize=(14,10))

predict.sort_values(by=['Training Accuracy'], ascending=False, inplace=True)

sns.barplot(x='Training Accuracy', y='Model', data = predict, palette='Reds_d',ax = axes[0])
#axes[0].set (xlabel= 'Region', ylabel='Charges')
axes[0].set_xlabel('Training Accuracy', size=16)
axes[0].set_ylabel('Model')
axes[0].set_xlim(0,1.0)
axes[0].set_xticks(np.arange(0, 1.1, 0.1))

predict.sort_values(by=['Test Accuracy'], ascending=False, inplace=True)

sns.barplot(x='Test Accuracy', y='Model', data = predict, palette='Blues_d', ax = axes[1])
#axes[0].set(xlabel='Region', ylabel='Charges')
axes[1].set_xlabel('Test Accuracy', size=16)
axes[1].set_ylabel('Model')
axes[1].set_xlim(0,1.0)
axes[1].set_xticks(np.arange(0, 1.1, 0.1))

plt.show()