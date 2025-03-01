def power_method(H, x, max_iter=10):
    """
    Perform the power method to find the dominant eigenvalue of a matrix.

    Parameters:
    x0 : numpy.ndarray
        Initial vector.
    H : numpy.ndarray
        Matrix for which to find the dominant eigenvalue.
    num_iter : int
        Number of iterations.

    Returns:
    value : float
        Dominant eigenvalue of the matrix H.
    """
    
    import numpy as np
    HT = H.T
    for k in range(max_iter):
        aux = np.dot(H, x)
        y = np.dot(HT, aux)
        n = np.linalg.norm(x)
        x = y / n
        value = n
#         print(k,value)
    return value


