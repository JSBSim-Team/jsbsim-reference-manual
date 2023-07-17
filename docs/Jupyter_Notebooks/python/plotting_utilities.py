def add_arrow_to_line2D(axes, line, arrow_locs=[0.2, 0.4, 0.6, 0.8],arrowstyle='-|>', arrowsize=1, transform=None):
    
    """
    Add arrows to a matplotlib.lines.Line2D at selected locations.

    Parameters:
    -----------
    axes: 
    line: list of 1 Line2D obbject as returned by plot command
    arrow_locs: list of locations where to insert arrows, % of total length
    arrowstyle: style of the arrow
    arrowsize: size of the arrow
    transform: a matplotlib transform instance, default to data coordinates

    Returns:
    --------
    arrows: list of arrows
    """
    
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.lines as mlines
    import matplotlib.patches as mpatches

    if (not(isinstance(line, list)) or not(isinstance(line[0],mlines.Line2D))):
        raise ValueError("expected a matplotlib.lines.Line2D object")
    
    x, y = line[0].get_xdata(), line[0].get_ydata()

    arrow_kw = dict(arrowstyle=arrowstyle, mutation_scale=10*arrowsize)
    color = line[0].get_color()
    
    use_multicolor_lines = isinstance(color, np.ndarray)
    if use_multicolor_lines:
        raise NotImplementedError("multicolor lines not supported")
    else:
        arrow_kw['color'] = color

    linewidth = line[0].get_linewidth()
    if isinstance(linewidth, np.ndarray):
        raise NotImplementedError("multiwidth lines not supported")
    else:
        arrow_kw['linewidth'] = linewidth

    if transform is None:
        transform = axes.transData

    arrows = []
    for loc in arrow_locs:
        s = np.cumsum(np.sqrt(np.diff(x) ** 2 + np.diff(y) ** 2))
        n = np.searchsorted(s, s[-1] * loc)
        arrow_tail = (x[n], y[n])
        arrow_head = (np.mean(x[n:n + 2]), np.mean(y[n:n + 2]))
        p = mpatches.FancyArrowPatch(
            arrow_tail, arrow_head, transform=transform,
            **arrow_kw)
        axes.add_patch(p)
        arrows.append(p)
    return arrows

#
#=======================================================================================================================
#    

def make_axis_equal_3d(x_data,y_data,z_data,axes,to_scale="XYZ"):
    """
    Makes sure that all the three axis, including the z-axis, are represented with the same
    scale and include all data. It is done by creating a fake bounding box around data.
    """
    
    import numpy as np
    
    # Create cubic bounding box to simulate equal aspect ratio
    max_range = np.array([x_data.max()-x_data.min(), y_data.max()-y_data.min(), z_data.max()-z_data.min()]).max()
    Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(x_data.max()+x_data.min())
    Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(y_data.max()+y_data.min())
    Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(z_data.max()+z_data.min())
    
    # Comment or uncomment following both lines to test the fake bounding box:
    if to_scale == 'XYZ':
        for xb, yb, zb in zip(Xb, Yb, Zb):
            axes.plot([xb], [yb], [zb], 'w')
    elif to_scale == 'XY':
        for xb, yb in zip(Xb, Yb):
            axes.plot([xb], [yb], 'w')