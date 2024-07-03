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
    if sorh == 's':
        tmp = np.abs(x) - t
        tmp = (tmp + np.abs(tmp)) / 2
        y = np.sign(x) * tmp
    elif sorh == 'h':
        y = x * (np.abs(x) > t)
    else:
        raise ValueError('Invalid argument value for sorh. Use "s" for soft or "h" for hard.')
    
    return y
