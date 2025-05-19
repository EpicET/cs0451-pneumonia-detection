import torch

class SVM: 
    """Support Vector Machine (SVM) implementation using stochastic gradient descent.
    """
    def __init__(self, n_iters = 1000, lam  = 0.0001, batch_size = 32): 
        self.n_iters = n_iters
        self.lam = lam
        self.batch_size = batch_size
        self.w = None

    def score(self, X):
        """
        Computes the score of the model on the input data.
        Args:
            X (torch.Tensor): Input data of shape (n_samples, n_features).
        Returns:
            torch.Tensor: Score of the model on the input data."""
        if self.w is None:
            raise ValueError("Model is not fitted yet.")
        return X @ self.w
    
    def fit(self, X, y):
        """
        Fits the SVM model to the training data using stochastic gradient descent.
        Args:
            X (torch.Tensor): Training data of shape (n_samples, n_features).
            y (torch.Tensor): Labels of shape (n_samples,).
        """ 
        y_ = torch.where(y <= 0, -1, 1)
        self.w = torch.zeros(X.shape[1]) 
        s = X.shape[0]
        for t in range(1, self.n_iters): 

            # Randomly select a batch of samples
            A = torch.randint(0, s, (self.batch_size,))
            ap_sum = torch.zeros_like(self.w)
            nu = 1 / (self.lam * t)
            for i in A:
                x_i = X[i]
                y_i = y_[i]
                if (y_i * self.score(x_i) < 1):
                    ap_sum += y_i * x_i
                else: 
                    continue
            # Update the weights
            self.w = (1 - nu * self.lam) * self.w  + (nu / self.batch_size) * ap_sum

    def predict(self, X):
        """
        Predicts the labels for the input data using the fitted model.
        Args:
            X (torch.Tensor): Input data of shape (n_samples, n_features).
        Returns:
            torch.Tensor: Predicted labels of shape (n_samples,).
        """
        if self.w is None:
            raise ValueError("Model is not fitted yet.")
        score = self.score(X) >= 0
        return score