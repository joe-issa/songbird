# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:54:44 2022

@author: Joe Issa
"""
import songbird as sb

in1 = sb.SBInput("Minor","Eb")

comp1 = sb.AIComp(in1)

sb.GenerateMelody(in1,comp1)
sb.Sound0(in1, comp1)

comp1.SaveTXT()
comp1.SaveWAV()
