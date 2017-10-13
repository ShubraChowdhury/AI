# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:09:54 2017

@author: shubra
"""

import tensorflow
import keras

from utils import *

# Load training set
X_train, y_train = load_data()
print("X_train.shape == {}".format(X_train.shape))
print("y_train.shape == {}; y_train.min == {:.3f}; y_train.max == {:.3f}".format(
    y_train.shape, y_train.min(), y_train.max()))

# Load testing set
X_test, _ = load_data(test=True)
print("X_test.shape == {}".format(X_test.shape))
#print("Num of Class == {}".format(len(np.unique(y_train[1:]))))

# Import deep learning resources from Keras
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Dropout
from keras.layers import Flatten, Dense


model = Sequential()

#model1.add(Convolution2D(filters=32, kernel_size=(3,3),activation='relu', padding='same', input_shape=X_train.shape[1:]))
#model1.add(Convolution2D(filters=32, kernel_size=(3,3),activation='relu'))
#model1.add(MaxPooling2D(pool_size=(2,2)))
#model1.add(Dropout(0.25))
#
#model1.add(Convolution2D(filters=64, kernel_size=(3,3),activation='relu', padding='same'))
#model1.add(Convolution2D(filters=64, kernel_size=(3,3),activation='relu'))
#model1.add(MaxPooling2D(pool_size=(2,2)))
#model1.add(Dropout(0.25))
#
#
#model1.add(Flatten())
#model1.add(Dense(512, activation='relu'))
#model1.add(Dropout(0.5))
#model1.add(Dense(30, activation='softmax'))

#model.add(Convolution2D(8, (3,3), input_shape=X_train.shape[1:]))
#model.add(MaxPooling2D(pool_size=(2, 2)))
## model.add(Dropout(0.3))
#
#model.add(Convolution2D(16, (2,2), activation='relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
## model.add(Dropout(0.3))
#
#model.add(Convolution2D(32, (2,2), activation='relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
## model.add(Dropout(0.3))
#
#model.add(Flatten())
#model.add(Dense(500))
#model.add(Dropout(0.3))
#
#model.add(Dense(30, activation='softmax'))

model.add(Convolution2D(filters=32, kernel_size=3,activation='relu', padding='same', input_shape=X_train.shape[1:]))
model.add(Convolution2D(filters=32, kernel_size=3,activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Convolution2D(filters=64, kernel_size=3,activation='relu', padding='same'))
model.add(Convolution2D(filters=64, kernel_size=3,activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))


model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(30))


# Summarize the model
model.summary()



from keras.optimizers import SGD, RMSprop, Adagrad, Adadelta, Adam, Adamax, Nadam

model.compile( loss="mean_squared_error",optimizer='adam', metrics=['accuracy'])

from keras.callbacks import ModelCheckpoint   
batch_size = 12
epochs = 10

checkpointer = ModelCheckpoint(filepath='my_model_model5.h5', verbose=1, save_best_only=True)
hist = model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split=0.2, callbacks=[checkpointer])

## TODO: Save the model as model.h5
model.save('my_model_model5.h5')

import matplotlib.pyplot as plt

plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='lower left')
plt.show()
# summarize history for loss
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.show()
print("Graph Done")





y_test = model.predict(X_test)
fig = plt.figure(figsize=(20,20))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(9):
    ax = fig.add_subplot(3, 3, i + 1, xticks=[], yticks=[])
    plot_data(X_test[i], y_test[i], ax)
    
    
    
    