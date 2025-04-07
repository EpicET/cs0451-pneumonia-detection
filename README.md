# cs0451-facial-detection
By Cameron Hudson, Robsan Dinka, and Emmanuel Towner

## Abstract

The problem we are attempting to solve is the improvement of automated security systems using facial detection. There are alot of security usages for being able to detect faces in images and video streams, such as detecting when a person is in an unauthorized area, home security and more. The approach we are doing to solve this problem is to create and train machine learning algorithm to detect faces in images, and learn how to integrate this algorithm in face detection in video streams. To assess the model's accuracy, we will make a train-test split on our data and  will be looking for 80-85% accuracy on testing data. 


## Motivation and Question

We have a dataset that contains facial and non-facial images. These will be used to train a neural network that can identify
faces in images and webcams which will be useful security devices.

## Planned Deliverables
Our project at its finished state will include a documented python package containing the code for the implementation and analysis of our convolutional neural network and camera integration, as well as a jupyter netwoork illustrating our codes usage.

Full success: In a full success scenario, we will deliver a real-time ilmage detection algorithm, which can utilize a camera to detect and trace a face within a video stream.

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
