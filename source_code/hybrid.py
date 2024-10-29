def hybrid(A,b,xo,my_lambda,Max_iter,e):
    """
    input
    A=source wavelet matrix
    b= data vector
    my_lambda=regularization parameter
    xo=initial guess
    Max_iter= no of iteration
    e=scaling factor
    output
    x_sol=solution of our data
    final_iter=no of iterations taken 
    
    
    """
    import numpy as np
    i=0
    while i<Max_iter: 
        temp=(np.dot(A,xo)-b)
        #use Re(x)norm in regularization term insted of L2 norm 
        #Re(x)=sqrt(x^2+e^2)-e
        #derivative of Re(x)=x/sqrt(x^2+e^2)
        r=np.dot(A.T,temp) +(my_lambda/2)*(np.divide(xo,(np.sqrt((xo)**2+e**2)))) 
        beta=0.1;#learning rate for algorithm or np.dot(r.T,r)/np.dot(r.T,np.dot(A.T,b))
        y=xo
        xo=xo-beta*r #updating solution 
        xnew=xo
        if np.linalg.norm(xnew-y)<0.0001: #stopping criteria
            break
        else:
            i=i+1
            
    x_sol=xnew;
    final_iter=i;

    return x_sol,final_iter
