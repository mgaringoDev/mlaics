---
title:  01 - Practical aspects of Deep Learning
author:     Mario Garingo
keywords: deepLearningSpecialization, tuningDNN
summary: DNN in a practical mindset
category: coursera
type: notes
sidebar: coursera_sidebar
---

## Setting up your Machine Learning Application

### Train / Dev / Test sets

- Its impossible to get all your hyperparameters right on a new application from the first time.
- So the idea is you go through the loop: `Idea ==> Code ==> Experiment`.
	- > intuitions from one domain or from one application area often do not transfer to other application areas.
	- > best choices may depend on the amount of data you have, the number of input features you have through your computer configuration and whether you're training on GPUs or CPU
	- > even very 
- You have to go through the loop many times to figure out your hyperparameters.
	- the goal is to go through this iterative process as efficiently as possible.
- Your data will be split into three parts:
	- Training set.       (Has to be the largest set)
	- Hold-out cross validation set / Development or "dev" set.
	- Testing set. (used to determine unbiased estimate of how well your algorithm is doing )	
- You will try to build a model upon training set then try to optimize hyperparameters on dev set as much as possible. Then after your model is ready you try and evaluate the testing set.
- so the trend on the ratio of splitting the models:
	- If size of the  dataset is 100 to 1000000  ==> 60/20/20 __old practices__
	- If size of the  dataset is 1000000  to INF  ==> 98/1/1 or  99.5/0.25/0.25 __modern practices__
		- reasoning is that you 1% can be 10,000 samples which is good enough to get an idea of what is happening and then test on another 10,000 samples
- The trend now gives the training data the biggest sets.
- __Make sure the dev and test set are coming from the same distribution.__
	- For example if cat training pictures is from the web and the dev/test pictures are from users cell phone they will mismatch. It is better to make sure that dev and test set are from the same distribution.
		-  webpages have very high resolution, very professional, very nicely framed pictures of cats
		-  users are uploading blurrier, lower res images just taken with a cell phone camera in a more casual condition
- The dev set rule is to try them on some of the good models you've created.
- Its OK to only have a dev set without a testing set. But a lot of people in this case call the dev set as the test set. A better terminology is to call it a dev set as its used in the development.
	- overfitting to the test set but this is okay the larger the dataset
	- >  more efficiently measure the bias and variance of your algorithm so you can more efficiently select ways to improve your algorithm

## Bias / Variance (Trade off)

- Bias / Variance techniques are Easy to learn, but difficult to master.
- So here the explanation of Bias / Variance:
	- If your model is underfitting (logistic regression of non linear data) it has a "high bias"
	- If your model is overfitting then it has a "high variance"
	- Your model will be alright if you balance the Bias / Variance
	- For more:
	- ![](biasVariance)
	- Higher dimension it is very hard to tell if you have under or overfitting
- Another idea to get the bias /  variance if you don't have a 2D plotting mechanism:
	- __High variance (overfitting)__ for example:	
		- Training error: 1%
		- Dev error: 11%
		- fitting to the training set but not to well to the dev set
	- __high Bias (underfitting)__ for example:
		- Training error: 15%
		- Dev error: 14%
		- generalizing pretty well because training and testing is pretty much the same
	- __high Bias (underfitting) && High variance (overfitting)__ for example:
		- Training error: 15%
		- Test error: 30%		
	- Best:
		- Training error: 0.5%
		- Test error: 1%
		- relatively good results for training and testing set. This is ideal
	- These Assumptions came from that human has 0% error. If the problem isn't like that you'll need to use human error as baseline.
		- you need to look at __Bayes Error__ as well if human error is not known

- > looking at your training set error you can get a sense of how well you are fitting, at least the training data, and so that tells you if you have a bias problem
-  >  looking at how much higher your error goes, when you go from the training set to the dev set, that should give you a sense of how bad is the variance problem, so you'll be doing a good job generalizing from a training set to the dev set, that gives you sense of your variance
- bais problem comes from training set error
- variance problem comes from dev set error

![](highBiasHighVar)
- in higher dimensional inputs you often see things like this even though in 2D it looks too contrived 

## Basic Recipe for Machine Learning
- first ask high bias?
	- look at training data
	- y?
		- bigger network (usually works)
		- bigger units
		- train longer
		- different NN architecture
	- do this until high bias disappears meaning your train set is as low as possible comparable to the bayes error.

- do you have high variance?
	- look at dev set
	- y?
		- more data
		- regularization
		- different NN architecture

- If your algorithm has a high bias:
	- Try to make your NN bigger (size of hidden units, number of layers)
	- Try a different model that is suitable for your data.
	- Try to run it longer.
	- Different (advanced) optimization algorithms.

- If your algorithm has a high variance:
	- More data.
	- Try regularization.
	- Try a different model that is suitable for your data.

- if you have high bias increasing the data does not help 

- You should try the previous two points until you have a low bias and low variance.

- In the older days before deep learning, there was a "Bias/variance tradeoff". But because now you have more options/tools for solving the bias and variance problem independently its really helpful to use deep learning.

- Training a bigger neural network never hurts.
	- main cost is just computation time as long as you are regularizing

- one of the big reasons that DNN is very efficient in supervised learning
	- bigger network -> reduce high bias so long as you regularize it
	- bigger data -> reduce variance and doesn't hurt your bias much

## Regularization

- This is the answer to the high variance problem

- Adding regularization to NN will help it reduce variance (overfitting)
- L1 matrix norm:
  - `||W|| = Sum(|w[i,j]|)  # sum of absolute values of all w`
- L2 matrix norm because of arcane technical math reasons is called Frobenius norm:
  - `||W||^2 = Sum(|w[i,j]|^2)	# sum of all w squared`
  - Also can be calculated as `||W||^2 = W.T * W if W is a vector`
- Regularization for logistic regression:
  - The normal cost function that we want to minimize is: `J(w,b) = (1/m) * Sum(L(y(i),y'(i)))`
  - The L2 regularization version: `J(w,b) = (1/m) * Sum(L(y(i),y'(i))) + (lambda/2m) * Sum(|w[i]|^2)`
  - The L1 regularization version: `J(w,b) = (1/m) * Sum(L(y(i),y'(i))) + (lambda/2m) * Sum(|w[i]|)`
  - The L1 regularization version makes a lot of w values become zeros, which makes the model size smaller.
  - L2 regularization is being used much more often.
  - `lambda` here is the regularization parameter (hyperparameter)
- Regularization for NN:
  - The normal cost function that we want to minimize is:   
    `J(W1,b1...,WL,bL) = (1/m) * Sum(L(y(i),y'(i)))`

  - The L2 regularization version which is technically the Frobenius norm:   
    `J(w,b) = (1/m) * Sum(L(y(i),y'(i))) + (lambda/2m) * Sum((||W[l]||^2)`

  - We stack the matrix as one vector `(mn,1)` and then we apply `sqrt(w1^2 + w2^2.....)`

  - To do back propagation (old way):   
    `dw[l] = (from back propagation)`

  - The new way:   
    `dw[l] = (from back propagation) + lambda/m * w[l]`

  - So plugging it in weight update step:

    - ```
      w[l] = w[l] - learning_rate * dw[l]
           = w[l] - learning_rate * ((from back propagation) + lambda/m * w[l])
           = w[l] - (learning_rate*lambda/m) * w[l] - learning_rate * (from back propagation) 
           = (1 - (learning_rate*lambda)/m) * w[l] - learning_rate * (from back propagation)
      ```

  - In practice this penalizes large weights and effectively limits the freedom in your model.

  - The new term `(1 - (learning_rate*lambda)/m) * w[l]`  causes the **weight to decay** in proportion to its size. This is the reason why sometimes this is called __weight decay__

## Why regularization reduces overfitting?

Here are some intuitions:
  - Intuition 1:
     - If `lambda` is too large - a lot of w's will be close to zeros which will make the NN simpler (you can think of it as it would behave closer to logistic regression).     	
     - If `lambda` is good enough it will just reduce some weights that makes the neural network overfit.
     ![](regIntuition)
  - Intuition 2 (with _tanh_ activation function):
     - If `lambda` is too large, w's will be small (close to zero) - will use the linear part of the _tanh_ activation function, so we will go from non linear activation to _roughly_ linear which would make the NN a _roughly_ linear classifier.
     - If `lambda` good enough it will just make some of _tanh_ activations _roughly_ linear which will prevent overfitting.
     ![](regIntuitionTanh)

{{site.data.alerts.warning}}
_**Implementation tip**_: if you implement gradient descent, one of the steps to debug gradient descent is to plot the cost function J as a function of the number of iterations of gradient descent and you want to see that the cost function J decreases **monotonically** after every iteration of gradient descent with regularization. If you plot the old definition of J (no regularization) then you might not see it decrease monotonically.
![](decreaseMonotonicallyJ)
{{site.data.alerts.end}}

## Dropout Regularization

- In most cases Andrew Ng tells that he uses the L2 regularization.
- The dropout regularization eliminates some neurons/weights on each iteration based on some probability.
- A most common technique to implement dropout is called "Inverted dropout".
- Code for Inverted dropout:

  ```python
  keep_prob = 0.8   # 0 <= keep_prob <= 1
  l = 3  # this code is only for layer 3
  # the generated number that are less than 0.8 will be dropped. 80% stay, 20% dropped
  d3 = np.random.rand(a[l].shape[0], a[l].shape[1]) < keep_prob

  a3 = np.multiply(a3,d3)   # keep only the values in d3

  # increase a3 to not reduce the expected value of output
  # (ensures that the expected value of a3 remains the same) - to solve the scaling problem
  a3 = a3 / keep_prob       
  ```
- Vector d[l] is used for forward and back propagation and is the same for them, but it is different for each iteration (pass) or training example.
- At test time we don't use dropout. If you implement dropout at test time - it would add noise to predictions.