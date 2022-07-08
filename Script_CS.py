#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:11:07 2022

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


Molecule = 'CS'
ProjNbr = 'CS'
#Project = list(input("Project name (list) :"))
Project = ['2012.1.00346.S', '2018.1.01208.S', 
           '2018.1.01208.S', '2018.1.01208.S', '2018.1.01208.S', 
           '2015.1.00169.S', '2015.1.00169.S', '2015.1.00169.S', 
           '2015.1.00169.S', '2015.1.00169.S', '2015.1.00169.S']

vis = ['/drf/projets/capucine.new/dcherouv/2012.1.00346.S/uid___A002_X7fc9da_X4324_fixed.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2018.1.01208.S/uid___A002_Xdee82d_X27be.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2018.1.01208.S/uid___A002_Xdf0444_X6182.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2018.1.01208.S/uid___A002_Xdf0444_X68be.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2018.1.01208.S/uid___A002_Xdf15dc_Xed3.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb57bb5_X451.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5aa7c_X4c04.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5bd46_X1b74.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5bd46_X2404.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd1daeb_X2e93.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd21a3a_X1d4a.ms.split.cal/']
       

phasecenter = 'J2000 19h37m00.9 +7d34m09.6'
imagename = '/drf/projets/capucine.new/dcherouv/ProjectCS/spw_CS/Dirty_cube/B335_Combine_CS_rob05_fit1_015kms_2sigma_dirty'
#imagename = '/drf/projets/capucine.new/dcherouv/ProjectCS/spw_CS/Dirty_cube/B335_Combine_CS_rob05_fit1_diffwt_dirty'
threshold = ' 0.002022Jy/beam'
#width = '0.854km/s'
width = '0.15km/s'
start = '-4km/s'
imsize = 1800
cell = '0.016arcsec'
restfreq = '342.8828503GHz'
nchan = 170

if len(vis) > 1:
    
    for i in range(len(vis)) :

        
        if Project[i] == '2015.1.00169.S' :
            
            if vis[i] == '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd1daeb_X2e93.ms.split.cal/' or vis[i] == '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd21a3a_X1d4a.ms.split.cal/':
            
                fitspw.append('2:100~200;1300~1500')
                field.append('B335')
                spw.append('2')
                
            else :
                
                fitspw.append('6:100~200;1300~1500')
                field.append('B335')
                spw.append('6')
                
        if Project[i] == '2012.1.00346.S' :
            
            fitspw.append('2:200~600;2700~3500')
            field.append('B335')
            spw.append('2')
            
        if Project[i] == '2013.1.01301.S' :
            
            fitspw.append('1:100~500;1400~1700')
            field.append('CB199')
            spw.append('1')
            
        if Project[i] == '2018.1.01208.S' :
            
            fitspw.append('31:100~300;700~900')
            field.append('B335')
            spw.append('31')
            
            
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
      
"""
vis_uvcontsub = ['/drf/projets/capucine.new/dcherouv/2012.1.00346.S/uid___A002_X7fc9da_X4324_fixed.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2018.1.01208.S/uid___A002_Xdee82d_X27be.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2018.1.01208.S/uid___A002_Xdf0444_X6182.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2018.1.01208.S/uid___A002_Xdf0444_X68be.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2018.1.01208.S/uid___A002_Xdf15dc_Xed3.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb57bb5_X451.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5aa7c_X4c04.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5bd46_X1b74.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5bd46_X2404.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd1daeb_X2e93.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd21a3a_X1d4a.ms.split.cal.contsub/']
"""
        
if do_mstransfo == True : 
    
    for i in range(len(vis)) :
        
        vis_transfo = Prename + 'Project' + str(ProjNbr) + '/Data/B335_' + str(Project[i]) + '_spw' + str(spw[i]) + '_015kms_' + str(i) + '_transfo.ms/' 
        
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
vis_mstransfo = ['/drf/projets/capucine.new/dcherouv/ProjectCS/Data/B335_2012.1.00346.S_spw2_015kms_0_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectCS/Data/B335_2018.1.01208.S_spw31_015kms_1_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectCS/Data/B335_2018.1.01208.S_spw31_015kms_2_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectCS/Data/B335_2018.1.01208.S_spw31_015kms_3_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectCS/Data/B335_2018.1.01208.S_spw31_015kms_4_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectCS/Data/B335_2015.1.00169.S_spw6_015kms_5_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectCS/Data/B335_2015.1.00169.S_spw6_015kms_6_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectCS/Data/B335_2015.1.00169.S_spw6_015kms_7_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectCS/Data/B335_2015.1.00169.S_spw6_015kms_8_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectCS/Data/B335_2015.1.00169.S_spw2_015kms_9_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectCS/Data/B335_2015.1.00169.S_spw2_015kms_10_transfo.ms/']
"""
#visweightscale = [0.002, 1e-9, 0.00067, 0.00067, 0.00067, 0.00067,
                  #0.000067, 0.000067, 0.000067, 0.000067, 0.000067, 0.000067]
                 
#visweightscale = [1e-9, 0.0002, 0.0002, 0.0002, 0.0002,
                  #0.000067, 0.000067, 0.000067, 0.000067, 0.000067, 0.000067]

if do_concat == True and len(vis_mstransfo) > 1 :
    
    concatvis = Prename + 'Project' + str(ProjNbr) + '/Data/B335_Combine_015kms_' + str(Molecule) + '_diffwt.ms/'
    
    concat(vis=vis_mstransfo, concatvis=concatvis)
    
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