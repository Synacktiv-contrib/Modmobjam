#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Jammer Gen
# Generated: Fri Jul 27 16:32:38 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import SimpleXMLRPCServer
import osmosdr
import threading
import time
import wx


class jammer_gen(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Jammer Gen")
        _icon_path = "/usr/local/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.var_rf_gain = var_rf_gain = 10
        self.var_if_gain = var_if_gain = 10
        self.var_cent_freq = var_cent_freq = 1874200000
        self.var_bb_gain = var_bb_gain = 10
        self.var_bandwidth = var_bandwidth = 10e6
        self.samp_rate = samp_rate = 5e6
        self.sample_rate = sample_rate = samp_rate
        self.rf_gain = rf_gain = var_rf_gain
        self.if_gain = if_gain = var_if_gain
        self.cent_freq = cent_freq = var_cent_freq
        self.bb_gain = bb_gain = var_bb_gain
        self.bandwidth = bandwidth = var_bandwidth

        ##################################################
        # Blocks
        ##################################################
        _sample_rate_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sample_rate_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sample_rate_sizer,
        	value=self.sample_rate,
        	callback=self.set_sample_rate,
        	label='Sample rate',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sample_rate_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sample_rate_sizer,
        	value=self.sample_rate,
        	callback=self.set_sample_rate,
        	minimum=2e6,
        	maximum=20e6,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_sample_rate_sizer)
        _rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	label='RF gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rf_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	minimum=10,
        	maximum=60,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rf_gain_sizer)
        _if_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._if_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	label='IF gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._if_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	minimum=10,
        	maximum=60,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_if_gain_sizer)
        _cent_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._cent_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_cent_freq_sizer,
        	value=self.cent_freq,
        	callback=self.set_cent_freq,
        	label='Freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._cent_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_cent_freq_sizer,
        	value=self.cent_freq,
        	callback=self.set_cent_freq,
        	minimum=900e6,
        	maximum=2200e6,
        	num_steps=500,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_cent_freq_sizer)
        _bb_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._bb_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	label='BB gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._bb_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	minimum=10,
        	maximum=60,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_bb_gain_sizer)
        _bandwidth_sizer = wx.BoxSizer(wx.VERTICAL)
        self._bandwidth_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_bandwidth_sizer,
        	value=self.bandwidth,
        	callback=self.set_bandwidth,
        	label='Bandwidth',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._bandwidth_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_bandwidth_sizer,
        	value=self.bandwidth,
        	callback=self.set_bandwidth,
        	minimum=2e6,
        	maximum=50e6,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_bandwidth_sizer)
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer(('localhost', 8888), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(sample_rate)
        self.osmosdr_sink_0.set_center_freq(cent_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(rf_gain, 0)
        self.osmosdr_sink_0.set_if_gain(if_gain, 0)
        self.osmosdr_sink_0.set_bb_gain(bb_gain, 0)
        self.osmosdr_sink_0.set_antenna('1', 0)
        self.osmosdr_sink_0.set_bandwidth(bandwidth, 0)

        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 50, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.osmosdr_sink_0, 0))

    def get_var_rf_gain(self):
        return self.var_rf_gain

    def set_var_rf_gain(self, var_rf_gain):
        self.var_rf_gain = var_rf_gain
        self.set_rf_gain(self.var_rf_gain)

    def get_var_if_gain(self):
        return self.var_if_gain

    def set_var_if_gain(self, var_if_gain):
        self.var_if_gain = var_if_gain
        self.set_if_gain(self.var_if_gain)

    def get_var_cent_freq(self):
        return self.var_cent_freq

    def set_var_cent_freq(self, var_cent_freq):
        self.var_cent_freq = var_cent_freq
        self.set_cent_freq(self.var_cent_freq)

    def get_var_bb_gain(self):
        return self.var_bb_gain

    def set_var_bb_gain(self, var_bb_gain):
        self.var_bb_gain = var_bb_gain
        self.set_bb_gain(self.var_bb_gain)

    def get_var_bandwidth(self):
        return self.var_bandwidth

    def set_var_bandwidth(self, var_bandwidth):
        self.var_bandwidth = var_bandwidth
        self.set_bandwidth(self.var_bandwidth)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sample_rate(self.samp_rate)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self._sample_rate_slider.set_value(self.sample_rate)
        self._sample_rate_text_box.set_value(self.sample_rate)
        self.osmosdr_sink_0.set_sample_rate(self.sample_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self._rf_gain_slider.set_value(self.rf_gain)
        self._rf_gain_text_box.set_value(self.rf_gain)
        self.osmosdr_sink_0.set_gain(self.rf_gain, 0)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self._if_gain_slider.set_value(self.if_gain)
        self._if_gain_text_box.set_value(self.if_gain)
        self.osmosdr_sink_0.set_if_gain(self.if_gain, 0)

    def get_cent_freq(self):
        return self.cent_freq

    def set_cent_freq(self, cent_freq):
        self.cent_freq = cent_freq
        self._cent_freq_slider.set_value(self.cent_freq)
        self._cent_freq_text_box.set_value(self.cent_freq)
        self.osmosdr_sink_0.set_center_freq(self.cent_freq, 0)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self._bb_gain_slider.set_value(self.bb_gain)
        self._bb_gain_text_box.set_value(self.bb_gain)
        self.osmosdr_sink_0.set_bb_gain(self.bb_gain, 0)

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self._bandwidth_slider.set_value(self.bandwidth)
        self._bandwidth_text_box.set_value(self.bandwidth)
        self.osmosdr_sink_0.set_bandwidth(self.bandwidth, 0)


def main(top_block_cls=jammer_gen, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
