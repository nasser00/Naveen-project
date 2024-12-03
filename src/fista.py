# soft and hard thresholding
def thresh(x, sorh, t):
    """
    Perform soft or hard thresholding.

    Parameters:
    x : numpy.ndarray
        Input vector or matrix.
    sorh : str
        Thresholding type ('s' for soft, 'h' for hard).
    t : float
        Threshold value.

    Returns:
    y : numpy.ndarray
        Thresholded output.
    """
    
    import numpy as np
    if sorh == 's':
        tmp = np.abs(x) - t
        tmp = (tmp + np.abs(tmp)) / 2
        y = np.sign(x) * tmp
    elif sorh == 'h':
        y = x * (np.abs(x) > t)
    else:
        raise ValueError('Invalid argument value for sorh. Use "s" for soft or "h" for hard.')
    
    return y

def fista(H, d, _lambda, alpha, Nit):
    """
    Perform FISTA algorithm.

    Parameters:
    y : numpy.ndarray
        Observed signal.
    H : numpy.ndarray
        Forward operator.
    _lambda : float
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
    import numpy as np
    J = np.zeros(Nit)  # Objective function
    x = np.zeros(H.shape[1])  # Initialize x
    T = _lambda/ (2 * alpha) # finding  alpha by use power method  alpha=maxeigenvalue(A.T*A) A is toeplitz matrix
    
    t = 1  # Variables used for FISTA
    yk = x
    HT = H.T

    for k in range(Nit):
        x1 = x  # Keep old model and use yk instead of x
        
        Hx = H @ x
        x = thresh(yk - (HT @ (Hx - d)) / alpha, 's', T)
        J[k] = np.sum(np.abs(Hx - d)**2) + _lambda * np.sum(np.abs(x))
        
        # FISTA part
        t1 = t
        t = (1 + np.sqrt(1 + 4 * t**2)) / 2
        yk = x + (t1 - 1) / t * (x - x1)  # Update new model to be thresholded
    
    return x, J
