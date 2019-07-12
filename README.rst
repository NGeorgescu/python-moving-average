======================
python-moving-average
======================

Why??
------
Numpy does not include a built-in moving average function as of yet.  
Most solutions are tedious and complicated. This solution is very nice.
This operates similar to the Wolfram Language's `MovingAverage[]` function, but
has the advantage that it can specify axis (Wolfram gets away with `f[#]&/@`, 
but that's a story for another day). 

Usage
------
See docs for examples.  But essentially, the usage is just:
::

    from mvgavg import mvgavg

    mvgavg(array, n, axis=0, weights = [list of weights])
    mvgavg(array, n, axis=0, binning = bool)


What This Code Does
--------------------
Consider the array `[a,b,c,d, ... x, y, z]`.  Taking the moving average of
length `n=3` results in a new array wherein the first element is `(a+b+c)/3`, the
second `(b+c+d)/3` and so on.  This can be done for arrays of arbitrary depth,
so if you put in a time series `[[t1,x1],[t2,x2],...]`, a moving average of 
along `axis=0` (the default) will give you back the moving average of all t's
along side all x's.

The output is a vector that is the same size and shape but has been shortened
on the `axis` axis by a length of `n-1`.

Axis and Weight Options
------------------------
Axis: The axis lets you operate at an increased depth, so using the `axis=1`
parameter, you can operate horizontally across columns with your moving average.
You can do this as deep as the array itself.

Weights allow you to customize the function.  The default weight (None) is 
described above (all values are given the same weight).  One other weight 
you can use is `'pascal'`. This gives a nth-line pascal's triangle weight, 
so for instance, for `n = 5`, the `ith` item in the array is 
`(i + 4j + 6k + 4l + m) / 16`, since the 5th line in pascal's triangle is
[1,4,6,4,1].  The other default weight options are `triangle` (i.e. 
`triangle(5)=[1,2,3,2,1]`, and quadratic is triangle squared. Or make your own 
list and put whatever you want in here (make sure `len(weights) == n`)

Binning
-------
Binning greatly shortens the array and loses some precision.  This is desirable
if you have an enormous amount of data and don't need to preserve every point.  The
difference between a default moving average and a binned moving average is that,
for an input array [a b c d e f...] and an output [A B C D E F...] over distance
3, the default moving average looks like this: ::

        A = [a b c]/3
        B =   [b c d]/3
        C =     [c d e]/3
        D =       [d e f]/3
        E =         [e f g]/3
        ....

but if binning = True: ::

        A = [a b c]/3
        B =       [d e f]/3
        C =             [g h i]/3
        .....

As you can see the output array is greatly shortened.  As arrays get very large,
binning can become orders of magnitude faster to compute, and if you don't need the
resolution of a moving average, are a much more efficient way of handling data,
because you may end up throwing most of your data away later when you go to plot
it up anyways.

Why Is This Function Important?
-------------------------------
Moving averages smooth data and illuminate trends that otherwise may not be
as apparent.  They also help with reverse interpolation when different x's
yield the same y. The reasons for using moving averages are myriad, so a
decent arbitrary-depth moving average function with numpy-speed and arbitrary
weighting needed to be written.

Acknowledgements
----------------
Credit to @fnjn on github for the sliding window function.

Misc
-------
If you have issues or questions, open an issue on Github at 
https://github.com/NGeorgescu/python-moving-average or if you think there's some
functionality that you would like to see, or if you have a faster algorithm

Thanks and Enjoy!
