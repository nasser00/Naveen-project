def cauchy(A,b,xo,my_lambda,Max_iter):
    i=0
    import numpy as np
    while i<Max_iter: 
        temp=(np.dot(A,xo)-b)
        r=np.dot(A.T,temp) +(my_lambda/2)*(np.divide(xo,((xo**2/2)+1)))
        beta=0.005;#np.dot(r.T,r)/np.dot(r.T,np.dot(A.T,b))
        y=xo
        xo=xo-beta*r
        xnew=xo
        if np.linalg.norm(xnew-y)<0.0001:
            break
        else:
            i=i+1
            
    x_sol=xnew;
    final_iter=i;

    return x_sol,final_iter