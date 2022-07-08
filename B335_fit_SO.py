#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 12:05:09 2022

@author: dc269993
"""

import pyspeckit
#from pyspeckit.spectrum.models import n2hp
from spectral_cube import SpectralCube
from radio_beam import Beam

import numpy as np

import astropy.units as u
from astropy.io import fits

from skimage.morphology import remove_small_objects,closing,disk,opening

#raw_file = '/data2/jpineda/ALMA/B335/fits_files/B335_ACA+12m_N2Hp_rob05_mscale_v1.fits'


vmean=8.34
vmin_plot=8.0; vmax_plot=9.0


file_in = 'SO/B335_SO_medsub.fits'
#rms_file 
file_par = 'SO/Spec_SO_3comp_5snr_slurm.fits'

freq_line = 261.84368400 * u.GHz


snr_min = 5.0
xmax = 618; ymax = 584
# range of parameters
vmin = 2.0; vmax = 12.5
tpeak_min = 0.0; tpeak_max = 500e-3
dv_min = 0.02; dv_max = 4.0


F=False
T=True
multicore=5

def load_myCube( file_in):
    cube = pyspeckit.Cube(file_in)
    cube.xarr.refX = freq_line
    cube.xarr.velocity_convention = 'radio'
    cube.xarr.convert_to_unit('km/s')
    return cube

plot_dv = F
plot_vc = T
plot_TdV = F
plot_Im = F

# Prepare extra files
Prepare_Files = F
Fit = F


err_map = np.ones((1200, 1200))*0.00378
# Initial guess value
guesses = np.array([80e-3, 8.34, 0.5])


if Fit :
   
    # Load cube and setup the spectral axis
    cube = load_myCube(file_in)

    cube.fiteach(guesses=guesses,
                 start_from_point=(xmax, ymax),
                 fittype='gaussian', blank_value=np.nan,verbose_level=3,
                 use_neighbor_as_guess=True,
                 limitedmax=[True, True, True],
                 limitedmin=[True, True, False],
                 maxpars=[tpeak_max, vmax, dv_max],
                 minpars=[tpeak_min, vmin, dv_min],
                 multicore=1, errmap=err_map, signal_cut=snr_min)

    cube.write_fit(file_par, overwrite=True)



import matplotlib.pyplot as plt
plt.ion()

if plot_dv:
    #
    cube = load_myCube( file_in)
    #cube.Registry.add_fitter('n2hp_vtau', pyspeckit.models.n2hp.n2hp_vtau_fitter, 4)
    cube.load_model_fit(file_par, npars=3, npeaks=2, _temp_fit_loc=(xmax,ymax))
    cube.mapplot()
    cube.plot_spectrum(xmax,ymax, plot_fit=True)
    cube.mapplot.plane = cube.parcube[9,:,:]
    cube.mapplot(estimator=None)
    plt.draw()
    plt.show()
    #plt.savefig('N2Hp_pyspeckit_poor_thin_fit.png')

if plot_vc:
    #
    cube = load_myCube( file_in)
    #cube.Registry.add_fitter('n2hp_vtau', pyspeckit.models.n2hp.n2hp_vtau_fitter, 4)
    cube.load_model_fit(file_par, npars=3, npeaks=3, _temp_fit_loc=(xmax,ymax))
    cube.mapplot()
    cube.plot_spectrum(xmax,ymax, plot_fit=True)
    cube.mapplot.plane = cube.parcube[1,:,:]
    cube.mapplot(estimator=None,vmin=vmin_plot,vmax=vmax_plot, cmap ='RdYlBu_r')
    plt.draw()
    plt.show()
    
if plot_TdV:
    #
    cube = load_myCube( file_in)
    #cube.Registry.add_fitter('n2hp_vtau', pyspeckit.models.n2hp.n2hp_vtau_fitter, 4)
    cube.load_model_fit(file_par, npars=3, npeaks=2, _temp_fit_loc=(xmax,ymax))
    cube.mapplot()
    cube.plot_spectrum(xmax,ymax, plot_fit=True)
    cube.mapplot.plane = cube.parcube[0,:,:]
    cube.mapplot(estimator=None)
    plt.draw()
    plt.show()
    #plt.savefig('N2Hp_pyspeckit_poor_thin_fit.png')
    
    
