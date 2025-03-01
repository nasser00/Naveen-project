import numpy as np
def nextpow2(n):
    # Returns the next power of 2 greater than or equal to n
    return int(np.ceil(np.log2(n)))

def inverse_radon_freq(d, dt, h, q, N, flow, fhigh):
    # INVERSE_RADON_FREQ: Inverse linear or parabolic Radon transform.
    #                    Frequency domain alg.
    '''
    
     IN   d:     seismic traces   
          dt:    sampling in sec
          h(nh): offset or position of traces in meters
          q(nq): ray parameters  if N=1
                 residual moveout at far offset if N=2
          N:     N=1 Linear tau-p  
                 N=2 Parabolic tau-p
          flow:  freq.  where the inversion starts in HZ (> 0Hz)
          fhigh: freq.  where the inversion ends in HZ (< Nyquist) 
          mu:    regularization parameter 
          sol:   sol='ls' least-squares solution
                 sol='adj' adjoint
    
     OUT  m:     the linear or parabolic tau-p panel
     '''
    
    
    
    nt, nh = d.shape
    nq = np.max(np.size(q))
   

    if N == 2:
        h = h / np.max(np.abs(h))
        
    nfft = 2 * (2 ** nextpow2(nt))

    D = np.fft.fft(d, nfft, axis=0)
    M = np.zeros((nfft, nq), dtype=complex)
    

    ilow = max(int(np.floor(flow * dt * nfft)), 1)
    ihigh = min(int(np.floor(fhigh * dt * nfft)), nfft // 2)

    
    for ifreq in range(ilow, ihigh + 1):
        
        f = 2. * np.pi * (ifreq - 1) / (nfft * dt)
        L = np.exp(1j * f * np.outer(np.power(h, N), q))
        
        y = D[ifreq, :].copy()
        x = np.conjugate(L).T @ np.conjugate(y)
        
       
        M[ifreq, :] = np.conjugate(x)
        M[nfft - ifreq, :] = x

    M[nfft // 2, :] = np.zeros(nq)
    m = np.fft.ifft(M, axis=0).real
    m = m[0:nt, :]
    return m

def forward_radon_freq(m, dt, h, q, N, flow, fhigh):
    import numpy as np

    nt, nq = m.shape

    nh = np.max(np.size(h))

    if N == 2:
        h = (h / np.max(np.abs(h))) ** 2

    nfft = 2 * (2 ** nextpow2(nt))

    M = np.fft.fft(m, n=nfft, axis=0)
    D = np.zeros((nfft, nh), dtype=complex)

    ilow = max(int(np.floor(flow * dt * nfft)), 1)
    ihigh = min(int(np.floor(fhigh * dt * nfft)), nfft // 2)

    for ifreq in range(ilow, ihigh + 1):
        f = 2 * np.pi * (ifreq - 1) / (nfft * dt)
        L = np.exp(1j * f * np.outer(h, q))  # Shape: (nh, nq)
        x = M[ifreq, :].copy()  # Shape: (nq,)
        y = L @ np.conjugate(x)  # Shape: (nh,)

        D[ifreq, :nh] = np.conjugate(y)  
        D[nfft - ifreq, :nh] = y

    D[nfft // 2, :] = np.zeros(nh)
    d = np.fft.ifft(D, axis=0).real
    d = d[:nt, :]

    return d
