import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import astropy.units as u
from astropy.utils.data import download_file
from astropy.io import fits
from astropy.utils import data
data.conf.remote_timeout = 60

from spectral_cube import SpectralCube
from spectral_cube import SpectralCube
from astroquery.esasky import ESASky
from astroquery.utils import TableList
from astropy.wcs import WCS
from reproject import reproject_interp
ngc_cii = fits.open('NGC1977_CII_Tmb_cube_0p3kms_original_res.fits')
cube = SpectralCube.read(ngc_cii)
ngc_cii.close()
print(cube)
moment_0 = sub_cube_slab.with_spectral_unit(u.km/u.s).moment(order=0)
sub_cube_slab = sub_cube.spectral_slab(-20. *u.km / u.s, 30. *u.km / u.s)
cube_slab = cube.spectral_slab(-20. *u.km / u.s, 30. *u.km / u.s)
moment_0 = cube_slab.with_spectral_unit(u.km/u.s).moment(order=0)
moment_0.write('ngc1977_cii_original_mom_0.fits') 