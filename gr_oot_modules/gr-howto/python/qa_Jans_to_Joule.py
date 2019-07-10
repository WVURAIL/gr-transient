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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from Jans_to_Joule import Jans_to_Joule

class qa_Jans_to_Joule (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        source_d = ( 10,2,-1)
        expected_result = ( 10*10e-26,2*10e-26, -1*10e-26)
        src = blocks.vector_source_f (source_d)
        atn = Jans_to_Joule ()
        dst = blocks.vector_sink_f () 
        self.tb.connect (src, atn)
        self.tb.connect (atn, dst)
        self.tb.run ()
        result = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result, 6)



if __name__ == '__main__':
    gr_unittest.run(qa_Jans_to_Joule, "qa_Jans_to_Joule.xml")
