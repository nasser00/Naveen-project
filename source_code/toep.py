import numpy as np
def toep(p,wo):
    """
    input
    p=length of data vector
    wo= initial wavelet vector
    output
    A=toeplitz matrix of  sorce wavelet
    """
    q=len(wo)
    col=np.hstack((wo,np.zeros(p-q)))  #first column and first row of toeplitz matr
    row=np.hstack((wo[0],np.zeros(p-q)))
    from scipy.linalg import toeplitz
    A=toeplitz(col,row)
    return(A)
