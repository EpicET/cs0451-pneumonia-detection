# cs0451-facial-detection
By Cameron Hudson, Robsan Dinka, and Emmanuel Towner

## Abstract
The problem we are attempting to solve is the improvement of automated security systems using facial detection. There are alot of security usages for being able to detect faces in images and video streams, such as detecting when a person is in an unauthorized area, home security and more.The approach we are doing to solve this problem is to implement a Convolutional Neural Network and train it on a face detection dataset. To assess the model's accuracy, we will be looking for 80-85% accuracy on testing data. 

## Motivation and Question

There are many ways traditional password systems can get stolen and grant hackers unauthorized access to our private information and assets. Therefore, another method of security is necessary, such as biometrics. We have a dataset of images that contain faces and images that do not contain faces. These will be used to implement a neural network that can identify faces in images and webcams which will be useful implementing biometric security.

## Planned Deliverables

Full success: In a full success scenario, we will deliver a real-time image detection algorithm, which can utilize a camera to detect and trace a face within a video stream.

Partial success: In a partial success scenario. Our algorithm will be able to classify images as containing or not containing a face with 80-85% accuracy.

## Resources Required

Our data is from Kaggle's [Face-Detection-Dataset](https://www.kaggle.com/datasets/fareselmenshawii/face-detection-dataset) that our model will be train on. The libraries we will use are PyTorch, Jupyter Notebook, and OpenCV.

## What You Will Learn
We all intend to improve our skills using Git version control, improve our teamworking skills, and learn the implementation of a convolutional neural network and
its application in facial detection.

Robsan Dinka: Specifically intrested in the math that goes into the implementation of a convolutional neural network, and wants to improve their skills with git command line. 
Cameron Hudson: Specifically interested in learning how we will use the algorithm to detect faces in a video stream, how to utilize our laptop's built-in camera and use our algorithm implementation in tandem. 
Emmanuel Towner: Has a high-level understanding of how neural networks work, and is interesting in how convolution neural networks differ from regular neural networks. Also wants to get better at the git command line.


1. Emmanuel Towner: Learn how to create a CNN and use a webcam for facial recognition.

## Risk Statement

1. We may not have the computational power to train and test our model efficiently.
2. The process to transform our static image algorithm to utilize webcams may be more involved than intially thought.

## Ethics Statement

1. The biggest benefactors are commercial companies, as they could use the model to provide additional security to their services. Customers are also potential benefactors as their data might be more secure. 

## Tentative Timeline
