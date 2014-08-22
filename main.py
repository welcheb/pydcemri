#!/usr/bin/env python

# Command line interface for PyDCEMRI
#
# Copyright (C) 2014   David S. Smith
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# 

import argparse
import os.path
#import pydce

def extant_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not os.path.exists(x):
        raise argparse.ArgumentError("{0} does not exist".format(x))
    return x

if __name__ == '__main__':

    # create parser object
    parser = argparse.ArgumentParser(description='Process DCE-MRI data.',
                                    epilog='For questions and bug reports, contact David Smith <david.smith@gmail.com>')
                                    
    # add arguments                                
    parser.add_argument('-x', '--extended',   dest='extended', help='use Extended Tofts-Kety instead of Standard', action='store_true')
    parser.add_argument('-p', '--plotting',   dest='plotting', help='plot intermediate results'                  , action='store_true')
    parser.add_argument('-v', '--verbose',    dest='verbose',  help='show verbose output'                        , action='store_true')
    parser.add_argument('-R', '--relaxivity', dest='R',        help='contrast agent relaxivity (1/s)',     type=float,       metavar='RELAXIVITY')
    parser.add_argument('-r', '--TR',         dest='TR',       help='repetition time (ms)',                type=float,       metavar='TIME')
    parser.add_argument('-d','--dce_flip',    dest='dce_flip', help='flip angle of DCE data',              type=float,       metavar='DEGREES')
    parser.add_argument('-t','--t1_flip',     dest='t1_flip',  help='flip angle(s) of T1 data',            type=float,       metavar='DEGREES', nargs='+')
    parser.add_argument('-D','--dcefile',     dest='dcefile',  help='path to DCE data file in MAT format', type=extant_file, metavar="FILE", required=True)
    parser.add_argument('-T','--t1file',      dest='t1file',   help='path to T1 data file in MAT format',  type=extant_file, metavar="FILE", required=True)
    parser.add_argument('-A','--aiffile',     dest='aiffile',   help='path to AIF data file in MAT format', type=extant_file, metavar="FILE", required=True)

    # parse arguments, e.g.
    # parms = '--dcefile ./invivo/data_dce.mat --t1file ./invivo/data_t1.mat --aiffile ./invivo/AIF.mat --relaxivity 4.76 --TR 7.939 --dce_flip 20.0 --t1_flip 20.0 18 16 14 12 10 8 6 4 2 -p -x -v'
    # args = parser.parse_args(parms.split())
    args = parser.parse_args()

    # print arguments if verbose
    if args.verbose:
        args_dict = vars(args)
        for key in sorted(args_dict):
            print "%10s = %s" % (key, str(args_dict[key])) 
        
#pydce.run_model(args.dcefile, args.t1file, args.t1_flip, R=args.R, 
#               TR=args.TR, dce_flip=args.dce_flip, 
#               extended=args.extended, plotting=args.plotting)

