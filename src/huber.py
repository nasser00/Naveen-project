import numpy as np
def steepest_descent_reg_huber(A,b,x0,beta,_lambda,epsilon, Max_iter):
    """
    A=source wavelet matrix
    b= data vector
    beta=gradient step size update
    _lambda=regularization parameter
    x0=initial guess
    epsilon: huber norm epsilon parameter: must be small to mimic l1 norm
    Max_iter= no of iteration
        
    output
    x_sol=solution of our data
    final_iter=no of iterations taken 
    """
    i=0
    x=x0
    while i<Max_iter: 
        temp=(np.dot(A,x)-b)
        r=np.dot(A.T,temp) #DEFINING RESIDUAL
        v=np.zeros(len(x))
        for i in range(len(x)): # derivative of huber norm
            if np.abs(x[i])<=epsilon:
                v[i]=x[i]/epsilon
            else:
                v[i]=np.sign(x[i])
        r=r+(_lambda/2)*v    #  complete residual 
        #np.dot(r.T,r)/np.dot(r.T,np.dot(A.T,b))
        y=x
        x=x-beta*r
        xnew=x
        if np.linalg.norm(xnew-y)<0.00001:#stopping criteria
            break
        else:
            i=i+1        
    x_sol=xnew;
    final_iter=i;
    return x_sol, final_iter