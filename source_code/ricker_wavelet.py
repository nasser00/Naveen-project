import numpy as np
import matplotlib.pyplot as plt

def ricker_wavelet(frequency, dt, length,phase_shift =np.pi/2):
    """
    input
    
    frequency=dominent frequency of ricker wavelet
    dt=sampling interval
    length=length of signal
    phase_shift = phase rotation
    
    output
    
    w =ricker wavelet
    t=time array
    """
#     time array centered around zero
    t = np.linspace(0, length , int(length / dt))
#     Ricker wavelet in the time domain
    x = (1.0 - 2.0 * (np.pi ** 2) * (frequency ** 2) * ((t - length / 2) ** 2)) * \
              np.exp(-(np.pi ** 2) * (frequency ** 2) * ((t - length / 2) ** 2))
    n = len(x)
#     frequency bins for the FFT
    freqs = np.fft.fftfreq(n, dt)
#     Fourier transform of the Ricker wavelet
    y_fft = np.fft.fft(x)
#     introduce phase shift factor in frequency domain 
    phase_shift_factor = np.exp(1j * phase_shift*np.sign(freqs))
    y_fft_shifted = y_fft * phase_shift_factor
#     inverse FFT to get  phase-shifted wavelet in the time domain
    w = np.real(np.fft.ifft(y_fft_shifted))
    return w,t



