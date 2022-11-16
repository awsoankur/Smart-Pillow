
# coding: utf-8

# In[2]:



# In[3]:


import os
os.environ["CUDA_VISIBLE_DEVICES"] = '-1'
import numpy as np
import matplotlib.pyplot as plt
import time
import tensorflow as tf
import wfdb
from sklearn.utils import class_weight


# In[4]:


tf.test.is_built_with_cuda()

from tensorflow.python.client import device_lib
tf.config.list_physical_devices('GPU')

device_lib.list_local_devices()


# In[5]:


save_here = os.path.join("/home/era/yukkta", "apn.h5")
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=save_here,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True)


# In[6]:


sequence_length = 240


# In[7]:


X_train = np.load('/home/era/yukkta/train_input.npy', allow_pickle=True)
y_train = np.load('/home/era/yukkta/train_label.npy', allow_pickle=True)

X_test = np.load('/home/era/yukkta/test_input.npy', allow_pickle=True)
y_test = np.load('/home/era/yukkta/test_label.npy', allow_pickle=True)


X1 = []
X2 = []
for index in range(len(X_train)):
    X1.append([X_train[index][0], X_train[index][1]])
    X2.append([X_train[index][2], X_train[index][3]])
X_train1, X_train2 = np.array(X1).astype('float64'), np.array(X2).astype('float64')



X1 = []
X2 = []
for index in range(len(X_test)):
    X1.append([X_test[index][0], X_test[index][1]])
    X2.append([X_test[index][2], X_test[index][3]])
X_test1, X_test2 = np.array(X1).astype('float64'), np.array(X2).astype('float64')

X_train1 = np.transpose(X_train1, (0, 2, 1))

X_test1 = np.transpose(X_test1, (0, 2, 1))

class_w = class_weight.compute_class_weight(class_weight = "balanced", classes = np.unique(y_train), y = y_train)


# In[7]:


layers = {'input': 2, 'hidden1': 256, 'hidden2': 256, 'output': 1}
x1 = tf.keras.layers.Input(shape=(sequence_length, layers['input']))
m1 = tf.keras.layers.LSTM(layers['hidden1'],                   
                recurrent_dropout=0.5,
               return_sequences=True)(x1)

m1 = tf.keras.layers.LSTM(
        layers['hidden2'],
        recurrent_dropout=0.5,
        return_sequences=False)(m1)

x2 = tf.keras.layers.Input(shape=(2,))
m2 = tf.keras.layers.Dense(32)(x2)

merged = tf.keras.layers.Concatenate(axis=1)([m1, m2])

out = tf.keras.layers.Dense(8)(merged)
out = tf.keras.layers.Dense(layers['output'], kernel_initializer='normal')(out)
out = tf.keras.layers.Activation("sigmoid")(out)


model = tf.keras.models.Model(inputs=[x1, x2], outputs=[out])

model.compile(loss="binary_crossentropy", optimizer="adam",
              metrics = ['accuracy'])


model.summary()


# In[ ]:


class_w = {i : class_w[i] for i in range(2)}
history = model.fit([X_train1, X_train2], y_train, epochs=20, batch_size=256, validation_split=0.1, class_weight=class_w, callbacks=[cp_callback])

