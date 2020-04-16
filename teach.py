from tensorflow.keras.datasets import mnist
from tensorflow.keras import  models, layers
from tensorflow.keras.utils import to_categorical
from numpy import genfromtxt
import numpy as np

data = genfromtxt('data_snake.csv', delimiter=',', dtype=str)
features, labels = data[..., :-1], data[..., -1]
features = features.astype("float32")
labels = to_categorical(labels.astype("float32"))


index_slicing = int(len(features) // 1.5)
train_features, test_features = features, features[index_slicing:]
train_label, test_label = labels, features[index_slicing:]

model = models.Sequential()
model.add(layers.Dense(512, activation="relu", input_shape=(len(train_features[0]),)))
model.add(layers.Dense(4, activation="softmax"))

model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(train_features, train_label, epochs=15, batch_size=128)
model.save('snake_ai_model.h5')
