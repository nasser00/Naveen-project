def irls_cg(A, d, x0, _lambda, out_maxiter, cg_maxiter):
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
    
    def conjugate_gradient_reg_Q(A, Q, d, x0, _lambda, max_iter=1000, tol=1e-6):
        """
        Conjugate Gradient Method to solve the regularized least squares problem:
        ||Ax - b||_2^2 + lambda * ||Q x||_2^2. where Q=diag(1.(|x|+epsilon))

        Parameters:
        A        : np.array, shape (m, n) - The convolutional matrix.
        d        : np.array, shape (m, ) - The recorded data.
        _lambda      : float - Regularization parameter.
        tol      : float - Tolerance for convergence.
        max_iter : int - Maximum number of iterations.

        Returns:
        x : np.array, shape (n, ) - Solution vector.
        """
        # Define H = A^T A + lambda * I
        m, n = A.shape
        H = np.dot(A.T, A) + _lambda * np.dot(Q.T, Q)
        d_tilde = np.dot(A.T, d)

        # Initialize variables
        x = x0 
        r = d_tilde - np.dot(H, x)
        p = r.copy()
        rs_old = np.dot(r.T , r)

        for i in range(max_iter):
            Hp = np.dot(H , p)
            alpha = rs_old / (np.dot(p.T, Hp))
            x = x + alpha * p
            r = r - alpha * Hp

            # Check for convergence
            rs_new = np.dot(r.T, r)
            #if np.sqrt(rs_new) < tol:
            #    print(f"Converged in {i+1} iterations.")
            #    break

            # Update p with the conjugate direction
            beta = 0.1#rs_new / rs_old
            p = r + beta * p
            rs_old = rs_new

        x_sol=x;
        final_iter=i;

        return x_sol, final_iter
    
    epsilon=1e-2  
    x=x0
    for i in  range(out_maxiter):
        Q=np.diag(1/(np.abs(x)+epsilon)) # add small positive number to avoid division by zero
        x, final_iter_cg=conjugate_gradient_reg_Q(A, Q, d, x0, _lambda, cg_maxiter, tol=1e-6)
    return x,Q