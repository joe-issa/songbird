# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:59:28 2022

@author: Joe Issa
"""

from songbird import frequencies
from datetime import datetime
import pytz
import numpy as np

class AIComp:
    
    def __init__(self, sbinput, comp=np.array([], dtype=int), t_comp=np.array([]), sig=np.array([]), cbs=np.array([])):
        self.comp = comp
        self.t_comp = t_comp
        self.sig = sig
        self.cbs = cbs
        
        self.scale_type = sbinput.scale_type
        self.tonic = sbinput.tonic        
        self.total_bars = sbinput.total_bars
        self.distinct_bars = sbinput.distinct_bars
        self.BPM = sbinput.BPM
        self.possible_note_lengths = sbinput.possible_note_lengths
        self.scale = frequencies.Scale(self.scale_type, self.tonic)
        
        location = pytz.timezone('Asia/Beirut')
        self.date_and_time = datetime.now(location).strftime("%d-%m-%y-%H%M%S")
        self.FS = 44100
        
    def SaveWAV(self):
        import scipy.io.wavfile
        
        wav_name = 'AI_comp_of_' + self.date_and_time + '.wav'
        scipy.io.wavfile.write(wav_name, self.FS, self.sig.astype(np.int16))
        return "SaveWAV... Success"
    
    def SaveTXT(self):
        f= open('details_of_comp_' + self.date_and_time + '.txt',"w+")
        f.writelines(["\nScale in Hz\n",str(self.scale)])
        f.writelines(["\nComposition\n",str(self.comp),"\n",str(self.scale[self.comp])])
        f.writelines(["\nComposition Note Length\n",str(self.t_comp)])
        f.close()
        return "SaveTXT... Success"
        