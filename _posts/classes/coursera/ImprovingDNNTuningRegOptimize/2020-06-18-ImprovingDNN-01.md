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
	- ![](https://drive.google.com/uc?id=1_o-8J9TgML5FBJSV1sz5NovYhGRoqidQ)
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

![](https://drive.google.com/uc?id=1LCGKHHbhAYhXYn1n243ZGJVij8f2nIVC)
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
     ![](https://drive.google.com/uc?id=1yotA-DhpHW4gvB5E7vrBdjOLWGr91UnI)
  - Intuition 2 (with _tanh_ activation function):
     - If `lambda` is too large, w's will be small (close to zero) - will use the linear part of the _tanh_ activation function, so we will go from non linear activation to _roughly_ linear which would make the NN a _roughly_ linear classifier.
     - If `lambda` good enough it will just make some of _tanh_ activations _roughly_ linear which will prevent overfitting.
     ![](https://drive.google.com/uc?id=1waBeWXTlDDMbB_Wl6lNu2U_OakkUM2Ji)

{{site.data.alerts.warning}}
_**Implementation tip**_: if you implement gradient descent, one of the steps to debug gradient descent is to plot the cost function J as a function of the number of iterations of gradient descent and you want to see that the cost function J decreases **monotonically** after every iteration of gradient descent with regularization. If you plot the old definition of J (no regularization) then you might not see it decrease monotonically.
![](![](https://drive.google.com/uc?id=1waBeWXTlDDMbB_Wl6lNu2U_OakkUM2Ji))
{{site.data.alerts.end}}

## Dropout Regularization

- In most cases Andrew Ng tells that he uses the L2 regularization.
- The dropout regularization eliminates some neurons/weights on each iteration based on some probability.
	- > for each training example, you would train it using one of these neural based networks
	- > imagine that because you're training a much smaller network on each example or maybe just give a sense for why you end up able to regularize the network, because these much smaller networks are being trained
- A most common technique to implement dropout is called __"Inverted dropout"__.
- Code for Inverted dropout:

  ```python
  keep_prob = 0.8   # 0 <= keep_prob <= 1
  l = 3  # this code is only for layer 3
  # the generated number that are less than 0.8 will be dropped. 
  # 80% stay, 20% dropped
  # works as well if the implementation is vectorized  
  d3 = np.random.rand(a[l].shape[0], a[l].shape[1]) < keep_prob


  # these are the activations for that layer
  # technically d3 is boolean but when multiplied it becomes 1/0 
  a3 = np.multiply(a3,d3)   # keep only the values in d3

  # increase a3 to not reduce the expected value of output
  # (ensures that the expected value of a3 remains the same) - to solve the scaling problem
  # ex. z[4] = w[4]*a[3] + b[4]
  # if 20% of a[3] is reduced then the expected value of z[4] is also reduced by that amount
  # to increase by 20% then you increase by the prop factor so that the expected value of a[3] remains the same
  # also this makes test time easier
  a3 = a3 / keep_prob       
  ```
- Vector d[l] is used for forward and back propagation and is the same for them, but it is __different for each iteration (pass) or training example__.
- __At test time we don't use dropout__. 
	- If you implement dropout at test time - it would add noise to predictions.

## Understanding Dropout

- In the previous video, the intuition was that dropout randomly knocks out units in your network. So it's as if on every iteration you're working with a smaller NN, and so using a smaller NN seems like it should have a regularizing effect.
- intuition
	- one unit can't rely on any one feature
	- can't rely on any one feature, so have to spread out weights.
	- shrinks the weights
	- adaptive form of L2 reg	
- It's possible to show that dropout has a similar effect to L2 regularization.
	-  > L2 regularization applied to different ways can be a little bit different and even more adaptive to the scale of different inputs
- __Dropout can have different `keep_prob` per layer__.
- The input layer dropout has to be near 1 (or 1 - no dropout) because you don't want to eliminate a lot of features.
- If you're more worried about some layers overfitting than others, you can set a lower `keep_prob` for some layers than others. The downside is, this gives you even more hyperparameters to search for using cross-validation. 
	- for layers that have high connections you want to apply reg more so the probability should be higher.  For instance in the image below w[2] has higher number of weights so you want that to not overfit so you want to increase regularization.  While in places that you don't think the model will overfit you want the prop to be as high as possible.
	- ![](https://drive.google.com/uc?id=1_vPSL35bbNqLUGr7rdbiVAUjx5OPfmzu)
	- this is similar to lambda in L2 reg
- One other alternative might be to have some layers where you apply dropout and some layers where you don't apply dropout and then just have one hyperparameter, which is a `keep_prob` for the layers for which you do apply dropouts.
- A lot of researchers are using dropout with Computer Vision (CV) because they have a very big input size and almost never have enough data, so overfitting is the usual problem. And dropout is a regularization technique to prevent overfitting.

{{site.data.alerts.warning}}
- > unless my algorithm is over-fitting, I wouldn't actually bother to use drop out. 
- > used somewhat less often than other application areas
	- > intuition doesn't always generalize I think to other disciplines
{{site.data.alerts.end}}

- A downside of dropout is that the cost function J is not well defined and it will be hard to debug (plot J by iteration).
  - To solve that you'll need to turn off dropout, set all the `keep_prob`s to 1, and then run the code and check that it monotonically decreases J and then turn on the dropouts again.

## Other regularization methods

- **Data augmentation**:
  - For example in a computer vision data:
    - You can flip all your pictures horizontally this will give you m more data instances.
    	- > training set is now a bit redundant this isn't as good as if you had collected an additional set of brand new independent examples
    - You could also apply a random position and rotation to an image to get more data.
  - For example in OCR, you can impose random rotations and distortions to digits/letters.
  - New data obtained using this technique isn't as good as the real independent data, but still can be used as a regularization technique.

- **Early stopping**:
  - In this technique we plot the training set and the dev set cost together for each iteration. At some iteration the dev set cost will stop decreasing and will start increasing.
  - We will pick the point at which the training set error and dev set error are best (lowest training cost with lowest dev cost).
  - We will take these parameters as the best parameters.
    - ![](![](https://drive.google.com/uc?id=1_vPSL35bbNqLUGr7rdbiVAUjx5OPfmzu))
  - Andrew prefers to use L2 regularization instead of early stopping because this technique simultaneously tries to minimize the cost function and not to overfit which contradicts the orthogonalization approach (will be discussed further).
  	- optimize cost function and not overfit are two separate tasks and should be tackled differently
  	- while you optimize cost function you minimize `J` and when you try not to overfit you increase `generalizability` of the model
  	- this concept of compartmentalizing each task is called `orthogonalizing approach`
  - But its advantage is that you don't need to search a hyperparameter like in other regularization approaches (like `lambda` in L2 regularization).
- **Model Ensembles**:
  - Algorithm:
    - Train multiple independent models.
    - At test time average their results.
  - It can get you extra 2% performance.
  - It reduces the generalization error.
  - You can use some snapshots of your NN at the training ensembles them and take the results.


## Normalizing inputs

- If you normalize your inputs this will speed up the training process a lot.
- Normalization are going on these steps:
  1. Get the mean of the training set: `mean = (1/m) * sum(x(i))`
  2. Subtract the mean from each input: `X = X - mean`
     - This makes your inputs centered around 0.
  3. Get the variance of the training set: `variance = (1/m) * sum(x(i)^2)`
  4. Normalize the variance. `X /= variance`
- These steps should be applied to training, dev, and testing sets (but using mean and variance of the train set).
	- use the values of the training set to the dev and test set when performing normalization so that you scale the train set the same way.  You want the dev and test go through the same way during your train set.
![](https://drive.google.com/uc?id=1TGiMQbVJPAGOBxLExpRAjfskVBfZrA_X)
- Why normalize?
  - If we __don't normalize the inputs our cost function will be deep and its shape will be inconsistent (elongated) then optimizing it will take a long time__.
  	- if you features have various scales then it can be elongated.
  		- a lot of steps to identify min
  	- if normalized then cost function will be more symmetric
  		- take larger steps  	
  - But if we normalize it the opposite will occur. The shape of the cost function will be consistent (look more symmetric like circle in 2D example) and we can use a larger learning rate alpha - the optimization will be faster.
 ![](https://drive.google.com/uc?id=1_vPSL35bbNqLUGr7rdbiVAUjx5OPfmzu)

## Vanishing / Exploding gradients

- The Vanishing / Exploding gradients occurs when your derivatives become very small or very big.
- To understand the problem, suppose that we have a deep neural network with number of layers L, and all the activation functions are **linear** and each `b = 0`
  - Then:   
    ```
    Y' = W[L]W[L-1].....W[2]W[1]X
    ```
  - Then, if we have 2 hidden units per layer and x1 = x2 = 1, we result in:

    ```
    if W[l] = [1.5   0] 
              [0   1.5] (l != L because of different dimensions in the output layer)
    Y' = W[L] [1.5  0]^(L-1) X = 1.5^L 	# which will be very large
              [0  1.5]
    ```
    ```
    if W[l] = [0.5  0]
              [0  0.5]
    Y' = W[L] [0.5  0]^(L-1) X = 0.5^L 	# which will be very small
              [0  0.5]
    ```
- The last example explains that the __activations (and similarly derivatives) will be decreased/increased exponentially as a function of number of layers__.
- So If `W > I` (Identity matrix) the __activation and gradients will explode in a very deep network__.
- And If `W < I` (Identity matrix) the __activation and gradients will vanish with a very deep network__.
- Recently Microsoft trained 152 layers (ResNet)! which is a really big number. With such a deep neural network, if your activations or gradients increase or decrease exponentially as a function of L, then these values could get really big or really small. And this makes training difficult, especially if your gradients are exponentially smaller than L, then gradient descent will take tiny little steps. It will take a long time for gradient descent to learn anything.
- There is a partial solution that doesn't completely solve this problem but it helps a lot - careful choice of how you initialize the weights (next video).


## Weight Initialization for Deep Networks

- A partial solution to the Vanishing / Exploding gradients in NN is better or more careful choice of the random initialization of weights
- In a single neuron (Perceptron model): `Z = w1x1 + w2x2 + ... + wnxn`
  - So if `n_x` is large we want `W`'s to be smaller to not explode the cost.
- So it turns out that we need the variance which equals `1/n_x` to be the range of `W`'s
- So lets say when we initialize `W`'s like this (better to use with `tanh` activation):   
  ```
  np.random.rand(shape) * np.sqrt(1/n[l-1]) 
  ```
  or variation of this (Bengio et al.):   
  ```  
  np.random.rand(shape) * np.sqrt(2/(n[l-1] + n[l]))
  ```
  >  it turns out that sampling a Gaussian random variable and then multiplying it by a square root of this, that sets the variance to be quoted this way, to be 2 over n
- Setting initialization part inside sqrt to `2/n[l-1]` for `ReLU` is better:   
  ```
  np.random.rand(shape) * np.sqrt(2/n[l-1])
  ```
- Number 1 or 2 in the numerator can also be a hyperparameter to tune (but not the first to start with)
	- this can be tuned by adding a multiplier to the numerator and tuning it and seeing the performance
- This is one of the best way of partially solution to Vanishing / Exploding gradients (ReLU + Weight Initialization with variance) which will help gradients not to vanish/explode too quickly
- The initialization in this video is called "He Initialization / Xavier Initialization" and has been published in 2015 paper.

- Relu activation function
	- $$\sqrt{\frac{2}{n^{l-1}}}$$
	- $$\sqrt{\frac{2}{n^{l-1}+n^l}}$$ # bengio
- tanh activation function
	- - $$\sqrt{\frac{12}{n^{l-1}}}$$ # xavier

## Numerical approximation of gradients

- There is an technique called gradient checking which tells you if your implementation of backpropagation is correct.
- There's a numerical way to calculate the derivative:   
  ![](Images/03-_Numerical_approximation_of_gradients.png)
- __Gradient checking approximates the gradients and is very helpful for finding the errors in your backpropagation implementation but it's slower than gradient descent (so use only for debugging)__.


## Gradient checking
- Implementation of this is very simple.
- Gradient checking:
  - First take `W[1],b[1],...,W[L],b[L]` and reshape into one big vector (`theta`)
  - The cost function will be `J(theta)`
  - Then take `dW[1],db[1],...,dW[L],db[L]` into one big vector (`d_theta`)
  - **Algorithm**:   
    ```
    eps = 10^-7   # small number
    for i in len(theta):
      d_theta_approx[i] = (J(theta1,...,theta[i] + eps) -  J(theta1,...,theta[i] - eps)) / 2*eps
    ```  
  - Finally we evaluate this formula `(||d_theta_approx - d_theta||) / (||d_theta_approx||+||d_theta||)` (`||` - Euclidean vector norm) and check (with eps = 10^-7):
    - __if it is < 10^-7  - great__, very likely the backpropagation implementation is correct
    - __if around 10^-5   - can be OK__, but need to inspect if there are no particularly big values in `d_theta_approx - d_theta` vector
    - __if it is >= 10^-3 - bad__, probably there is a bug in backpropagation implementation
    	- check which value of `i` is correct and then based on that `i` you can go backwards

## Gradient checking implementation notes
- Don't use the gradient checking algorithm at training time because it's very slow.
	- __Use gradient checking only for debugging__.
- If algorithm fails grad check, look at components to try to identify the bug.
- Don't forget to add `lamda/(2m) * sum(W[l])` to `J` if you are using L1 or L2 regularization.
- __Gradient checking doesn't work__ with dropout because J is not consistent. 
  - You can first turn off dropout (set `keep_prob = 1.0`), run gradient checking and then turn on dropout again.
  - > turns out that dropout can be viewed as optimizing some cost function J, but it's cost function J defined by summing over all exponentially large subsets of nodes they could eliminate in any iteration
  - > the cost function J is very difficult to compute, and you're just sampling the cost function every time you eliminate different random subsets in those we use dropout
- Run gradient checking at random initialization and train the network for a while maybe there's a bug which can be seen when w's and b's become larger (further from 0) and can't be seen on the first iteration (when w's and b's are very small).