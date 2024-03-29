import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,2,3,4,5,6,7,8,9,10])

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(1, input_dim=1, activation='relu'))

model.compile(loss='mse', optimizer='adam',metrics=['accuracy'])

model.fit(x,y, epochs= 500, batch_size=1)

loss, acc = model.evaluate(x,y, batch_size=1)

print('loss: ', loss)
print("acc ", acc)
