
# Regularized  Inversion Techniques

This projects uses different iterative methods to recover the reflectivity series from sesmic data. The package can be used for any linearized inversion problem.

Different algorithms included in the package :

1)Steepest Descent with smoothness regularization
2)Steepest Descent with sparsirty regularization (Huber, Cauchy, Hybrid and Hoyer squared norms)
3)Conjucate gradient with smoothness regularization
4)Conjucate gradient with sparsirty regularization (Iterative Re-wieghted Least squares Algorithm)
5) Fast Iterative Shrinkage Thresholding Algorithm
6) Alternating minimization Algorithm


We tested each algorithm  on  both synthetically  generated seismic data and real data .you  can get the code for each algorithms  in the `src` directory .Each algorithm works trace by trace 

## data
synthetic data generated is saved in   `data` directory.It contain data with noise and without noise.Also the source signature is stored in it 
# Application
Multiple supression using steepest descent with Hoyer norm for real and synthetic data  
## Results
Results are autmatically  store at results folder `results`.It contain results with noisy data and noise free data .It shows the deconvolution perform on 2D siesmic data set and multiple supression on real and synthetic data 

## Tutorial 
It contains five Demo files , all the Demo file must run in  must be run in `src` directory .
1)Demo_decon.ipynb:-1D deconvolution problem has performed in this demo on synthetic data

2)Demo_syn_decon_2D.ipynb:-2D deconvolution problem has performed in this demo on synthetic data

3)Demo_decon_real_2D.ipynb:-2D deconvolution problem has performed in this demo on real data

4)Demo_synthetic_radon.ipynb:- Multiple supression in synthetic data set 

5)Demo_real_radon.ipynb:-Multiple supression in real data set 
To deploy this project run Demos in present in   file in `src` directory  and make sure that you are in src directory
https://github.com/nasser00/Naveen-project/blob/main/src/tutorial.ipynb


## dependencies 
matplotlib      ==          3.7.1

numpy           ==          1.25.0

scipy           ==          1.10.1

