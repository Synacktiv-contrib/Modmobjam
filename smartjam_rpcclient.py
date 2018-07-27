#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <sebastien.dudek(<@T>)synacktiv.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return FlUxIuS ;)
# ----------------------------------------------------------------------------

from __future__ import print_function

import time
import json
import random
import xmlrpclib
import argparse
from utils.eu_arfcn_calc import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Modmodjam - Software-Defined Radio Jammer')
    parser.add_argument('-s', '--host', dest='host', default='localhost',
            help='hostname to send RPC commands (default: "localhost")')
    parser.add_argument('-p', '--port', dest='port', default=8888,
            help='RPC server port (e.g: 8888 by default)')
    parser.add_argument('-f', '--file', dest='filepath', required=True,
            help='Modmobmap json file')
    parser.add_argument('-d', '--delay', dest='delay', default=2,
            help='Delay between each frequency to jam in sec (default: 2)')
    parser.add_argument('-b', '--bandwidth', dest='bandwidth', default=None,
            help='Define a static bandwidth. Will also influence the sample rate. By default it will use the bandwidth of the JSON file')
    parser.add_argument('-l', '--linkjam', dest='linkjam', default=0,
            help='Link to jam: "0" for downlink and "1" for uplink (default: "0")')
    parser.add_argument('-w', '--filterplm', dest='filterplmn', default=None,
            help='PLMN to filter. Example: 2082-1 (separated with commas)')

    t_freqs = {}
    args = parser.parse_args()
    host = args.host
    port = int(args.port)
    linkjam = int(args.linkjam)
    filepath = args.filepath
    delay = int(args.delay)
    filterplmn = args.filterplmn
    bandwidth = args.bandwidth

    s = xmlrpclib.Server("http://%s:%s" % (host, port))
    
    with open(filepath) as f:
        modmobdata = json.load(f)

    plmns = []
    if filterplmn is not None:
        plmns = args.filterplmn.split(',')

    for key, val in modmobdata.items():
        plmn = val['PLMN']
        if plmn in plmns or filterplmn is None:
            band = None
            ctype = None
            findex = None
            downlink = None
            uplink = None
            cbandwidth = 10 # MHz
            if 'RX' in val:
                findex = val['RX']
            elif 'eARFCN' in val:
                findex = val['eARFCN']
            if 'band' in val:
                band = val['band']
            if 'type' in val:
                ctype = val['type']
            if bandwidth is not None:
                cbandwidth = bandwidth
            else:
                if 'bandwidth' in val:
                    cbandwidth = int(val['bandwidth'].replace('MHz',''))
            try:
                if ctype == '3G':
                    downlink, uplink = uarfcn2freq(band, findex, None)
                elif ctype == '4G':
                    downlink, uplink = earfcn2freq(band, findex, None)
                elif ctype == '2G':
                    pass
                    # not implemented for our purposes
                if downlink is not None and uplink is not None:
                    cent_freq = downlink
                    if linkjam == 1:
                        cent_freq = uplink
                    t_freqs[key] = {    'freq' : cent_freq,
                                        'bandwidth' : cbandwidth } 
            except Exception as e:
                print (e)
    while True:
        for key, val in t_freqs.items():
            print ("[+] Jamming cell {cell} central frequency at {freq} MHz with {bandwidth} MHz bandwidth".format(cell=key, freq=val['freq'], bandwidth=val['bandwidth']))
            s.set_var_cent_freq(val['freq']*1000000)
            s.set_var_bandwidth(val['bandwidth']*1000000)
            time.sleep(delay)
