import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def GenerateTimeLine(data, title="Timeline", xaxis_format="%d %b", day_interval=5, figsize=(8, 5)):
    """Generates timeline from a pandas dataframe

    data : Pandas dataframe with datetimeindex
    titile  Title of the plot
    zaxis_format ="%d %b %Y" valids strdate format
    dayinterval =1 default, can be anything

    Insipred from Matplotlib's excellent examples

    author: sukhbinder
    date 5/6/2018
    """
    levels = np.array([-5, 5, -3, 3, -1, 1])
    fig, ax = plt.subplots(figsize=figsize)
    # Create the base line
    start = min(data.index)
    stop = max(data.index)
    ax.plot((start, stop), (0, 0), 'k', alpha=.5)
    # Iterate through data annoting each one
    for ii, (idate, iname) in enumerate(data.itertuples()):
        level = levels[ii % 6]
        vert = 'top' if level < 0 else 'bottom'

        ax.scatter(idate, 0, s=100, facecolor='w', edgecolor='k', zorder=9999)
        # Plot a line up to the text
        ax.plot((idate, idate), (0, level), c='r', alpha=.7)
        # Give the text a faint background and align it properly
        ax.text(idate, level, iname,ha='right', va=vert, fontsize=14,
                backgroundcolor=(1., 1., 1., .3))
    ax.set(title=title)
    # Set the xticks formatting
    # format xaxis with days intervals
    ax.get_xaxis().set_major_locator(mdates.DayLocator(interval=day_interval))
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter(xaxis_format))
    fig.autofmt_xdate()
    # Remove components for a cleaner look
    plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
              list(ax.spines.values())), visible=False)
    
    return ax
