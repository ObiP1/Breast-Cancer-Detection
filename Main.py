import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import keras
from keras import Sequential
from keras.layers import Conv1D, MaxPool1D, Dense, BatchNormalization, Flatten, Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier

cancer = datasets.load_breast_cancer()

#Use Gradient boosting to train and test model then display accuracy
y = cancer.target
X_train, X_test, y_train, y_test = train_test_split(cancer.data, y, stratify=y, random_state=42)
tree = GradientBoostingClassifier(random_state=0, max_depth=1)
tree.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))

#Plot important features
def plot_feature_importances_cancer(model):
    n_features = cancer.data.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align= 'center', color='pink')
    plt.yticks(np.arange(n_features), cancer.feature_names)
    plt.xlabel('Feature Importance', fontweight='bold', fontsize=15)
    plt.ylabel('Name of Feature', fontweight='bold',fontsize=15)
    plt.rcParams['figure.figsize'] = (10,10)

plot_feature_importances_cancer(tree)

X = pd.DataFrame(data= cancer.data, columns= cancer.feature_names)
y = cancer.target
X.head()

#Allows us to see how much data we are necessarily working with
X.shape

#Scales our data in to the training and test sizes
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 0, stratify = y) 

#Get an updated look at data
X_train.shape
X_test.shape

#Scaling of data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Reshape Data
X_train = X_train.reshape(455,30,1)
X_test = X_test.reshape(114,30,1)

#Create model
epochs = 75
model = Sequential()
model.add(Conv1D(filters = 32, kernel_size=2, activation = 'relu', input_shape = (30,1)))
model.add(BatchNormalization())
model.add(Dropout(0,2))

model.add(Conv1D(filters=64, kernel_size=2, activation ='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1, activation = 'sigmoid'))

#Take a look at what your model
model.summary()

#Compile Model
model.compile(optimizer=Adam(lr=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

#Train model
history = model.fit(X_train, y_train, epochs=epochs, verbose=1, validation_data=(X_test, y_test))

 def learningCurve(history, epoch):
   #Plot for visulaization of Training & accuracy of validation values
  epoch_range = range(1, epoch+1)
  plt.plot(epoch_range, history.history['accuracy'])
  plt.plot(epoch_range, history.history['val_accuracy'])
  plt.title('Overall Model Accuracy')
  plt.ylabel('Accuracy')
  plt.xlabel('Epochs')
  plt.legend(['Train', 'Val'], loc='upper right')
  plt.ylim((0.8, 1.000))
  plt.rcParams['figure.figsize'] = (10,10)
  plt.show()

  #Plot for visualization of Training and Val losses
  plt.plot(epoch_range, history.history['loss'])
  plt.plot(epoch_range, history.history['val_loss'])
  plt.title('Model losses')
  plt.ylabel('Loss', fontsize=15)
  plt.xlabel('Epochs', fontsize= 15)
  plt.legend(['Train', 'Val'], loc='upper right')
  plt.rcParams['figure.figsize'] = (10,10)
  plt.show()

#Call back function
learningCurve(history, epochs)
