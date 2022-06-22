# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:26:00 2022

@author: Joe Issa
"""

import numpy as np
import random as r

BREAK = 0
FS = 44_100

#def GenerateMelody (scale, n_bars=4, BPM=120, t_break=BREAK):
def GenerateMelody (sbin, aicomp):
    
    fills = sbin.possible_note_lengths
    t_fills = fills*240/sbin.BPM # 60/(BPM/4) == 240/BPM
    
    cbs = np.array([0])
    comp_note_lengths = np.array([]);

    for i in range(sbin.distinct_bars):
        #print("i\t",i)
        bar_fill_i = 0;
        bar_i = np.array([])
        fills_i = fills
        
        
        while bar_fill_i < 1:
            a = r.randint(0,len(fills_i)-1)
            #print("a\t",a)
            bar_i = np.append(bar_i, a)
            bar_fill_i += fills_i[a]
            #print("Bar Fill\t",bar_fill_i)
            #print("Remove?\t",(fills_i[-1]+bar_fill_i) > 1," && ", len(fills_i)>0)
            while (fills_i[-1]+bar_fill_i > 1) and len(fills_i)>1:
                #print("Note too long\t",fills_i[-1])
                fills_i = np.delete(fills_i, -1)   
            #print("# of notes after removing\t",len(fills_i))
        #print("Bar Notes\t",bar_i)
        
        comp_note_lengths = np.append(comp_note_lengths, bar_i)
        cbs = np.append(cbs, cbs[-1]+len(bar_i))
        i += 1
    
    comp_note_lengths = np.concatenate(comp_note_lengths, axis=None) #Duration of every Musical Note
    comp = np.random.randint(1,len(sbin.scale),len(comp_note_lengths)) # Musical Notes
    aicomp.cbs = cbs
    
    full_comp = np.array([])
    t_full_comp = np.array([])
    for i in range(aicomp.total_bars):
        b = r.randint(0,aicomp.distinct_bars-1)
        full_comp = np.append(full_comp, comp[cbs[b]:cbs[b+1]])
        t_full_comp = np.append(t_full_comp, t_fills[comp_note_lengths.astype(int)[cbs[b]:cbs[b+1]]])
    aicomp.comp = full_comp.astype(int)
    aicomp.t_comp = t_full_comp
    
    
    #return comp, t_fills[comp_note_lengths.astype(int)]
    return "GenerateMelody... Success"

#def Sound0 (scale, comp, t_comp, A = 0.05 , ADSR=np.array([.1, .05, .1, .1]), t_break=BREAK):
def Sound0 (sbin, aicomp):
                           
    #A is the peak reached in the attack (above 1)
    #ADSR = [time % of attack, time % of decay, time % of release]. 
    #Sustain is assumed to be the complement to 1  
    
    sig = np.array([])
    f = sbin.scale[aicomp.comp]
    import matplotlib.pyplot as plt

    comp = aicomp.comp
    t_comp = aicomp.t_comp

    for i in range(len(comp)):
        t = np.linspace(0,t_comp[i],int(t_comp[i]*FS)+1)
        a = (1+sbin.A) * np.linspace(0,1,int(sbin.ADSR[0]*len(t)))
        d = (1+sbin.A) - (sbin.A * np.linspace(0,1,int(sbin.ADSR[1]*len(t))))
        r = 1 - np.linspace(0,1,int(sbin.ADSR[3]*len(t)))
        s = np.ones(len(t)-len(a)-len(d)-len(r))
        s += sbin.ADSR[2] * np.sin(2*np.pi*np.linspace(0,t_comp[i]*s.size/len(t),s.size)*20)
        _adsr = np.append(a,d)
        _adsr = np.append(_adsr, s)
        _adsr = np.append(_adsr, r)
        sig = np.append(sig, 4096*_adsr*np.sin(2*np.pi*t*f[i]))
        #print(np.size(sig),'\t',np.size(sig)/FS)
        #sig = np.append(sig, np.zeros(int(t_break*FS)))
    sig = np.append(sig,  np.zeros(int(0.2*FS)))
    plt.plot(np.linspace(0,10,len(sig)),sig)
    plt.show()
    #date_and_time = SaveWAV(sig)
    #SaveTXT(scale, comp, t_comp, date_and_time)
    aicomp.sig = sig
    
    return "Sound0... Success"
        
