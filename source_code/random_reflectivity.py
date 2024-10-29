import numpy as np
import matplotlib.pyplot as plt

def random_reflectivity(l, dt):
    """
    Generate a random reflectivity series.
    
    Parameters:
    l : int
        Length of the reflectivity series.
    dt : float
        Time interval between samples in seconds (default is 0.001 seconds).
        
    Returns:
    time : numpy.ndarray
        Time vector for the reflectivity series.
    r : numpy.ndarray
        Reflectivity series.
    """
    # Set seed for reproducibility
    np.random.seed(1)
    # Generate random reflectivity series and normalize
    r = (np.random.normal(0, 1, l))**7
    r = r / max(r)
    
    # Create a time vector based on the length and sampling interval
    time = np.arange(0, l * dt, dt)
    return time, r
