import numpy as np
from scipy.fft import fft, ifft

def bp_filter_1D(d, dt, f1, f2, f3, f4):
    """
    BP_Filter: Apply a band-pass filter to a group of traces.

    input:
    ----------
    d : numpy.ndarray
        Input data array where each column represents a trace.
    dt : float
        Sampling interval in seconds.
    f1 : float
        Lower frequency cutoff in Hz.
    f2 : float
        Lower transition frequency in Hz.
    f3 : float
        Upper transition frequency in Hz.
    f4 : float
        Upper frequency cutoff in Hz.

    output:
    -------
    d_f : numpy.ndarray
        Filtered output (columns are traces).
    """

    nt = d.shape[0]
    k = int(np.ceil(np.log2(nt)))
    nf = 4 * (2 ** k)

    i1 = int(np.floor(nf * f1 * dt)) + 1
    i2 = int(np.floor(nf * f2 * dt)) + 1
    i3 = int(np.floor(nf * f3 * dt)) + 1
    i4 = int(np.floor(nf * f4 * dt)) + 1

    up = np.arange(1, i2 - i1 + 1) / (i2 - i1)
    down = np.arange(i4 - i3, 0, -1) / (i4 - i3)
    aux = np.concatenate((np.zeros(i1), up, np.ones(i3 - i2), down, np.zeros(nf // 2 + 1 - i4)))
    aux2 = np.flip(aux[1:nf // 2])

    c = 0  # zero phase (could apply rotations as well)
    F = np.concatenate((aux, aux2))
    Phase = (np.pi / 180.) * np.concatenate(([0.], -c * np.ones(nf // 2 - 1), [0.], c * np.ones(nf // 2 - 1)))
    Transfer = F * np.exp(-1j * Phase)

    D = fft(d, nf, axis=0)

    D_f = np.zeros_like(D, dtype=np.complex128)
    #for k in range(nx):
    D_f = Transfer * D

    o = ifft(D_f, nf, axis=0)

    d_f = np.real(o[:nt])

    return o