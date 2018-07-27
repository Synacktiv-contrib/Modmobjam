# Modmobjam

A smart jamming proof of concept for mobile equipments that could be powered with [Modmobmap](https://github.com/Synacktiv/Modmobmap)

For more information, this little tool has been presented during SSTIC rump 2018:

- english slides: https://www.synacktiv.com/ressources/sstic_rump_2018_modmobjam.pdf
- french presentation: https://static.sstic.org/rumps2018/SSTIC_2018-06-14_P10_RUMPS_22.mp4

## Warning

You should be warned that Jamming is illegal and you're responsible for any damages when using it on your own.

## Prerequisites

- a radio devices that is enabled to transmit signal (HackRF, USRP, bladeRF, and so on.)
- GNU Radio installed
- Modmobmap to perform automatic smartjamming: https://github.com/Synacktiv/Modmobmap

## Usage

### Manual jamming 

If you have a HackRF or any device compatible with osmocom drivers, you can directly run the code provided in ``GRC/jammer_gen.py`` as follows:

``bash
$ python GRC/jammer_gen.py
``

For those who want to use another device like USRP, edit the GNU Radio block schema ``GRC/jammer_gen.grc``:

``bash
$ gnuradio-companion GRC/jammer_gen.grc
``

Then you can configure the central frequency with the WX GUI to target a frequency. But this tool has also a feature to do it automatically.

### Automatic smartjamming

To automate jamming, you can first get a list of we the [Modmobmap](https://github.com/Synacktiv/Modmobmap) that saves a JSON file after monitoring surrounding cells in a precise location. This JSON file looks as follows:

``bash
$ cat cells_<generated timestamp>.json 
{
    "****-***50": {
        "PCI": "****", 
        "PLMN": "208-01", 
        "TAC": "50****", 
        "band": 3, 
        "bandwidth": "20MHz", 
        "eARFCN": 1850, 
        "type": "4G"
    }, 
    "7-***": {
        "PLMN": "208-20", 
        "arfcn": 1018, 
        "cid": "***", 
        "type": "2G"
    }, 
    "****:-****12": {
        "PLMN": "208-1", 
        "RX": 10712, 
        "TX": 9762, 
        "band": 1, 
        "type": "3G"
    },
    [...] 
}
``

After generating this file containing cells to jam, you can launch the RPC client that communicate with ``GRC/jammer_gen.py`` as follows:

``bash
python smartjam_rpcclient.py -f cells_<generated timestamp>.json
``

Then leverage the gain for transmission and you should observe that a lot of noise is overflowing the targeted cells.

Please note that the delay between each targeted cell can be set with the provided arguments.

## Arguments

``bash
$ python smartjam_rpcclient.py -h                                                                                                                                                                            2 ↵
usage: smartjam_rpcclient.py [-h] [-s HOST] [-p PORT] -f FILEPATH [-d DELAY]
                             [-b BANDWIDTH] [-l LINKJAM] [-w FILTERPLMN]

Modmodjam - Software-Defined Radio Jammer

optional arguments:
  -h, --help            show this help message and exit
  -s HOST, --host HOST  hostname to send RPC commands (default: "localhost")
  -p PORT, --port PORT  RPC server port (e.g: 8888 by default)
  -f FILEPATH, --file FILEPATH
                        Modmobmap json file
  -d DELAY, --delay DELAY
                        Delay between each frequency to jam in sec (default:
                        2)
  -b BANDWIDTH, --bandwidth BANDWIDTH
                        Define a static bandwidth. Will also influence the
                        sample rate. By default it will use the bandwidth of
                        the JSON file
  -l LINKJAM, --linkjam LINKJAM
                        Link to jam: "0" for downlink and "1" for uplink
                        (default: "0")
  -w FILTERPLMN, --filterplm FILTERPLMN
                        PLMN to filter. Example: 2082-1 (separated with
                        commas)
``
