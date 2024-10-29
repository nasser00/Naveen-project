def cauchy(A,b,xo,my_lambda,Max_iter,a):
    """
    A=source wavelet matrix
    b= data vector
    my_lambda=regularization parameter
    xo=initial guess
    Max_iter= no of iteration
    epsilon =thresholding parameter  
    output
    x_sol=solution of our data
    final_iter=no of iterations taken 
    """
    import numpy as np 
    i=0
    while i<Max_iter: 
        temp=(np.dot(A,xo)-b)
        r=np.dot(A.T,temp) +(my_lambda)*((2*xo)/(xo**2+a))
        beta=0.005;#np.dot(r.T,r)/np.dot(r.T,np.dot(A.T,b))
        y=xo
        xo=xo-beta*r
        if np.linalg.norm(r)<0.0000001:
            break
        else:
            i=i+1
            
    x_sol=xo;
    final_iter=i;

    return x_sol,final_iter