This is a small Python project, which allows you to plot geo-located data onto a [WebGL Globe](https://www.chromeexperiments.com/globe) ([WebGL Sources](https://github.com/dataarts/webgl-globe))


![screenshot](doc/screenshot_globeplot.png)



Install
=======

For the moment you cannot install the program via pip or similar.

Clone the repository:


```
#!bash
  hg clone https://ikkjo@bitbucket.org/ikkjo/globeplot

```

Subsequently, add `globeplot` to your Python path. In case you are using `virtualenv-wrapper`:

```
#!bash
  add2virtualenv /path/to/globeplot
```

Requirements
============

Python 2.7 Note, the HTTP server will not work with Python 3 directly.

You will need to have the following Python modules to be installed in your environment:
```
  jinja2
  ipython notebook
```

To display the plots you will need a browser which supports WebGL. I tested Firefox, Chromium, Safari, and Opera. They all work, but it seems that WebKit-based browsers are performing better. The program is only tested on Ubuntu and OS X, not on Windows.


Usage
=====


```
#!python
import numpy as np
from globeplot.plotting import GlobePlot


# data and coordinates are one- or two-dimensional NumPy arrays
lats = np.array([...])
lons = np.array([...])
values = np.array([...])

plot = GlobePlot(lats=lats, lons=lons, data=values)

# append more data to the plot if needed
plot.append(more_lats, more_lons, more_values)

plot.show(title='A GlobePlot', creator='You', creator_addr='http://...',
          code_link='http://...')
```