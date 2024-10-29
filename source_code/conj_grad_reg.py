import numpy as np
def conj_grad_reg(A, b, xo,my_lambda,Max_iter,tol=0.000001):
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
    a=A
    A=np.dot(a.T,a)
    b=np.dot(a.T,b) # replacing A by 𝑨^𝑻 𝑨 and b by 𝑨^𝑻 𝒃 (normalize equation)
    A=A+my_lambda*np.eye(A.shape[0])
    x = xo
    r = np.dot(A, x)-b #residual
    d = r                #initial search direction
    rs_old = np.dot(r.T, r)
    i=1
    mat_norm=[]
    while i<Max_iter:
        Ad = np.dot(A, d)
        beta = rs_old / (np.dot(d.T, Ad)) #learning rate beta
        x = x - beta * d                #updating solution
        r = r - beta * Ad               #updating residual
        rs_new = np.dot(r.T, r)  
        if np.sqrt(rs_new) < tol:       #stopping criteria
            break
        d = r + (rs_new / rs_old) * d  #updating  search direction 
        rs_old = rs_new
        i=i+1
    x_sol=x;
    final_iter=i;

    return x_sol, final_iter

