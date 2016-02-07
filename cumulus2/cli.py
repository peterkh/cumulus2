"""
Main line module for cumulus.
Looks after setting up logging, parsing args and creating template and
megastack objects.
"""
from __future__ import print_function
import argparse
import logging
import sys


def _parse_args(args):
    """
    Use argparse to parse cli arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        help="Action to preform: create, check, update, delete or watch")
    parser.add_argument(
        "-y", "--yamlfile",
        dest="yamlfile", required=False, default="cumulus.yaml",
        help="The yaml file to read mega stack configuration from "
             "(default: ./cumulus.yaml)")
    parser.add_argument(
        "-l", "--log",
        dest="loglevel", required=False, default="info",
        help="Log Level for output messages, "
             "CRITICAL, ERROR, WARNING, INFO or DEBUG")
    parser.add_argument(
        "-s", "--stack",
        dest="stackname", required=False,
        help="The stack name, used with the watch action,"
             " ignored for other actions")
    return parser.parse_args(args)


def _setup_logging(level):
    """Set up logging levels and return logger object."""
    # Get and configure the log level
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        print('Invalid log level: %s' % level)
        sys.exit(1)
    logging.basicConfig(level=numeric_level)
    return logging.getLogger(__name__)


def main():
    """Main entry point for cumulus."""
    args = _parse_args(sys.argv[1:])
    logger = _setup_logging(args.loglevel)
    logger.debug('Command line  options: %s', args)

if __name__ == '__main__':
    main()
