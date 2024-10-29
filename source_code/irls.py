def irls(A,d,x,my_lambda,out,inn):
    """
    A=source wavelet matrix
    b= data vector
    my_lambda=regularization parameter
    x=initial guess
    Max_iter= no of iteration
    
    out=outer loop iteration for updating weights   
    inn=inner loop iteration for updating gradient and solution  
    output
    x=solution of our data
    """
    import numpy as np
    epsilon=0.05  
    for i in  range(out):
        Q=np.diag(1/(np.abs(x)+epsilon)) #weight add small no to avoid division by zero
        for i in range(inn):
            grad=A.T@(A@x-d)+my_lambda*(Q.T@Q)@x  #include weight in regularization term
            x=x-0.01*grad
    return x,Q
        
