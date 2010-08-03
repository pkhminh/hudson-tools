#!/usr/bin/env python
# encoding: utf-8
"""
convertJtJunit.py

Created by Mahmood Ali on 2009-12-19.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import getopt
import junit
import jtreg

help_message = '''
The help message goes here.
'''


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def unit_name(name):
    return name.replace(".xml", "-TEST.xml")

def convert(xml_input):
    output = unit_name(xml_input)
    listener = junit.JunitListener(output=output)
    replay = jtreg.JTregReplay(report=xml_input, listener=listener)
    replay.process()

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
        except getopt.error, msg:
            raise Usage(msg)
    
        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-o", "--output"):
                output = value

        convert(args[0])
        
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())
