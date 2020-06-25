---
title:  03 - Hyperparameter tuning Batch Normalization and Programming Frameworks
author:     Mario Garingo
keywords: deepLearningSpecialization, tuningDNN
summary: Techniques to tune hyperparameters
category: coursera
type: notes
sidebar: coursera_sidebar
---

## Tuning process

- We need to tune our hyperparameters to get the best out of them.
- Hyperparameters importance are (as for Andrew Ng): __Ordered by importance__
  1. Learning rate.
  2. Momentum beta. `0.9` is a good default
  3. Mini-batch size.
  4. No. of hidden units.
  5. No. of layers.
  6. Learning rate decay.
  7. Adam `beta1`, `beta2` & `epsilon`. `0.9` `0.999` `10^-8`
  8. Regularization lambda.
  9. Activation functions.
- __Its hard to decide which hyperparameter is the most important in a problem. It depends a lot on your problem.__
- One of the ways to tune is to sample a grid with `N` hyperparameter settings and then try all settings combinations on your problem.
- Try random values: don't use a grid.
	- richly sample the search space
![](https://drive.google.com/uc?id=1q9qKXsf6aHsK7YtNerH3lOJHVbHNAgQC)
- You can use `Coarse to fine sampling scheme`:
  	- When you find some hyperparameters values that give you a better performance 
  		- zoom into a smaller region around these values and sample more densely within this space.
![](https://drive.google.com/uc?id=1e__QY3IcE6hmxljrZg55iFSjdi_0iFFw)
- These methods can be automated.

## Using an appropriate scale to pick hyperparameters

- >  sampling at random doesn't mean sampling uniformly at random, over the range of valid values. Instead, it's important to pick the appropriate scale on which to explore the hyperparamaters.

![](https://drive.google.com/uc?id=1UqSy2RCQgafF1tskxO3keN4IErYGB5bY)
- Let's say you have a specific range for a hyperparameter from "a" to "b". It's better to search for the right ones using the logarithmic scale rather then in linear scale:
  - Calculate: `a_log = log(a)  # e.g. a = 0.0001 then a_log = -4`
  - Calculate: `b_log = log(b)  # e.g. b = 1  then b_log = 0`
  - Then:
    ```
    r = (a_log - b_log) * np.random.rand() + b_log
    # In the example the range would be from [-4, 0] because rand range [0,1)
    result = 10^r
    ```
    __It uniformly samples values in log scale from [a,b]__.
- If we want to use the last method on exploring on the "momentum beta":
  - Beta best range is from 0.9 to 0.999.
  - You should search for `1 - beta in range 0.001 to 0.1 (1 - 0.9 and 1 - 0.999)` and the use `a = 0.001` and `b = 0.1`. Then:
    ```
    a_log = -3
    b_log = -1
    r = (a_log - b_log) * np.random.rand() + b_log
    beta = 1 - 10^r   # because 1 - beta = 10^r
    ```
  - >  in that this way, you spend as much resources exploring the range 0.9 to 0.99, as you would exploring 0.99 to 0.999
  - > So what this whole sampling process does, is it causes you to sample more densely in the region of when beta is close to 1

## Hyperparameters tuning in practice: Pandas vs. Caviar 

- > one nice development in deep learning is that people from different application domains do read increasingly research papers from other application domains to look for inspiration for cross-fertilization.
- Intuitions about hyperparameter settings from one application area may or may not transfer to a different one.
- If you don't have much computational resources you can use the `babysitting model`:
  - > this if you have maybe a huge data set but not a lot of computational resources, not a lot of CPUs and GPUs, so you can basically afford to train only one model or a very small number of models at a time
  - Day 0 you might initialize your parameter as random and then start training.
  - Then you watch your learning curve gradually decrease over the day.
  - And __each day you nudge your parameters a little during training__.
    - __Called panda approach__.
    - one child at a time for pandas and take care of them
- If you have enough computational resources, you can __run some models in parallel and at the end of the day(s) you check the results__.
  - __Called Caviar approach__.
  - fish reproduction and don't pay too much attention for one of them and then the best one survives
![](https://drive.google.com/uc?id=1n3xtPD5Y4C3MJZ7ymRCwJ10490l4D54L)
- larger dataset you tend to use panda approach because too large to train entire dataset
- > if you have enough computers to train a lot of models in parallel, then by all means take the caviar approach and try a lot of different hyperparameters and see what works

## Normalizing activations in a network

- In the rise of deep learning, one of the most important ideas has been an algorithm called **batch normalization**, created by two researchers, Sergey Ioffe and Christian Szegedy.
- Batch Normalization speeds up learning.
- Before we normalized input by subtracting the mean and dividing by variance. This helped a lot for the shape of the cost function and for reaching the minimum point faster.
- The question is: *for any hidden layer can we normalize `A[l]` to train `W[l+1]`, `b[l+1]` faster?* This is what batch normalization is about.
- There are some debates in the deep learning literature about whether you should normalize values before the activation function `Z[l]` or after applying the activation function `A[l]`. __In practice, normalizing `Z[l]` is done much more often__ and that is what Andrew Ng presents.
- Algorithm:
  - Given `Z[l] = [z(1), ..., z(m)]`, i = 1 to m (for each input)
    - the following computation is for some layer `l`
  - Compute `mean = 1/m * sum(z[i])`
  - Compute `variance = 1/m * sum((z[i] - mean)^2)`
  - Then `Z_norm[i] = (z[i] - mean) / np.sqrt(variance + epsilon)` (add `epsilon` for numerical stability if variance = 0)
    - Forcing the inputs to a distribution with zero mean and variance of 1.
  - Then `Z_tilda[i] = gamma * Z_norm[i] + beta`
    - To make inputs belong to other distribution (with other mean and variance).
    - gamma and beta are learn-able parameters of the model.
      - you need to update gamma and beta just as you would update the weights of your NN
    - Making the NN learn the distribution of the outputs.
      - > notice that the effect of gamma and beta is that it allows you to set the mean of z tilde to be whatever you want it to be
      - >  if gamma equals square root sigma squared plus epsilon, so if gamma were equal to this denominator term
      - > beta were equal to mu, so this value up here, then the effect of gamma z norm plus beta is that it would exactly invert this equation
    - _Note:_ if `gamma = sqrt(variance + epsilon)` and `beta = mean` then `Z_tilda[i] = z[i]`
- > difference between the training input and these hidden unit values is you might not want your hidden unit values be forced to have mean 0 and variance 1
- > might want them to have a larger variance or have a mean that's different than 0, in order to better take advantage of the nonlinearity of the sigmoid function rather than have all your values be in just this linear region
- >  that's why with the parameters gamma and beta, you can now make sure that your zi values have the range of values that you want
![](https://drive.google.com/uc?id=1-oDPx1qR6EYpBwQZ8eCK4Ev-iKeWzI0A)

## Fitting Batch Normalization into a neural network

- Using batch norm in 3 hidden layers NN:
    ![](https://drive.google.com/uc?id=119dLxv9Qa9aDScTVWxqDj_ftviKMOn3H)
  - the bn happens in between computing Z and A in a neuron
- Our NN parameters will be:
  - `W[1]`, `b[1]`, ..., `W[L]`, `b[L]`, `beta[1]`, `gamma[1]`, ..., `beta[L]`, `gamma[L]`
  - `beta[1]`, `gamma[1]`, ..., `beta[L]`, `gamma[L]` are updated using any optimization algorithms (like GD, RMSprop, Adam)
- If you are using a deep learning framework, you won't have to implement batch norm yourself:
  - Ex. in Tensorflow you can add this line: `tf.nn.batch-normalization()`
- __Batch normalization is usually applied with mini-batches__.


- If we are using batch normalization parameters `b[1]`, ..., `b[L]` doesn't count because they will be eliminated after mean subtraction step, so:
  ```
  Z[l] = W[l]A[l-1] + b[l] => Z[l] = W[l]A[l-1]
  Z_norm[l] = ...
  Z_tilde[l] = gamma[l] * Z_norm[l] + beta[l]
  ```
  - > Batch Norm zeroes out the mean of these ZL values in the layer, there's no point having this parameter BL, and so you must get rid of it, and instead is sort of replaced by Beta L, which is a parameter that controls that ends up affecting the shift or the biased terms
  - Taking the mean of a constant `b[l]` will eliminate the `b[l]`
    - any constant that you add will get canceled out by the mean and subtraction step of BN
  - intuition is that `b[l]` is y intercept but because we are normalizing `b[l]` will be zeros.  Your moving the distribution symmetrically over the origin.
- So if you are using batch normalization, you can remove b[l] or make it always zero.
![](https://drive.google.com/uc?id=1cmFuh1itCD9SwRCRyZ_CX03tCTe7rzBJ)
{{site.data.alerts.warning}}
- So the parameters will be `W[l]`, `beta[l]`, and `alpha[l]`.
- Shapes:
  - `Z[l]       - (n[l], m)`
  - `beta[l]    - (n[l], m)`
  - `gamma[l]   - (n[l], m)`
{{site.data.alerts.end}}

Pseudocode:
```
for t=1 .... numMiniBact
  compute forward propr on X{t}
    in each hidden layer, use BN to replace z[l] with z_tilda[l] to obtain a[l]
  compute back prop to compute dW[l] dBeta[l] dGamma[l]
  update parameters W beta gamma 
    using GD, momentum, adam
``` 


## Why does Batch normalization work?
- reasoning:
  - `covariate shift`
    - > if you've learned some X to Y mapping, if the distribution of X changes, then you might need to retrain your learning algorithm. 
    - >  if the function, the ground true function, mapping from X to Y, remains unchanged, which it is in this example, because the ground true function is, is this picture a cat or not
![](https://drive.google.com/uc?id=1xtqjAoe8iPedxkYsmrxJDR9xJfaxCDlT)

- The __first reason is the same reason as why we normalize X__.
  - each layer treats the previous layer as input layer similar to X. 
  - > what batch norm does, is it reduces the amount that the distribution of these hidden unit values shifts around
  - recall that we normalize Z and not A because we want some nonlinear activation instead of consistently applying a particular mean and variance.
  - > it limits the amount to which updating the parameters in the earlier layers can affect the distribution of values that the third layer now sees and therefore has to learn on.
  - > reduces the coupling of each layer
  - > it allows each layer of the network to learn by itself, a little bit more independently of other layers, and this has the effect of speeding up of learning in the whole network
![](https://drive.google.com/uc?id=1zpHcJ5yniAJ-RE1FSKeG27LLrZHJjmSd)

- The __second reason is that batch normalization reduces the problem of input values changing (shifting)__.
- Batch normalization does some regularization:
  - Each mini batch is scaled by the mean/variance computed of that mini-batch.
  - This adds some noise to the values `Z[l]` within that mini batch. So similar to dropout it adds some noise to each hidden layer's activations.
  - This has a slight regularization effect.
    - __Using bigger size of the mini-batch you are reducing noise and therefore regularization effect__.
    - Dropout has multiplicative noise
      - > one other slightly non-intuitive effect is that, if you use a bigger mini-batch size, right, so if you use use a mini-batch size of, say, 512 instead of 64, by using a __larger mini-batch size, you're reducing this noise and therefore also reducing this regularization effect__
    - BN has both multiplicative and additive noise
      - this causes some regularization effect
  - __Don't rely on batch normalization as a regularization. It's intended for normalization of hidden units, activations and therefore speeding up learning__. For regularization use other regularization techniques (L2 or dropout).
    - you can use both both

## Batch normalization at test time

- When we train a NN with Batch normalization, we compute the mean and the variance of the mini-batch.
- In testing we might need to process examples one at a time. The mean and the variance of one example won't make sense.
- We have to compute an estimated value of mean and variance to use it in testing time.
- We can use the weighted average across the mini-batches.
- >  typical implementations of batch norm, what you do is estimate this using a __exponentially weighted average__ where the average is across the mini batches
![](https://drive.google.com/uc?id=1cdwyXcv5yKb0aFgJZRRKROpCw59pVh1d)
  - This method is also sometimes called `Running average`.

>  from this is that during training time mu and sigma squared are computed on an entire mini batch of say 64 engine, 28 or some number of examples. But that test time, you might need to process a single example at a time. The way to do that is to estimate mu and sigma squared from your training set and there are many ways to do that.

- In practice most often you will use a deep learning framework and it will contain some default implementation of doing such a thing.


## Softmax Regression

- In every example we have used so far we were talking about binary classification.
- There are a __generalization of logistic regression called Softmax regression that is used for multiclass classification/regression__.
- For example if we are classifying by classes `dog`, `cat`, `baby chick` and `none of that`
  - Dog `class = 1`
  - Cat `class = 2`
  - Baby chick `class = 3`
  - None `class = 0`
  - To represent a dog vector `y = [0 1 0 0]`
  - To represent a cat vector `y = [0 0 1 0]`
  - To represent a baby chick vector `y = [0 0 0 1]`
  - To represent a none vector `y = [1 0 0 0]`
- Notations:
  - `C = no. of classes`
  - Range of classes is `(0, ..., C-1)`
  - In output layer `Ny = C`
- __Each of C values in the output layer will contain a probability of the example to belong to each of the classes__.
  - all numbers in each node must equal to one
- In the last layer we will have to activate the __Softmax activation function instead of the sigmoid activation__.
- Softmax activation equations:
  ```
  # shape(C, m) element wise exponentiation
  t = e^(Z[L])                      

  # shape(C, m), sum(t) - sum of t's for each example (shape (1, m)) 
  A[L] = e^(Z[L]) / sum(t)          
  ```

![](https://drive.google.com/uc?id=15CVlTYD1hbK0LY2tjddOs_W2yljFS1lR)
- > so this algorithm takes the vector zL and is four probabilities that sum to 1
- > summarize what we just did to math from zL to aL, this whole computation computing exponentiation to get this temporary variable t and then normalizing, we can summarize this into a Softmax activation function and say aL equals the activation function g applied to the vector zL
- > A[L] = g[L](Z[L])
- >  unusual thing about the Softmax activation function is, because it needs to normalized across the different possible outputs, and needs to take a vector and puts in outputs of vector
![](https://drive.google.com/uc?id=1YI8Jh_44Op-rV3U5j-eEoEIWPhCGgynH)

>  one intuition is that the decision boundary between any two classes will be more linear. That's why you see for example that decision boundary between the yellow and the various classes, that's the linear boundary where the purple and red linear in boundary between the purple and yellow and other linear decision boundary
![](https://drive.google.com/uc?id=105vF0FVorDvSjlHHaBxitWxK6DugG767)

- The examples above shows only softmax layer and no hidden layer.  Notice that it is computing linear decision boundaries.  Now imagine if you add hidden layers. You will get more complex non-linear decision boundaries and get better accuracy.

## Training a Softmax classifier

- There's an activation which is called hard max, which gets 1 for the maximum value and zeros for the others. Which is how it gets its name.

  - If you are using NumPy, its `np.max` over the vertical axis.
- The Softmax name came from softening the values and not harding them like hard max.
- Softmax is a generalization of logistic activation function to `C` classes. If `C = 2` softmax reduces to logistic regression.
- > more generally, what this loss function does is it looks at whatever is the ground true class in your training set, and it tries to make the corresponding probability of that class as high as possible. This turns out to be a form of maximum likelyhood estimation.  

$$-\sum_{j=1}^{C}y_jlog(\hat{y}_j)  = L(\hat{y},y)$$
- The loss function used with softmax:
  ```
  L(y, y_hat) = - sum(y[j] * log(y_hat[j])) # j = 0 to C-1
  ```
- The cost function used with softmax:
  ```
  J(w[1], b[1], ...) = - 1 / m * (sum(L(y[i], y_hat[i]))) # i = 0 to m
  ```
- Back propagation with softmax:
  ```
  dZ[L] = Y_hat - Y
  ```
- The derivative of softmax is:
  ```
  Y_hat * (1 - Y_hat)
  ```
- Example:
    ![](https://drive.google.com/uc?id=1RODO16FpwLKadOqNjLF1xKJNH2u2MsS-)

## Deep learning frameworks

- It's not practical to implement everything from scratch. Our numpy implementations were to know how NN works.
- There are many good deep learning frameworks.
- Deep learning is now in the phase of doing something with the frameworks and not from scratch to keep on going.
- Here are some of the leading deep learning frameworks:
  - Caffe/ Caffe2
  - CNTK
  - DL4j
  - Keras
  - Lasagne
  - mxnet
  - PaddlePaddle
  - TensorFlow
  - Theano
  - Torch/Pytorch
- These frameworks are getting better month by month. Comparison between them can be found [here](https://en.wikipedia.org/wiki/Comparison_of_deep_learning_software).
- How to choose deep learning framework:
  - Ease of programming (development and deployment)
  - Running speed
  - Truly open (open source with good governance)
    - trust will remain open source overtime
- Programming frameworks can not only shorten your coding time but sometimes also perform optimizations that speed up your code.

## TensorFlow

- In this section we will learn the basic structure of TensorFlow programs.
- Lets see how to implement a minimization function:
  - Example function: `J(w) = w^2 - 10w + 25`
  - The result should be `w = 5` as the function is `(w-5)^2 = 0`
  - Code v.1:
    ```python
    import numpy as np
    import tensorflow as tf
    
    # creating a variable w
    w = tf.Variable(0, dtype=tf.float32)         

    # can be written as this - cost = w**2 - 10*w + 25
    cost = tf.add(tf.add(w**2, tf.multiply(-10.0, w)), 25.0)        
    train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

    init = tf.global_variables_initializer()
    session = tf.Session()
    session.run(init)
    session.run(w)    # Runs the definition of w, if you print this it will print zero
    session.run(train)

    print("W after one iteration:", session.run(w))

    for i in range(1000):
      session.run(train)

    print("W after 1000 iterations:", session.run(w))
    ```
  - Code v.2 (we feed the inputs to the algorithm through coefficients):

    ```python
    import numpy as np
    import tensorflow as tf
    
    
    coefficients = np.array([[1.], [-10.], [25.]])

    x = tf.placeholder(tf.float32, [3, 1])
    w = tf.Variable(0, dtype=tf.float32)                 # Creating a variable w
    cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]

    train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

    init = tf.global_variables_initializer()
    session = tf.Session()
    session.run(init)
    session.run(w)    # Runs the definition of w, if you print this it will print zero
    session.run(train, feed_dict={x: coefficients})

    print("W after one iteration:", session.run(w))

    for i in range(1000):
      session.run(train, feed_dict={x: coefficients})

    print("W after 1000 iterations:", session.run(w))
    ```
- In TensorFlow you implement only the forward propagation and TensorFlow will do the backpropagation by itself.
- In TensorFlow a placeholder is a variable you can assign a value to later.
- If you are using a mini-batch training you should change the `feed_dict={x: coefficients}` to the current mini-batch data.
- Almost all TensorFlow programs use this:
  ```python
  with tf.Session() as session:       # better for cleaning up in case of error/exception
    session.run(init)
    session.run(w)
  ```

- > The heart of a TensorFlow program is something to compute at cost, and then TensorFlow automatically figures out the derivatives in how to minimize that costs
- > So what this equation or what this line of code is doing is allowing TensorFlow to construct a computation graph
![](https://drive.google.com/uc?id=1RkwdIP2iop8eW14tYAp7Jk7l3ZZEerLZ)

- In deep learning frameworks there are a lot of things that you can do with one line of code like changing the optimizer.
_**Side notes:**_
- Writing and running programs in TensorFlow has the following steps:
  1. Create Tensors (variables) that are not yet executed/evaluated.
  2. Write operations between those Tensors.
  3. Initialize your Tensors.
  4. Create a Session.
  5. Run the Session. This will run the operations you'd written above.
- Instead of needing to write code to compute the cost function we know, we can use this line in TensorFlow :
  `tf.nn.sigmoid_cross_entropy_with_logits(logits = ...,  labels = ...)`
- To initialize weights in NN using TensorFlow use:
  ```
  W1 = tf.get_variable("W1", [25,12288], initializer = tf.contrib.layers.xavier_initializer(seed = 1))

  b1 = tf.get_variable("b1", [25,1], initializer = tf.zeros_initializer())
  ```
- For 3-layer NN, it is important to note that the forward propagation stops at `Z3`. The reason is that in TensorFlow the last linear layer output is given as input to the function computing the loss. Therefore, you don't need `A3`!
- To reset the graph use `tf.reset_default_graph()`

