---
title:  01 - Recurrent Neural Networks
author:     Mario Garingo
keywords: deepLearningSpecialization, sequenceModeling
summary: Learn about recurrent neural networks. This type of model has been proven to perform extremely well on temporal data. It has several variants including LSTMs, GRUs and Bidirectional RNNs, which you are going to learn about in this section.
category: coursera
type: notes
sidebar: coursera_sidebar
---

## Why sequence models
- Sequence Models like RNN and LSTMs have greatly transformed learning on sequences in the past few years.
- Examples of sequence data in applications:
  - Speech recognition (**sequence to sequence**):
  	- both input and output are sequence
    - X: wave sequence
    - Y: text sequence
  - Music generation (**one to sequence**):
  	- only the output Y is the sequence
    - X: nothing or an integer (few notes or genre of music)
    - Y: wave sequence
  - Sentiment classification (**sequence to one**):
  	- some text to the rating
    - X: text sequence
    - Y: integer rating from one to five
  - DNA sequence analysis (**sequence to sequence**):
    - X: DNA sequence (4 alphabet AGCT)
    - Y: DNA Labels (Type protein)
  - Machine translation (**sequence to sequence**):
    - X: text sequence (in one language)
    - Y: text sequence (in other language)
  - Video activity recognition (**sequence to one**):  	
    - X: video frames
    - Y: label (activity)
  - Name entity recognition (**sequence to sequence**):
    - X: text sequence
    - Y: label sequence
    - Can be used by search engines to index different type of words inside a text.
- notice that `X` and `Y` can be different length of sequences
- All of these problems with different input and output (sequence or not) can be addressed as supervised learning with label data X, Y as the training set.

## Notation

Example:
- **Motivating example**:
	- let `X` be some text
	- name entity recognition indexing people in news articles so that they can index them accordingly
		- people, name, time, country, company in various text	

  - Named entity recognition example:
    - X: "Harry Potter and Hermoine Granger invented a new spell."
    - Y:   1   1   0   1   1   0   0   0   0
    - Both elements has a shape of 9. 1 means its a name, while 0 means its not a name.
- We will index the first element of x by x<sup><1></sup>, the second x<sup><2></sup> and so on.
  - x<sup><1></sup> = Harry
  - x<sup><2></sup> = Potter
- Similarly, we will index the first element of y by y<sup><1></sup>, the second y<sup><2></sup> and so on.
  - y<sup><1></sup> = 1
  - y<sup><2></sup> = 1

- T<sub>x</sub> is the size of the input sequence and T<sub>y</sub> is the size of the output sequence.
  - T<sub>x</sub> = T<sub>y</sub> = 9 in the last example although they can be different in other problems.
- x<sup>(i)\<t></sup> is the element t of the sequence of input vector i. Similarly y<sup>(i)\<t></sup> means the t-th element in the output sequence of the i training example.
- T<sub>x</sub><sup>(i)</sup> the input sequence length for training example i. It can be different across the examples. Similarly for T<sub>y</sub><sup>(i)</sup> will be the length of the output sequence in the i-th training example.


- **Representing words**:
    - We will now work in this course with **NLP** which stands for natural language processing. One of the challenges of NLP is how can we represent a word?

    1. We need a **vocabulary** list that contains all the words in our target sets.
        - Example:
            - [a ... And   ... Harry ... Potter ... Zulu]
            - Each word will have a unique index that it can be represented with.
            - The sorting here is in alphabetical order.
        - Vocabulary sizes in modern applications are from 30,000 to 50,000. 100,000 is not uncommon. Some of the bigger companies use even a million.
        - To build vocabulary list, you can read all the texts you have and get m words with the most occurrence, or search online for m most occurring words.
    2. Create a **one-hot encoding** sequence for each word in your dataset given the vocabulary you have created.
        - While converting, what if we meet a word thats not in your dictionary?
        - We can add a token in the vocabulary with name `<UNK>` which stands for unknown text and use its index for your one-hot vector.
    - Full example:   
        ![](notationExample)

- The goal is given this representation for x to learn a mapping using a sequence model to then target output y as a supervised learning problem.

## Recurrent Neural Network Model

- Why not a standard network?
  - inputs and outputs can be different length in different examples/samples
    - padding wont help either
  - doesn't share features learned across different position of text
    - > And this is maybe similar to what you saw in ConvNets where you want things learned for one part of the image to generalize quickly to other parts of the image, and we like a similar effects for sequence data as well. And similar to what you saw with ConvNets using a better representation will also let you reduce the number of parameters in your model.
  - large input layer and would lead to large parameters
  - RNN doesn't have any of these disadvantages

- What is RNN?
![](rnn)
  - At each time step, the RNN that passes on as activation to the next time step for it to use.
    - at time 0 there is a<sup><0></sup> where it can be initialized to 0, random values, or some other techniques
  - scans through the data from left to the right and the parameters are shared
    - Wax are weights the govern the input
    - Waa are weights that governs activations that are passed between each time step
    - Way are weights the governs the output
    - The weight matrix Waa is the memory the RNN is trying to maintain from the previous layers.
    - When making prediction from later layers, it uses information from previous layer, (this is a upside and a downside)
      - problem: you don't get information from future words in the sequence
      - solution: BRNN - bi-directional recurrent neural network

### Forward Prop
![](forwardProp)
  - activation function for computing output and activation for that layer
    - often tanh but ReLU sometimes (activation for that layer `a`)
    - sigmoid (output `y`)

![](forwardPropSimplified)
  - general:
    - w<sub>a</sub> is w<sub>aa</sub> and w<sub>ax</sub> stacked horizontally.
    - [a<sup>\<t-1></sup>, x<sup>\<t></sup>] is a<sup>\<t-1></sup> and x<sup>\<t></sup> stacked vertically.
        - the advantage of this is that you are only keeping track of one parameter matrix
    - w<sub>a</sub> shape: (NoOfHiddenNeurons, NoOfHiddenNeurons + n<sub>x</sub>)
    - [a<sup>\<t-1></sup>, x<sup>\<t></sup>] shape: (NoOfHiddenNeurons + n<sub>x</sub>, 1)

### Back Prop
![](backpropRNN)
- w<sub>a</sub>, b<sub>a</sub>, w<sub>y</sub>, and b<sub>y</sub> are shared across each element in a sequence.
- loss function
  - we will use the sum cross-entropy loss function losses for each time step
- > 1) So, this is the computation problem and from the earlier examples you've seen of backpropagation, it shouldn't surprise you that backprop then just requires doing computations or parsing messages in the opposite directions.
- > 2) So, all of the forward propagation steps arrows, so you end up doing that.
- > 3) And that then, allows you to compute all the appropriate quantities that lets you then, take the riveters, respected parameters, and update the parameters using gradient descent.

- the most important part of back prop is RNN is the left to right propagation (`Back propagation through time`)
  - recall that RNN looks right to left

## Different Types of RNN
![](exampleSequence)
- based on the examples above `Tx` and `Ty` may not be the same length, so there are different architectures to tackle different situations

- The ideas in this section was inspired by Andrej Karpathy [blog](http://karpathy.github.io/2015/05/21/rnn-effectiveness/). Mainly this image has all types:   
  ![](exampleRNNGitHUb)

- The architecture we have described before is called **Many to Many**.
- In sentiment analysis problem, X is a text while Y is an integer that rangers from 1 to 5. 
- A **One to Many** architecture application would be music generation.    
  - Note that starting the second layer we are feeding the generated output back to the network.  

- There are another interesting architecture in **Many To Many**. Applications like machine translation inputs and outputs sequences have different lengths in most of the cases __(many to many with Tx and Ty different sizes)__. So an alternative _Many To Many_ architecture that fits the translation would be as follows:   
  ![](manyToMany)
  - There are an encoder and a decoder parts in this architecture. The encoder encodes the input sequence into one matrix and feed it to the decoder to generate the outputs. Encoder and decoder have different weight matrices.

__Summary:__

![](rnnArchitecture)


## Language model and sequence generation

- What is language modeling? 
  - > So what a language model does is given any sentence is job is to tell you what is the probability of a sentence, of that particular sentence. 
  - Example:
      - Let's say we are solving a speech recognition problem and someone says a sentence that can be interpreted into to two sentences:
        - The apple and **pair** salad
        - The apple and **pear** salad
          - **Pair** and **pear** sounds exactly the same, so how would a speech recognition application choose from the two.
        - That's where the language model comes in. It gives a probability for the two sentences and the application decides the best based on this probability.

- Language modeling with an RNN
  - Training Set: large corpus of English text
    - corpus is vocabulary
    - tokenizer
      - one hot vector for each word in the training set
      - `<EOS>` is a token to signify the end of a sentence
      - `.` add a period as part of the tokens
      - `<UNK>` unknown token for unrecognized word
    - model the chance of the sequence occurring

- RNN model
![](rnnLanguageModel)
  - softmax to identify what are the chances that each word in the sentence occurs next in the sequence
    - softmax of 10000 words in the dictionary
  - > So each step in the RNN will look at some set of preceding words such as, given the first three words, what is the distribution over the next word? And so this RNN learns to predict one word at a time going from left to right.  
  - To use this model:
  1.  For predicting the chance of **next word**, we feed the sentence to the RNN and then get the final y<sup>^\<t></sup> hot vector and sort it by maximum probability.
  2.  For taking the **probability of a sentence**, we compute this:
      - p(y<sup><1></sup>, y<sup><2></sup>, y<sup><3></sup>) = p(y<sup><1></sup>) * p(y<sup><2></sup> | y<sup><1></sup>) * p(y<sup><3></sup> | y<sup><1></sup>, y<sup><2></sup>)
      - This is simply feeding the sentence into the RNN and multiplying the probabilities (outputs).

## Sampling Novel Sequences

### Word Level
- Lets see the steps of how we can sample a novel sequence from a trained sequence language model:
  1. Given this model:   
     ![](novelSequence)
  2. We first pass a<sup><0></sup> = zeros vector, and x<sup><1></sup> = zeros vector.
  3. Then we choose a prediction randomly from distribution obtained by y&#770;<sup><1></sup>. For example it could be "The".
     - In numpy this can be implemented using: `numpy.random.choice(...)`
     - This is the line where you get a random beginning of the sentence each time you sample run a novel sequence.
  4. We pass the last predicted word with the calculated  a<sup><1></sup>
  5. We keep doing 3 & 4 steps for a fixed length or until we get the `<EOS>` token.
  6. You can reject any `<UNK>` token if you mind finding it in your output.  


### Character Level
- the vocub will now will be the alphabet, digit and punctuations
  - training set corpus to define the library 
- the sequence are now characters instead of words
- Character-level language model has some pros and cons compared to the word-level language model
  - Pros:
    1. There will be no `<UNK>` token - it can create any word.
  - Cons:
    1. The main disadvantage is that you end up with much longer sequences. 
    2. Character-level language models are not as good as word-level language models at capturing long range dependencies between how the the earlier parts of the sentence also affect the later part of the sentence.
    3. Also more computationally expensive and harder to train.

- The trend Andrew has seen in NLP is that for the most part, a word-level language model is still used, but as computers get faster there are more and more applications where people are, at least in some special cases, starting to look at more character-level models. Also, they are used in specialized applications where you might need to deal with unknown words or other vocabulary words a lot. Or they are also used in more specialized applications where you have a more specialized vocabulary.

## Vanishing Gradients with RNNs
- One of the problems with naive RNNs that they run into **vanishing gradient** problem.

- An RNN that process a sequence data with the size of 10,000 time steps, has 10,000 deep layers which is very hard to optimize.

- Let's take an example. Suppose we are working with language modeling problem and there are two sequences that model tries to learn:

  - "The **cat**, which already ate ..., **was** full"
  - "The **cats**, which already ate ..., **were** full"
  - Dots represent many words in between.

- What we need to learn here that "was" came with "cat" and that "were" came with "cats". The naive RNN is not very good at capturing very long-term dependencies like this.

- As we have discussed in Deep neural networks, deeper networks are getting into the vanishing gradient problem. That also happens with RNNs with a long sequence size.   
  ![](vanishingGrad)   
  - For computing the word "was", we need to compute the gradient for everything that came before it. Multiplying fractions tends to vanish the gradient, while multiplication of large number tends to explode it.
  - Therefore some of your weights may not be updated properly.
  - especially the earlier ones
  - __Vanishing gradients__ problem tends to be the bigger problem with RNNs than the _exploding gradients_ problem. We will discuss how to solve it in next sections.
    - > It turns out that vanishing gradients tends to be the bigger problem with training RNNs, although when exploding gradients happens, it can be catastrophic because the exponentially large gradients can cause your parameters to become so large that your neural network parameters get really messed up. 
  - __Exploding gradients__ can be easily seen when your weight values become `NaN`. So one of the ways solve exploding gradient is to apply **gradient clipping** means if your gradient is more than some threshold - re-scale some of your gradient vector so that is not too big. So there are cliped according to some maximum value.
    - > exploding gradients are easier to spot because the parameters just blow up and you might often see `NaN`s, or not a numbers, meaning results of a numerical overflow in your neural network computation.
      - solution to this is to apply `gradient clipping`. Which is is apply some threshold and rescale so that it is not too large
        - robust solution that can overcome this problem

- In the problem we descried it means that its hard for the network to memorize "was" word from "cat" which was appeared earlier on in the sequence. So in this case, the network won't identify the singular/plural words so that it gives it the right grammar form of verb was/were.

- The conclusion is that RNNs aren't good in **long-term dependencies**.

- In theory, RNNs are absolutely capable of handling such “long-term dependencies.” A human could carefully pick parameters for them to solve toy problems of this form. Sadly, in practice, RNNs don’t seem to be able to learn them. http://colah.github.io/posts/2015-08-Understanding-LSTMs/

- **Extra**:
  - Solutions for the Exploding gradient problem:
    - Truncated backpropagation.
      - Not to update all the weights in the way back.
      - Not optimal. You won't update all the weights.
    - Gradient clipping.
  - Solution for the Vanishing gradient problem:
    - Weight initialization.
      - Like He initialization.
    - Echo state networks.
    - Use LSTM/GRU networks.
      - Most popular.
      - We will discuss it next.

## Gated Recurrent Unit (GRU)

- the basic RNN unit can be simplified to the following diagram
![](rnnUnit)


- [On the properties of neural machine translation: Encoder-decoder approaches](https://arxiv.org/pdf/1409.1259.pdf)
- [Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling](https://arxiv.org/pdf/1412.3555.pdf?ref=hackernoon.com)

### Simplified
![](gruSimplified)
- In GRUs, C<sup>\<t></sup> = a<sup>\<t></sup>

- Equations of the GRUs:   
  - The update gate is between 0 and 1
    - To understand GRUs imagine that the update gate is either 0 or 1 most of the time.
  - So we update the memory cell based on the update cell and the previous cell.

- Lets take the cat sentence example and apply it to understand this equations:

  - Sentence: "The **cat**, which already ate ........................, **was** full"

  - We will suppose that `gamma` is 0 or 1 and is a bit that tells us if a singular word needs to be memorized.

  - Splitting the words and get values of C and U at each place:

    - | Word    | Update gate(`Gamma`)         | Cell memory (C) |
      | ------- | -------------------------- | --------------- |
      | The     | 0                          | val             |
      | cat     | 1                          | new_val         |
      | which   | 0                          | new_val         |
      | already | 0                          | new_val         |
      | ...     | 0                          | new_val         |
      | was     | 1 (I don't need it anymore)| newer_val       |
      | full    | ..                         | ..              |
- Drawing for the GRUs     
  - Drawings like in http://colah.github.io/posts/2015-08-Understanding-LSTMs/ is so popular and makes it easier to understand GRUs and LSTMs. But Andrew Ng finds it's better to look at the equations.
- Because the update gate `gamma` is usually a small number like 0.00001, GRUs doesn't suffer the vanishing gradient problem.
  - In the equation this makes C<sup>\<t></sup> = C<sup>\<t-1></sup> in a lot of cases.
- Shapes:
  - a<sup>\<t></sup> shape is (NoOfHiddenNeurons, 1)
  - c<sup>\<t></sup> is the same as a<sup>\<t></sup>
  - c<sup>~\<t></sup> is the same as a<sup>\<t></sup>
  - u<sup>\<t></sup> is also the same dimensions of a<sup>\<t></sup>
- The multiplication (`*`) in the equations are element wise multiplication.

### Full
![](fullGRU)
- The full GRU contains a new gate that is used with to calculate the candidate C. The gate tells you how relevant is C<sup>\<t-1></sup> to C<sup>\<t></sup>
  - Shapes are the same
- So why we use these architectures, why don't we change them, how we know they will work, why not add another gate, why not use the simpler GRU instead of the full GRU; well researchers has experimented over years all the various types of these architectures with many many different versions and also addressing the vanishing gradient problem. They have found that full GRUs are one of the best RNN architectures  to be used for many different problems. You can make your design but put in mind that GRUs and LSTMs are standards.

- in the literature it can be `h`, `u`, and `r` but Andrew said that he changed the notion to make it easier to understand


## Long Short Term Memory (LSTM)
[Long Short-Term Memory](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.676.4320&rep=rep1&type=pdf)

- LSTM - the other type of RNN that can enable you to account for long-term dependencies. It's more powerful and general than GRU.
- In LSTM , C<sup>\<t></sup> != a<sup>\<t></sup>
- Here are the equations of an LSTM unit:   
  ![](lstmEquation)
- In GRU we have an update gate `U`, a relevance gate `r`, and a candidate cell variables C<sup>\~\<t></sup> while in LSTM we have an update gate `U` (sometimes it's called input gate I), a forget gate `F`, an output gate `O`, and a candidate cell variables C<sup>\~\<t></sup>
- Drawings (inspired by http://colah.github.io/posts/2015-08-Understanding-LSTMs/):    
  ![](lstmPictures)
- Some variants on LSTM includes:
  - LSTM with **peephole connections**.
    - The normal LSTM with C<sup>\<t-1></sup> included with every gate.
- There isn't a universal superior between LSTM and it's variants. One of the advantages of GRU is that it's simpler and can be used to build much bigger network but the LSTM is more powerful and general.


## Bi-Directional RNN (BRNN)

- As we saw before, here is an example of the Name entity recognition task:  
  ![](brnnExample)
- The name **Teddy** cannot be learned from **He** and **said**, but can be learned from **bears**.
- BiRNNs fixes this issue.

- Here is BRNNs architecture:   
  ![](brnnArchitecture)
- Note, that BiRNN is an **acyclic graph**.
- Part of the forward propagation goes from left to right, and part - from right to left. It learns from both sides.
  - notice that if we are trying to predict `3` we get information from `-1-3` in the left to right section while `3-4` gets passed on in the right to left section. The current information `3` gets passed on to both directions.
- To make predictions we use y&#770;<sup>\<t></sup> by using the two activations that come from left and right.
- The blocks here can be any RNN block including the basic RNNs, LSTMs, or GRUs.
- For a lot of NLP or text processing problems, a __BiRNN with LSTM appears to be commonly used.__
- __The disadvantage of BiRNNs that you need the entire sequence before you can process it.__ 
  - For example, in live speech recognition if you use BiRNNs you will need to wait for the person who speaks to stop to take the entire sequence and then make your predictions.


## Deep RNNs
- In a lot of cases the standard one layer RNNs will solve your problem. But in some problems its useful to stack some RNN layers to make a deeper network.
- For example, a deep RNN with 3 layers would look like this:  
  ![](deepRNN)
  - 3 is already quite big because the temporal dimension, these networks can already get quite big even if you have just a small handful of layers and not stacked up for 100 layers
  - one thing is that the output can have a deep network only connected vertically and not horizontally
- In some cases you might see some feed-forward network layers connected after recurrent cell.
