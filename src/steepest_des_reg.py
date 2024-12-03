import numpy as np
def steepest_des_reg(A,b,x0, _lambda,Max_iter):
    """
    input
    
    A=source wavelet matrix
    b= data vector
    _lambda=regularization parameter
    x0=initial guess for solution
    beta=is step size for gradient update
    Max_iter= no of iterations
    
    output
    
    x_sol=solution of our data
    final_iter=no of iterations taken 
    
    """
    
    import numpy as np
    i=0
    x=x0
    H=np.dot(A.T,A)
    while i<Max_iter: 
        temp=(np.dot(A,x)-b)
        g=np.dot(A.T,temp)+_lambda*x   # calculating residual with regularization term
        k=(np.dot(H,g)+_lambda*g)
        beta=np.dot(g.T,g)/np.dot(g.T,k) #learning rate
        y=x
        x=x-beta*g                       #update the solution 
        xnew=x
        if np.linalg.norm(xnew-y)<0.0001:    #stopping criteria
            break
        else:
            i=i+1
            
    x_sol=xnew;
    final_iter=i;

    return x_sol, final_iter

