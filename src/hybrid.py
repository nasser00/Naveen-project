import numpy as np
def steepest_descent_reg_hybrid(A,b,x0,beta,_lambda,epsilon,Max_iter):
    
    """
    input
    A=source wavelet matrix
    b= data vector
    _lambda=regularization parameter
    x0=initial guess
    Max_iter= no of iteration
    epsilon: is Hybrid norm parameter, must be small to mimic l1 norm
    
    output
    x_sol=solution of our data
    final_iter=no of iterations taken 
    """
    i=0
    x=x0
    while i<Max_iter: 
        
        temp=(np.dot(A,x)-b)
        r=np.dot(A.T,temp) +(_lambda/2)*(np.divide(x,(np.sqrt(x**2+epsilon**2)))) 
        y=x
        x=x-beta*r #updating solution 
        xnew=x
        if np.linalg.norm(xnew-y)<0.00001: #stopping criteria
            break
        else:
            i=i+1
            
    x_sol=xnew;
    final_iter=i;

    return x_sol,final_iter