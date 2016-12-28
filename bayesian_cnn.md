Title: Bayesian Convolutional Neural Networks with Bernoulli Approximate Variational Inference
Date: 2016-12-08 23:45
Category: Papers

After a long hiatus, I’m going to write about another paper I read recently, that is changing the way I think about using deep networks for computational biology problems.  Anyone that’s working in applied machine learning these days is familiar with the idea of convolutional neural networks (abbr. convent).  They have a long history of success in all sorts of supervised learning tasks (usually object recognition in images), but have since been extended to almost any domain you can properly define a convolution (or more often cross-correlation, see this excellent chapter from [the deep learning textbook](http://www.deeplearningbook.org/contents/convnets.html) for more details).  The key idea behind a convolutional network, at least in the context of a unit that is composed to build a deeper model, is that if can be understood as a sparse form of a fully connected layer with a specific way of tying together the values of certain parameters.  This reduction in the ratio of free parameters to training data means we should be able to get better estimates for the model parameters without requiring anything more than the tools used for training regular feed forward nets.  

A typical contemporary convnet, however, will employ very many local receptive fields (also known as filters), which act as feature detectors, possibly in a larger network.  They employ many, many layers, in pursuit of better discriminative performance, which eats away at any previously realized gains in reducing the number of parameters.  All this is to say that they may overfit in situations where training data is scarce.  This paper, by Yarin Gal and Zoubin Ghahramani, examines how placing a distribution over the kernels that parameterize the CNNs, they  in a Bayesian framework can control overfitting naturally, without either incurring much more computational overhead or significantly altering the form of the network. 
  
## Summary 

The authors pick up on a previous line of work showing that dropout in neural networks can be interpreted as an approximation to GPs.  In this work, they go on to show that networks trained using [dropout](http://www.jmlr.org/papers/volume15/srivastava14a.old/source/srivastava14a.pdf) can be interpreted as variational inference in Bayesian neural networks, using Bernoulli approximating distributions.  

Dropout, usually understood in the context of model averaging, is instead cast here as approximate variational inference in a Bayesian neural network model.  What this means I’ll establish below.  

## Bayesian Neural Nets	

The defining feature of a Bayesian neural network is the treatment of model weights as random variables : $$\mathbf{W}_i \backsim \mathcal{N}(0,\mathbf{I})$$
Leaving out the bias vectors for simplicity and assuming a multi-class likelihood, the output of the network given input $x$ is 
$$ \hat{f}(x, (\mathbf{W_i}_{i=i}^{L})) $$
which itself is a random variable.  Given $\hat{f} := \hat{f}(\mathbf{x}, (\mathbf{W_i}_{i=i}^{L}))$, the likelihood is 
$$ p(y | \mathbf{x}, (\mathbf{W_i}_{i=i}^{L})) = \text{Cat}\left( \frac{exp(\hat{f})}{\sum\limits{d’}exp(\hat{f_{d’}}) \right)$$

In contrast with most neural nets, where the goal is to optimize the values of the model parameters to minimize some loss or objective function, the goal of a Bayesian NN is to estimate the posterior distribution over the model parameters: $P((\mathbf{W_i})|\mathbf{X,Y})$.  Exact calculation of the posterior is intractable in general, but can be estimated by either MCMC or variational inference.  The authors here choose the latter, placing an approximating variational distribution over the weights $q((\mathbf{W_i}))$, and minimizing the KL divergence between $q$ and the true posterior:
$$ KL\left( q((\mathbf{W_i}))||p((\mathbf{W}_i)|\mathbf{X,Y}) \right) $$

## Bernoulli variational approximation, and MC dropout

The authors define their approximating variational distribution $q(\mathbf{W}_i$ for each layer $i$ as 
\begin{align}
\mathbf{W}_i &= \mathbf{M}_i \cdot \text{diag}\left( \left[ \mathbf{z}_{i,j} \right]_{j=1}^{K_i} \right) \\
\mathbf{z}_{i,j} &\backsim \text{Bernoulli}(p_i) \text{for} i = 1, \dots, L, j - 1, \dots, K_{i-1}
\end{align}

The $\mathbf{z}_{i,j}$ are Bernoulli distributed random variables, and the $M_i$ are variational parameters.  So, once the posterior is approximated using VI, you use the model to generate predictions for new data $\mathbf{x}^{*}$ by replacing the (intractable) true posterior with the approximate one:

\begin{align}
p(y^{*} | \mathbf{x}^{*},\mathbf{X,Y}) &\approx \int p\left(y^{*}|\mathbf{x}^{*},(\mathbf{W}_i)\right)q\left((\mathbf{W}_i) \right) \approx \frac{1}{T}\sum\limits_{t=1}^{T}p\left( y^{*}|\mathbf{x}^{*},(\mathbf{W}_i)_t \right)
\end{align} 

in the above, $(\mathbf{W}_i)_t \backsim q\left( (\mathbf{W}_i)\right)$; basically they approximate the posterior with super-quickie MC integration.  This is the coolest part of the paper, imo.  It says that once you find a good $q\left((\mathbf{W})_i \right)$, you can get fully Bayesian predictions for new data by simply averaging together several runs of the new input through your model, each time drawing a new set of realized weights from $q$ along with dropout masks $\mathbf{z}$.  They call this MC dropout.  


## My two cents

The paper continues on to test their new proposed dropout (which can apply equally well to weights representing kernels in a convolutional NN as well as fully connected layers) against a set of comparative networks on both MNIST and CIFAR10, measuring the resistance to overfitting conferred by MC dropout on standard models (lenet), versus conventional dropout.  I won’t reproduce the figures here, but their experiments show a small but significant effect.

Equally interesting IMO is the methodology they use to measure overfitting: sub-divide your labeled training data, train on a subset, and measure how quickly the model begins to overfit.  


So, to sum up, I really like this paper.  For very little extra computational effort, you can turn your convnet into a Bayesian convnet.  This gives you the dual benefits of better protection against over-fitting, as well as uncertainty estimates in your predictions, two crucial qualities that are lacking in most deep learning models for biological sequence data.  I’m excited to try it out!



