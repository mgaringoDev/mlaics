---
title:  02 - Neural Networks Basics
author:     Mario Garingo
keywords: deepLearningSpecialization, nndl
summary: Learn to set up a machine learning problem with a neural network mindset. Learn to use vectorization to speed up your model.
category: coursera
type: notes
sidebar: coursera_sidebar
gDrivePDFile: 1XckExNX-QXsqiG1dD9Q7C7X4zfx9vHpJ
---

## Binary Classification
![](https://drive.google.com/uc?id=1RQfj_wP6NdLw2aTJ2Vpd8_MkQbe-1SBW)
- Given an image
	- each image consists of RGB channel and each channel is a matrix whose size is the image size
	- to create a feature vector we take each channel vecotrize it by taking the rows and concatinating them and then concatinating the channels together
		- if the image is 64x64 then the final feature vector will be 64x64x3

## Notation
![](https://drive.google.com/uc?id=1k5tMu0z07q3SAv30ilnvabvUBr_MEV7M)
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

### Why this Cost Function?
By minimizing this cost function J(w,b) we're really carrying out maximum likelihood estimation with the logistic regression model. Under the assumption that our training examples were IID, or identically independently distributed. Check the written notes below for a full derivation.  

### Gradient Descent
Look at my notes on this as well. To sum it up, go opposite of the direction of the derivative of the cost function and take a step defined by the learning rate.  

### Computation Graphs
In many cases you always want to find to find the derivative of the cost function w.r.t to some sort of variable.  Usually one of the input variables or one of the intermediate variables.  In the example in the notes, to back propagate from ```J``` to ```a``` we first take the derivative of ```J``` w.r.t ```v``` then with ```a```.  In computational graphs you can do it one step at a time but in calculus this is just the chain rule.  Follow calc rules because to me that is more intuitive, until of course the computational graphs become easier to understand.

![](https://drive.google.com/uc?id=1prvTcMBdAG4f5A_bY_PACo6b_-u19iwC)
![](https://drive.google.com/uc?id=1-W3A6jex1pbrSUIr6RGS3CzSSOYUK294)
{{site.data.alerts.note}}

-  quotes and in red are suggested var names in python when implementing
- the derivative of s sigmoid function can be found [here](https://bit.ly/2A7PPpo)
- the derivations in this note can be found in the [datahackers](http://datahacker.rs/computation-graph/)

{{site.data.alerts.end}}

## Forward Prop
![](https://drive.google.com/uc?id=12OFOYo2OGjpbzHiQqtSnPi158puM0ge6)

## Backwards Prop
![](https://drive.google.com/uc?id=1lSgwCHO-B2dGiSJP2rXpK_H6dm6pnkkk)