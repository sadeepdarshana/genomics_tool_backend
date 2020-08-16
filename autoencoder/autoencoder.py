import keras
from keras import Sequential
from keras.layers import Dense
import numpy as np
from keras import backend as K


def normalize_over_axis1(arr2d):
    for i in range(arr2d.shape[0]):
        hori_sum = sum(arr2d[i])
        if hori_sum!= 0 : arr2d[i] = (arr2d[i])/hori_sum

def build_model(layers_sizes, activation ):
    model = Sequential()
    model.add(Dense(layers_sizes[1], input_dim=layers_sizes[0],activation = activation))
    for i in range(2,len(layers_sizes)):
        model.add(Dense(layers_sizes[i], activation = activation))
    model.compile(loss='mse', optimizer=keras.optimizers.Adam())
    return model

def train(model,epochs,vectors):
    model.fit(vectors,vectors,epochs=epochs)

def get_result_points(model, vectors):
    middle_layer=model.layers[int(len(model.layers) / 2 - 1)]
    input_layer=model.layers[0]
    mapping_function = K.function([input_layer.input], [middle_layer.output])
    points = mapping_function(vectors)[0]
    return points

def process(vectors, epochs, activation, layers_sizes, train_perc):
    model = build_model(layers_sizes,activation)
    np_vectors = np.array(vectors).astype(np.float32)
    normalize_over_axis1(np_vectors)
    train_set = np_vectors[np.random.choice(np_vectors.shape[0], int(np_vectors.shape[0] * train_perc), replace=False)]
    np.random.shuffle(train_set)
    train(model,epochs,train_set)
    return get_result_points(model, np_vectors)
