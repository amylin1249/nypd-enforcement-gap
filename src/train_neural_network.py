import numpy as np
import torch
import torch.nn as nn
from sklearn.preprocessing import StandardScaler
from sklearn.exceptions import UndefinedMetricWarning
from train_linear_model import split_dataset
import warnings

# Silence warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)


class Network:
    def __init__(self, sizes):
        self.L = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(n, 1) for n in self.sizes[1:]]
        self.weights = [
            np.random.randn(n, m) * 0.01
            for (m, n) in zip(self.sizes[:-1], self.sizes[1:])
        ]
        self.acc_train_array = []
        self.acc_test_array = []

    def g(self, z):
        """
        ADD DOCSTRING - TBD if sigmoid is the most suitable activation function
        """
        return sigmoid(z)

    def g_prime(self, z):
        """
        ADD DOCSTRING
        """
        return sigmoid_prime(z)

    def forward_prop(self, a):
        """
        ADD DOCSTRING
        """
        ### ADD IN CODE - currently part of Homework 4

    def grad_cost(self, a, y):
        """
        ADD DOCSTRING - TBD cost function
        """
        return a - y

    def log_train_progress(self, train, test, epoch):
        """
        ADD DOCSTRING
        """
        acc_train = self.evaluate(train)
        self.acc_train_array.append(acc_train)
        if test is not None:
            acc_test = self.evaluate(test)
            self.acc_test_array.append(acc_test)
            print(
                "Epoch {:4d}: Train {:10.5f}, Test {:10.5f}".format(
                    epoch + 1, acc_train, acc_test
                )
            )
        else:
            print("Epoch {:4d}: Train {:10.5f}".format(epoch + 1, acc_train))

    def SGD_train(self, train, epochs, eta, lam=0.0, verbose=True, test=None):
        """
        ADD DOCSTRING
        """
        n_train = len(train)
        for epoch in range(epochs):
            perm = np.random.permutation(n_train)
            for kk in range(n_train):
                self.SGD_step(*train[perm[kk]], eta, lam)
            if verbose and epoch == 0 or (epoch + 1) % 20 == 0:
                self.log_train_progress(train, test, epoch)

    def SGD_step(self, x, y, eta, lam):
        """
        Get gradients with x, y and do SGD on weights and biases

        Args:
            x: single sample features.
            y: single sample target.
            eta: learning rate.
            lam: Regularization parameter.

        """
        ### ADD IN CODE - currently part of Homework 4
        return None

    def back_prop(self, x, y):
        """
        Backpropagation for derivatives of C wrt parameters
        """
        db_list = [np.zeros(b.shape) for b in self.biases]
        dW_list = [np.zeros(W.shape) for W in self.weights]

        x = x.reshape(-1, 1)
        y = np.array([[y]])

        a = x
        a_list = [a]
        z_list = [np.zeros(a.shape)]

        for W, b in zip(self.weights, self.biases):
            z = np.dot(W, a) + b
            z_list.append(z)
            a = self.g(z)
            a = a.reshape(-1, 1)
            a_list.append(a)

        ### ADD IN CODE - currently part of Homework 4

        return (dW_list, db_list)

    def evaluate(self, test):
        """
        Evaluate current model on labeled test data
        """
        ctr = 0
        for x, y in test:
            yhat = self.forward_prop(x)
            y = np.squeeze(y)

            prediction = int(yhat >= 0.5)
            ctr += int(prediction == y)

        return ctr / len(test)


def sigmoid(z, threshold=20):
    z = np.clip(z, -threshold, threshold)
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_prime(z):
    return sigmoid(z) * (1.0 - sigmoid(z))


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = split_dataset()
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    train = list(zip(X_train, y_train))
    test = list(zip(X_test, y_test))
    print(train[:5])

    input_dimensions = len(train[0][0])
    output_dimensions = 1

    nns = []
    hidden_layer_dimensions = [1, 2, 4, 8, 16]

    for hidden_layer_dimension in hidden_layer_dimensions:
        print("\nHidden Layer Dimensions: ", hidden_layer_dimension)
        nn = Network([input_dimensions, hidden_layer_dimension, output_dimensions])
        nns.append(nn)
        nn.SGD_train(train, epochs=200, eta=0.01, lam=0.0001, verbose=True, test=test)

    # CURRENTLY STILL WIP (quite a few changes compared to homework because of the data shape) - Need to check hyperparameters, activation function, loss function, etc.
