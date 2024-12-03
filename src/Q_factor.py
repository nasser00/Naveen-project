def quality_factor(x_sol,x_true):
    import numpy as np
    """
    input 
    r_sol= recovered reflectivity series 
    r_true=true reflectivity series
    
    output
    Q=quality factor
    """
    Q=10*np.log10((np.linalg.norm(x_true))**2/((np.linalg.norm(x_true-x_sol))**2))
    return Q