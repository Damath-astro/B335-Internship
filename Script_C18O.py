#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 12:28:20 2022

@author: dc269993
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:34:51 2022

@author: dc269993
"""

solint = 'int'
excludechans = False
fitorder = 1
datacolumn = 'data'
niter = 10000
phasecenter = 'J2000 19h37m00.9 +7d34m09.6'
vis_uvcontsub = []
vis_mstransfo = []
Prename = '/drf/projets/capucine.new/dcherouv/'
fitspw = []  
spw = []
field = []

do_uvcontsub = False
do_concat = False
do_mstransfo = False
do_clean = True



Molecule = 'C18O'
ProjNbr = 'C18O_complete'
Project = ['2013.1.00211.S_7m', '2013.1.00211.S_7m', 
           '2013.1.00211.S_7m', '2013.1.00211.S_7m', '2013.1.00211.S_7m', 
           '2013.1.00211.S_7m', '2013.1.00211.S_7m', '2013.1.00211.S_7m', 
           '2013.1.00211.S_7m', '2013.1.00211.S', '2013.1.00211.S', 
           '2013.1.00211.S', '2013.1.00879.S', '2017.1.00288.S', 
           '2017.1.00288.S', '2017.1.00288.S', '2017.1.00288.S', 
           '2017.1.00288.S']

vis = ['/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X85b7b2_X3c8.ms.split.cal/', 
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X85c183_X16c6.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X85c183_Xf73.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X86cc63_Xe69.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X86e521_X1298.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X86fcfa_X1379.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X877956_X66.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X877e41_Xcd3.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X879b80_Xbeb.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/uid___A002_Xa14be9_X17cb.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/uid___A002_Xa14be9_X2267.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/uid___A002_Xa14be9_X28d7.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00879.S/uid___A002_X8a951a_X55b.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5802b_X5a5.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5e6d0_Xe87.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5f05e_X51e.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc6141c_X2d94.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc63024_X3e51.ms.split.cal/']
       

phasecenter = 'J2000 19h37m00.9 +7d34m09.6'
imagename = '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/spw_C18O/Clean_cube/B335_Combine_C18O_HRA_rob05_fit1_01kms_hogbom_3sigma_self_clean'
threshold = '0.006806Jy/beam'
#width = '0.667km/s'
width = '0.1km/s'
start = '3km/s'
#imsize = 1152
imsize = 1000
cell = '0.05arcsec'
restfreq = '219.56035410GHz'
nchan = 120


if len(vis) > 1:
    
    for i in range(len(vis)) :
        
        if Project[i] == '2013.1.00879.S' :
            
            fitspw.append('0:100~350;600~900')
            field.append('B335')
            spw.append('0')
            
        if Project[i] == '2018.1.00452.S' :
            
            fitspw.append('31:30~170')
            field.append('B335')
            spw.append('31')
            
        if Project[i] == '2013.1.00211.S' :
            
            fitspw.append('6:100~400;600~900')
            field.append('B335')
            spw.append('6')
            
        if Project[i] == '2013.1.00211.S_7m' :
            
            fitspw.append('6:100~400;600~900')
            field.append('B335')
            spw.append('6')
        
        if Project[i] == '2017.1.00288.S' :
            
            fitspw.append('3:500~600;1700~1800')
            field.append('B335')
            spw.append('3')
            
if do_uvcontsub == True :
    
    for i in range(len(vis)) :
        
        uvcontsub(vis=vis[i], fitspw=fitspw[i], 
                  excludechans=excludechans, solint=solint, 
                  fitorder=fitorder, spw=spw[i], field=field[i])
    
        vis_uvcontsub.append(vis[i][:-1] + '.contsub/')   


vis_uvcontsub = ['/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X85b7b2_X3c8.ms.split.cal.contsub/', 
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X85c183_X16c6.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X85c183_Xf73.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X86cc63_Xe69.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X86e521_X1298.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X86fcfa_X1379.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X877956_X66.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X877e41_Xcd3.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X879b80_Xbeb.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/uid___A002_Xa14be9_X17cb.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/uid___A002_Xa14be9_X2267.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/uid___A002_Xa14be9_X28d7.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00879.S/uid___A002_X8a951a_X55b.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5802b_X5a5.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5e6d0_Xe87.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5f05e_X51e.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc6141c_X2d94.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc63024_X3e51.ms.split.cal.contsub/']

if do_mstransfo == True : 
    
    for i in range(len(vis)) :
        
        vis_transfo = Prename + 'Project' + str(ProjNbr) + '/Data/B335_' + str(Project[i]) + '_spw' + str(spw[i]) + '_015kms_' + str(i+1) + '_transfo.ms/' 
        
        mstransform(vis=vis_uvcontsub[i], outputvis=vis_transfo, 
                    field = '*', spw = '*', regridms = True, 
                    mode = 'velocity', nchan=nchan, start=start, width=width, 
                    phasecenter=phasecenter, outframe = 'LSRK', 
                    veltype = 'radio', restfreq=restfreq, hanning = True, 
                    datacolumn=datacolumn)
        
        vis_mstransfo.append(vis_transfo)
        
vis_mstransfo = ['/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_015kms_1_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_015kms_2_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_015kms_3_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_015kms_4_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_015kms_5_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_015kms_6_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_015kms_7_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_015kms_8_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_015kms_9_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_spw6_015kms_10_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_spw6_015kms_11_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_spw6_015kms_12_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00879.S_spw0_015kms_13_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2017.1.00288.S_spw3_015kms_14_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2017.1.00288.S_spw3_015kms_15_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2017.1.00288.S_spw3_015kms_16_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2017.1.00288.S_spw3_015kms_17_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2017.1.00288.S_spw3_015kms_18_transfo.ms/']

#visweightscale = [0.00009, 0.63e-7, 0.63e-7, 0.63e-7, 0.63e-7, 0.63e-7, 
                  #0.63e-7, 0.63e-7, 0.63e-7, 0.63e-7, 0.0004, 0.00025, 0.00025, 
                  #0.000004, 5e-5, 5e-5, 5e-5, 5e-5, 5e-5]

#visweightscale = [0.63e-7, 0.63e-7, 0.63e-7, 0.63e-7, 0.63e-7, 
                  #0.63e-7, 0.63e-7, 0.63e-7, 0.63e-7, 0.0001, 0.0001, 0.0001, 
                  #0.000002, 7e-5, 7e-5, 7e-5, 7e-5, 7e-5]

visweightscale = [0.63e-7, 0.63e-7, 0.63e-7, 0.63e-7, 0.63e-7, 
                  0.63e-7, 0.63e-7, 0.63e-7, 0.63e-7, 0.0004, 0.00025, 0.00025, 
                  0.000002, 5e-5, 5e-5, 5e-5, 5e-5, 5e-5]
                  
#visweightscale = [0.00009, 0.2e-6, 0.2e-6, 0.2e-6, 0.2e-6, 0.2e-6, 
                  #0.2e-6, 0.2e-6, 0.2e-6, 0.2e-6, 0.0004, 0.00025, 0.00025, 
                  #0.000002, 4e-4, 4e-4, 4e-4, 4e-4, 4e-4]  

#visweightscale = [0.00009, 0.8e-6, 0.8e-6, 0.8e-6, 0.8e-6, 0.8e-6, 
                 # 0.8e-6, 0.8e-6, 0.8e-6, 0.8e-6, 0.0004, 0.00025, 0.00025, 
                  #0.000002, 5e-5, 5e-5, 5e-5, 5e-5, 5e-5]                  

if do_concat == True and len(vis_mstransfo) > 1 :
    
    concatvis = Prename + 'Project' + str(ProjNbr) + '/Data/B335_Combine_HRA_015kms_' + str(Molecule) + '.ms/'
    
    concat(vis=vis_mstransfo, concatvis=concatvis, visweightscale=visweightscale)
    
concatvis = Prename + 'Project' + str(ProjNbr) + '/Data/B335_Combine_HRA_015kms_' + str(Molecule) + '.ms/'
    
if do_clean == True :
    
    tclean(vis=concatvis, imagename=imagename, imsize=imsize,
           #width=width, start=start, phasecenter=phasecenter, nchan=nchan,
           #pblimit = 0.05,
           threshold=threshold,
           cell=cell, field = '*', spw = '*',
           restfreq=restfreq, 
           specmode = 'cube', gridder = 'mosaic', 
           deconvolver = 'hogbom', 
           #deconvolver = 'multiscale', scales = [0,5,15,45,135],
           niter = 50000, weighting = 'briggs', 
           robust = 0.5,
           restoringbeam = 'common', 
           datacolumn = 'data', outframe = 'LSRK', veltype = 'radio', 
           interactive = True)