import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


def wiggle(data,
           time,
           xpos,
           ax=None,
           skip=1,
           perc=99.0,
           gain=1.0,
           oversampling=100,
           rgb=(0, 0, 0),
           alpha=1.0,
           lw=0.5,
           time_units='s'):
    """
    Plots wiggle traces of seismic data.
    
    Args:
        data (ndarray): 2D seismic array (ntraces x ntimes).
        time (ndarray): 1D array of time samples.
        xpos (ndarray): 1D array of x positions (traces).
        ax (Axes): Matplotlib Axes object (optional).
        skip (int): Skip=1, every trace; skip=2, every second trace, etc.
        perc (float): Percentile to scale the data, default 99%.
        gain (float): Gain applied to the data.
        oversampling (int): Number of samples for interpolation to smooth traces.
        rgb (tuple): 3-tuple specifying the RGB color for traces.
        alpha (float): Opacity of the fill (default 1.0).
        lw (float): Line width of the trace lines (default 0.5).
        time_units (str): Units of time axis, 's' for seconds, 'ms' for milliseconds.

    Returns:
        Axes: A Matplotlib Axes object with the wiggle plot.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(2, 6))

    ntraces, nt = data.shape
    rgba = list(rgb) + [alpha]
    sc = np.percentile(data, perc)  # Normalization factor
    wigdata = data[::skip, :]
    # xpos = np.arange(ntraces)[::skip]  # If you need default x positions

    # Convert time to the desired units
    if time_units == 'ms':
        t = 1000 * time  # Convert seconds to milliseconds
    else:
        t = time

    for x, trace in zip(xpos, wigdata):
        # Compute high-resolution trace
        amp = gain * trace / sc + x
        hypertime = np.linspace(t[0], t[-1], (oversampling * t.size - 1) + 1)
        interp = interp1d(t, amp, kind='cubic')
        hyperamp = interp(hypertime)

        # Plot the trace line, then the filled area
        ax.plot(hyperamp, hypertime, color=rgb, lw=lw)
        ax.fill_betweenx(hypertime, hyperamp, x,
                         where=hyperamp > x,
                         facecolor=rgba,
                         interpolate=True,
                         lw=0)

    ax.invert_yaxis()  # Seismic convention to plot time increasing downwards
    plt.tight_layout()
    return ax
