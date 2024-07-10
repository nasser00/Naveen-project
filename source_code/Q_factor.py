def quality_factor(r_sol,r_true):
    import numpy as np
    """
    input 
    r_sol= recovered reflectivity series 
    r_true=true reflectivity series
    
    output
    Q=quality factor
    """
    Q=10*np.log10((np.linalg.norm(r_true))**2/((np.linalg.norm(r_true-r_sol))**2))
    return Q
