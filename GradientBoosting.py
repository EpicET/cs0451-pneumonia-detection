import torch 
import numpy as np 
from sklearn.tree import DecisionTreeRegressor

class GradientBoostClassifier:
    def __init__(self, num_iterations, learning_rate, max_depth):
        self.log_odds = None
        self.num_iterations = num_iterations
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []

    def sigmoid(x):
        return 1 / (1 + torch.exp(-x))

    def fit(self, X, y):
        self.prediction_0 = torch.log(y.mean() / (1-y.mean()))
        Fm = np.full(y.shape, self.prediction_0)
    
        for _ in range(self.num_iterations):
            prob_pneumonia = self.sigmoid(Fm)
            gradient = y - prob_pneumonia #Observed - Predicted
            tree = DecisionTreeRegressor(max_depth=self.mex_depth) # Weak learner
            tree.fit(X, gradient)
            tree_output = tree.predict(X)
            Fm += self.learning_rate * tree_output
            self.trees.append(tree)
        self.Fm = Fm
    
    def predict_proba(self, X):
        Fm = torch.full(X.shape[0], self.prediction_0)
        for tree in self.trees: #Iterate through weak learners: this is the boosting process
            Fm += self.learning_rate * tree.predict(X)
        return self.sigmoid(Fm)

    def predict(self, X):
        proba = self.predict_proba(X)
        return (proba >= 0.5).float()
        