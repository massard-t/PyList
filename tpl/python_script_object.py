#!/usr/bin/env python
# coding: utf-8
import os
import sys
import logging
import argparse

from logging.handlers import RotatingFileHandler

__author__ = "Theo Massard <massar_t@etna-alternance.net"


def prepare_my_parser():
    """
    Prepares the parser to allow arguments.
    Current args:
     -q quiet mode        | -v verbose mode
     -o output filename   | -e error log filename
     -m mode (ip|name)    | -c custom config file
     -i custom input file | -n max ips to display (0 is infinite)
     --set-boolean display related ips to the req (False by default)
    """
    desc = "Find weird IPs accessing the apache server a lotof time"
    parser = argparse.ArgumentParser(description=desc)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quiet", action="store_true", default=False,
                        help="Quiet mode, silences logging\
                        below CRITICAL level")
    group.add_argument("-v", "--verbose", action="store_true", default=False,
                        help="Verbose mode, beware.")
    parser.add_argument("-o", "--output-file",
                        help="Recapitulative log file", default="recap.log")
    parser.add_argument("-e", "--error-file",
                        help="Error log", default="error.log")
    parser.add_argument("-m", "--mode", choices=["ip", "name"],
                        help="Chose the mode to use to analyze",
                        default="name")
    parser.add_argument("-c", "--config-file", default="bot_finder.conf",
                        help="Custom config file (yaml format)")
    parser.add_argument("-i", "--input-file", default="access.log",
                        help="Input file containing the log to analyze")
    parser.add_argument("--set-boolean", default=False,
                        action="store_true",
                        help="Allows to store a boolean.")
    parser.add_argument("-n", "--max-display", default=40, type=int,
                        help="Maximum results to display. Leave at 0 for fulle")
    parser.add_argument("-r", "--min-requests", default=40, type=int,
                        help="Required number of requests by the same\
                        suspect to be displayed.")
    return parser


def prepare_my_logger(args):
    """
    Prepares the logger
    There are two filehandlers, one for results and another
    used to store errors.
    """
    global LOGGER
    if args['quiet']:
        level = logging.CRITICAL
    elif args['verbose']:
        level = logging.DEBUG
    else:
        level = logging.INFO
    LOGGER = logging.getLogger()
    LOGGER.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s] %(message)s')
    file_formatter = logging.Formatter(
        '[%(levelname)s] %(message)s'
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    error_handler = RotatingFileHandler(
        args['error_file'], 'w', 1000000000, 1
    )
    error_handler.setLevel(logging.DEBUG)
    error_handler.setFormatter(file_formatter)
    recap_handler = RotatingFileHandler(
        args['output_file'], 'w', 1000000000, 1
    )
    recap_handler.setLevel(logging.INFO)
    recap_handler.setFormatter(file_formatter)
    LOGGER.addHandler(error_handler)
    LOGGER.addHandler(recap_handler)
    LOGGER.addHandler(stream_handler)

class SomeClass(object):
    """
    A complete description of the object
    """
    def __init__(self, name, **args):
        self.settings = args
        self.name = name
        LOGGER.info("%s is set", self.name)

    def __repr__(self):
        LOGGER.debug("%s object", self.name)
        for k, v in self.settings:
            LOGGER.debug("%s : %s", k, v)

def main():
    parser = prepare_my_parser()
    try:
        args = vars(parser.parse_args(sys.argv[1:]))
    except IndexError:
        args = vars(parser.parse_args())
    
    prepare_my_logger(args)
    sc = SomeClass(args)
    print sc

if __name__ == '__main__':
    main()
