import numpy as np

from .mvgavg import fnjn_mvgavg, cumsum_mvgavg, binning_mvgavg

def mvgavg(a, n, axis=0, weights=False, binning=False):
    """
    Performs a moving average along a single axis

    Parameters
    ----------
    a : array_like
        Array to be averaged
    n : int
        Width of the moving average
    axis: int
        Axis along which the moving average is to take place, 0 if unspecified
    weights: 'pascal', 'triangle', 'quadratic', or a list
        weights to multiply the moving average by
    binning:
        Bins the values rather than 

    Returns
    -------
    mvgavg : nd_array
        An array with the elements averaged over a length of n.  The array will be
        of a length n-1 shorter than the original along the chosen axis, unless 
        binning=True, in which case it will return an array n times shorter along
        the chosen axis.
    
    See Also
    --------
    ndarray.mean : equivalent to setting n equal to the length of data along
        the specified axis

    Notes
    -----
    Consider the list [a, b, c, d, e....] with a moving average of length 3.  The
    First element in the list will be (a+b+c)/3.  The next (b+c+d)/3.  And so on.
    The result is a smoothed version of the original data with length (n-1) shorther
    than the original data.  This works with arrays of any dimension, summing along
    as it goes. This function will sometimes fail for a ragged array.  Use a list
    comprehension with np.mvgavg embedded in it instead.

    If you have any doubts of how a moving average works, try it out with an array of
    symbols in sympy.

    axis
    -----
    The axis parameter controls the axis over which the moving average happens. In a
    2D array, for instance, for axis=0, the array will average along the columns, and
    axis=1 will average along the rows.

    Binning vs Unbinned
    --------------------
    Consider the array [a b c d e... ] that is being averaged to the product array,
    [A B C D... ] over a distance of 3. If binning = False:

        A = [a b c]/3
        B =   [b c d]/3
        C =     [c d e]/3 
        D =       [d e f]/3
        ....

    but if binning = True:

        A = [a b c]/3
        B =       [d e f]/3
        C =             [g h i]/3
        .....

    Thus, a binned moving average decreases the array length by a factor of n. This
    throws out some precision but greatly decreases computational time for very 
    long arrays.

    Examples
    --------
    >>> from mvgavg import mvgavg
    >>> 
    >>> example_array=[[i,(-1)**i] for i in np.arange(5)]
    >>> mvgavg(example_array,2)
    array([[0.5, 0. ],
           [1.5, 0. ],
           [2.5, 0. ],
           [3.5, 0. ]])
    >>> mvgavg(example_array,2,axis=1)
    array([[0.5],
           [0. ],
           [1.5],
           [1. ],
           [2.5]])

    """
    if binning:
        return binning_mvgavg(np.asarray(a),n,axis=axis)
    else:
        if weights:
            return fnjn_mvgavg(np.asarray(a),n,axis=axis,weights=weights)
        else:
            return cumsum_mvgavg(np.asarray(a),n,axis=axis)



