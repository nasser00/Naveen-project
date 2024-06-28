def generate_data_noise(y,r,noise_level):
    """
    input 
    y=source wavelet matrix
    r=reflectivity series 
    noise=standard deviation 
    output 
    d=synthetically generated data with noise 
    """
    d=np.convolve(y,r) #convolution of walelet and reflectivity
    noise = np.random.normal(loc=0, scale=noise_level, size=d.shape)
    d_new = d+ noise
    return(d_new,d)

