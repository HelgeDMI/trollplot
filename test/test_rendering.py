import pytest
from netCDF4 import Dataset
from globeplot.plotting import GlobePlot


def test_rendering():

    ds = Dataset('./test/ssmi_f18_201605260450_s.nc')
    lat = ds.variables['lat_l'][:]
    lon = ds.variables['lon_l'][:]
    values = ds.variables['tb37v'][:]

    plot = GlobePlot(lats=lat, lons=lon, data=values)
    plot.show(title='Tb37 SSMIS F18 2016-05-26 04:50', creator='Helge',
              creator_addr='http://www.dmi.dk', code_link='http://www.dmi.dk')
