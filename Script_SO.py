#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:46:14 2022

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


Molecule = 'SO'
ProjNbr = 'SO'
#Project = list(input("Project name (list) :"))
Project = ['2013.1.01102.S', '2015.1.01188.S', '2015.1.01188.S',
           '2016.1.01376.S', '2016.1.01376.S', '2016.1.01376.S',
           '2016.1.01376.S']

vis = ['/drf/projets/capucine.new/dcherouv/2013.1.01102.S/uid___A002_Xa0b40d_X9d64.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.01188.S/uid___A002_Xb36550_X3ec6.target.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.01188.S/uid___A002_Xb3e112_X1b95.target.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2016.1.01376.S/uid___A002_Xc2c2f2_X1961.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2016.1.01376.S/uid___A002_Xc3173a_X4708.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2016.1.01376.S/uid___A002_Xc3173a_X4ec1.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2016.1.01376.S/uid___A002_Xc37375_X1ae3.ms.split.cal/']
       

phasecenter = 'J2000 19h37m00.9 +7d34m09.6'
imagename = '/drf/projets/capucine.new/dcherouv/ProjectSO/spw_SO/Clean_cube/B335_Combine_SO_rob05_fit1_2sigma_clean'
#imagename = '/drf/projets/capucine.new/dcherouv/ProjectSO/spw_SO/Dirty_cube/B335_Combine_SO_rob05_diffwt_fit1_dirty'
threshold = '0.0015058Jy/beam'
#width = '0.559km/s'
width = '0.14km/s'
start = '-2km/s'
imsize = 1200
cell = '0.03arcsec'
restfreq = '261.84368400GHz'
nchan = 150

sidelobethresh = 3.0
noisethresh = 5.0
minbeamfrac = 0.3
lownoisethresh = 1.5
negativethresh = 7.0

if len(vis) > 1:
    
    for i in range(len(vis)) :

        
        if Project[i] == '2016.1.01376.S' :
        
            fitspw.append('13:100~200;450~550;800~900')
            field.append('IRAS19347+0727')
            spw.append('13')
    
        if Project[i] == '2015.1.01188.S' :
            
            fitspw.append('4:40~120;340~440')
            field.append('B335')
            spw.append('4')
        
        if Project[i] == '2013.1.01102.S' :
        
            fitspw.append('7:100~250;650~850')
            field.append('B335')
            spw.append('7')
            
        if Project[i] == '2018.1.01311.S' :
            
            fitspw.append('45:320~400')
            field.append('3')
            spw.append('45')
            

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
           
vis_uvcontsub = ['/drf/projets/capucine.new/dcherouv/2013.1.01102.S/uid___A002_Xa0b40d_X9d64.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.01188.S/uid___A002_Xb36550_X3ec6.target.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2015.1.01188.S/uid___A002_Xb3e112_X1b95.target.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2016.1.01376.S/uid___A002_Xc2c2f2_X1961.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2016.1.01376.S/uid___A002_Xc3173a_X4708.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2016.1.01376.S/uid___A002_Xc3173a_X4ec1.ms.split.cal.contsub/',
                 '/drf/projets/capucine.new/dcherouv/2016.1.01376.S/uid___A002_Xc37375_X1ae3.ms.split.cal.contsub/']
            
if do_mstransfo == True : 
    
    for i in range(len(vis)) :
        
        vis_transfo = Prename + 'Project' + str(ProjNbr) + '/Data/B335_' + str(Project[i]) + '_spw' + str(spw[i]) + '_' + str(i) + '_transfo.ms/' 
        
        mstransform(vis=vis_uvcontsub[i], outputvis=vis_transfo, 
                    field = '*', spw = '*', regridms = True, 
                    mode = 'velocity', nchan=nchan, start=start, width=width, 
                    phasecenter=phasecenter, outframe = 'LSRK', 
                    veltype = 'radio', restfreq=restfreq, hanning = False, 
                    datacolumn=datacolumn)#, 
                    #douvcontsub = True, 
                    #fitspw=fitspw[i], fitorder=fitorder)
        
        vis_mstransfo.append(vis_transfo)
        
     
"""        
vis_mstransfo = ['/drf/projets/capucine.new/dcherouv/ProjectSO/Data/B335_2013.1.01102.S_spw7_3_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectSO/Data/B335_2015.1.01188.S_spw4_4_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectSO/Data/B335_2015.1.01188.S_spw4_5_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectSO/Data/B335_2016.1.01376.S_spw13_6_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectSO/Data/B335_2016.1.01376.S_spw13_7_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectSO/Data/B335_2016.1.01376.S_spw13_8_transfo.ms/',
                 '/drf/projets/capucine.new/dcherouv/ProjectSO/Data/B335_2016.1.01376.S_spw13_9_transfo.ms/']


visweightscale = [7e-6, 7e-6, 7e-6, 1e-5, 2.857e-5, 2.857e-5, 8e-6,
                  8e-6, 8e-6, 8e-6]
                 
#visweightscale = [8.333e-6, 8.333e-6, 8.333e-6, 4e-5, 2.857e-5, 2.857e-5, 8e-6,
                  #4e-6, 4e-6, 4e-6]

"""

if do_concat == True and len(vis_mstransfo) > 1 :
    
    concatvis = Prename + 'Project' + str(ProjNbr) + '/Data/B335_Combine_' + str(Molecule) + '.ms/'
    
    concat(vis=vis_mstransfo, concatvis=concatvis)
    
concatvis = Prename + 'Project' + str(ProjNbr) + '/Data/B335_Combine_' + str(Molecule) + '.ms/'
    
if do_clean == True :
    
    tclean(vis=concatvis, imagename=imagename, imsize=imsize,
           cell=cell, field = '*', spw = '*',
           #width=width,start=start, phasecenter=phasecenter, nchan=nchan, field = '*', spw = '*',
           restfreq=restfreq, datacolumn=datacolumn,
           specmode = 'cube', gridder = 'mosaic', 
           #deconvolver = 'hogbom', 
           niter = 10000,
           threshold=threshold,
           deconvolver = 'multiscale', scales = [0,3,9,27,81],
           weighting = 'briggs', 
           #usemask='auto-multithresh', 
           #sidelobethreshold=sidelobethresh, 
           #noisethreshold=noisethresh, lownoisethreshold=lownoisethresh, 
           #minbeamfrac=minbeamfrac, growiterations = 75, 
           #negativethreshold=negativethresh, 
           interactive = True,
           mask = Prename + 'Project5/spw_SO/Clean_cube/B335_Combine_SO_rob05_fit1_2sigma_clean.mask/',
           robust = 0.5, restoringbeam = 'common',
           verbose = True)