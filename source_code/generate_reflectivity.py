import numpy as np
import matplotlib.pyplot as plt
def random_reflectivity (l):
    """
    input
    
    l= length of reflectivity series 
    output
    
    r= reflectivity sereis 

    """
    
    # making seed ID
    np.random.seed(1)
    #Generate a random reflectivity series of length l by normal distribution, raised to the 7th power
    r= (np.random.normal(0, 1, l))**7
    r=r/max(r)
    return(r)
