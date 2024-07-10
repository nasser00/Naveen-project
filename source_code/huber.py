def huber(A,b,xo,my_lambda,Max_iter):
    """
    A=source wavelet matrix
    b= data vector
    my_lambda=regularization parameter
    xo=initial guess
    Max_iter= no of iteration
        
    output
    x_sol=solution of our data
    final_iter=no of iterations taken 
    """
    import numpy as np
    i=0
    epsilon=0.001  
    while i<Max_iter: 
        temp=(np.dot(A,xo)-b)
        r=np.dot(A.T,temp) #DEFINING RESIDUAL
        v=np.zeros(len(xo))
        for i in range(len(xo)): # derivative of huber norm
            if np.abs(xo[i])<=epsilon:
                v[i]=xo[i]/epsilon
            else:
                v[i]=epsilon*np.sign(xo[i])
        r=r+(my_lambda/2)*v    #  complete residual 
        beta=0.01;#np.dot(r.T,r)/np.dot(r.T,np.dot(A.T,b))
        y=xo
        xo=xo-beta*r
        xnew=xo
        if np.linalg.norm(xnew-y)<0.00001:#stopping criteria
            break
        else:
            i=i+1        
    x_sol=xnew;
    final_iter=i;
    return x_sol, final_iter
