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
import time

def _dedisperse( disp_pulse, vec_length, dms, f_obs, bw, nt, time_length, ndm):
    """
    Dedisperses data that has been given to it

    INPUT

    disp_pulse : (float) The data that is being dedispersed
    vec_length : (int) This is the number of frequencies that the incoming data has. In GNU radio, this is the vector size that is produced by an FFT sink
    dms        : (float vector) The range of dispersion measures that will be tested to see which is the correct one
    f_obs      : (float) The central frequency in MHz at which the bandwidth is centred about
    bw         : (float) The total observing bandwidth in MHz that is being observed
    nt         : (int) The number of time samples that are in the data set after integration. This is found by the integer ratio of the length of the data set, and freqnecy channels and integration size
    time_length: (float) The total time in seconds that the data covers. Ie the total observing time
    """
    nf = vec_length
    nt = nt
    ndm = ndm
    dmk = 4.148808e3/(time_length/nt)
    de_dis_ar = np.zeros((nt,ndm))
    #indecies = np.arange(nt)
    #print(disp_pulse.shape)
    disp_pulse = disp_pulse.reshape((nt,vec_length))
    #print(disp_pulse[10,20])
    #print(disp_pulse[31,0])
    f_low = f_obs - bw/2
    inv_flow_sq = 1/(f_low)**2
    for i in range(ndm):
        de_dis = np.zeros((nt,nf))
        for j in range(nf):
            #ys = indecies.copy()
            #shift = int(round(dmk*self.dms[i] * (inv_flow_sq -1/((self.bw*(nf-j))/nf + f_low)**2 )) )  #nf-j if freq inverted.
            shift = (round(dmk*dms[i] * (inv_flow_sq -1/( (bw*(j))/nf + f_low)**2 )) )
            #print(dmk)
            #print(shift)
            de_dis[:,j] = np.roll(disp_pulse[:,j], int(round(shift)))
        de_dis_ar[:,i] = np.sum(de_dis, axis= 1)        
    de_dis_ar = np.transpose(de_dis_ar)
    #print(np.std(de_dis_ar[0]))
    #print(de_dis_ar[0,0])
    #print(de_dis_ar[31,49])
    return de_dis_ar.flatten()

    



class dedisperse_roll(gr.sync_block):
    """
    Must add a .0 after the float values otherwise the block will not work
    """
    def __init__(self, vec_length, dms, f_obs, bw, nt, time_length):
        self.ndm = len(dms)
        gr.sync_block.__init__(self,
            name="dedisperse_roll",
            in_sig=[(np.float32, vec_length*nt)],
            out_sig=[(np.float32, nt*self.ndm)])
        self.vec_length = vec_length
        self.dms = dms
        #print(dms)
        #print(self.dms)
        self.f_obs = f_obs
        self.bw = bw
        self.nt = nt
        self.time_length = time_length



    def dedisperse(self, disp_pulse):
        """
        Dedisperses data that has been given to it
        """
        dedis_ar = _dedisperse(disp_pulse, self.vec_length, self.dms, self.f_obs, self.bw, self.nt, self.time_length, self.ndm )
        return dedis_ar
    

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        current_time = time.time()
        out[:] = self.dedisperse(in0)
        new_time = time.time()
        time_difference = new_time-current_time
        print(time_difference)
        return len(output_items[0])






