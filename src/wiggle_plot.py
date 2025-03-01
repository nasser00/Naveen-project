import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def wiggle_plot(data, time, trace_offset, fill_color, linewidth, ax, title, xlabel, ylabel, label):
    """
    Create a publication-quality wiggle plot from seismic data within a given axis.

    Parameters:
    - data: 2D numpy array of shape (n_samples, n_traces)
    - time: 1D numpy array representing time samples (default: np.arange(n_samples))
    - trace_offset: float value to control the horizontal offset between traces
    - fill_color: color used to fill the positive lobes
    - linewidth: line width for the wiggles
    - ax: Matplotlib axis object where the wiggle plot should be drawn
    - title: title for the plot
    - xlabel: label for the x-axis
    - ylabel: label for the y-axis
    - label: label for figure

    The function modifies the given subplot (`ax`).
    """

    n_samples, n_traces = data.shape

    # Create a default time axis if none is provided.
    if time is None:
        time = np.arange(n_samples)

    # Normalize each trace individually for consistent amplitude scaling.
    norm_data = data / np.max(np.abs(data), axis=0)

    # Set the Seaborn style
    sns.set_style('whitegrid')

    # Loop through each trace to plot the wiggle and fill positive lobes.
    for i in range(n_traces):
        offset = i * trace_offset
        trace = norm_data[:, i] + offset  # Offset each trace horizontally.
        ax.plot(trace, time, color='k', linewidth=linewidth)  # Plot the wiggle line.
        ax.fill_betweenx(time, offset, trace, where=(trace > offset),
                         facecolor=fill_color, interpolate=True)

    # Invert the y-axis to follow seismic plotting conventions.
    ax.invert_yaxis()

    # Set labels and title.
    ax.xaxis.tick_top()  # Move x-axis to top
    ax.xaxis.set_label_position('top')  # Move x-axis label to top
    ax.set_xlabel(xlabel, fontsize=20, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=20, fontweight='bold')
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.text(-0.1, 1.2, label, transform=ax.transAxes, fontsize=24, fontweight='bold',
            ha='right', va='top', color='black')

    # Customize tick parameters.
    ax.tick_params(axis='both', which='major', labelsize=16)
