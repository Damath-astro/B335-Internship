#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:16:41 2022

@author: dc269993
"""

import pyspeckit
#from pyspeckit.spectrum.models import n2hp
from spectral_cube import SpectralCube
from radio_beam import Beam

import numpy as np

import astropy.units as u
from astropy.io import fits

Prename = '/drf/projets/capucine.new/dcherouv/'

file_in = Prename + 'ProjectC18O_complete/spw_C18O/Clean_cube/B335_Combine_C18O_rob05_fit1_3sigma_self_clean.fits'
#rms_file 
file_par = Prename + 'Spec_fit/Spec_C18O_fit_5snr.fits'


#SO
#freq_line = 261.84368400 * u.GHz

#C18O

freq_line = 219.56035410 * u.GHz


snr_min = 5.0
xmax = 450; ymax = 450
# range of parameters
vmin = 2; vmax = 14
tpeak_min = 0.0; tpeak_max = 500e-3
dv_min = 0.02; dv_max = 6.0

# Load cube and setup the spectral axis
cube = pyspeckit.Cube(file_in)
cube.xarr.refX = freq_line
cube.xarr.velocity_convention = 'radio'
cube.xarr.convert_to_unit('km/s')

err_map = np.ones((900, 900))*1.4e-3
# Initial guess value
guesses = np.array([50e-3, 8.34, 1])

cube.fiteach(guesses=guesses,
    start_from_point=(xmax, ymax),
    fittype='gaussian', blank_value=np.nan,verbose_level=0,
    use_neighbor_as_guess=True,
    limitedmax=[True, True, True],
    limitedmin=[True, True, False],
    maxpars=[tpeak_max, vmax, dv_max],
    minpars=[tpeak_min, vmin, dv_min],
    multicore=20, errmap=err_map, signal_cut=snr_min)

cube.write_fit(file_par, overwrite=True)
