---
title:  02 - Neural Networks Basics
author:     Mario Garingo
keywords: deepLearningSpecialization, nndl
summary: Learn to set up a machine learning problem with a neural network mindset. Learn to use vectorization to speed up your model.
category: coursera
type: notes
sidebar: coursera_sidebar
---

## Binary Classification
![](binaryCalc)
- Given an image
	- each image consists of RGB channel and each channel is a matrix whose size is the image size
	- to create a feature vector we take each channel vecotrize it by taking the rows and concatinating them and then concatinating the channels together
		- if the image is 64x64 then the final feature vector will be 64x64x3

## Notation
![](notation)
- training example
	- $$ (x,y) ; x \in  {\rm I\!R}^{n_x} , y \in {0,1}$$ 
	- ```n``` here is the size of the feature vector
- training sets
	- ```m``` will denote training set
	- sometimes it will be $$m_{train}$$
- feature matrix
	- ```X``` capital letter for matrix
	- horizontal concat of the training examples
	- the size would be [m,n]
	- in python this would be 

	```python
	X.shape = (n_x,m)
	```

- output vector
	- ```Y``` in some cases this is ```y``` representing a vector
	- $$ y \in  {\rm I\!R}^{1 x m}$$ 

	```python
	Y.shape = (1,m)
	```

## Logistic Regression
This is similar to the logistic regression notes that I did but with a different cost function.  In this case the cost function is defined by

$$loss(y\hat,y) = -(ylog(y\hat) + (1-y)log(1-y\hat))$$

Often using logistic regression they do not use the sum of squared errors because it doesn't produce a convex function but rather a function with various min and max producing sub-optimal results for minimizing the loss function.  When using gradient descent to update the weights the algo may not converge.  The above loss function will give us a convex function, when performing gradient descent.

### Gradient Descent
Look at my notes on this as well. To sum it up, go opposite of the direction of the derivative of the cost function and take a step defined by the learning rate.

### Computation Graphs




