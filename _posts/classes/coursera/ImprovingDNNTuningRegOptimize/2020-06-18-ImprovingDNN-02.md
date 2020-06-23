---
title:  02 - Optimization algorithms
author:     Mario Garingo
keywords: deepLearningSpecialization, tuningDNN
summary: Using optimization algorithms to improve DNN
category: coursera
type: notes
sidebar: coursera_sidebar
---

## Mini-batch gradient descent

- Training NN with a large data is slow. So to find an optimization algorithm that runs faster is a good idea.
- Suppose we have `m = 50 million`. To train this data it will take a huge processing time for one step.
  - because 50 million won't fit in the memory at once we need other processing to make such a thing.
- > it turns out that you can get a faster algorithm if you __let gradient descent start to make some progress__ even before you finish processing your entire, your giant training sets of 5 million examples
- Suppose we have split m to **mini batches** of size 1000.
  - `X{1} = 0    ...  1000`
  - `X{2} = 1001 ...  2000`
  - `...`
  - `X{bs} = ...`
- We similarly split `X` & `Y`.
- So the definition of mini batches ==> `t: X{t}, Y{t}` or when writing this it is `t: X^{t}, Y^{t}`.
	- not the curly braces is a super script
- Recall notation
	- `()` - round brackets are each training example 
	- `[]` - layer
	- `{}` - mini-batch
- In **Batch gradient descent** we run the gradient descent on the whole dataset.
- While in **Mini-Batch gradient descent** we run the gradient descent on the mini datasets.
- the sizes should be X{t}: (n_x,minibatchSize)
- the sizes should be Y{t}: (1,minibatchSize)
- this is as if you are training the NN by a miniBatchSize dataset and updating the weights.  Then update again using another miniBatchSize array.
- Mini-Batch algorithm pseudo code:
  ```
  # this is called an epoch
  for t = 1:No_of_batches                         
  	AL, caches = forward_prop(X{t}, Y{t})
  	cost = compute_cost(AL, Y{t})
  	grads = backward_prop(AL, caches)
  	update_parameters(grads)
  ```
![](https://drive.google.com/uc?id=1i0UC4Ba2BQGygEcR10d8-_8VuelVYY8o)
- The code inside an epoch should be vectorized.
- Mini-batch gradient descent works much faster in the large datasets.

## Understanding mini-batch gradient descent

- in batch grad desc if it ever goes up even on iteration then something is wrong
- In mini-batch algorithm, the cost won't go down with each step as it does in batch algorithm. It could contain some ups and downs but generally it has to go down (unlike the batch gradient descent where cost function descreases on each iteration).
  ![](https://drive.google.com/uc?id=1WM9llvrvqTjA9ucnZwGA4WcIbp3TGy-x)

![](https://drive.google.com/uc?id=1hBEYPwdsfFlxzACAFOEJJ4w2wS1tKc4H)
- Mini-batch size:
  - (`mini batch size = m`)  ==>    Batch gradient descent
  	- too long per iteration (epoch)
  	- gradual and larger steps 
  	- less noise
  - (`mini batch size = 1`)  ==>    Stochastic gradient descent (SGD)
  	- too noisy regarding cost minimization 
  		- can be reduced by using smaller learning rate
  	- lose speedup from vectorization because this is basically a loop
  	- never converge 
  - (`mini batch size = between 1 and m`) ==>    Mini-batch gradient descent
  	1. faster learning:
      - you have the vectorization advantage
      - make progress without waiting to process the entire training set
	2. doesn't always exactly converge 
		- oscillate in a very small region, but you can reduce learning rate

- Guidelines for choosing mini-batch size:
	1. If small training set (< 2000 examples) - use batch gradient descent.
	2. It has to be a power of 2 (because of the way computer memory is layed out and accessed, sometimes your code runs faster if your mini-batch size is a power of 2):
	`64, 128, 256, 512, 1024, ...`
	3. Make sure that mini-batch fits in CPU/GPU memory.

- Mini-batch gradient descent:
  
- Mini-batch size is a `hyperparameter`.

## Exponentially weighted averages

- There are optimization algorithms that are better than **gradient descent**, but you should first learn about Exponentially weighted averages.
- If we have data like the temperature of day through the year it could be like this:
  ```
  t(1) = 40
  t(2) = 49
  t(3) = 45
  ...
  t(180) = 60
  t(181) = 56
  ...
  ```
- This data is small in winter and big in summer. If we plot this data we will find it some noisy.
![](https://drive.google.com/uc?id=1ojHsd6CYpqdm-KC3IfnYiLWdZvTHc4-6)
- Now lets compute the __Exponentially weighted averages__:
  ```
  V0 = 0
  V1 = 0.9 * V0 + 0.1 * t(1) = 4		# 0.9 and 0.1 are hyperparameters
  V2 = 0.9 * V1 + 0.1 * t(2) = 8.5
  V3 = 0.9 * V2 + 0.1 * t(3) = 12.15
  ...
  ```
- General equation
  ```
  V(t) = beta * v(t-1) + (1-beta) * theta(t)
  ```
- If we plot this it will represent averages over `~ (1 / (1 - beta))` entries:
    - `beta = 0.9` will average last 10 entries
    - `beta = 0.98` will average last 50 entries
    	- there is a bit more latency
    	- larger weight from the previous value
    - `beta = 0.5` will average last 2 entries
    	- noisy and susceptible to outliers but more adaptive
- Best beta average for our case is between 0.9 and 0.98



## Understanding exponentially weighted averages
Recall:
$$v_t = \beta v_{t-1} + (1-\beta)\theta_t$$ 
where $$\beta$$ is a hyperparamater and $$\theta$$ is the current value

- **Intuition**: The reason why exponentially weighted averages are useful for further optimizing gradient descent algorithm is that it can give different weights to recent data points (`theta`) based on value of `beta`. If `beta` is high (around 0.9), it smoothens out the averages of skewed data points (oscillations w.r.t. Gradient descent terminology). So this reduces oscillations in gradient descent and hence makes faster and smoother path towards minima.
- Another imagery example:   
    ![](Images/Nasdaq1_small.png)   
    _(taken from [investopedia.com](https://www.investopedia.com/))_


- Intuitions:   
    ![](https://drive.google.com/uc?id=1fbCwE-pLtSAuoEzDq6qnhQWSlMUexSGC)
- We can implement this algorithm with more accurate results using a moving window. But the code is more efficient and faster using the exponentially weighted averages algorithm.
- Algorithm is very simple:
  ```
  v = 0
  Repeat
  {
  	Get theta(t)
  	v = beta * v + (1-beta) * theta(t)
  }
  ```
- less accurate than an actual moving avg but very efficient and computation

## Bias correction in exponentially weighted averages

- The bias correction helps make the exponentially weighted averages more accurate.
- Because `v(0) = 0`, the bias of the weighted averages is shifted and the accuracy suffers at the start. Green was theoretical but technically you get purple in the image below
![](https://drive.google.com/uc?id=1TpSyAbRMixexZVgqd1k4Q-cJmHu0Qfuy)
- To solve the bias issue we have to use this equation:
  ```
  v(t) = (beta * v(t-1) + (1-beta) * theta(t)) / (1 - beta^t)
  ```
- As t becomes larger the `(1 - beta^t)` becomes close to `1`

- So in machine learning, for most implementations of the exponential weighted average, people don't often bother to implement bias corrections

## Gradient descent with momentum

- __The momentum algorithm almost always works faster than standard gradient descent.__
- > the basic idea is to compute an exponentially weighted average of your gradients, and then use that gradient to update your weights instead

- oscillations in standard grad desc causes:
	- slower learning due to you having to have a lower learning rate
		- larger learning rate might diverge
		- smaller meaning slower step towards the minima
- instead of these oscillations you will get an average general direction smoothening out path of grad desc
![](https://drive.google.com/uc?id=1uQtda5-_pE10ghWtNY36vsMVX_tQsVFI)
- Pseudo code:
  ```
  vdW = 0, vdb = 0
  on iteration t:
  	# can be mini-batch or batch gradient descent
  	compute dw, db on current mini-batch                
  			
  	vdW = beta * vdW + (1 - beta) * dW
  	vdb = beta * vdb + (1 - beta) * db
  	W = W - learning_rate * vdW
  	b = b - learning_rate * vdb
  ```

- Momentum helps the cost function to go to the minimum point in a more fast and consistent way.
- `beta` is another `hyperparameter`. `beta = 0.9` is very common and works very well in most cases.
- In practice people don't bother implementing **bias correction**.
- in the __literature__ the (1-beta) but the net effect
	- vdW ends up being scaled by a factor of 1 minus Beta, or really 1 over 1 minus Beta
	- so when you're performing these gradient descent updates, alpha just needs to change by a corresponding value of 1 over 1 minus Beta
	- __problem__: one impact of this is that if you end up tuning the hyperparameter Beta, then this affects the scaling of vdW and vdb as well. 
	 -  end up needing to retune the learning rate, alpha, as well

## RMSprop

- Stands for **Root mean square prop**.
- This algorithm speeds up the gradient descent by reducing the oscillation and increasing the step towards the minima
- Pseudo code:
  ```
  sdW = 0, sdb = 0
  on iteration t:
  	# can be mini-batch or batch gradient descent
  	compute dw, db on current mini-batch
  	
  	sdW = (beta_2 * sdW) + (1 - beta_2) * dW^2  # squaring is element-wise
  	sdb = (beta_2 * sdb) + (1 - beta_2) * db^2  # squaring is element-wise
  	W = W - learning_rate * dW / sqrt(sdW)
  	b = B - learning_rate * db / sqrt(sdb)
  ```
- RMSprop will make the cost function move slower on the vertical direction and faster on the horizontal direction in the following example:
    ![](https://drive.google.com/uc?id=1mHUNO773qXScE8AfOD_16xJRAx2XaGuN)
    - one advantage of this is that you can increase the learning rate to speed up the algorithm
- Ensure that `sdW` is not zero by adding a small value `epsilon` (e.g. `epsilon = 10^-8`) to it:   
   `W = W - learning_rate * dW / (sqrt(sdW) + epsilon)`
	- > Db is also very high-dimensional parameter vector, but your intuition is that in dimensions where you're getting these oscillations, you end up computing a larger sum
	- > A weighted average for these squares and derivatives, and so you end up dumping out the directions in which there are these oscillations.
- Developed by Geoffrey Hinton and firstly introduced on [Coursera.org](https://www.coursera.org/) course.


## Adam optimization algorithm

- Stands for **Adaptive Moment Estimation**.
- __Adam optimization and RMSprop are among the optimization algorithms that worked very well with a lot of NN architectures.__
	- Adam optimization simply puts RMSprop and momentum together!
- Pseudo code:
  ```
  vdW = 0, vdW = 0
  sdW = 0, sdb = 0
  on iteration t:
  	# can be mini-batch or batch gradient descent
  	compute dw, db on current mini-batch                
  			
  	vdW = (beta1 * vdW) + (1 - beta1) * dW     # momentum
  	vdb = (beta1 * vdb) + (1 - beta1) * db     # momentum
  			
  	sdW = (beta2 * sdW) + (1 - beta2) * dW^2   # RMSprop
  	sdb = (beta2 * sdb) + (1 - beta2) * db^2   # RMSprop
  			
  	vdW = vdW / (1 - beta1^t)      # fixing bias
  	vdb = vdb / (1 - beta1^t)      # fixing bias
  			
  	sdW = sdW / (1 - beta2^t)      # fixing bias
  	sdb = sdb / (1 - beta2^t)      # fixing bias
  					
  	W = W - learning_rate * vdW / (sqrt(sdW) + epsilon)
  	b = B - learning_rate * vdb / (sqrt(sdb) + epsilon)
  ```
{{site.data.alerts.warning}}
- Hyperparameters for Adam:
  - Learning rate: needed to be tuned.
  - `beta1`: parameter of the momentum - `0.9` is recommended by default.
  	- first moment
  - `beta2`: parameter of the RMSprop - `0.999` is recommended by default.
  	- second moment
  - `epsilon`: `10^-8` is recommended by default.
{{site.data.alerts.end}}

## Learning rate decay

- Slowly reduce learning rate.
![](https://drive.google.com/uc?id=1KFbcSNwC-csDA6wFHZF1J5FHHVkfBjmA)
- As mentioned before mini-batch gradient descent won't reach the optimum point (converge). But by making the learning rate decay with iterations it will be much closer to it because the steps (and possible oscillations) near the optimum are smaller.
	- > So the intuition behind slowly reducing alpha, is that maybe during the initial steps of learning, you could afford to take much bigger steps.
	- > But then as learning approaches converges, then having a slower learning rate allows you to take smaller steps
- One technique equations is
$$\alpha = \frac{1}{1 + decayRate*epochNum} * \alpha_0$$
```python
learning_rate = (1 / (1 + decay_rate * epoch_num)) * learning_rate_0
```
  - `epoch_num` is over all data (not a single mini-batch).
- Other learning rate decay methods (continuous):	
  - `learning_rate = (0.95 ^ epoch_num) * learning_rate_0`
  - `learning_rate = (k / sqrt(epoch_num)) * learning_rate_0`  
- Some people perform learning rate decay discretely - repeatedly decrease after some number of epochs.
- Some people are making changes to the learning rate manually.
- `decay_rate` is another `hyperparameter`.
- For Andrew Ng, learning rate decay has less priority.

## The problem of local optima

- The normal local optima is not likely to appear in a deep neural network because data is usually high dimensional. For point to be a local optima it has to be a local optima for each of the dimensions which is highly unlikely.
- It's unlikely to get stuck in a bad local optima in high dimensions, it is much more likely to get to the __saddle point__ rather to the local optima, which is not a problem.
![](https://drive.google.com/uc?id=1l4S5k3_dE7-BqlDjc8BFTOh92PZww8gb)
- Plateaus can make learning slow:
  - Plateau is a region where the derivative is close to zero for a long time.
  - This is where algorithms like momentum, RMSprop or Adam can help.
![](https://drive.google.com/uc?id=1w7mNoRsyttXnP9djTQ2BnTQhsXTBpVYg)