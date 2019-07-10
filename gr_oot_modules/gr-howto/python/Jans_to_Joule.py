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

import numpy
from gnuradio import gr

class Jans_to_Joule(gr.sync_block):
    """
    converts Janskys to Jouls per second per meter^2
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="Jans_to_Joule",
            in_sig=[numpy.float32], # Input signature: 1 float output
            out_sig=[numpy.float32] # Output Signature: 1 float output
        ) 


    def work(self, input_items, output_items):
        # <+signal processing here+>
        output_items[0][:] = input_items[0] * 10e-26 #This works for numpy arrays, and will convert to desired units
        return len(output_items[0])

