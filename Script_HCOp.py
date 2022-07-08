#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:09:12 2022

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

do_uvcontsub = False
do_concat = False
do_mstransfo = False
do_clean = True
Molecule = 'HCO'
ProjNbr = 'HCO_complete'
#Project = list(input("Project name (list) :"))
Project = ['2013.1.01301.S', '2015.1.00169.S', '2015.1.00169.S',
           '2015.1.00169.S', '2015.1.00169.S', '2015.1.00169.S',
           '2015.1.00169.S']

vis = ['/drf/projets/capucine.new/dcherouv/2013.1.01301.S/uid___A002_Xa8df68_X143d.ms.split_fixed.cal/', 
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb57bb5_X451.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5aa7c_X4c04.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5bd46_X1b74.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5bd46_X2404.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd1daeb_X2e93.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd21a3a_X1d4a.ms.split.cal/']
       

phasecenter = 'J2000 19h37m00.9 +7d34m09.6'
#imagename = '/drf/projets/capucine.new/dcherouv/ProjectC18O_complete/spw_C18O/Dirty_cube/B335_Combine_C18O_rob05_fit1_dirty'
threshold = '0.017817096Jy/beam'
width = '0.8207km/s'
#width = '0.620km/s'
start = '0km/s'
imsize = 900
cell = '0.03arcsec'
restfreq = '356.734223GHz'
nchan = 30

if len(vis) > 1:
    
    for i in range(len(vis)) :

        
        if Project[i] == '2013.1.01301.S' :
        
            fitspw.append('2:90~110;280~300')
            field.append('CB199')
            spw.append('2:500~1000')
            #spw.append('2')
            
        if Project[i] == '2012.1.00346.S' :
            
            fitspw.append('1:20~100;180~230')
            field.append('B335')
            spw.append('1')
            
        if Project[i] == '2015.1.00169.S' :
            
            if vis[i] == '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd1daeb_X2e93.ms.split.cal/' or vis[i] == '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd21a3a_X1d4a.ms.split.cal/':
            
                fitspw.append('1:200~400;1700~1800')
                field.append('B335')
                spw.append('1')
                
            else :
                
                fitspw.append('5:200~400;1700~1800')
                field.append('B335')
                spw.append('5')
            
if do_uvcontsub == True :
    
    for i in range(len(vis)) :
        
        uvcontsub(vis=vis[i], fitspw=fitspw[i], 
                  excludechans=excludechans, solint=solint, 
                  fitorder=fitorder, spw=spw[i], field=field[i])
    
        vis_uvcontsub.append(vis[i][:-1] + '.contsub/')                
           
vis_uvcontsub = ['/drf/projets/capucine.new/dcherouv/2013.1.01301.S/uid___A002_Xa8df68_X143d.ms.split_fixed.cal.contsub/', 
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb57bb5_X451.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5aa7c_X4c04.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5bd46_X1b74.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5bd46_X2404.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd1daeb_X2e93.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd21a3a_X1d4a.ms.split.cal.contsub/']    
            
if do_mstransfo == True : 
    
    for i in range(len(vis)) :
        
        vis_transfo = Prename + 'Project' + str(ProjNbr) + '/Data/B335_' + str(Project[i]) + '_spw' + str(spw[i]) + '_' + str(i) + '_transfo.ms/' 
        
        mstransform(vis=vis_uvcontsub[i], outputvis=vis_transfo, 
                    field = '*', spw = '*', regridms = True, 
                    mode = 'velocity', nchan=nchan, start=start, width=width, 
                    phasecenter=phasecenter, outframe = 'LSRK', 
                    veltype = 'radio', restfreq=restfreq, hanning = True, 
                    datacolumn=datacolumn)#, 
                    #douvcontsub = True, 
                    #fitspw=fitspw[i], fitorder=fitorder)
        
        vis_mstransfo.append(vis_transfo)

visweightscale = [0.04, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005]

if do_concat == True and len(vis_mstransfo) > 1 :
    
    concatvis = Prename + 'Project' + str(ProjNbr) + '/Data/B335_Combine_' + str(Molecule) + '.ms/'
    
    concat(vis=vis_mstransfo, concatvis=concatvis, visweightscale=visweightscale)
    
    
if do_clean == True :
    
    tclean(vis=concatvis, imagename=imagename, imsize=imsize,
           #width=width, start=start, phasecenter=phasecenter, nchan=nchan,
           #pblimit = 0.05,
           threshold=threshold,
           cell=cell, field = '*', spw = '*',
           restfreq=restfreq, 
           specmode = 'cube', gridder = 'mosaic', 
           #deconvolver = 'hogbom', 
           deconvolver = 'multiscale', scales = [0,5,15,45,135],
           niter = 10000, weighting = 'briggs', 
           robust = 0.5,
           restoringbeam = 'common', 
           datacolumn = 'data', outframe = 'LSRK', veltype = 'radio', 
           interactive = True)