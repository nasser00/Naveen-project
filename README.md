
# Regularized  Inversion Techniques

This projects uses different iterative methods to recover the reflectivity series from sesmic data. The package can be used for any linearized inversion problem.

Different algorithms included in the package :

1)Steepest Descent with smoothness regularization
2)Steepest Descent with sparsirty regularization (Huber, Cauchy, Hybrid norms)
3)Conjucate gradient with smoothness regularization
4)Conjucate gradient with sparsirty regularization (Iterative Re-wieghted Least squares Algorithm)
5) Fast Iterative Shrinkage Thresholding Algorithm
5) Alternating minimization Algorithm


We tested each algorithm  on  both synthetically  generated seismic data and real data .you  can get the code for each algorithms  in the `src` directory .Each algorithm works on a single trace.

## data
synthetic data generated is saved in   `data` directory.It contain data with noise and without noise.Also the source signature is stored in it 
## Results
Results are autmatically  store at results folder `results`.It contain results with noisy data and noise free data

## Demo
To deploy this project run tutorial  file in source folder  and make sure that you are in src directory
https://github.com/nasser00/Naveen-project/blob/main/src/tutorial.ipynb


## dependencies 
matplotlib      ==          3.7.1

numpy           ==          1.25.0

scipy           ==          1.10.1

