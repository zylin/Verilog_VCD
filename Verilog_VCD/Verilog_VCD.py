# The guts has been moved into pydev_reader.reader.py, what remains here
# is just enough to make it compatible with the 0.11 API

import pydev_reader
from pydev_reader import VCDParseError

global timescale
global endtime


def list_sigs(file):
    """Parse input VCD file into data structure, 
    then return just a list of the signal names."""

    vcd, _, _ = pydev_reader._parse_vcd(file, only_sigs=1)

    sigs = []
    for k in vcd.keys():
        v = vcd[k]
        nets = v['nets']
        sigs.extend(n['hier'] + '.' + n['name'] for n in nets)

    return sigs


def parse_vcd(file, only_sigs=0, use_stdout=0, siglist=[], opt_timescale=''):
    """Parse input VCD file into data structure.
    Also, print t-v pairs to STDOUT, if requested."""

    global endtime
    global timescale
    data, timescale, endtime = pydev_reader._parse_vcd(
        file, only_sigs, use_stdout, siglist, opt_timescale)
    return data


def calc_mult(statement, opt_timescale=''):
    """ 
    Calculate a new multiplier for time values.
    Input statement is complete timescale, for example:
      timescale 10ns end
    Input new_units is one of s|ms|us|ns|ps|fs.
    Return numeric multiplier.
    Also sets the package timescale variable.
    """

    global timescale
    time_value, timescale = pydev_reader._calc_mult(statement, opt_timescale)
    return time_value


def get_timescale():
    return timescale


def get_endtime():
    return endtime
