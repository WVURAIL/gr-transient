#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
from gnuradio import gr
from scipy import signal

def peakfinder_pulsar_DM(x, threshold):
    '''
    Finds the peaks in a dedispersed pulsar that has been run through a matched filter with a Gaussian.
    
    Note: The array or list used for x must have two dimensions. The first specifying which DM we are looking at, and 
          the second representing the number of data points.
          
          The threshold must be appropriate for every DM. This means that it should have the same length as the 
          number of DMs
    
    
    INPUTS:
    
    x         : (array or list) The power of the pulse for every DM that has been looked at.
    threshold : (float) The y value at which peaks can be designated as peaks.
    
    
    OUTPUTS:
    
    peaksy: (list) The values ,for every DM, that can be called peaks over the threshold. 
    
    
    '''
    
    peaksy = []
    for j in range(np.shape(x)[0]):
        peakssy= []
        DM_intensity = x[j]
        for i in range(len(DM_intensity)-1):
            if DM_intensity[i] > threshold[j] and DM_intensity[i-2]<DM_intensity[i] and DM_intensity[i-1] <DM_intensity[i] and DM_intensity[i+1] < DM_intensity[i] and DM_intensity[i+2] < DM_intensity[i]:
                peakssy.append(DM_intensity[i])
        peaksy.append(peakssy)
    return peaksy




def _detection(img1, img2, pac_size, pw, nt, ndm):
    """
    Determines if a pulsar has been detected. If so, the data is let through and the dedispersed pulsar is given as an output array. If not, then nothing is given
    and the statement that a pulsar has not been detected is printed.

    NOTES:


    INPUT:

    img1    : (float array) The dedispersed pulsar that we are anylizing.
    img2    : (float array) The noise that is assumed to be the background noise for the pulsar.
    pac_size: (int) The number of samples wide the pulse will be
    pw      : (float) The variance of the pulse


    OUTPUT

    SNR: The signal to noise ratio of the pulsar to noise




    """

    img1 = img1.reshape((ndm, nt))
    img2 = img2.reshape((ndm,nt))
    gau = np.exp(.5*-( np.arange(-int(pac_size/2),int(pac_size/2)) /pw)**2)
    correlates = []
    corr_bb = []
    #print(gau)
    
    for i in range(len(img1)):
        correlates.append(signal.convolve(img1[i], gau, mode='same'))
        corr_bb.append(signal.convolve(img2[i],gau,mode='valid'))
    correlates = np.asarray(correlates)
    corr_bb = np.asarray(corr_bb)
    #print(correlates.shape)
    
    
    mean_heights = np.zeros(len(correlates))
    for i in range(len(correlates)):
        mean_heights[i] = np.mean(correlates[i])
    peak_heights = peakfinder_pulsar_DM(correlates, mean_heights)
    #print(peak_heights)
    maximums = np.zeros(len(peak_heights))
    for i in range(len(peak_heights)):
        maximums[i] = np.mean(peak_heights[i])
    #Find the mean and standard deviation
    corr_mean = np.mean(corr_bb, axis=1)
    corr_std = np.std(corr_bb, axis=1)
    #print(corr_bb.shape)
    print(corr_std)
    #print(corr_mean)
    #print(maximums)
    SNR = (maximums-corr_mean)/(corr_std)

    return SNR.flatten(), img1






class Pulse_Detection(gr.sync_block):
    """
    This block detects whether or not a pulsar or FRB is present in the dataset. 

    INPUT:



    OUTPUT:


    """
    def __init__(self, pac_size, pw, nt, dms):
        self.ndm = len(dms)
        gr.sync_block.__init__(self,
            name="Pulse_Detection",
            in_sig=[(np.float32, nt*self.ndm),(np.float32,nt*self.ndm)],
            out_sig=[(np.float32, nt)])
        self.pac_size = pac_size 
        self.pw = pw
        self.nt = nt
        self.dms=dms


    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]
        outcome, sig= _detection(in0,in1, self.pac_size, self.pw, self.nt, self.ndm)
        #print(len(np.where(outcome>10)[0]))
        signals = []
        for i in range(self.ndm):
            if len(np.where(outcome>10)[0]) <=1:
                print("NO PULSAR DETECTED")
                sig = 0
            elif  outcome[i]==outcome.max():
                signals = sig[i]
        signals = np.asarray(signals)

        # <+signal processing here+>
        out[:] = signals
        return len(output_items[0])

