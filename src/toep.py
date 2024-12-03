import numpy as np
def toep(w,p):
    """
    input
    p=length of data vector
    w= wavelet vector
    output
    A=toeplitz matrix of  source wavelet
    """
    q=len(w)
    col=np.hstack((w,np.zeros(p-q)))  #first column and first row of toeplitz matr
    row=np.hstack((w[0],np.zeros(p-q)))
    from scipy.linalg import toeplitz
    A=toeplitz(col,row)
    return(A)