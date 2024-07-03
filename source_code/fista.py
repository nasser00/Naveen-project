def fista(y, H, my_lambda, alpha, Nit):
    """
    Perform FISTA algorithm.

    Parameters:
    y : numpy.ndarray
        Observed signal.
    H : numpy.ndarray
        Forward operator.
    lambda_ : float
        Regularization parameter.
    alpha : float
        Must satisfy alpha >= max(eig(H.T @ H)).
    Nit : int
        Number of iterations.

    Returns:
    x : numpy.ndarray
        Result of deconvolution.
    J : numpy.ndarray
        Objective function values.
    """
    J = np.zeros(Nit)  # Objective function
    x = np.zeros(H.shape[1])  # Initialize x
    T = my_lambda/ (2 * alpha) # finding  alpha by use power method  alpha=maxeigenvalue(A.T*A) A is toeplitz matrix
    
    t = 1  # Variables used for FISTA
    yk = x
    HT = H.T

    for k in range(Nit):
        tmpx = x  # Keep old model and use yk instead of x
        
        Hx = H @ x
        x = thresh(yk - (HT @ (Hx - y)) / alpha, 's', T)
        J[k] = np.sum(np.abs(Hx - y)**2) + my_lambda * np.sum(np.abs(x))
        
        # FISTA part
        tmpt = t
        t = (1 + np.sqrt(1 + 4 * t**2)) / 2
        yk = x + (tmpt - 1) / t * (x - tmpx)  # Update new model to be thresholded
    
    return x, J
