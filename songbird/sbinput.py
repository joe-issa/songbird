# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:41:03 2022

@author: Joe Issa
"""
import numpy as np
from songbird import frequencies
#import frequencies

class SBInput: 
    def __init__ (self, scale_type="Major", tonic="C", total_bars=6, distinct_bars=4, BPM=120, A=0.1, ADSR=np.array([.1, .05, .1, .1])):
        self.scale_type = scale_type
        self.tonic = tonic        
        self.total_bars = total_bars
        self.distinct_bars = distinct_bars
        self.BPM = BPM
        self.A = A
        self.ADSR = ADSR
        self.possible_note_lengths = np.array([1/16,1/8,1/4,1/2])
        self.scale = frequencies.Scale(self.scale_type, self.tonic)
    
    def change_scale_to(self, new_scale_type, new_tonic):
        self.scale_type = new_scale_type
        self.tonic = new_tonic
        self.scale = frequencies.Scale(new_scale_type, new_tonic)
        