# How would i even start something like this...
#Takes in a feature vector X and a label vector y and performs gradient boosting on it 
import torch 
import numpy as np 

class GradientBoost():
    def __init__(self):
        self.w = None
    #initalize some weight vector, this will be predicted by thre 
    #Lets think about the vector i should be expecting
    # a bunch of vectors for the images
    # each image gets a vector of features
    # def score(self, X):
    #     #Still needs to get a random score?
    #     #And then do the dot product of score and X vector, perhaps?






    
# Here, we need to compute the loss function
#
    def loss(X):
        #What algorithm are we using, likely to be cross-entropy since this is a binary classification problem
        #First do log odds
        # We are trying to get the average of all the good and bad cases, the same as the mean in a regression problem
        # y such that y = 1 (malignant)
        # malignant = y.float.mean()
        # # y such that y = 0 (benign)
        # benign = 1 - malignant
        # # Then you can get log odds
        # log_odds = log(maligant/benign)
        # prob_malignant = np.exp(log_odds) / (1 + np.exp(log_odds))
        # residual = 
    
