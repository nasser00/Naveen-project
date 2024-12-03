import numpy as np
def steepest_descent_reg_cauchy(A,b,x0,beta,_lambda,epsilon,Max_iter):
    """
    A=source wavelet matrix
    b= data vector
    _lambda=regularization parameter
    x0=initial guess
    Max_iter= no of iteration
    epsilon: is Cauchy parameter, must be small to mimic l1 norm
    output
    x_sol=solution of our data
    final_iter=no of iterations taken 
    """
    import numpy as np 
    i=0
    x=x0
    while i<Max_iter: 
        temp=(np.dot(A,x)-b)
        r=np.dot(A.T,temp) +(_lambda)*(np.divide(2*x,x**2+epsilon**2))
        x=x-beta*r
        if np.linalg.norm(r)<0.00001:
            break
        else:
            i=i+1
        #epsilon=0.01*max(np.abs(x)) # This types of update may result in better solutions
            
    x_sol=x;
    final_iter=i;

    return x_sol,final_iter