import numpy as np
def conj_grad_reg(A, d, x0, _lambda, max_iter=1000, tol=1e-6):
    """
    Conjugate Gradient Method to solve the regularized least squares problem:
    ||Ax - b||_2^2 + lambda * ||x||_2^2.
    
    Parameters:
    A        : np.array, shape (m, n) - The convolutional matrix.
    d        : np.array, shape (m, ) - The recorded data.
    _lambda  : Regularization parameter.
    tol      : Tolerance for convergence.
    max_iter : Maximum number of iterations.
    
    Returns:
    x : np.array, shape (n, ) - Solution vector.
    """
    # Define H = A^T A + lambda * I
    m, n = A.shape
    H = np.dot(A.T, A) + _lambda * np.eye(n)
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
        if np.sqrt(rs_new) < tol:
        #    print(f"Converged in {i+1} iterations.")
            break
        
        # Update p with the conjugate direction
        beta = rs_new / rs_old
        p = r + beta * p
        rs_old = rs_new
    
    x_sol=x;
    final_iter=i;

    return x_sol, final_iter

