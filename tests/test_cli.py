"""Test cli module."""
import argparse
from cumulus2 import cli
from nose.tools import assert_raises, assert_equals


def test_parse_args_with_cmd():
    """_parse_args(): Namespace object returned with correct action."""
    response = argparse.Namespace(
        action='create', loglevel='info', stackname=None,
        yamlfile='cumulus.yaml')
    assert_equals(cli._parse_args(['create']), response)


def test_parse_args_no_cmd():
    """_parse_args(): SystemExit if no command arguemnt passed in."""
    assert_raises(SystemExit, cli._parse_args, [])
