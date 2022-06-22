# -*- coding: utf-8 -*-
"""
Return scale and chords frequencies

@author: Joe Issa
"""
#

import numpy as np

freq = np.zeros(36, dtype=float)
A_calib = 880 #Hz
for i in range(0,36,1):
    freq[i] = A_calib*(2**((i-21)/12))

data_scale = {
        "Major": [0,2,4,5,7,9,11,12],
        "Minor": [0,2,3,5,7,8,10,12],
        "MajorPenta": [0,2,4,7,9,12],
        "MinorPenta": [0,3,5,7,10,12],
        "Egyptian": [0,2,5,7,10,12]
        }

data_chords = {
        "Major": [0,2,4,5,7,9,11,12,14,16,17,19,21,23,24],
        "Minor": [0,2,3,5,7,8,10,12,14,15,17,19,20,22,24],
        "MajorPenta": [0,2,4,7,9,12,14,16,19,21,24],
        "MinorPenta": [0,3,5,7,10,12,15,17,19,22,24],
        "Egyptian": [0,2,5,7,10,12,14,17,19,22,24]
        }

def Scale(type='Major', tonic='C'):
    skips = data_scale[type]
    root_note_index = _index_in_keyboard(tonic)
    scale = np.zeros(len(skips)+1, dtype=float)
    for i in range(len(skips)):
        scale[i] = freq[root_note_index+skips[i]]
    return scale

def Chords(type='Major', tonic='C'):
    skips = data_chords[type]
    root_note_index = _index_in_keyboard(tonic)
    chords = np.zeros((len(data_scale[type])+1, 3), dtype=float)
    for i in range(len(data_scale[type])):
        chords[i,:] = [freq[root_note_index+skips[i]], freq[root_note_index+skips[i+2]], freq[root_note_index+skips[i+4]] ]
    return chords/2 #Divide by to bring down an octave

def _index_in_keyboard(num):
    switch = {
    "C":0,
    "C#":1,
    "D":2,
    "D#":3,
    "Eb":3,
    "E":4,
    "F":5,
    "F#":6,
    "Gb":6,
    "G":7,
    "G#":8,
    "Ab":8,
    "A":9,
    "A#":10,
    "Bb":10,
    "B":11,
    }
    return switch.get(num,"Invalid Input")