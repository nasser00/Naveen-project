import numpy as np
from scipy.signal import convolve
from scipy.signal.windows import hamming
def generate_data_noise(w,r,SNR):
    """
    input 
    y=source wavelet matrix
    r=reflectivity series 
    SNR= signal to noise ratio
    d=synthetically generated data with noise
    
    output
    d_new= noisy data given SNR
    d=data without noise 
    """
    #convolution of walelet and reflectivity
    d=np.convolve(y,r) 
    #Calculate the standard deviation of the noise-free data
    sed = np.std(d)   
    # Generate random noise with the same size as the data 
    noise = np.random.randn(*d.shape)   
    # Convolve the noise with a Hamming window of size 5x5
    hamming_window = hamming(5) 
    noise = np.convolve(noise, hamming_window, mode='same')
    # Calculate the standard deviation of the noise
    sen = np.std(noise)
    # Scale the noise to  desired SNR
    noise = noise * (sed / sen) / SNR
    d_new = d+ noise
    return(d,d_new)

