Title: Basset: multi-task convolutional networks for predicting regions chromatin from sequence
Date: 2016-02-15 17:45
Category: Papers

I've been reading a few papers recently that each involve training a deep network that takes input directly from sequence and predicts some aspect of 
chromatin.  [Deep Bind](http://www.nature.com/nbt/journal/v33/n8/full/nbt.3300.html) predicts protein-DNA binding, and 
[DeepSEA](http://www.nature.com/nmeth/journal/v12/n10/full/nmeth.3547.html) predicts the effect of SNPs on chromatin state.  The most recent paper, 
and the one I find most accessible, is [Basset](http://biorxiv.org/content/early/2015/10/05/028399). Authored by David R. Kelley (from John Rinn's lab),
as well as former U of T alumnus Jasper Snoek, this is a great paper which should make a lasting contribution to sequence modeling.

### Summary 

The authors build (and more importantly distribute) a deep CNN to learn functional activity of DNA sequences directly from the sequences themselves.  
They trained Basset on DNA sequences from 2 million different loci to predict DNA accessibility.  They took DNAseI accessible peaks encoded as BED 
files for 125 different cell types from ENCODE (and another 39 from Epigenomics Roadmap), extended each peak 300bp in each direction from the midpoint, 
and merged proximal peaks.  These 600bp sequences were then encoded as one-hot 4 x 600 matrices.  For each sequence, the network had to 
simultaneously predict whether this site was open or closed in each cell type.  

They use mini-batch stochastic gradient descent (RMSprop) to train the network, with (now) standard tricks for regularization like batch-norm & 
dropout.  They also cleverly make use of Bayesian optimization to tune their hyper-parameters via the excellent 
[Spearmint](https://github.com/HIPS/Spearmint) package.  They compare to state of the art predictors that learn complex kernels (gkm-SVM in this case), 
and win handily.  Satisfied with their ability to predict accessibility, they perform neat experiments of in-silico mutagenisis to try and nail down 
which SNPs might have the greatest effect on accessibility.  They also inspect the final forms of their first layer convolutional filters, interpreting 
them as PSSMs.  Here results seem mixed; some filters are clear matches for known TF binding sites, others are merely indicative of more general 
aspects of local sequence state (AT rich regions, for example).  

### My two cents

If a person from an NLP or computer vision background were to check out this model (pictured as figure 1), it might not elicit much 
excitement.  "What's the big deal?  It's a convnet with multi-task binary output prediction".  The big deal is that only recently have people 
figured out how to make convents work properly on sequence predition problems for biological sequences.  And from my perspective, this is the best 
effort yet.  Not only because their code is most readily accessible, but also because their experiments are meticulously documented, and their data set 
is readily compiled.  The authors considerable effort to produce a robust software tool that yields reproducible results is a huge step forward for 
computational biology.  

It took me a bit of extra effort to try this out.  For strange reasons, we can't run Torch natively on our GPU-capable cluster nodes.  It's related to 
the version of CentOS running on each node, and the constraints for kernels & version of glibc this entails.  Happily, docker now exists and can 
stomp all goombas (**n. m.** dependency related problems); you'll find my version on [docker hub](https://hub.docker.com/r/lzamparo/basset/).

I'm really interested in two extensions of this paper.  The first figuring out how to look at much longer input sequences.  We know from various other
assays (e.g HiC) that there are longer genomic distance dependencies of cis-sequence which could determine accessibility, so finding an efficient way
to consider longer input sequences would be interesting (maybe some attention mechanism so the model learns where to pay attention would help mitigate
the computational burden).  The second is figuring out how to use these predicitons of accessibility to improve gene expression prediction.  By 
combining a model like this with a dataset like GTex, I think we could get really interesting results.  
