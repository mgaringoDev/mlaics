---
title:  01 - Structuring Machine Learning Projects - Homework
author:     Mario Garingo
keywords: deepLearningSpecialization, mlStrat
summary: To help you practice strategies for machine learning, the following exercise will present an in-depth scenario and ask how you would act.
category: coursera
type: notes
sidebar: coursera_sidebar
---


## Introduction

Consider airplane pilots who’s training involves time spent in flight simulators. These flight simulators accelerate the pilots’ learning by allowing them to experience a volume and variety of scenarios that they otherwise may have needed a much longer time to acquire.

The following exercise is a “flight simulator” for machine learning. Rather than you needing to spend years working on a machine learning project before you get to experience certain scenarios, you’ll get to experience them right here.

> Personal note from Andrew: I’ve found practicing with scenarios like these to be useful for training PhD students and advanced Deep Learning researchers. This is the first time this type of “airplane simulator” for machine learning strategy has ever been made broadly available. I hope this helps you gain “real experience” with machine learning much faster than even full-time machine learning researchers typically do from work experience.

`Bird recognition in the city of Peacetopia (case study)`


## Problem Statement
The people of Peacetopia have a common characteristic: they are afraid of birds. To save them, you have to build an algorithm that will detect any bird flying over Peacetopia and alert the population.

The City Council gives you a dataset of 10,000,000 images of the sky above Peacetopia, taken from the city’s security cameras. They are labelled:

- y = 0: There is no bird on the image
- y = 1: There is a bird on the image

Your goal is to build an algorithm able to classify new images taken by security cameras from Peacetopia.

There are a lot of decisions to make:

What is the evaluation metric?
How do you structure your data into train/dev/test sets?

## Metric of success
The City Council tells you that they want an algorithm that

- __Has high accuracy__
- __Runs quickly__ and takes only a short time to classify a new image.
- Can fit in a __small amount of memory__, so that it can run in a small processor that the city will attach to many different security cameras.