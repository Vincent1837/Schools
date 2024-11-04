import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from matplotlib import pyplot as plt

def sigmoid(x):
    x = np.clip(x, -500, 500)
    return 1.0 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1.0 - sigmoid(x))

def rmse(predictions, targets):
    predictions = np.clip(predictions, -1e9, 1e9)
    return np.sqrt(((predictions - targets) ** 2).mean())

def purelin(x):
    return x

def purelin_derivative(x):
    return 1

input_size = 4
hidden_size = 10
output_size = 1

np.random.seed(42)

X = pd.read_csv('iris_in.csv', header=None).values
y = pd.read_csv('iris_out.csv', header=None).iloc[:, 0].values 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42, shuffle=True)

W1 = np.random.randn(input_size, hidden_size)
b1 = np.random.randn(1, hidden_size)
W2 = np.random.randn(hidden_size, output_size)
b2 = np.random.randn(1, output_size)
epochs = 300
loss_list = []

learning_rate = 0.01

for epoch in tqdm(range(epochs)):
    total_loss = 0

    for i in range(len(X_train)):
        X_sample, y_sample = X_train[i:i+1], y_train[i:i+1]

        hidden = sigmoid(np.dot(X_sample, W1) + b1)
        predict = purelin(np.dot(hidden, W2) + b2)

        predict = np.array([[1]]) if predict <= 0.33 else np.array([[2]]) if predict <= 0.66 else np.array([[3]])
        
        total_loss += rmse(predict, y_sample)

        delta2 = -1*(predict - y_sample) * purelin_derivative(predict)
        delta1 = delta2.dot(W2.T) * sigmoid_derivative(hidden)
        
        W2 += hidden.T.dot(delta2) * learning_rate
        b2 += np.sum(delta2, axis=0) * learning_rate
        W1 += X_sample.T.dot(delta1) * learning_rate
        b1 += np.sum(delta1, axis=0) * learning_rate

    loss_list.append(total_loss / len(X_train))

y_pred = []
y_test = []
for i in range(len(X_test)):
    hidden = sigmoid(np.dot(X_test[i:i+1], W1) + b1)
    predict = purelin(np.dot(hidden, W2) + b2)
    y_test.append(predict)
    predict_class = 1 if predict <= 0.33 else 2 if predict <= 0.66 else 3
    y_pred.append(predict_class)


accuracy = np.mean(np.array(y_pred) == y_test)
print(y_test)
print(f"Acc: {accuracy * 100:.2f}%")
plt.plot(loss_list)
plt.xlabel('Epochs')
plt.ylabel('RMSE Loss')
plt.show()