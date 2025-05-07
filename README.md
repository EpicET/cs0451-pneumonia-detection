# cs0451-pneumonia-detection
By Cameron Hudson, Robsan Dinka, Lia Smith, and Emmanuel Towner

## Abstract

This project addresses the problem of automating pneumonia diagnosis using chest X-ray images. We propose a deep learning approach using convolutional and variational autoencoders, along with supervised contrastive learning, to extract meaningful latent representations of X-ray images for disease classification. Our pipeline evaluates the effectiveness of these representations using dimensionality reduction (PCA), logistic regression, and transformer-based classifiers. Success will be measured by classification accuracy and separation of normal vs. pneumonia classes in latent space visualizations.

## Motivation and Question

We have a Kaggle dataset that contains 5,863 X-ray images. The dataset is divided into training and validation folders, within each folder are subfolders correlating to each category (Pneumonia/Normal). These images will be used to train a convolutional neural network (CNN) designed to detect pneumonia in X-ray images. This algorithm could be particularly useful for healthcare applications. In this implementation it makes identifing pneumonia easier and more efficient for doctors. But when expanded upon could possibly make identifying other diseases simpler.

## Planned Deliverables

We will deliver:
* A documented Python package.
* Jupyter notebooks demonstrating model performance, latent space visualizations, and evaluation metrics.

Full Success: We achieve 85%+ classification accuracy on the test set, clear PCA/3D latent space separation of classes, and demonstrate transferability of learned embeddings to multiple classifiers (logistic regression and transformer).

Partial Success: We demonstrate that contrastive VAE representations contain disease-relevant structure, even if classification performance is modest (70–80%).


## Resources Required

Our data is from Kaggle's [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) that our model will be trained on. The tools we will use are PyTorch and Jupyter Notebook.

## What You Will Learn

We all intend to improve our skills using Git version control, improve our teamworking skills, and learn the implementation of a convolutional neural network and its application in healthcare.

Robsan Dinka: Specifically intrested in the math that goes into the implementation of a convolutional neural network, and wants to improve their skills with git command line.

Cameron Hudson: Specifically interested in learning how we will use the algorithm to detect faces in a video stream, how to utilize our laptop's built-in camera and use our algorithm implementation in tandem. 

Emmanuel Towner: Has a high-level understanding of how neural networks work, and is interesting in how convolution neural networks differ from regular neural networks. Also wants to get better at the git command line.

Lia Smith: Has a little experience with convolutional layers but is very excited to work more with them in an unsupervised learning framework. Additionally, is excited in encoding video data. 

## Risk Statement

1. The learned latent features might not provide clear separability between pneumonia and normal cases, limiting classifier performance.

2. High computational requirements for training VAEs and transformers could exceed available resources, especially with cross-validation or hyperparameter tuning.


## Ethics Statement
1. Our model is designed to benefit healthcare professionals and institutions by supporting the early detection of pneumonia from chest X-rays. This can reduce diagnostic delays, improve treatment outcomes, and relieve pressure on radiologists in resource-constrained settings. It may also support telemedicine services in remote or underserved areas.

2. On the other hand, the model may inadvertently harm certain groups if the training data is not sufficiently representative. For instance, if the dataset contains disproportionate samples by age, gender, race, or comorbid conditions, the model may underperform on underrepresented patients. Misdiagnosis due to such bias could lead to inappropriate treatment decisions or missed interventions, especially in clinical settings where human oversight is minimal.

3. While our model is not intended to replace medical professionals, overreliance on AI by non-specialists could lead to misuse or blind trust in algorithmic outputs. Additionally, storing and processing medical imagery introduces risks around data privacy and security, particularly if used in real-world deployments without rigorous compliance with healthcare data regulations (e.g., HIPAA, GDPR).

The following assumptions underlie our ethical stance:

* The model will be deployed as an assistive tool, with final diagnostic decisions made by certified medical professionals.
* The dataset used for training is sufficiently diverse and reflects the populations on which the model will be applied.
* Any real-world deployment of this model will include transparency about its limitations and be subject to continuous validation.
* Patient data used in training and testing has been anonymized and collected with proper consent.




## Tentative Timeline
For Week 3: Implementation of convolutional neural network with the classifiers is in a working, runnable state.

For Week 6: Our implementation of the convolutional neural network is trained on images, and is able to classify pneumonia and non-pneumonia images.
