"""
Main line module for cumulus.
Looks after setting up logging, parsing args and creating template and
megastack objects.
"""
import argparse
import sys


def _parse_args(args):
    """
    Use argparse to parse cli arguments.

    >>> _parse_args(['create'])
    Namespace(action='create', botologlevel='critical', loglevel='info', stackname=None, yamlfile='cumulus.yaml')

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
        "-L", "--botolog",
        dest="botologlevel", required=False, default="critical",
        help="Log Level for boto, CRITICAL, ERROR, WARNING, INFO or DEBUG")
    parser.add_argument(
        "-s", "--stack",
        dest="stackname", required=False,
        help="The stack name, used with the watch action,"
             " ignored for other actions")
    return parser.parse_args(args)


def main():
    """Main entry point for cumulus."""
    args = _parse_args(sys.argv[1:])

if __name__ == '__main__':
    main()
