# cs0451-pneumonia-detection
By Cameron Hudson, Robsan Dinka, Lia Smith, and Emmanuel Towner

## Abstract
[Our-Project](https://github.com/EpicET/cs0451-pneumonia-detection)
Within our blog post, we created a neural network and implemented three different binary classifers trained on chest x-ray image data to detect pneumonia based on images. We used convolution layers to convert images into latent vectors by which we could feed into our various machine learning models: a transformer, an SVM, and a gradient boosting model. Through analyzing the accuracy of each model, we discovered a similar accuracy between the models of around 75% on testing data.

## Introduction

## Values Statement
Our project at its finished state will include a documented python package containing the code for the implementation and analysis of our convolutional neural network and camera integration, as well as a jupyter netwoork illustrating our codes usage.

Full success: In a full success scenario, we will deliver a real-time image detection algorithm, which can utilize a camera to detect and trace a face within a video stream.

Partial success: In a partial success scenario. Our algorithm will be able to classify images as containing or not containing a face with 80-85% accuracy.

model fairness: evaluating the fairness of the model via false positive rates and sufficiency of factors such as race.

## Resources Required

Our data is from Kaggle's [Chest X-Ray Images (Pneumonia) Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) that our model will be trained on. The tools we will use are PyTorch and Jupyter Notebook.

## What You Will Learn

We all intend to improve our skills using Git version control, improve our teamworking skills, and learn the implementation of a convolutional neural network and
its application in facial detection.

Robsan Dinka: Specifically intrested in the math that goes into the implementation of a convolutional neural network, and wants to improve their skills with git command line.

Cameron Hudson: Specifically interested in learning how we will use the algorithm to detect faces in a video stream, how to utilize our laptop's built-in camera and use our algorithm implementation in tandem. 

Emmanuel Towner: Has a high-level understanding of how neural networks work, and is interesting in how convolution neural networks differ from regular neural networks. Also wants to get better at the git command line.

Lia Smith: has a little experience with convolutional layers but is very excited to work more with them in an unsupervised learning framework. Additionally, is excited in encoding video data. 

## Risk Statement

1. Transforming our static image algorithm to work with webcams may be more complex than we originally anticipated.  
2. There is a risk that the data consists of very homogeneous facial images, which could hinder our ability to accurately identify diverse groups of people 

## Ethics Statement
1. Our model will benefit companies involved in home security, surveillance, and even social media platforms. These companies can use our model to enhance their security systems which will make homeowners feel more secure. For example, home security companies can use our model to detect intruders in real-time and alert homeowners. Social media platforms can use our model to enhance user experience by providing filters and effects that modify faces in images and videos.
2. On the other hand, our model may exclude benefit or even harm marginalized groups, general public, and activists. For example, our model may have higher error rates for marginalized groups if our training data is not reflective of the population it is used on. Additionally, our model may be used to collect data on individuals without their consent, violating their privacy. This can be especially harmful for activists and protesters who may be targeted by law enforcement agencies.
3. There are many applications of facial detection systems such as facial recognition, photo filters, surveillance and more. Overall, our model will be more beneficial than harmful, because it will improve security. However, we must be cautious about the ethical implications because it can be used to violate privacy. We believe that the increased security our model brings outweighs the potential harm caused by enhanced by facial data collection. 

The following are assumptions that we have made while doing this project:
* People who use our model will do so ethically and responsibly (ie. no data collection without consent, no tracking, respect privacy, etc.)
* Our model will be able to detect faces accurately regardless of race, gender, lighting, and other factors.
* The cameras capture clear images and videos.
* The data used to train our model is diverse and representative of the population it is being used on




## Tentative Timeline
For Week 3: Implementation of convolutional neural network is in a working, runnable state.

For Week 6: Our implementation of the convolutional neural network is trained on images, and able to classify images in pictures and video streams.
