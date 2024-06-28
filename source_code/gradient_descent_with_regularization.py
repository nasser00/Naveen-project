def decon_reg(A,b,xo,my_lambda,Max_iter):
    """
    input
    
    A=source wavelet matrix
    b= data vector
    my_lambda=regularization parameter
    xo=initial guess
    Max_iter= no of iterations
    
    output
    
    x_sol=solution of our data
    final_iter=no of iterations taken 
    
    """
    i=0
    while i<Max_iter: 
        temp=(np.dot(A,xo)-b)
        r=np.dot(A.T,temp)+my_lambda*xo   # calculating residual with regularization term
        beta=0.1;  #np.dot(r.T,r)/np.dot(r.T,np.dot(A.T,b)) #learning rate
        y=xo
        xo=xo-beta*r                       #update the solution 
        xnew=xo
        if np.linalg.norm(xnew-y)<0.0001:    #stopping criteria
            break
        else:
            i=i+1
            
    x_sol=xnew;
    final_iter=i;

    return x_sol, final_iter
