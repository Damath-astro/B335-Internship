#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:46:27 2022

@author: dc269993
"""

solint = 'int'
excludechans = False
fitorder = 1
datacolumn = 'data'
niter = 10000
phasecenter = 'J2000 19h37m00.9 +7d34m09.6'
Prename = '/drf/projets/capucine.new/dcherouv/'
fitspw = []  
spw = []
field = []

vis_mstransfo = []
vis_uvcontsub = []

do_statwt = False
do_uvcontsub = False
do_mstransfo = False
do_concat = False
do_clean = True


Molecule = '13CO'
ProjNbr = '13CO'
#Project = list(input("Project name (list) :"))
Project = ['2017.1.00288.S', '2017.1.00288.S', '2017.1.00288.S',
           '2017.1.00288.S', '2017.1.00288.S', '2013.1.00879.S', 
           '2013.1.00211.S_7m', '2013.1.00211.S_7m', '2013.1.00211.S_7m', 
           '2013.1.00211.S_7m', '2013.1.00211.S_7m', '2013.1.00211.S_7m', 
           '2013.1.00211.S_7m', '2013.1.00211.S_7m', '2013.1.00211.S_7m', 
           '2013.1.00211.S', '2013.1.00211.S', '2013.1.00211.S']

vis = ['/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5802b_X5a5.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5e6d0_Xe87.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5f05e_X51e.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc6141c_X2d94.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc63024_X3e51.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00879.S/uid___A002_X8a951a_X55b.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X85b7b2_X3c8.ms.split.cal/', 
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
       '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/uid___A002_Xa14be9_X28d7.ms.split.cal/']
       

phasecenter = 'J2000 19h37m00.9 +7d34m09.6'
imagename = '/drf/projets/capucine.new/dcherouv/Project13CO/spw_13CO/Dirty_cube/B335_Combine_13CO_rob05_fit1_dirty'
#imagename = '/drf/projets/capucine.new/dcherouv/ProjectCS/spw_CS/Dirty_cube/B335_Combine_CS_rob05_fit1_diffwt_dirty'
threshold = ' 0.002022Jy/beam'
#width = '0.854km/s'
width = '0.1km/s'
start = '2.3km/s'
imsize = 1800
cell = '0.01arcsec'
restfreq = '220.3986842GHz'
nchan = 120

if len(vis) > 1:
    
    for i in range(len(vis)) :
        
        if Project[i] == '2013.1.00879.S' :
            
            fitspw.append('2:50~350;600~900')
            field.append('B335')
            spw.append('2')

        if Project[i] == '2013.1.00211.S' :
            
            fitspw.append('7:100~400;600~900')
            field.append('B335')
            spw.append('7')
            
        if Project[i] == '2013.1.00211.S_7m' :
            
            fitspw.append('7:100~400;600~900')
            field.append('B335')
            spw.append('7')
        
        if Project[i] == '2017.1.00288.S' :
            
            fitspw.append('4:500~600;1700~1800')
            field.append('B335')
            spw.append('4')
            
if do_statwt == True :
        
    for i in range(len(vis)) :
        
        statwt(vis=vis[i], fitspw=fitspw[i], excludechans=excludechans, 
               spw=spw[i], field=field[i], datacolumn=datacolumn)        
    
if do_uvcontsub == True :
    
    for i in range(len(vis)) :
        
        uvcontsub(vis=vis[i], fitspw=fitspw[i], 
                  excludechans=excludechans, solint=solint, 
                  fitorder=fitorder, spw=spw[i], field=field[i])
    
        vis_uvcontsub.append(vis[i][:-1] + '.contsub/')                
           
vis_uvcontsub = ['/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5802b_X5a5.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5e6d0_Xe87.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc5f05e_X51e.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc6141c_X2d94.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2017.1.00288.S/uid___A002_Xc63024_X3e51.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00879.S/uid___A002_X8a951a_X55b.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/7m/uid___A002_X85b7b2_X3c8.ms.split.cal.contsub/', 
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
                 '/drf/projets/capucine.new/dcherouv/2013.1.00211.S/uid___A002_Xa14be9_X28d7.ms.split.cal.contsub/']
            
if do_mstransfo == True : 
    
    for i in range(len(vis)) :
        
        vis_transfo = Prename + 'Project' + str(ProjNbr) + '/Data/B335_' + str(Project[i]) + '_spw' + str(spw[i]) + '_01kms_' + str(i) + '_transfo.ms/' 
        
        mstransform(vis=vis_uvcontsub[i], outputvis=vis_transfo, 
                    field = '*', spw = '*', regridms = True, 
                    mode = 'velocity', nchan=nchan, start=start, width=width, 
                    phasecenter=phasecenter, outframe = 'LSRK', 
                    veltype = 'radio', restfreq=restfreq, hanning = True, 
                    datacolumn=datacolumn)#, 
                    #douvcontsub = True, 
                    #fitspw=fitspw[i], fitorder=fitorder)
        
        vis_mstransfo.append(vis_transfo)
        

"""
vis_mstransfo = ['/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2017.1.00288.S_spw3_01kms_0_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2017.1.00288.S_spw3_01kms_1_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2017.1.00288.S_spw3_01kms_2_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2017.1.00288.S_spw3_01kms_3_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2017.1.00288.S_spw3_01kms_4_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00879.S_spw0_01kms_5_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_01kms_6_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_01kms_7_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_01kms_8_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_01kms_9_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_01kms_10_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_01kms_11_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_01kms_12_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_01kms_13_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_7m_spw6_01kms_14_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_spw6_01kms_15_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_spw6_01kms_16_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/Data/B335_2013.1.00211.S_spw6_01kms_17_transfo.ms/']
"""
#visweightscale = [0.002, 1e-9, 0.00067, 0.00067, 0.00067, 0.00067,
                  #0.000067, 0.000067, 0.000067, 0.000067, 0.000067, 0.000067]
                 
#visweightscale = [1e-9, 0.0002, 0.0002, 0.0002, 0.0002,
                  #0.000067, 0.000067, 0.000067, 0.000067, 0.000067, 0.000067]

if do_concat == True and len(vis_mstransfo) > 1 :
    
    concatvis = Prename + 'Project' + str(ProjNbr) + '/Data/B335_Combine_015kms_' + str(Molecule) + '_diffwt.ms/'
    
    concat(vis=vis_mstransfo, concatvis=concatvis)#, visweightscale=visweightscale)
    
concatvis = Prename + 'Project' + str(ProjNbr) + '/Data/B335_Combine_015kms_' + str(Molecule) + '_diffwt.ms/'
    
if do_clean == True :
    
    tclean(vis=concatvis, imagename=imagename, imsize=imsize,
           cell=cell, field = '*', spw = '*',
           #width=width,start=start, phasecenter=phasecenter, nchan=nchan, field = '*', spw = '*',
           restfreq=restfreq, datacolumn=datacolumn,
           specmode = 'cube', gridder = 'mosaic', 
           #deconvolver = 'hogbom', 
           #niter = 10000,
           niter = 0,
           threshold=threshold,
           deconvolver = 'multiscale', scales = [0,3,9,27,81],
           weighting = 'briggs', 
           robust = 0.5, interactive = False, restoringbeam = 'common')