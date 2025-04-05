# cs0451-facial-detection
By Cameron Hudson, Robsan Dinka, and Emmanuel Towner

## Abstract


The problem we are attempting to solve is the improvement of automated security systems using facial detection. There are alot of security usages for being able to detect faces in images and video streams, such as detecting when a person is in an unauthorized area, home security and more. The approach we are doing to solve this problem is to create and train machine learning algorithm to detect faces in images, and learn how to integrate this algorithm in face detection in video streams. To assess the model's accuracy, we will make a train-test split on our data and  will be looking for 80-85% accuracy on testing data. 


## Motivation and Question

We have a dataset that contains facial and non-facial images. These will be used to train a neural network that can identify
faces in images and webcams which will be useful security devices.

## Planned Deliverables

Full success: In a full success scenario, we will deliver a real-time image detection algorithm, which can utilize a camera to detect and trace a face within a video stream.

Partial success: In a partial success scenario. Our algorithm will be able to classify images as containing or not containing a face with 80-85% accuracy.

## Resources Required

Our data is from Kaggle's [Face-Detection-Dataset](https://www.kaggle.com/datasets/fareselmenshawii/face-detection-dataset) that our model will be train on. The libraries we will use are PyTorch and Jupyter Notebook.

## What You Will Learn
We all intend to improve our skills using Git version control, improve our teamworking skills, and learn the implementation of a convolutional neural network and
its application in facial detection.

Robsan Dinka: Specifically intrested in the math that goes into the implementation of a convolutional neural network, and wants to improve their skills with git command line. 
Cameron Hudson: Specifically interested in learning how we will use the algorithm to detect faces in a video stream, how to utilize our laptop's built-in camera and use our algorithm implementation in tandem. 
Emmanuel Towner: Has a high-level understanding of how neural networks work, and is interesting in how convolution neural networks differ from regular neural networks. Also wants to get better at the git command line.



## Risk Statement

1. The process to transform our static image algorithm to utilize webcams may be more involved than intially thought.
2. There is a risk that data has very homogenous facial images therefore making it unsuccessful in identifying diverse groups of people. 

## Ethics Statement
Using our facial detection system, we will be able to detect faces in images and videos. This can be used for various purposes, such as security, surveillance, and even social media applications. Our model will be able to detect faces in real-time, which can be useful for video conferencing and live streaming. However, we must be cautions that our model is not used to violate privacy by collecting data without consent. Overall, our model will be more useful than harmful, as it can be used to improve security and enhance user experience in various applications.

While making this project, we are assuming that people who use our model will do so ethically and responsibly. Another assumption that we are making is that our model will be able to detect faces accurately reguardless of lighting, race, and other factors. 

1. The biggest benefactors are commercial companies, as they could use the model to provide additional security to their services. Customers are also potential benefactors as their data might be more secure. 


## Tentative Timeline
For Week 3: Implementation of convolutional neural network is in a working, runnable state.

For Week 6: Our implementation of the convolutional neural network is trained on images, and able to classify images in pictures and video streams.
