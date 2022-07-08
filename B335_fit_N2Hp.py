import pyspeckit
from pyspeckit.spectrum.models import n2hp
from spectral_cube import SpectralCube
from radio_beam import Beam

import numpy as np

import astropy.units as u
from astropy.io import fits

from skimage.morphology import remove_small_objects,closing,disk,opening

raw_file = '/data2/jpineda/ALMA/B335/fits_files/B335_ACA+12m_N2Hp_rob05_mscale_v1.fits'
file_in = 'data/B335_N2H+_10_K_v1.fits'

file_thick='B335_N2Hp_v1_thick_fitted_parameters_2comp_3snr.fits'
file_thin= 'B335_N2Hp_v1_thin_fitted_parameters_snr3.fits'
rms_file='data/B335_N2H+_10_v1_rms.fits'
Tpeak_file='data/B335_N2H+_10_v1_Tpeak.fits'
mask_file='data/B335_N2H+_10_v1_mask.fits'

#freq_line=93173.3920e6*u.Hz
freq_line=93173.7000e6*u.Hz
snr_min = 3.

xmax=226; ymax=223
vmin=8.0; vmax=8.8
vmean=8.4
vmin_plot=8.0; vmax_plot=8.8

F=False
T=True
multicore=1

plot_dv=F

# Prepare extra files
Prepare_Files       =F
# Optically thin
Optically_Thin      =F
Show_Optically_Thin =T
# Optically thick
Optically_Thick     =F
Show_Optically_Thick=F

def load_myCube( file_in):
    cube = pyspeckit.Cube(file_in)
    cube.xarr.refX = freq_line
    cube.xarr.velocity_convention = 'radio'
    cube.xarr.convert_to_unit('km/s')
    return cube
"""
if Prepare_Files:
    data, hd = fits.getdata( raw_file, header=True)
    beam =  Beam.from_fits_header( hd)
    data *= beam.jtok( freq_line).value
    hd['BUNIT'] = 'K'
    hd['RESTFRQ'] = freq_line.to(u.Hz).value
    fits.writeto( file_in, data, hd, overwrite=True)
    cube = load_myCube( file_in)
    rms_map = cube.slice(0.8, 6.8, unit='km/s').cube.std(axis=0)
    Tpeak =  cube.slice(vmin, vmax, unit='km/s').cube.max(axis=0)
    peaksnr =  Tpeak/rms_map #cube.slice(vmin, vmax, unit='km/s').cube.max(axis=0)/rms_map
    planemask = (peaksnr>snr_min) 
    planemask = remove_small_objects(planemask,min_size=40)
    planemask = opening(planemask,disk(1))

    hd_cube=cube.header.copy()
    key_remove=['NAXIS3','CRPIX3','CDELT3','CUNIT3','CTYPE3','CRVAL3','SPECSYS']
    for key_i in key_remove:
        hd_cube.remove(key_i)
    hd_cube['WCSAXES']=2
    hd_cube['NAXIS']=2
    fits.writeto(rms_file, rms_map, hd_cube, overwrite=True)
    fits.writeto(Tpeak_file, Tpeak, hd_cube, overwrite=True)
    hd_cube['BITPIX']=8
    fits.writeto(mask_file, planemask.astype(int), hd_cube, overwrite=True)
else:
"""
planemask=fits.getdata(mask_file)#.astype(bool)
Tpeak=fits.getdata(Tpeak_file)
rms_map=fits.getdata(rms_file)
peaksnr =  Tpeak/rms_map

import matplotlib.pyplot as plt
plt.ion()


if Optically_Thin:
    cube = load_myCube( file_in)
    cube.Registry.add_fitter('n2hp_vtau', pyspeckit.models.n2hp.n2hp_vtau_fitter, 4)

    print('start optically thin fit')
    cube.fiteach(fittype='n2hp_vtau',  guesses=[5.0, 0.1, vmean, 0.1], # Tex=5K, tau=0.1, v_center=7.1, \sigma_v=0.2 km/s
                 verbose_level=1, signal_cut=snr_min,
                 limitedmin=[T,T,T,T],
                 limitedmax=[T,F,T,T],
                 minpars=[ 0,  0,vmin,0.05],
                 maxpars=[250.0,0,vmax,1.0],
                 fixed=[F,T,F,F, F,T,F,F], 
                 use_neighbor_as_guess=True, 
                 position_order = peaksnr,
                 start_from_point = (xmax, ymax),
                 errmap=rms_map, 
                 maskmap=planemask,
                 multicore=multicore)

    cube.write_fit( file_thin, overwrite=True)

if Optically_Thick:
    cube = load_myCube( file_in)
    cube.Registry.add_fitter('n2hp_vtau', pyspeckit.models.n2hp.n2hp_vtau_fitter, 4)
    guesses=np.array([7.0, 2.0, 8.2, 0.1, 7.0, 2.0, 8.6, 0.1])
    print('start optically thick fit')
    cube.fiteach(fittype='n2hp_vtau',  guesses=[7.0, 2.0, vmean, 0.1], # Tex=5K, tau=5.0, v_center=10.3, \sigma_v=0.2 km/s
                 verbose_level=2, signal_cut=snr_min,
                 limitedmin=[T,T,T,T],
                 limitedmax=[T,T,T,T],
                 minpars=[ 0.1,  0,vmin,0.05],
                 maxpars=[20.,50,vmax,1.0],
                 fixed=[F,F,F,F], 
                 use_neighbor_as_guess=True, 
                 position_order = peaksnr,
                 start_from_point = (xmax, ymax),
                 errmap=rms_map, 
                 maskmap=planemask,
		 #skip_failed_fits=True,
                 multicore=multicore)

    cube.write_fit( file_thick, overwrite=True)


if Show_Optically_Thin:
    #
    cube = load_myCube( file_in)
    cube.Registry.add_fitter('n2hp_vtau', pyspeckit.models.n2hp.n2hp_vtau_fitter, 4)
    cube.load_model_fit(file_thin, npars=4, npeaks=1, _temp_fit_loc=(xmax,ymax))
    cube.mapplot()
    cube.plot_spectrum(xmax,ymax, plot_fit=True)
    if plot_dv:
        cube.mapplot.plane = cube.parcube[3,:,:]
        cube.mapplot(estimator=None, vmin=0.05, vmax=0.25)
    else:
        cube.mapplot.plane = cube.parcube[2,:,:]
        cube.mapplot(estimator=None, vmin=vmin_plot, vmax=vmax_plot)
    plt.draw()
    plt.show()
    #plt.savefig('N2Hp_pyspeckit_poor_thin_fit.png')


if Show_Optically_Thick:
    #
    cube = load_myCube( file_in)
    cube.Registry.add_fitter('n2hp_vtau', pyspeckit.models.n2hp.n2hp_vtau_fitter, 4)
    cube.load_model_fit( file_thick, npars=4, npeaks=2, _temp_fit_loc=(xmax,ymax))
    cube.mapplot()
    cube.plot_spectrum(xmax,ymax, plot_fit=True)
    if plot_dv:
        cube.mapplot.plane = cube.parcube[3,:,:]
        cube.mapplot(estimator=None, vmin=0.05, vmax=0.21)#, origin='lowest')
    else:
        cube.mapplot.plane = cube.parcube[2,:,:]
        cube.mapplot(estimator=None, vmin=vmin_plot, vmax=vmax_plot, 
                     cmap='RdYlBu_r')#, origin='lowest')
    plt.draw()
    plt.show()
    #plt.savefig('N2Hp_pyspeckit_poor_thick_fit.png')
