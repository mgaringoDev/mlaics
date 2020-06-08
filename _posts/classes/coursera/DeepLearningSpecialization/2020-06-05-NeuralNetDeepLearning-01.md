---
title:  01 - Introduction to Deep Learning
author:     Mario Garingo
keywords: deepLearningSpecialization, nndl
summary: Be able to explain the major trends driving the rise of deep learning, and understand where and how it is applied today.
category: coursera
type: notes
sidebar: coursera_sidebar
---

## What is a Neural Network?
![](https://drive.google.com/uc?id=1itWmUiTgDbGIOTUpojBamwOprIfEqcLi)
Single nueron using RELU and comparing it to regression.


![](https://drive.google.com/uc?id=15Mr6INmeNiwIDUG6unOj_NLlmYRCnaiW)
- Neuron extension based on many other features
	- each neuron will have a RELU activation function
	- given large number of x and y NN typically generate very accurate representations of feature relations

## Supervised Learning with NN
- supervised: given an input(X) there is some mapping function such that you get output(y)
	- need to identify what x and y are
	- image ----- CNN
	- speech,nlp ----- RNN b/c it is a sequence
		- Recurrent neural networks are very good for this type of one-dimensional sequence data that has a temporal component
	- image, radar info ----- Custom or Hybrid approach

### Types of NN 
![](https://drive.google.com/uc?id=1Fx28JX-ib4BQkKjVUANl6aoiqGKNc2Ez)

### Types of Data
![](https://drive.google.com/uc?id=1-0CI4X2cCM-ztN0MLorcunM3v1jhzO3T)
- Structured data:
	- x has tangible meanings
		- databases
	- great economical value because it can be applied to stuff like advertisement and databases that already exist
- Unstructured data:
	- x doesn't have any specific meaning in the context of being one single value
		- pixel, word, volume, pitch etc....
		- overall they may be valuable but individually they don't have meaning.
	- we have learned so much about this recently because computers can now do things that we can do

## Why Deep Learning is Taking Off?
![](https://drive.google.com/uc?id=14nmhjnrzfGPGaUEAVJEN-cZiJJXqWoOd)
- big data because of the digitization of activity
- traditional learning
	- SVM and regression type analysis
- scale in this case means two things
	- size of the data 
	- size of the NN
- lower case ```m``` is the size of training samples
- small training sets
	- the relative performance comparison between the algorithms are not defined and performance is purely dependent on the hand crafted features
- large training sets
	- only until you get to left side of the figure you will see the performance increase when using larger and larger NN

- improving NN from sigmoid to RELU for computational improvement
	- sigmoid function at extreme when the derivative is almost 0 the learning is very slow during gradient descent
	- relu the gradient is 1 with anything greater than 0 has some change




