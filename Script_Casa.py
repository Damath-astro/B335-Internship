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
excludechans = True
fitorder = 1
datacolumn = 'data'
niter = 10000
phasecenter = 'J2000 19h37m00.9 +7d34m09.6'
vis_split = []
vis_uvcontsub = []
vis_mstransfo = []
Prename = '/drf/projets/capucine.new/dcherouv/'
fitspw = []  
spw = []
field = []

do_uvcontsub = False
do_split = False
do_concat = True
do_mstransfo = True
do_clean = False
Interactive = False
Molecule = 'HCO'
ProjNbr = 'HCO'
#Project = list(input("Project name (list) :"))
Project = ['2013.1.01301.S', '2015.1.00169.S', '2015.1.00169.S',
           '2015.1.00169.S', '2015.1.00169.S', '2015.1.00169.S',
           '2015.1.00169.S', '2012.1.00346.S']

vis = ['/drf/projets/capucine.new/dcherouv/2013.1.01301.S/uid___A002_Xa8df68_X143d.ms.split.cal/', 
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb57bb5_X451.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5aa7c_X4c04.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5bd46_X1b74.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xb5bd46_X2404.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd1daeb_X2e93.ms.split.cal/',
       '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd21a3a_X1d4a.ms.split.cal/']

phasecenter = 'J2000 19h37m00.9 +7d34m09.6'
imagename = '/drf/projets/capucine.new/dcherouv/Project0/spw_HCO/Dirty_cube/B335_Combine_HCO_rob05_fit1_dirty'
threshold = '0.017817096Jy/beam'
#width = '0.8206km/s'
width = '0.950km/s'
start = '0km/s'
imsize = 900
cell = '0.03arcsec'
restfreq = '356.734223GHz'
nchan = 50
mask = '/drf/projets/capucine.new/dcherouv/Project4/spw_SO/Clean_cube/B335_Combine_SO_rob05_2sigma_automask_std_clean.mask/'


if len(vis) > 1:
    
    for i in range(len(vis)) :
        
        if Project[i] == '2013.1.00879.S' and Molecule == 'C18O' :
            
            fitspw.append('0:40~85')
            field.append('3')
            spw.append('0')
            
        if Project[i] == '2018.1.00452.S' and Molecule == 'C18O' :
            
            fitspw.append('0:180~239')
            field.append('2')
            spw.append('31')
            
        if Project[i] == '2013.1.00211.S' and Molecule == 'C18O' :
            
            fitspw.append('0:40~80')
            field.append('4')
            spw.append('6')
            
        if Project[i] == '2013.1.00211.S_7m' and Molecule == 'C18O':
            
            fitspw.append('0:400~600')
            field.append('B335')
            spw.append('6')
    
        if Project[i] == '2016.1.01376.S' and Molecule == 'SO' :
        
            fitspw.append('0:120~220;260~380')
            field.append('4')
            spw.append('13')
    
        if Project[i] == '2015.1.01188.S' :
        
            if Molecule == 'H13CO' :
            
                fitspw.append('0')
                field.append('0')
                spw.append('5')
            
            elif Molecule == 'SO' :
            
                fitspw.append('0:160~340')
                field.append('0')
                spw.append('4')
        
        if Project[i] == '2013.1.01102.S' and Molecule == 'SO' :
        
            fitspw.append('0:300~600')
            field.append('4')
            spw.append('7')
        
        if Project[i] == '2013.1.01301.S' and Molecule == 'HCO' :
        
            fitspw.append('0:750~1850')
            field.append('CB199')
            #spw.append('2:500~1000')
            spw.append('2')
            
        if Project[i] == '2012.1.00346.S' and Molecule == 'HCO' :
            
            fitspw.append('0:105~175')
            field.append('B335')
            spw.append('1')
            
        if Project[i] == '2015.1.00169.S' :
            
            if Molecule == 'HCO' and vis[i] == '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd1daeb_X2e93.ms.split.cal/' or vis[i] == '/drf/projets/capucine.new/dcherouv/2015.1.00169.S/uid___A002_Xd21a3a_X1d4a.ms.split.cal/':
            
                fitspw.append('0:200~400;1700~1800')
                field.append('B335')
                spw.append('1')
                
            else :
                
                fitspw.append('0:200~400;1700~1800')
                field.append('B335')
                spw.append('5')
            
            #elif Molecule == 'CS' :
                
                

if do_split == True :
    
    #vis = list(input("Vis (list):"))
    
    for i in range(len(vis)) :
        
        outputvis = Prename + 'Project' + str(ProjNbr) + '/Data/B335_' + str(Project[i]) + '_spw' + str(spw[i]) + '_' + str(i) + '.ms/' 
        
        if Project[i] == '2013.1.01102.S' :
        
            split(vis=vis[i], outputvis=outputvis, field=field[i], 
                  spw=spw[i], datacolumn=datacolumn, width = 2)
        
            vis_split.append(outputvis)
            
        elif Project[i] == '2018.1.00452.S' :
         
             split(vis=vis[i], outputvis=outputvis, field=field[i], 
                   spw=spw[i], datacolumn=datacolumn)
         
             vis_split.append(outputvis)   
             
        elif Project[i] == '2012.1.00346.S': 
            
            split(vis=vis[i], outputvis=outputvis, field=field[i], 
                  spw=spw[i], datacolumn=datacolumn) 
                  #width = 16)
        
            vis_split.append(outputvis)   
            
        elif Project[i] == '2015.1.00169.S' and Molecule == 'HCO' :
            
            split(vis=vis[i], outputvis=outputvis, field=field[i], 
                  spw=spw[i], datacolumn=datacolumn)
        
            vis_split.append(outputvis) 
            
        else : 
            
            split(vis=vis[i], outputvis=outputvis, field=field[i], 
                  spw=spw[i], datacolumn=datacolumn)
        
            vis_split.append(outputvis)
            
        

if do_uvcontsub == True :
    
    for i in range(len(vis)) :
        
        if Project[i] == '2015.1.00169.S' and Molecule == 'HCO' :
            
            uvcontsub(vis=vis_split[i], fitspw=fitspw[i], 
                      excludechans = False, solint=solint, 
                      fitorder=fitorder)
        
            vis_uvcontsub.append(vis_split[i][:-1] + '.contsub/')
    
        else :
            
            uvcontsub(vis=vis_split[i], fitspw=fitspw[i], 
                      excludechans=excludechans, solint=solint, 
                      fitorder=fitorder)
    
            vis_uvcontsub.append(vis_split[i][:-1] + '.contsub/')
            
#vis_split = #['/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2013.1.01301.S_spw2_0.ms/',
             #'/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_1.ms/',
             #'/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_2.ms/',
             #'/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_3.ms/',
             #'/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_4.ms/',
vis_split = ['/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw1_5.ms/',
             '/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw1_6.ms/']#,
             #'/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2012.1.00346.S_spw1_0.ms/']

#vis_uvcontsub = #['/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2013.1.01301.S_spw2_0.ms.contsub/',
                 #'/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_1.ms.contsub/',
                 #'/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_2.ms.contsub/',
                 #/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_3.ms.contsub/',
                 #'/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_4.ms.contsub/',
vis_uvcontsub = ['/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw1_5.ms.contsub/',
                 '/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw1_6.ms.contsub/']#,
                 #'/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2012.1.00346.S_spw1_0.ms.contsub/']
            
if do_mstransfo == True : 
    
    for i in range(len(vis_split)) :
        
        vis_transfo = vis_split[i][:-1] + '_transfo.contsub/'
        
        mstransform(vis=vis_uvcontsub[i], outputvis=vis_transfo, 
                    field = '*', spw = '*', regridms = True, mode = 'velocity', 
                    nchan=nchan, start=start, width=width, phasecenter=phasecenter,
                    outframe = 'LSRK', veltype = 'radio', 
                    restfreq=restfreq, 
                    hanning = True, datacolumn=datacolumn)
        
        vis_mstransfo.append(vis_transfo)


vis_mstransfo = ['/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2013.1.01301.S_spw2_0.ms_transfo.contsub/',
                 '/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_1.ms_transfo.contsub/',
                 '/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_2.ms_transfo.contsub/',
                 '/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_3.ms_transfo.contsub/',
                 '/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw5_4.ms_transfo.contsub/',
                 '/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw1_5.ms_transfo.contsub/',
                 '/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2015.1.00169.S_spw1_6.ms_transfo.contsub/',
                 '/drf/projets/capucine.new/dcherouv/ProjectHCO/Data/B335_2012.1.00346.S_spw1_0.ms_transfo.contsub/']

visweightscale = [0.011, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.0005, 0.000000025]

if do_concat == True and len(vis_mstransfo) > 1 :
    
    concatvis = Prename + 'Project' + str(ProjNbr) + '/Data/B335_Combine_' + str(Molecule) + '.ms/'
    
    concat(vis=vis_mstransfo, concatvis=concatvis, visweightscale=visweightscale)
    
    
if do_clean == True :
    
    tclean(vis=concatvis, imagename=imagename, imsize=imsize,
           cell=cell, field = '*', spw = '*',
           #width=width,start=start, phasecenter=phasecenter, nchan=nchan, field = '*', spw = '*',
           restfreq=restfreq, datacolumn=datacolumn,
           specmode = 'cube', gridder = 'mosaic', 
           deconvolver = 'hogbom', niter = 0, weighting = 'briggs', 
           robust = 0.5, interactive = False, restoringbeam = 'common')